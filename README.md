# Ensemble Transformer for Cross-Lingual Semantic Textual Similarity (STS)

This project implements and extends the method proposed in:

**Piroozfar et al., 2024 – Ensemble Transformer for Cross-Lingual Semantic Textual Similarity**

The goal is to compute semantic similarity between **Persian–English sentence pairs**
without relying on machine translation, using multilingual transformer-based sentence embeddings.

---

## 📌 Overview

Semantic Textual Similarity (STS) measures how semantically equivalent two sentences are.
In cross-lingual STS, sentences are written in different languages.

In this project:
- We use **multilingual sentence transformers**
- We compare **single-model baselines** with **ensemble embeddings**
- We analyze **dimensionality reduction (PCA)** on concatenated embeddings
- Performance is evaluated using **Pearson correlation** against human similarity scores

---

## 🧠 Models Used

The following pretrained multilingual models are evaluated:

- `paraphrase-xlm-r-multilingual-v1`
- `paraphrase-multilingual-mpnet-base-v2`
- `paraphrase-multilingual-MiniLM-L12-v2`

---

## 📂 Dataset

The dataset consists of Persian–English sentence pairs with human-annotated similarity scores.

**Required columns:**
- `farsiSentence`
- `englishSentence`
- `score`

> ⚠️ The dataset file is **not included** in this repository.
> Please update the dataset path inside the notebook or script before running the project.

---

## ⚙️ Installation

It is recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows
Install the required dependencies:

pip install -r requirements.txt
▶️ Running the Project
Launch Jupyter Notebook:

jupyter notebook
Then open the provided notebook and run all cells.

The pipeline includes:

Dataset loading and cleaning

Sentence embedding using multilingual transformers

Cosine similarity computation

Pearson correlation evaluation

Ensemble embedding construction

PCA-based dimensionality analysis

📊 Evaluation Metric
Model performance is measured using the Pearson correlation coefficient (r)
between:

Model-generated similarity scores

Human-annotated similarity scores

Higher correlation indicates better semantic alignment.

🔬 Experimental Analysis
The experiments include:

Single-model baseline evaluation

Ensemble embeddings via concatenation

PCA dimension sweep

Cross-lingual similarity examples

📎 Example
s1 = "این یک جمله آزمایشی است"
s2 = "This is a test sentence"
The ensemble similarity score is computed as the average cosine similarity
across all transformer models.

📚 Reference
Piroozfar, A., et al. (2024).
Ensemble Transformer for Cross-Lingual Semantic Textual Similarity.

👤 Author
Amir Reza SharifZade
NLP Course Project

