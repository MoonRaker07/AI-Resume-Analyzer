import re
import pandas as pd


class SkillExtractor:

    def __init__(self, skill_file="data/skills.csv"):

        self.df = pd.read_csv(skill_file)

    def extract_skills(self, text):

        text = text.lower()

        found = []

        for _, row in self.df.iterrows():

            skill = row["Skill"]

            pattern = r"\b" + re.escape(skill.lower()) + r"\b"

            if re.search(pattern, text):

                found.append({
                    "Category": row["Category"],
                    "Skill": skill
                })

        return found