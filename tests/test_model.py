import pytest
from ai_model.parser import extract_skills, extract_experience, extract_education
from ai_model.scoring import calculate_score, rank_candidates

def test_extract_skills_nlp():
    text = "A proficient software engineer experienced with python and java."
    skills = extract_skills(text)
    assert "python" in skills
    assert "java" in skills

def test_extract_experience():
    text = "I have 5 year solid development track"
    assert extract_experience(text) > 0

def test_extract_education():
    text = "completed my b.tech degree"
    assert extract_education(text) == 1

def test_scoring_algorithm_accuracy():
    candidate = {
        "skills": ["python", "react"],
        "experience": 3,
        "education": 1
    }
    job_skills = ["python", "java", "react"]
    # Formula check: Match = 2/3 * 0.5 (0.33) + Exp = 3*0.1*0.3 (0.09) + Edu = 1*0.2 (0.2)
    # Expected round(0.333 + 0.09 + 0.2, 2) ~ 0.62
    score = calculate_score(candidate, job_skills)
    assert score > 0.0
    assert score == 0.62

def test_candidate_ranking_fairness():
    # Model should rank equally skilled candidates identical, preventing alphabetical bias
    c1 = {"name": "Alice", "skills": ["python"], "experience": 1, "education": 1}
    c2 = {"name": "Bob", "skills": ["python"], "experience": 1, "education": 1}
    
    # Run scoring
    c1["score"] = calculate_score(c1, ["python"])
    c2["score"] = calculate_score(c2, ["python"])
    
    assert c1["score"] == c2["score"]
    
    ranked = rank_candidates([c1, c2], ["python"])
    assert len(ranked) == 2
