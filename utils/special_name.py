import os 
from Sentence_Sim.setup_model import SentenceSim
def find_special(SIM,sentence):
    sentence = sentence.split('.').lower()
    special_list =os.readlink('../special_list.json').get('special_list')
    max_sim = 0
    max_special = ""
    for special in special_list:
        for word in sentence:
            sim = SIM.get_sim_score(word, special)
            if sim > max_sim:
                max_sim = sim
                max_special = special
    return max_special

SIM = SentenceSim('paraphrase-multilingual-MiniLM-L12-v2')
print(find_special(SIM,"Where is Blue Ocean Maritime"))