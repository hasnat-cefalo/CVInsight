import json

from ollama import Client

from app.config import settings
from app.models.cv_model import CVModel
from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt


class OllamaService(BaseService):
    def __init__(self):
        self.model = settings.ollama_model
        self.client = Client(
            host=settings.ollama_host,
        )

    def _call_api(self, text: str) -> dict:
        """Calls Ollama model to extract CV details."""
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        'role': 'user',
                        'content': f"You are a CV parsing assistant.\n{prompt}\n###pdf content\n{text}",
                    },
                ],
                format=CVModel.model_json_schema(),
            )
            print(response.message.content)
            print(type(response.message.content))

            return json.loads(response.message.content)
        except Exception as e:
            raise RuntimeError(f"Ollama API error: {e}")
