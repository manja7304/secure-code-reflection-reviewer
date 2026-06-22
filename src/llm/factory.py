"""Ollama-first LLM factory with optional cloud providers."""

from __future__ import annotations

import os
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatGeneration, ChatResult


class MockChatModel(BaseChatModel):
    """Deterministic mock LLM for tests and offline demos."""

    default_response: str = "Mock agent response for testing."

    @property
    def _llm_type(self) -> str:
        return "mock"

    def _generate(self, messages: list, stop: list | None = None, **kwargs: Any) -> ChatResult:
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=self.default_response))])


def get_llm(**kwargs: Any) -> BaseChatModel:
    provider = os.getenv("LLM_PROVIDER", "mock").lower()
    model = os.getenv("OLLAMA_MODEL", "llama3.2")
    temperature = float(os.getenv("LLM_TEMPERATURE", "0.1"))

    if provider == "mock" or os.getenv("USE_MOCK_LLM", "").lower() in ("1", "true", "yes"):
        return MockChatModel(**kwargs)

    if provider == "ollama":
        from langchain_ollama import ChatOllama

        return ChatOllama(model=model, temperature=temperature, base_url=os.getenv("OLLAMA_BASE_URL", "http://ollama:11434"))

    if provider == "openai":
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), temperature=temperature)

    if provider == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI

        return ChatGoogleGenerativeAI(model=os.getenv("GEMINI_MODEL", "gemini-2.0-flash"), temperature=temperature)

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")
