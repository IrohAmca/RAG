from typing import Any, Union

import torch
import torch.nn.functional as F

from Database.mongo import MongoDB

from utils.response_time import ShowResponseTime
from utils.setup import setup_model, setup_sim_model
from utils.special_name import find_closest_match, find_special


def dict_to_text(d: Union[Any, dict[str, Any]]) -> str:
    if not isinstance(d, dict):
        return str(d)
    return " ".join([f"{k}: {str(v)}" for k, v in d.items()])

class SentenceSim:
    def __init__(self, name, device_map="cuda"):
        self.device_map = device_map
        self.model, self.tokenizer = setup_sim_model(name, device_map=device_map, is_decoder=True)

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def get_sentence_embedding(self, sentence):
        encoded_input = self.tokenizer(sentence, padding=True, truncation=True, return_tensors="pt").to(self.device_map)
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        sentence_embedding = self.mean_pooling(model_output, encoded_input["attention_mask"])
        return sentence_embedding

    def find_most_similar_sentences(self, sentences1, sentences2, top_k=5):
        with ShowResponseTime("RAG Dict"):
            embeddings1 = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences1])
            embeddings2 = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences2])

            similarities = []
            for i, embedding1 in enumerate(embeddings1):
                for j, embedding2 in enumerate(embeddings2):
                    similarity = F.cosine_similarity(embedding1.unsqueeze(0), embedding2.unsqueeze(0))
                    similarities.append((sentences1[i], sentences2[j], similarity.item()))

            sorted_similarities = sorted(similarities, key=lambda x: x[2], reverse=True)[:top_k]
        return sorted_similarities

    def find_most_similar_sentence(self, prompt: str, sentences: list[str], top_k=5):
        with ShowResponseTime("Special Word"):
            prompt_embedding = self.get_sentence_embedding(prompt)
            embeddings = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences])

            similarities = []
            for i, embedding in enumerate(embeddings):
                similarity = F.cosine_similarity(prompt_embedding, embedding, dim=1)
                similarities.append((sentences[i], similarity.item()))

            sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
        return sorted_similarities

def get_system_prompt(dbclient: MongoDB, prompt: str, rag_dict_list: list, special_list: list, SIM=None):
    label = find_closest_match(prompt, special_list)
    command = find_closest_match(prompt, rag_dict_list)
    print(f"Label: {label} Command: {command}")
    result = get_query(dbclient, label, command)
    return dict_to_text(result)

def get_command(SIM, prompt, rag_dict):
    rag_dict_keys = list(rag_dict.keys())

    most_dict = SIM.find_most_similar_sentence(prompt, rag_dict_keys)
    command = rag_dict[most_dict[0][0]]
    print(f"Most similar sentence: {most_dict[0][0]}")
    print(f"Most similar command: {command}")
    return command

def get_query(client: MongoDB, special: str, command: str) -> Any:
    print(f"Special: {special}")
    result = client.find_one({"company_name": special})
    print(f"Initial result: {result}")
    
    if result is None:
        return None 
    
    keys = command.split(".")
    for key in keys:
        result = result.get(key)
        if result is None:
            break
    
    print(f"Data: {result}")
    return result