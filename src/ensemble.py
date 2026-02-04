import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cosine_sim(e1, e2):
    return cosine_similarity(e1.reshape(1, -1), e2.reshape(1, -1))[0][0]

def ensemble_similarity(sentence1, sentence2, models):
    sims = []
    for model in models:
        e1 = model.encode(sentence1, convert_to_numpy=True)
        e2 = model.encode(sentence2, convert_to_numpy=True)
        sims.append(cosine_sim(e1, e2))
    return float(np.mean(sims))
