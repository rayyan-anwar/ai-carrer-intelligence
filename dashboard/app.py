import streamlit as st
from backend.app.services.matcher import match_profile

st.set_page_config(page_title="AI Career Intelligence", page_icon="AI", layout="wide")
st.title("AI Career Intelligence")
st.caption("Explainable resume-to-job matching research dashboard")

resume = st.text_area("Resume / profile", height=180, value="Python, machine learning, SQL, FastAPI, Docker, NLP")
job = st.text_area("Job description", height=180, value="We need a Python machine learning engineer with SQL, NLP and Docker experience.")

if st.button("Analyze match", type="primary"):
    result = match_profile(resume, job)
    c1, c2, c3 = st.columns(3)
    c1.metric("Match score", f'{result["score"]}%')
    c2.metric("Semantic similarity", f'{result["semantic_similarity"]:.2f}')
    c3.metric("Matched skills", len(result["matched_skills"]))

    st.subheader("Matched skills")
    st.write(", ".join(result["matched_skills"]) or "None detected")

    st.subheader("Skill gaps")
    st.write(", ".join(result["missing_skills"]) or "No detected gaps")

    st.subheader("Methodology")
    st.info(result["methodology"])
