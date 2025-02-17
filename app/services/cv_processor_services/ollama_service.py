import json
from typing import Optional

from ollama import Client

# from app.config import settings
from app.models.cv_model import CVModel
from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt


class OllamaService(BaseService):
    def __init__(self, model: str):
        self.model = model
        self.client = Client(
            host="localhost:11434",
        )

    def _call_api(self, text: str) -> dict:
        """
        Calls Ollama model to extract CV details.
        Reference: https://github.com/ollama/ollama-python
        """
        try:
            response = self.client.chat(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that organizes CV text into structured JSON format."
                    },
                    {
                        'role': 'user',
                        'content': f"{prompt}\nCV Text:\n{text}",
                    },
                ],
                format=CVModel.model_json_schema(),
            )
            return json.loads(response.message.content)
        except Exception as e:
            raise RuntimeError(f"Ollama API error: {e}")
