from typing import List
from app.models.cv_model import CVModel, Education, Experience
# import spacy
#
# nlp = spacy.load("en_core_web_sm")

class CVProcessor:
    @staticmethod
    def parse_cv(text: List[str]) -> CVModel:
        full_text = " ".join(text)
        # doc = nlp(full_text)

        # Example parsing logic (customize as needed)
        name = "John Doe"  # Extract name using NLP
        email = "john.doe@example.com"  # Extract email using regex
        phone = "123-456-7890"  # Extract phone using regex
        education = [
            Education(
                institution="University of Example",
                degree="Bachelor of Science",
                field_of_study="Computer Science",
                start_date="2015-09-01",
                end_date="2019-05-01"
            )
        ]
        experience = [
            Experience(
                company="Example Corp",
                position="Software Engineer",
                start_date="2019-06-01",
                end_date="2021-12-31",
                description="Developed web applications using Python and FastAPI."
            )
        ]
        skills = ["Python", "FastAPI", "Machine Learning"]

        return CVModel(
            name=name,
            email=email,
            phone=phone,
            education=education,
            experience=experience,
            skills=skills
        )
