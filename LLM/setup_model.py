from utils.setup import setup_model
import os


class LLM:
    def __init__(self, model_name, torch_dtype="auto", device_map="cuda"):
        self.device_map = device_map
        self.model, self.tokenizer = setup_model(model_name, torch_dtype, device_map)

    def generate(self, prompt, db_info, llm_hyperparameters, max_new_tokens=32):
        system_prompt = db_info + llm_hyperparameters["system_prompt"]

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        model_inputs = self.tokenizer([text], return_tensors="pt", padding=True, truncation=True).to(self.device_map)

        attention_mask = model_inputs["attention_mask"].to(self.device_map)

        generated_ids = self.model.generate(
            input_ids=model_inputs.input_ids,
            attention_mask=attention_mask,
            max_new_tokens=max_new_tokens,
        )
        generated_ids = [
            output_ids[len(input_ids) :] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        return self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
