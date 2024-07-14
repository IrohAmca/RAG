import re
from difflib import SequenceMatcher

from utils.response_time import ShowResponseTime

def find_special(SIM, text: str, special_list: dict) -> dict[str, tuple[str, str, float]]:
    sentences = [i.strip() for i in re.split(r'[.!?]', text.lower())]
    special_keys = list(special_list.keys())
    
    most_similar_sentences: dict[str, str] = SIM.find_most_similar_sentences(special_keys, sentences)
    
    for i, (key, sentence, similarity) in enumerate(most_similar_sentences):
        if key in special_list:
            most_similar_sentences[i] = (special_list[key], sentence, similarity)

    return most_similar_sentences

def find_closest_match(prompt: str, special_list: dict[str, str]) -> str:
    prompt = prompt.lower().strip()
    
    highest_ratio = 0
    closest_match = None
    
    with ShowResponseTime("Find Closest"):
        for key, value in special_list.items():
            seq = SequenceMatcher(None, prompt, key.lower().strip())
            if (ratio := seq.ratio()) > highest_ratio:
                highest_ratio = ratio
                closest_match = value
    
    return closest_match
