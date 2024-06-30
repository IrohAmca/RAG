from setup_model import SentenceSim
from get_query import get_query
import os
sim = SentenceSim('paraphrase-MiniLM-L6-v2')

def get_command(client,database,collection,input):
    rag_dict  =os.readlink("RAG/rag_dict.json")
    label=sim.get_label(input,rag_dict)
    result = get_query(client,database,collection,label)
    return result
    