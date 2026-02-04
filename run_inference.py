import sys
from src.models import load_models
from src.ensemble import ensemble_similarity

if len(sys.argv) != 3:
    print("Usage: python run_inference.py <sentence1> <sentence2>")
    sys.exit(1)

s1 = sys.argv[1]
s2 = sys.argv[2]

models = load_models()
score = ensemble_similarity(s1, s2, models)

print("Ensemble Similarity Score:", score)
