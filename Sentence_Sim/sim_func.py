from Sentence_Sim.get_query import get_query
from utils.special_name import find_special, find_closest_match
import time
def dic_to_text(dic):
    if not isinstance(dic, dict):
        return str(dic)
    text = ""
    for key in dic:
        text += f"{key}: {str(dic[key])} "
    return text


def get_system_prompt(client, collection, prompt, rag_dict_list, special_list,SIM=None):
    label = find_closest_match(prompt, special_list)
    command = find_closest_match(prompt, rag_dict_list)
    print(f"Label: {label} Command: {command}")
    result = get_query(client, collection, label, command)
    return dic_to_text(result)


def get_command(SIM, prompt, rag_dict):
    rag_dict_keys = list(rag_dict.keys())

    most_dict = SIM.find_most_similar_sentence(prompt, rag_dict_keys)
    command = rag_dict[most_dict[0][0]]
    print(f"Most similar sentence: {most_dict[0][0]}")
    print(f"Most similar command: {command}")
    return command
