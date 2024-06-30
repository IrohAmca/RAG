
from RAG.LLM.setup_model import LLM
from Sentence_Sim.setup_model import SentenceSim
from Sentence_Sim.get_query import get_query
from Database.db_functions.query import find,find_one
from Database.connect_mongo.connect import server_db, local_db
import os

LLM = LLM('Qwen/Qwen2-1.5B-Instruct',"auto","cuda")
SIM = SentenceSim('paraphrase-multilingual-MiniLM-L12-v2')

client = server_db()
database = 'test_db'
collection = 'business'
rag_dict_path = 'RAG/rag_dict.json'
rag_dict = os.readlink(rag_dict_path)

if __name__ == "__main__":
    while True:
        input = input("Enter your query: ")
        label = SIM.get_label(input, rag_dict)
        result = get_query(client, database , collection, label)
