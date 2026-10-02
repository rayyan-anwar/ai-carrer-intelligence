# Research Protocol

## Research question
Can a transparent hybrid NLP baseline improve candidate-job relevance while retaining interpretable evidence?

## Baseline
Hybrid score = 0.70 × skill overlap + 0.30 × TF-IDF cosine similarity.

## Experimental roadmap
1. Replace TF-IDF with sentence-transformer embeddings.
2. Compare embedding models.
3. Add seniority and experience features.
4. Evaluate Precision@K, Recall@K, F1, MRR and NDCG@K.
5. Perform error analysis by job family.
6. Measure calibration and robustness to noisy resumes.

Every experiment should record dataset version, preprocessing version, model ID, seed, split and metric definitions.
