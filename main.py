import time
from LLM.setup_model import LLM
from Sentence_Sim.setup_model import SentenceSim
from Sentence_Sim.sim_func import get_system_prompt
from Sentence_Sim.get_query import get_query
from Database.db_functions.query import find
from Database.connect_mongo.connect import server_db,local_db
from utils.special_name import find_special
from Database.db_functions.query import find_one

import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))

LLM = LLM('Qwen/Qwen2-1.5B-Instruct')
SIM = SentenceSim('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2',device_map='cpu')

client = local_db()
print(f"Connected to database ", client)

database = 'test_db'
collection = 'business'

rag_dict_path = 'rag_dict.json'
current_rag_dict_path = os.path.join(current_dir,rag_dict_path)
with open(current_rag_dict_path, encoding='utf-8') as f:
    rag_dict_list = json.load(f)

special_list_path = 'special_list.json'
current_special_list_path = os.path.join(current_dir,special_list_path)
with open(current_special_list_path, encoding='utf-8') as f:
    special_list = json.load(f)
    
LLM_hyperparameters_path = 'LLM\\LLM_hyperparameters.json'
current_LLM_hyperparameters_path = os.path.join(current_dir,LLM_hyperparameters_path)
with open(current_LLM_hyperparameters_path, encoding='utf-8') as f:
    LLM_hyperparameters = json.load(f)
    
if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ")
        start_time=time.time()
        db_info = get_system_prompt(client,database,collection,SIM,prompt,rag_dict_list,special_list)
        print(db_info)
        print(f"Qwen Yanıt: {LLM.generate(prompt,db_info,LLM_hyperparameters,max_new_tokens=128)}")
        print(f"Response Time: {time.time()-start_time} seconds")