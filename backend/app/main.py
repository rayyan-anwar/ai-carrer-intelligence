from fastapi import FastAPI
from backend.app.schemas import MatchRequest, MatchResponse
from backend.app.services.matcher import match_profile

app = FastAPI(title="AI Career Intelligence API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-career-intelligence"}

@app.post("/api/v1/match", response_model=MatchResponse)
def match(request: MatchRequest):
    return match_profile(request.resume, request.job_description)
