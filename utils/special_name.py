import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Sentence_Sim.setup_model import SentenceSim
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

def find_special(SIM, text):
    sentences = text.split('.')
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip().lower()  

    special_list_path = os.path.join(current_dir, '../special_list.json')
    
    with open(special_list_path) as f:
        special_list = json.load(f)
        
    special_keys = list(special_list['special_list'].keys())
    most_dict = SIM.find_most_similar_sentences(special_keys, sentences)
    
    for i in range(len(most_dict)):
        key = most_dict[i][0]
        if key in special_list['special_list']:
            most_dict[i] = (special_list['special_list'][key], most_dict[i][1], most_dict[i][2])
    
    return most_dict

