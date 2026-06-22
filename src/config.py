"""Application configuration."""

from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "cyber-ai-agent")
    llm_provider: str = os.getenv("LLM_PROVIDER", "mock")
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    chroma_host: str = os.getenv("CHROMA_HOST", "localhost")
    chroma_port: int = int(os.getenv("CHROMA_PORT", "8000"))
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./data/incidents.db")
    demo_data_dir: str = os.getenv("DEMO_DATA_DIR", "demo-data")


settings = Settings()
