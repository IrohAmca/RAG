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
RESOURCES = CWD / "Resources"

rag_dict_file            = RESOURCES / "rag_dict.json"
special_list_file        = RESOURCES / "special_list.json"
LLM_hyperparameters_file = RESOURCES / "LLM_hyperparameters.json"
# -------------
