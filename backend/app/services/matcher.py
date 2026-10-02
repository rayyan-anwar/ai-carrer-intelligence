import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

SKILLS = {
    "python","machine learning","deep learning","sql","fastapi","pytorch",
    "tensorflow","docker","kubernetes","aws","nlp","transformers","pandas",
    "scikit-learn","git","react","postgresql","statistics","data analysis",
    "computer vision","llm","generative ai","natural language processing"
}

def extract_skills(text: str) -> set[str]:
    normalized = re.sub(r"[^a-z0-9+#.\s-]", " ", text.lower())
    return {s for s in SKILLS if s in normalized}

def semantic_similarity(a: str, b: str) -> float:
    matrix = TfidfVectorizer(stop_words="english").fit_transform([a, b])
    return float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0])

def match_profile(resume: str, job_description: str) -> dict:
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_description)
    matched = sorted(resume_skills & job_skills)
    missing = sorted(job_skills - resume_skills)
    skill_score = len(matched) / len(job_skills) if job_skills else 0.0
    semantic = semantic_similarity(resume, job_description)
    score = round((0.70 * skill_score + 0.30 * semantic) * 100, 2)

    return {
        "score": score,
        "semantic_similarity": round(semantic, 4),
        "matched_skills": matched,
        "missing_skills": missing,
        "evidence": [{"skill": s, "source": "resume + job description"} for s in matched],
        "methodology": "70% explicit skill overlap + 30% TF-IDF cosine similarity."
    }
