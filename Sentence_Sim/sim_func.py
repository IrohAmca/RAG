from Sentence_Sim.get_query import get_query
from utils.special_name import find_special
import os


def dic_to_text(dic):
    text = ""
    for key in dic:
        text += f"{key}: {dic[key]} "
    print(f"Text: {text}")
    return text


def get_system_prompt(client, collection, SIM, prompt, rag_dict_list, special_list):
    label = find_special(SIM, prompt, special_list)[0][0]
    command = get_command(SIM, prompt, rag_dict_list)
    result = get_query(client, collection, label, command)
    return dic_to_text(result)


def get_command(SIM, prompt, rag_dict):
    rag_dict_keys = list(rag_dict.keys())

    most_dict = SIM.find_most_similar_sentence(prompt, rag_dict_keys)
    command = rag_dict[most_dict[0][0]]
    print(f"Most similar sentence: {most_dict[0][0]}")
    print(f"Most similar command: {command}")
    return command
