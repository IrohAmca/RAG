from utils.setup import  setup_sim_st

class SentenceSim:
    def __init__(self,name):
        self.sim = setup_sim_st(name)
    
    def get_sim_score(self, query, text):
        return self.sim.encode(query, text)

    def get_label(self, query, rag_dict):
        max_score = 0
        max_label = ""
        for key in rag_dict:
            score = self.get_sim_score(query, rag_dict[key])
            if score > max_score:
                max_score = score
                max_label = key
        return max_label