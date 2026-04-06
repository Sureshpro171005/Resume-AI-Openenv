from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def calculate_similarity(resume, job):
    emb1 = model.encode(resume, convert_to_tensor=True)
    emb2 = model.encode(job, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2).item()
    return float(max(0, min(score, 1)))