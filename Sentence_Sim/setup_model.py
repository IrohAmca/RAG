from utils.setup import setup_model
import torch
import torch.nn.functional as F


class SentenceSim:
    def __init__(self, name, device_map="cuda"):
        self.model, self.tokenizer = setup_model(name, device_map=device_map)

    def mean_pooling(self, model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def get_sentence_embedding(self, sentence):
        encoded_input = self.tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        sentence_embedding = self.mean_pooling(model_output, encoded_input["attention_mask"])
        return sentence_embedding

    def find_most_similar_sentences(self, sentences1, sentences2, top_k=5):
        embeddings1 = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences1])
        embeddings2 = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences2])

        similarities = []
        for i, embedding1 in enumerate(embeddings1):
            for j, embedding2 in enumerate(embeddings2):
                similarity = F.cosine_similarity(embedding1.unsqueeze(0), embedding2.unsqueeze(0))
                similarities.append((sentences1[i], sentences2[j], similarity.item()))

        sorted_similarities = sorted(similarities, key=lambda x: x[2], reverse=True)[:top_k]
        return sorted_similarities

    def find_most_similar_sentence(self, prompt, sentences, top_k=5):
        prompt_embedding = self.get_sentence_embedding(prompt)
        embeddings = torch.vstack([self.get_sentence_embedding(sentence) for sentence in sentences])

        similarities = []
        for i, embedding in enumerate(embeddings):
            similarity = F.cosine_similarity(prompt_embedding, embedding, dim=1)
            similarities.append((sentences[i], similarity.item()))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:top_k]
        return sorted_similarities
