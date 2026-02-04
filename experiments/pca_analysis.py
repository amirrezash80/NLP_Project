import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr
from src.models import load_models

PCA_DIMS = [50, 100, 200, 300, 350, 400]

def main(path):
    df = pd.read_csv(path)
    models = load_models()

    emb1_all, emb2_all = [], []

    for _, row in df.iterrows():
        e1, e2 = [], []
        for m in models:
            e1.append(m.encode(row["sentence1"], convert_to_numpy=True))
            e2.append(m.encode(row["sentence2"], convert_to_numpy=True))
        emb1_all.append(np.concatenate(e1))
        emb2_all.append(np.concatenate(e2))

    results = []
    for dim in PCA_DIMS:
        pca = PCA(n_components=dim)
        e1p = pca.fit_transform(emb1_all)
        e2p = pca.transform(emb2_all)

        sims = [
            cosine_similarity(a.reshape(1,-1), b.reshape(1,-1))[0][0]
            for a, b in zip(e1p, e2p)
        ]
        results.append(pearsonr(sims, df["score"])[0])

    plt.plot(PCA_DIMS, results, marker="o")
    plt.xlabel("PCA Dimensions")
    plt.ylabel("Pearson Correlation")
    plt.title("PCA Dimension Analysis")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main("path/to/pests.csv")
