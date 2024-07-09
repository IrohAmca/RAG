from modules.rag_transformers import LLM, LTK
from transformers import AutoModel as SIM_Model , AutoTokenizer as SIM_Tokenizer

def setup_model(model_name, torch_dtype="auto", device_map="auto"):
    # Load model and tokenizer
    model = LLM.from_pretrained(model_name, torch_dtype=torch_dtype, device_map=device_map)
    tokenizer = LTK.from_pretrained(model_name)
    return model, tokenizer

def setup_sim_model(model_name, torch_dtype="auto", device_map="auto", is_decoder=False):
    # Load model and tokenizer
    model = SIM_Model.from_pretrained(model_name, torch_dtype=torch_dtype, device_map=device_map, is_decoder=is_decoder)
    tokenizer = SIM_Tokenizer.from_pretrained(model_name)
    return model, tokenizer