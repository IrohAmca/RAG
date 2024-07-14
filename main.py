import json
from argparse import Namespace
from pathlib import Path


def main(args: Namespace, CWD = Path.cwd()):
    from Database.mongo import MongoDB
    from LLM.setup_model import LLM as LLM_
    from Sentence_Sim.SIM import SentenceSim, get_query, get_system_prompt
    from utils.response_time import ShowResponseTime
    from utils.special_name import find_special
    
    print(f"Using {args.device.upper()} to run the model. (Change with -d argument)")

    LLM = LLM_("Qwen/Qwen2-1.5B-Instruct", device_map=args.device)
    # SIM = SentenceSim("", device_map="cuda")

    mongo = MongoDB(args.mongo_uri, args.db, args.collection)

    rag_dict_file = "rag_dict.json"
    special_list_file = "special_list.json"
    LLM_hyperparameters_file = "LLM/LLM_hyperparameters.json"

    with open(CWD / rag_dict_file, encoding="utf-8") as f:
        rag_dict_list = json.load(f)

    with open(CWD / special_list_file, encoding="utf-8") as f:
        special_list = json.load(f)

    with open(CWD / LLM_hyperparameters_file, encoding="utf-8") as f:
        LLM_hyperparameters = json.load(f)
    
    while True:
        prompt = input("Enter your query: ")
        with ShowResponseTime():
            db_info = get_system_prompt(dbclient=mongo, prompt= prompt, rag_dict_list= rag_dict_list, special_list=special_list)
            print(f"Qwen Yanıt: {LLM.generate(prompt,db_info,LLM_hyperparameters,max_new_tokens=32)}")

if __name__ == "__main__":
    print("Do not run this file directly. Run `python .` instead.")
    exit(1)