from typing import Dict, Any

from app.core.config import settings


class LLMClient:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def explain(self, text: str, context: Dict[str, Any]) -> str:
        if self.provider == "stub":
            return text
        return text


llm_client = LLMClient(settings.llm_provider)
