import modules
import modules.transformers

def setup(model_name, torch_dtype,device_map):
    # Load model and tokenizer
    model = modules.transformers.LLM.from_pretrained(model_name,torch_dtype,device_map)
    tokenizer = modules.transformers.LTK.from_pretrained(model_name)
    return model, tokenizer

