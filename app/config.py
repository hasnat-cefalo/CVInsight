from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    deepseek_api_key: Optional[str]
    deepseek_model: Optional[str]
    openai_api_key: Optional[str]
    openai_model: Optional[str]
    gemini_api_key: Optional[str]
    gemini_model: Optional[str]
    ollama_host: Optional[str]
    ollama_model: Optional[str]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra='ignore')


settings = Settings()
