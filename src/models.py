from sentence_transformers import SentenceTransformer

MODEL_NAMES = [
    "paraphrase-xlm-r-multilingual-v1",
    "paraphrase-multilingual-mpnet-base-v2",
    "paraphrase-multilingual-MiniLM-L12-v2"
]

def load_models():
    return [SentenceTransformer(name) for name in MODEL_NAMES]
