import json
from argparse import Namespace
from pathlib import Path

from config import LLM_MAX_NEW_TOKENS, rag_dict_file, special_list_file, LLM_hyperparameters_file

def main(args: Namespace):
    from Database.mongo import MongoDB
    from LLM.setup_model import LLM as LLM_
    from Sentence_Sim.SIM import SentenceSim, get_query, get_system_prompt
    from utils.response_time import ShowResponseTime
    from utils.special_name import find_special
    
    print(f"Using {args.device.upper()} to run the model. (Change with -d argument)")

    LLM = LLM_("Qwen/Qwen2-1.5B-Instruct", device_map=args.device)
    # SIM = SentenceSim("", device_map="cuda")

    mongo = MongoDB(args.mongo_uri, args.db, args.collection)

    with open(rag_dict_file, encoding="utf-8") as f_rag, \
         open(special_list_file, encoding="utf-8") as f_special, \
         open(LLM_hyperparameters_file, encoding="utf-8") as f_hyper:
        rag_dict_list = json.load(f_rag)
        special_list = json.load(f_special)
        LLM_hyperparameters = json.load(f_hyper)
    
    while True:
        prompt = input("Enter your query: ")
        with ShowResponseTime():
            db_info = get_system_prompt(dbclient=mongo, prompt=prompt, rag_dict_list=rag_dict_list, special_list=special_list)
            print(f"Qwen Yanıt: {LLM.generate(prompt, db_info, LLM_hyperparameters, max_new_tokens=LLM_MAX_NEW_TOKENS)}")

if __name__ == "__main__":
    print("Do not run this file directly. Run `python .` instead.")
    exit(1)