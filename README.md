# 🤖 AI-Based Resume Screening System

This project is an automated **AI-Based Resume Screening and Ranking System** designed to streamline the HR recruitment process. By leveraging Natural Language Processing (NLP) techniques via Python and robust web architectures via FastAPI & Chart.js, this application can read PDF resumes, extract key information (skills, experience, and education), and rank candidates based on user-defined job requirements.

## ✨ Key Features
- **📄 Resume Parsing:** Automatically extracts text from uploaded PDF resumes using `pdfplumber`.
- **🧠 NLP Skill Extraction:** Identifies and registers specific technical skills directly from candidate resumes.
- **📊 Candidate Ranking Engine:** Calculates an "Affinity Score" comparing candidate skills against required job skills.
- **📈 Global Talent Dashboard:** Features a modern, responsive HTML interface using a beautiful glassmorphism dark-theme.
- **📉 Dynamic Data Visualizations:** Integrated with `Chart.js` to render immersive graphical analytics:
  - Skill Demographics (Doughnut Chart)
  - Experience Distribution (Histogram)
  - Education Profiles (Pie Chart)
  - Scoring Rankings (Bar Chart)

---

## 🏗️ Project Architecture
The project follows a modular, scalable architecture separating core backend logic from frontend visualization:

```
AI-Based-Resume-Screening/
│
├── ai_model/                # Core AI Engine
│   ├── parser.py            # PDF text extraction & NLP tokenization
│   └── scoring.py           # Affinity scoring & ranking algorithms
│
├── apis/                    # Backend Server Logic
│   ├── main.py              # FastAPI application factory
│   └── routes.py            # RESTful endpoints (/upload, /rank, /stats)
│
├── dashboard/               # Frontend Client Application
│   └── index.html           # Unified UI & Data Visualization layer
│
├── tests/                   # Quality Assurance
│   ├── test_model.py        # Pytest suite for algorithm accuracy validation
│
├── requirements.txt         # Dependency tree
└── run.py                   # Application entrypoint
```

---

## 🚀 Installation & Execution

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system. 

### 2. Environment Setup
Clone the repository and install the dependencies:
```bash
git clone https://github.com/nandhu91/AI-Resume-screening.git
cd AI-Resume-screening
python -m venv .venv
source .venv/Scripts/activate  # On Windows PowerShell
pip install -r requirements.txt
```

### 3. Running the System
Start the local FastAPI ASGI server layout:
```bash
python run.py
```

### 4. Access the Dashboard
Open your local web browser and navigate directly to:
**[http://localhost:8000/](http://localhost:8000/)**

From here, you can seamlessly upload candidate resumes (in `.pdf` format), type in comma-separated `Job Skills` (e.g., *python, sql, javascript*), and execute the Ranking Engine to visualize your applicant array!

---

## 🧪 Testing
This application was built securely using Test-Driven Development logic targeting algorithm fairness and reliability. To run the automated unit testing suite:
```bash
pytest tests/
```
