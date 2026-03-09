from fastapi import APIRouter, UploadFile, File
import shutil
import os

from ai_model.parser import parse_resume
from ai_model.scoring import rank_candidates

router = APIRouter()

# In-memory database array to hold temporary data for the dashboard demo
DATABASE = []

@router.get("/")
def api_home():
    return {"msg": "AI APIs Running"}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data = parse_resume(path)
    data["filename"] = file.filename
    DATABASE.append(data)

    return {"parsed": data}

@router.post("/rank")
def rank(skills: list[str]):
    return rank_candidates(DATABASE, skills)

@router.get("/candidates")
def candidates():
    return DATABASE

@router.get("/stats")
def stats():
    if not DATABASE:
        return {
            "total": 0, "avg_exp": 0, "top_skills": [], "avg_score": 0,
            "skill_labels": [], "skill_data": [],
            "exp_labels": [], "exp_data": [],
            "edu_labels": [], "edu_data": []
        }
        
    avg_exp = sum(c.get("experience", 0) for c in DATABASE) / len(DATABASE)
    
    # Calculate average score if ranking has been done
    scores = [c.get("score") for c in DATABASE if "score" in c]
    avg_score = sum(scores) / len(scores) if scores else 0
    
    all_skills = []
    exp_bins = {"0-2 Yrs": 0, "3-5 Yrs": 0, "6-10 Yrs": 0, "10+ Yrs": 0}
    edu_bins = {"Degree Verified": 0, "Not Found": 0}

    for c in DATABASE:
        all_skills.extend(c.get("skills", []))
        
        # Experience distribution
        exp = c.get("experience", 0)
        if exp <= 2: exp_bins["0-2 Yrs"] += 1
        elif exp <= 5: exp_bins["3-5 Yrs"] += 1
        elif exp <= 10: exp_bins["6-10 Yrs"] += 1
        else: exp_bins["10+ Yrs"] += 1

        # Education distribution
        if c.get("education", 0):
            edu_bins["Degree Verified"] += 1
        else:
            edu_bins["Not Found"] += 1
        
    from collections import Counter
    skill_counts = Counter(all_skills)
    top_skills = [{"skill": k, "count": v} for k, v in skill_counts.most_common(5)]
    
    return {
        "total": len(DATABASE),
        "avg_exp": round(avg_exp, 1),
        "avg_score": round(avg_score * 100, 1),
        "top_skills": top_skills,
        "skill_labels": [s["skill"] for s in top_skills],
        "skill_data": [s["count"] for s in top_skills],
        "exp_labels": list(exp_bins.keys()),
        "exp_data": list(exp_bins.values()),
        "edu_labels": list(edu_bins.keys()),
        "edu_data": list(edu_bins.values())
    }

@router.delete("/clear")
def clear():
    DATABASE.clear()
    return {"msg": "cleared"}
