# AI-Based Resume Screening & Ranking System

## Objective Framework
This project operates as an automated engine solving the problem of time-consuming manual HR screening. 

### Architecture
1. **AI Model (`ai_model/`)**: NLP Python logic to tokenize files using NLTK and assess heuristic scoring logic objectively tracking fairness.
2. **APIs (`apis/`)**: FastAPI backends handling user request data via multipart upload endpoints securely interacting with ranking models.
3. **Dashboard (`dashboard/`)**: Responsive, HR visualization dashboard that reflects live ranking metrics visually via Chart.js over dark theme UI elements. 
4. **Testing (`tests/`)**: Continuous testing framework mitigating AI biases utilizing PyTest configurations.

### Running the Application
```bash
pip install -r requirements.txt
python run.py
```
View the dashboard at `http://localhost:8000/`. To test accuracy and algorithm validation, run `pytest tests/`.
