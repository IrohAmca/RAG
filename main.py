
from LLM.setup_model import LLM
from Sentence_Sim.setup_model import SentenceSim
from Sentence_Sim.get_query import get_query
from Database.db_functions.query import find
from Database.connect_mongo.connect import server_db
from utils.special_name import find_special
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

# LLM = LLM('Qwen/Qwen2-1.5B-Instruct',"auto","cuda")
SIM = SentenceSim('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

client = server_db()
print(f"Connected to database ", client)

database = 'test_db'
collection = 'business'
rag_dict_path = 'rag_dict.json'
current_rag_dict_path = os.path.join(current_dir,rag_dict_path)

with open(current_rag_dict_path, encoding='utf-8') as f:
    rag_dict_list = json.load(f)

if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ")
        label=find_special(SIM, prompt)[0][0]
        print(f"Label: {label}")
        # label to command parts
