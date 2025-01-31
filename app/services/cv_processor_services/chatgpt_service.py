from openai import OpenAI

from app.services.cv_processor_services.base_service import BaseService
from app.utils.prompt import prompt


class ChatGPTService(BaseService):
    def __init__(self, model: str, api_key: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, )

    def _call_api(self, text: str) -> dict:
        """
        Calls OpenAI model to extract CV details.
        Reference: https://platform.openai.com/docs/api-reference/introduction
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                store=False,
                messages=[
                    {"role": "system", "content": "You are a CV parsing assistant."},
                    {"role": "user", "content": prompt},
                    {"role": "user", "content": f"###pdf content\n{text}"}
                ],
                response_format={'type': 'json_object'},
                timeout=8
            )
            print(response.choices[0].message)
            return response.choices[0].message
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}")
