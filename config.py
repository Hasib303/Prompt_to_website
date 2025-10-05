from pathlib import Path

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
EMBEDDINGS_DIR = DATA_DIR / 'embeddings'

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)

COMPONENTS_CSV = PROCESSED_DATA_DIR / 'components.csv'
FAISS_INDEX_PATH = EMBEDDINGS_DIR / 'components_index.faiss'
METADATA_PATH = EMBEDDINGS_DIR / 'metadata.pkl'

EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'

LLM_MODEL = 'Qwen/Qwen2.5-Coder-3B-Instruct'
LLM_FILE = None  

TOP_K_RESULTS = 5
MAX_TOKENS = 2048
TEMPERATURE = 0.7