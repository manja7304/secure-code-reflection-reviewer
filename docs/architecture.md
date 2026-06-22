# Architecture — Secure Code Reflection Reviewer

## Context

Analysts interact via REST API. The agent orchestrates security tools over bundled synthetic data.

## Containers

- **app** — FastAPI + agent runtime
- **ollama** — Local LLM (llama3.2)
- **chroma/postgres** — Optional persistence layers

## Components

- `src/api/` — HTTP layer
- `src/agents/` — Framework-specific workflows
- `src/tools/` — Deterministic security utilities
- `src/llm/factory.py` — Provider abstraction
