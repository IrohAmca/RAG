from pathlib import Path

__title__   = "RAG"
__author__  = "STARS"
__version__ = '1.0.0'
__license__ = None

# --- Constants ---
LLM_MAX_NEW_TOKENS = 32
# -----------------

# --- Paths ---
CWD = Path.cwd()
rag_dict_file            = CWD / "rag_dict.json"
special_list_file        = CWD / "special_list.json"
LLM_hyperparameters_file = CWD / "LLM" / "LLM_hyperparameters.json"
# -------------
