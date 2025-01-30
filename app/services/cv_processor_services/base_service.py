import json
import logging
from abc import ABC, abstractmethod

from app.models.cv_model import CVModel, Contact, Education, Experience

logger = logging.getLogger(__name__)

class BaseService(ABC):
    @abstractmethod
    def _call_api(self, text: str) -> CVModel:
        """call the api of specific service."""
        pass

    def parse_cv(self, text: str) -> CVModel:
        structured_data: json = self._call_api(text)

        name = structured_data.get("name", "N/A")
        title = structured_data.get("title", "N/A")
        contact = Contact(**structured_data.get("contact", {}))

        education = [
            Education(**edu) for edu in structured_data.get("education", [])
        ]
        experience = [
            Experience(**exp) for exp in structured_data.get("experience", [])
        ]
        skills = structured_data.get("skills", [])
        skills_from_work_experience = structured_data.get("skills_from_work_experience", [])

        return CVModel(name=name,
                       title=title,
                       contact=contact,
                       education=education,
                       experience=experience,
                       skills=skills,
                       skills_from_work_experience=skills_from_work_experience)
