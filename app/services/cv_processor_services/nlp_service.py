from typing import List

# import spacy
from app.models.cv_model import CVModel, Education, Experience, Contact
from app.services.cv_processor_services.base_service import BaseService


class NLPService(BaseService):
    def __init__(self):
        # self.nlp = spacy.load("en_core_web_sm")
        pass

    def parse_cv(self, text: List[str]) -> CVModel:
        full_text = " ".join(text)
        # doc = self.nlp(full_text)
        # print(doc)
        # Example parsing logic (customize as needed)
        name = "John Doe NLP"
        title = "Senior Software Engineer"
        email = "john.doe@example.com"
        phone = "123-456-7890"
        location = "New York, USA"
        linkedin = "https://linkedin.com/in/johndoe"
        github = "https://github.com/johndoe"
        website = "https://johndoe.com"

        # Contact information
        contact = Contact(
            email=email,
            phone=phone,
            location=location,
            linkedin=linkedin,
            github=github,
            website=website
        )

        # Education
        education = [
            Education(
                degree="Bachelor of Science",
                field_of_study="Computer Science",
                institution="University of Example",
                location="New York, USA",
                start_date="2015-09-01",
                end_date="2019-06-01"
            ),
            Education(
                degree="Master of Science",
                field_of_study="Data Science",
                institution="Example Tech University",
                location="New York, USA",
                start_date="2019-09-01",
                end_date="2021-06-01"
            )
        ]

        # Experience
        experience = [
            Experience(
                position="Data Analyst",
                company="Tech Solutions Inc.",
                location="New York, USA",
                start_date="2021-06-01",
                end_date="2023-12-01",
                responsibilities="Analyzed large datasets to identify trends and improve business decisions."
            ),
            Experience(
                position="Data Scientist",
                company="Innovative Data Co.",
                location="Remote",
                start_date="2023-12-01",
                end_date="Present",
                responsibilities="Developed machine learning models for predictive analytics and automation."
            )
        ]

        # Skills
        skills = ["Python", "SQL", "Machine Learning", "Data Visualization", "Big Data Technologies"]
        skills_from_work_experience = ["Data Analysis", "Statistical Modeling", "Data Wrangling",
                                       "Time Series Forecasting"]

        # Return the final CVModel
        return CVModel(
            name=name,
            title=title,
            contact=contact,
            education=education,
            experience=experience,
            skills=skills,
            skills_from_work_experience=skills_from_work_experience
        )