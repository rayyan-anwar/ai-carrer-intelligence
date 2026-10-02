from backend.app.services.matcher import match_profile, extract_skills

def test_skill_extraction():
    skills = extract_skills("Python, SQL and Docker")
    assert {"python", "sql", "docker"} <= skills

def test_match_score_is_bounded():
    result = match_profile("Python machine learning SQL", "Python SQL Docker")
    assert 0 <= result["score"] <= 100

def test_missing_skill_is_reported():
    result = match_profile("Python SQL", "Python SQL Docker")
    assert "docker" in result["missing_skills"]
