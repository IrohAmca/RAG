from utils.setup import setup_model
import os
class LLM:
    def __init__(self,model_name,torch_dtype,device_map):
        self.model, self.tokenizer = setup_model(model_name,torch_dtype,device_map)
        
    def generate(self, input_text,db_info, max_new_tokens=32,device_map="cuda"):
        llm__hyperparameters = os.readlink('LLM_hyperpara meters.json')
        system_prompt = db_info + llm__hyperparameters['system_prompt']
    
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input_text},
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([input_text], return_tensors="pt").to(device_map)

        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_new_tokens,
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        return self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]