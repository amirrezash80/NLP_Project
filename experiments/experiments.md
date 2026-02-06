# Experiments and Evaluation

---

## 1. Dataset

All experiments are conducted on the **PESTS** dataset, a publicly available
Persian–English semantic textual similarity corpus.

- Language pair: Persian–English
- Number of sentence pairs: 5,375
- Label type: Continuous similarity score in the range [0, 5]
- Annotation: Human-annotated semantic similarity

Dataset source:
https://github.com/mohammadabdous/PESTS

The dataset is not included in this repository and must be downloaded
separately by the user.

---

## 2. Evaluation Metric

The primary evaluation metric used in all experiments is the
**Pearson Correlation Coefficient** between the model-generated similarity
scores and the gold human similarity scores.

Pearson correlation is commonly used in STS benchmarks as it measures
the linear relationship between predicted and reference similarity values.

---

## 3. Baseline Experiment

### 3.1 Model

As a baseline, a single multilingual sentence transformer model was used:

- `paraphrase-xlm-r-multilingual-v1`

### 3.2 Procedure

1. Each Persian and English sentence was independently encoded into a
   fixed-dimensional vector using the selected model.
2. Cosine similarity was computed between each pair of sentence embeddings.
3. The resulting similarity scores were compared against the gold labels
   using Pearson correlation.

### 3.3 Result

The baseline experiment provides a reference performance level for a
single-model CL-STS system.

---

## 4. Ensemble Experiment

### 4.1 Models Used

To improve robustness and capture complementary semantic information,
an ensemble of three multilingual sentence transformer models was used:

- `paraphrase-xlm-r-multilingual-v1`
- `paraphrase-multilingual-mpnet-base-v2`
- `paraphrase-multilingual-MiniLM-L12-v2`

### 4.2 Ensemble Strategy

For each model:

1. Sentence embeddings for Persian and English sentences were computed.
2. Embeddings from all models were concatenated along the feature dimension,
   forming a high-dimensional joint representation.

This concatenation-based ensemble allows the system to combine different
semantic perspectives learned by individual models.

---

## 5. Dimensionality Reduction with PCA

### 5.1 Motivation

Concatenating embeddings from multiple models results in a very
high-dimensional vector, which can increase computational cost and
risk of overfitting.

To address this, **Principal Component Analysis (PCA)** was applied
to reduce dimensionality while preserving the most informative components.

### 5.2 Experimental Setup

PCA was applied to the concatenated embeddings using different target
dimensions:

- 50
- 100
- 200
- 300
- 400

For each PCA dimension:
1. PCA was fitted on the Persian sentence embeddings.
2. The same transformation was applied to the corresponding English embeddings.
3. Cosine similarity was computed in the reduced space.
4. Pearson correlation was calculated against gold similarity scores.

### 5.3 Results and Analysis

The results show a consistent improvement in Pearson correlation as
the PCA dimension increases, with diminishing returns after approximately
200–300 dimensions.

This indicates that most of the useful semantic information is captured
within a relatively compact subspace.

---

## 6. Qualitative Example

In addition to quantitative evaluation, a qualitative test was performed
using a manually selected sentence pair:

- Persian: "این یک جمله آزمایشی است"
- English: "This is a test sentence"

Each model produced a similarity score, and the final ensemble similarity
was computed as the average of individual cosine similarities.

The high similarity score confirms that the ensemble model correctly
captures cross-lingual semantic equivalence in practice.

---

## 7. Summary

The experiments demonstrate that:

- A single multilingual transformer provides a strong baseline for CL-STS.
- Combining multiple models through embedding concatenation improves robustness.
- PCA effectively reduces dimensionality with minimal performance loss.
- The proposed approach provides a practical and scalable solution for
  cross-lingual semantic similarity without machine translation.
