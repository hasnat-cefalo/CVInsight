import sys
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

# Define the path to .env
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"

# Check if .env exists
if not ENV_FILE.exists():
    print(f"⚠️ Warning: .env file not found at {ENV_FILE}", file=sys.stderr)


class Settings(BaseSettings):
    deepseek_api_key: Optional[str]
    deepseek_model: Optional[str]
    openai_api_key: Optional[str]
    openai_model: Optional[str]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra='ignore')


settings = Settings()
