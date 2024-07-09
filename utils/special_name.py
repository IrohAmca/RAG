
import difflib
import time

def find_special(SIM, text, special_list):
    sentences = text.split(".")
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip().lower()

    special_keys = list(special_list.keys())
    most_dict = SIM.find_most_similar_sentences(special_keys, sentences)

    for i in range(len(most_dict)):
        key = most_dict[i][0]
        if key in special_list:
            most_dict[i] = (special_list[key], most_dict[i][1], most_dict[i][2])

    return most_dict

def find_closest_match(prompt, special_list):
    start_time = time.time()
    prompt = prompt.lower()
    highest_ratio = 0
    closest_match = None
    
    for key, value in special_list.items():
        seq = difflib.SequenceMatcher(None, prompt, key.lower().strip())
        ratio = seq.ratio()
        
        if ratio > highest_ratio:
            highest_ratio = ratio
            closest_match = value
    print(f"Find Closest Response Time: {time.time()-start_time:.5f} seconds")
    return closest_match