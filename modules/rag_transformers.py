from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer

# Automodel and Autotokenizer modules
LLM = AutoModelForCausalLM
LTK = AutoTokenizer

# SentenceTransformer module
SIM = SentenceTransformer