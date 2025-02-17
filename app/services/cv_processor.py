from typing import List

from app.config import settings
from app.models.cv_model import CVModel
from app.services.cv_processor_services.chatgpt_service import ChatGPTService
from app.services.cv_processor_services.deepseek_service import DeepSeekService
from app.services.cv_processor_services.gemini_service import GeminiService
from app.services.cv_processor_services.ollama_service import OllamaService
from app.utils.models import ModelType


class CVProcessor:
    @staticmethod
    def parse_cv(text: str, model_type: ModelType) -> CVModel:
        service_map = {
            ModelType.CHATGPT: ChatGPTService(model = settings.openai_model, api_key=settings.openai_api_key),
            ModelType.DEEPSEEK_API: DeepSeekService(model = settings.deepseek_model, api_key=settings.deepseek_api_key),
            ModelType.DEEPSEEK_R1_1_5B: OllamaService(model=ModelType.DEEPSEEK_R1_1_5B),
            ModelType.DEEPSEEK_R1_8B: OllamaService(model=ModelType.DEEPSEEK_R1_8B),
            ModelType.DEEPSEEK_R1_14B: OllamaService(model=ModelType.DEEPSEEK_R1_14B),
            ModelType.MISTRAL: OllamaService(model=ModelType.MISTRAL),
            ModelType.QWEN_1_8B: OllamaService(model=ModelType.QWEN_1_8B),
            ModelType.QWEN_14B: OllamaService(model=ModelType.QWEN_14B),
            ModelType.GEMINI: GeminiService(model=settings.gemini_model),
            ModelType.OLLAMA: OllamaService(model=settings.ollama_model),
        }
        service = service_map.get(model_type)

        return service.parse_cv(text)
