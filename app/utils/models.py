from enum import Enum


class ModelType(str, Enum):
    CHATGPT = "chatgpt"
    DEEPSEEK_API = "deepseek-api"
    DEEPSEEK_R1_1_5B = "deepseek-r1:1.5b"
    DEEPSEEK_R1_8B = "deepseek-r1:8b"
    DEEPSEEK_R1_14B = "deepseek-r1:14b"
    MISTRAL = "mistral"
    QWEN_1_8B="qwen:1.8b"
    QWEN_14B="qwen:14b"
    GEMINI = "gemini"
    OLLAMA = "ollama"
