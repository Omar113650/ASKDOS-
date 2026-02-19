from sentence_transformers import SentenceTransformer, util
import numpy as np

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def semantic_similarity(predicted, ground_truth):
    emb1 = model.encode(predicted, convert_to_tensor=True)
    emb2 = model.encode(ground_truth, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return float(score)

def exact_match(predicted, ground_truth):
    return int(predicted.strip().lower() == ground_truth.strip().lower())
