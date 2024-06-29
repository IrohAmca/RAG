import utils.setup as setup

# Define model name, torch data type, and device map

model_name = 'Qwen/Qwen2-1.5B-Instruct'
torch_dtype = "auto"
device_map = "cuda"

# Load model and tokenizer
model, tokenizer = setup.setup(model_name, torch_dtype, device_map)

