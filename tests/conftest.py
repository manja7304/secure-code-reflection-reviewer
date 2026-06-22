import os

import pytest


@pytest.fixture(autouse=True)
def mock_llm_env(monkeypatch):
    monkeypatch.setenv("USE_MOCK_LLM", "true")
    monkeypatch.setenv("LLM_PROVIDER", "mock")
