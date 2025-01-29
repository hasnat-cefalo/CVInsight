from openai import OpenAI
from typing import List
from app.config import settings
from app.models.cv_model import CVModel, Experience, Education, Contact
from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt

class ChatGPTService(BaseService):
    def __init__(self):
        self.model = settings.openai_model
        self.client = OpenAI(
            api_key=settings.openai_api_key,  # This is the default and can be omitted
        )

    def _call_api(self, text: str) -> dict:
        """Calls OpenAI model to extract CV details."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                store=False,
                messages=[{"role": "system", "content": "You are a CV parsing assistant."},
                          {"role": "user", "content": prompt},
                          {"role": "user", "content": f"###pdf content\n{text}"}],
                response_format={'type': 'json_object'},
                timeout=8
            )
            print(response)
            return response.choices[0].message
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}")

    def parse_cv(self, text: List[str]) -> CVModel:
        full_text = " ".join(text)
        api_response = self._call_api(full_text)

        # Convert OpenAI's response (string) to structured JSON
        structured_data = eval(api_response)  # Ensure a safer parsing method in production

        name = structured_data.get("name", "Unknown")
        title = structured_data.get("title", "N/A")
        contact = Contact(**structured_data.get("contact", {}))

        education = [
            Education(**edu) for edu in structured_data.get("education", [])
        ]
        experience = [
            Experience(**exp) for exp in structured_data.get("experience", [])
        ]
        skills = structured_data.get("skills", [])

        return CVModel(name=name, title=title, contact=contact, education=education, experience=experience, skills=skills, skills_from_work_experience=skills)