from enum import Enum


class ModelType(str, Enum):
    CHATGPT = "chatgpt"
    DEEPSEEK_API = "deepseek-api"
    DEEPSEEK_R1_1_5B = "deepseek-r1-1.5b"
    DEEPSEEK_R1_7B = "deepseek-r1-7b"
    GEMINI = "gemini"
    OLLAMA = "ollama"
