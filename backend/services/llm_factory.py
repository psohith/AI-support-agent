from typing import Any, Type
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from config.settings import get_settings


class LLMFactory:
    def __init__(self, provider: str):
        self.provider = provider
        self.settings = getattr(get_settings(), provider)
        self.client = self._initialize_client()

    def _initialize_client(self) -> Any:
        """Initialize the LangChain client for the specified provider."""
        if self.provider == "openai":
            return ChatOpenAI(
                model=self.settings.default_model,
                temperature=self.settings.temperature,
                api_key=self.settings.api_key,
                max_retries=self.settings.max_retries,
                max_tokens=self.settings.max_tokens,
            )
        raise ValueError(f"Unsupported LLM provider: {self.provider}")

    def create_completion(self, response_model: Type[BaseModel], messages) -> Any:
        """Generate a response using the LLM."""
        response = self.client.invoke(messages)
        response_content = dict(response)["content"]
        return response_content