import json
from time import perf_counter
from pathlib import Path

from Database.connect_mongo.connect import local_db, server_db
from Database.db_functions.query import find, find_one
from LLM.setup_model import LLM as LLM_
from Sentence_Sim.get_query import get_query
from Sentence_Sim.setup_model import SentenceSim
from Sentence_Sim.sim_func import get_system_prompt
from utils.special_name import find_special

CWD = Path.cwd()

LLM = LLM_("Qwen/Qwen2-1.5B-Instruct")
SIM = SentenceSim("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", device_map="cpu")

client = local_db()
print(f"Connected to database:", client)

database = "test_db"
collection = "business"

rag_dict_file = "rag_dict.json"
special_list_file = "special_list.json"
LLM_hyperparameters_file = "LLM/LLM_hyperparameters.json"

with open(CWD / rag_dict_file, encoding="utf-8") as f:
    rag_dict_list = json.load(f)

with open(CWD / special_list_file, encoding="utf-8") as f:
    special_list = json.load(f)

with open(CWD / LLM_hyperparameters_file, encoding="utf-8") as f:
    LLM_hyperparameters = json.load(f)

def main():
    while True:
        prompt = input("Enter your query: ")
        start_time = perf_counter()
        db_info = get_system_prompt(client, database, collection, SIM, prompt, rag_dict_list, special_list)
        print(db_info)
        print(f"Qwen Yanıt: {LLM.generate(prompt,db_info,LLM_hyperparameters,max_new_tokens=128)}")
        print(f"Response Time: {perf_counter()-start_time:.5f} seconds")

if __name__ == "__main__":
    main()
