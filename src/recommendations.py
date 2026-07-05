import pandas as pd


class RecommendationEngine:

    def __init__(self, csv_path="data/role_skills.csv"):

        self.df = pd.read_csv(csv_path)

    def recommend_skills(self, predicted_role, extracted_skills):

        expected_skills = self.df[
            self.df["Role"] == predicted_role
        ]["Skill"].tolist()

        extracted = {
            skill["Skill"].lower()
            for skill in extracted_skills
        }

        missing = []

        for skill in expected_skills:

            if skill.lower() not in extracted:

                missing.append(skill)

        return missing