import dotenv
import argparse
import json
from time import perf_counter
from pathlib import Path
from os import getenv

from Database.mongo import MongoDB
from LLM.setup_model import LLM as LLM_
from Sentence_Sim.get_query import get_query
from Sentence_Sim.setup_model import SentenceSim
from Sentence_Sim.sim_func import get_system_prompt
from utils.special_name import find_special

dotenv.load_dotenv(".env")
parser = argparse.ArgumentParser()
parser_db = parser.add_argument_group("Database Arguments")
parser_db.add_argument("--uselocal", action="store_true", help="Use local database instead of server. (uses: MONGO_LOCAL in .env)", default=False)
parser_db.add_argument("--db", type=str, help="Database name (default: DATABASE in .env)", default=getenv("DATABASE"))
parser_db.add_argument("--collection", type=str, help="Collection name (default: COLLECTION in .env)", default=getenv("COLLECTION"))
args = parser.parse_args()

CWD = Path.cwd()

LLM = LLM_("Qwen/Qwen2-1.5B-Instruct")
# SIM = SentenceSim("", device_map="cuda")

uri = getenv("MONGO_LOCAL") if args.uselocal else getenv("MONGO_SERVER")
mongo = MongoDB(uri, args.db, args.collection)

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
        db_info = get_system_prompt(client=mongo, collection=args.collection,prompt= prompt,rag_dict_list= rag_dict_list, special_list=special_list)
        print(f"Qwen Yanıt: {LLM.generate(prompt,db_info,LLM_hyperparameters,max_new_tokens=32)}")
        print(f"Response Time: {perf_counter()-start_time:.5f} seconds")

if __name__ == "__main__":
    main()
