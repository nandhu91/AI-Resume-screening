import numpy as np

def calculate_score(candidate: dict, job_skills: list[str]) -> float:
    if not job_skills:
        return 0.0

    skill_match = len(
        set(candidate["skills"]) & set(job_skills)
    ) / len(job_skills)

    exp_score = min(candidate["experience"] * 0.1, 1.0)
    edu_score = candidate["education"]

    # Basic ranking engine weight configurations
    score = (skill_match * 0.5) + (exp_score * 0.3) + (edu_score * 0.2)
    return float(round(score, 2))

def rank_candidates(candidates: list[dict], job_skills: list[str]) -> list[dict]:
    for c in candidates:
        c["score"] = calculate_score(c, job_skills)
    return sorted(candidates, key=lambda x: x.get("score", 0), reverse=True)
