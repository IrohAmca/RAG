import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.rag_transformers import LLM, LTK

def setup_model(model_name, torch_dtype="auto", device_map="cuda"):
    # Load model and tokenizer
    model = LLM.from_pretrained(model_name)
    tokenizer = LTK.from_pretrained(model_name)
    return model, tokenizer



