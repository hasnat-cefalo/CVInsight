import json
import logging
import traceback

import google.generativeai as genai
from app.config import settings
from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt

logger = logging.getLogger(__name__)

class GeminiService(BaseService):
    def __init__(self):
        self.model = settings.gemini_model
        genai.configure(api_key=settings.gemini_api_key)

    def _call_api(self, text: str) -> dict:
        """Calls Gemini model to extract CV details."""
        try:
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(
                contents=[
                    {"role": "user", "parts": ["You are a CV parsing assistant."]},
                    {"role": "user", "parts": [prompt]},
                    {"role": "user", "parts": [f"###pdf content\n{text}"]}
                ],
                generation_config=genai.GenerationConfig(
                    response_mime_type="application/json")
            )

            logger.info(f"Response: {response.text}")
            logger.info(f"json parsed: {response.text}")
            return json.loads(response.text)
        except Exception as e:
            logging.error(traceback.format_exc())
            raise RuntimeError(f"Gemini API error: {e}")
