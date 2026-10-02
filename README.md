# AI Career Intelligence

Research-to-production platform for explainable resume-to-job matching and skill-gap analysis.

## Highlights
- Transparent skill extraction and weighted matching baseline
- Semantic-similarity extension point
- Explainable evidence for every match
- FastAPI REST API
- Streamlit research dashboard
- Evaluation utilities
- Docker and GitHub Actions CI
- Model card and research protocol
- Tests and sample data

## Architecture
```text
Resume + Job Description
        |
        v
 Document Normalization
        |
        +----------+-----------+
        |                      |
        v                      v
Skill Taxonomy          TF-IDF Similarity
        |                      |
        +----------+-----------+
                   v
             Hybrid Scorer
                   |
          +--------+--------+
          |                 |
          v                 v
    Skill Gap        Explainability
          |                 |
          +--------+--------+
                   v
                API/UI
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
```

API docs: http://localhost:8000/docs

Dashboard:
```bash
streamlit run dashboard/app.py
```

## Research note
The baseline is a transparent prototype and is not validated for automated employment decisions. Use representative, legally appropriate data and human review before any real-world deployment.
