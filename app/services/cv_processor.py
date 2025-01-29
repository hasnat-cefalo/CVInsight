from typing import List

from app.models.cv_model import CVModel
from app.services.cv_processor_services.chatgpt_service import ChatGPTService
from app.services.cv_processor_services.deepseek_service import DeepSeekService
from app.services.cv_processor_services.nlp_service import NLPService


class CVProcessor:
    @staticmethod
    def parse_cv(text: List[str], service_type: str) -> CVModel:
        service_map = {
            "chatgpt": ChatGPTService,
            "deepseek": DeepSeekService,
            "nlp": NLPService,
        }
        service_class = service_map.get(service_type)
        service = service_class()

        return service.parse_cv(text)
