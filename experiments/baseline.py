import argparse
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.stats import pearsonr

def main(path):
    df = pd.read_csv(path)
    model = SentenceTransformer("paraphrase-xlm-r-multilingual-v1")

    preds = []
    for _, row in df.iterrows():
        e1 = model.encode(row["sentence1"], convert_to_numpy=True)
        e2 = model.encode(row["sentence2"], convert_to_numpy=True)
        preds.append(cosine_similarity(e1.reshape(1,-1), e2.reshape(1,-1))[0][0])

    print("Baseline Pearson:", pearsonr(preds, df["score"])[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()
    main(args.data_path)
