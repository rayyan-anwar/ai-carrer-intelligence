from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
    resume: str = Field(min_length=20)
    job_description: str = Field(min_length=20)

class Evidence(BaseModel):
    skill: str
    source: str

class MatchResponse(BaseModel):
    score: float
    semantic_similarity: float
    matched_skills: list[str]
    missing_skills: list[str]
    evidence: list[Evidence]
    methodology: str
