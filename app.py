import streamlit as st

from src.pdf_reader import extract_text_from_pdf
from src.predictor import predict_resume_category
from src.preprocessing import preprocess_text
from src.skill_extractor import SkillExtractor
from src.ats import calculate_ats_score
from src.recommendations import RecommendationEngine
from collections import defaultdict

def group_skills(skills):
    grouped = defaultdict(list)

    for skill in skills:
        grouped[skill["Category"]].append(skill["Skill"])

    return grouped

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and receive an AI-powered analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    cleaned_text = preprocess_text(resume_text)

    predictor_result = predict_resume_category(resume_text)

    extractor = SkillExtractor()

    skills = extractor.extract_skills(cleaned_text)

    ats_score, feedback = calculate_ats_score(resume_text)

    recommender = RecommendationEngine()

    missing_skills = recommender.recommend_skills(
        predictor_result,
        skills
    )

    st.success("Resume analyzed successfully!")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🤖 Predicted Job Role")

        st.info(predictor_result)

        st.subheader("📊 ATS Score")

        st.progress(ats_score / 100)

        st.metric(
            "Overall Score",
            f"{ats_score}%"
        )

    with col2:

        st.subheader("🛠 Detected Skills")

        if skills:
            grouped_skills = group_skills(skills)

            for category, skill_list in grouped_skills.items():

                st.markdown(f"### {category}")

                cols = st.columns(3)

                for i, skill in enumerate(skill_list):

                    cols[i % 3].success(skill)
        else:
            st.warning("No skills detected.")

    st.divider()

    st.subheader("Recommended Skills")

    if missing_skills:

        for skill in missing_skills:

            st.write("✅", skill)

    else:

        st.success("No missing skills detected!")

    st.divider()

    st.subheader("Suggestions")

    if feedback:

        for item in feedback:

            st.warning(item)

    else:

        st.success("Excellent ATS score!")

    with st.expander("View Extracted Resume Text"):

        st.text(resume_text)