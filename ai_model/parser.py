import pdfplumber
import re

SKILLS_DB = [
    "python","java","sql","react",
    "machine learning","fastapi","django","html","css",
    "nlp", "data science", "angular", "node", "javascript", "typescript",
    "kubernetes", "docker", "aws"
]

def extract_text(path: str) -> str:
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()

def extract_skills(text: str) -> list[str]:
    # Using python NLP regex to tokenize and extract entities
    words = re.findall(r'\b\w+\b', text)
    
    found_skills = set()
    for word in words:
        if word in SKILLS_DB:
            found_skills.add(word)
    
    # Check multi-word skills manually by raw scanning space-separated phrases
    for skill in SKILLS_DB:
        if " " in skill and skill in text:
            found_skills.add(skill)
            
    return list(found_skills)

def extract_experience(text: str) -> int:
    # Basic heuristic NLP mapping
    return text.count("year")

def extract_education(text: str) -> int:
    # Heuristic matching for education parsing
    return 1 if ("b.tech" in text or "bachelor" in text or "mca" in text or "degree" in text) else 0

def parse_resume(path: str) -> dict:
    text = extract_text(path)
    return {
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text)
    }
