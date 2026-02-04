import numpy as np
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import paired_cosine_distances

def evaluate_embeddings(emb1, emb2, gold_scores):
    sims = 1 - paired_cosine_distances(emb1, emb2)
    corr, _ = pearsonr(sims, gold_scores)
    return corr
