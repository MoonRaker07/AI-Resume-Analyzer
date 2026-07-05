import re

def calculate_ats_score(resume_text):
    score = 0
    feedback = []

    text = resume_text.lower()

    # Email
    if re.search(r'[\w\.-]+@[\w\.-]+', resume_text):
        score += 10
    else:
        feedback.append("Add a professional email address.")

    # Phone
    phone_pattern = r'(\+\d{1,3}[-.\s]?)?(\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}'

    if re.search(phone_pattern, resume_text):
        score += 10
    else:
        feedback.append("Add a valid phone number.")

    # Skills
    if "skill" in text:
        score += 20
    else:
        feedback.append("Include a dedicated Skills section.")

    # Education
    if any(word in text for word in ["education", "b.tech", "btech", "degree", "university", "college"]):
        score += 15
    else:
        feedback.append("Mention your education details.")

    # Experience
    if any(word in text for word in ["experience", "internship", "worked"]):
        score += 20
    else:
        feedback.append("Add work experience or internships.")

    # Projects
    if "project" in text:
        score += 15
    else:
        feedback.append("Include your academic or personal projects.")

    # Resume Length
    words = len(text.split())

    if words >= 250:
        score += 10
    else:
        feedback.append("Resume is too short. Add more relevant details.")

    return score, feedback