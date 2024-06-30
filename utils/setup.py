from modules.rag_transformers import LLM ,LTK, SIM

def setup_llm(model_name, torch_dtype,device_map):
    # Load model and tokenizer
    model = LLM.from_pretrained(model_name,torch_dtype,device_map)
    tokenizer = LTK.from_pretrained(model_name)
    return model, tokenizer

def setup_sim_st(model_name):
    model = SIM('sentence-tranformers/'+model_name)
    return model