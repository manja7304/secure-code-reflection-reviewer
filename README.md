# Secure Code Reflection Reviewer

![CI](https://github.com/manja7304/secure-code-reflection-reviewer/actions/workflows/ci.yml/badge.svg)

> **Part of [Cyber AI Portfolio](https://github.com/manja7304)** — 10 containerized security AI repos.

## Problem

Security teams face backlog and false-positive fatigue in **SAST-style code review**. This repo demonstrates a production-style **Reflection / Self-Critique** agent using **LangChain**.

Two-pass reflection agent with CWE mapping over vulnerable code snippets.

## Architecture

```mermaid
flowchart TB
  User[Security Analyst] --> API[FastAPI]
  API --> Agent[LangChain Agent]
  Agent --> Tools[Security Tools]
  Agent --> LLM[Ollama llama3.2]
  Tools --> DemoData[(Synthetic Demo Data)]
```

## Design Patterns

| Pattern | Where Used | Alternative Considered |
|---------|------------|------------------------|
| Reflection / Self-Critique | Core agent flow | Simple prompt chain |
| Tool Calling | Structured security actions | Raw LLM-only answers |
| Ollama-first LLM | `src/llm/factory.py` | Cloud-only APIs |

## Quickstart

```bash
cp .env.example .env
docker compose -f docker/docker-compose.yml up --build
curl -X POST http://localhost:8080/api/v1/agent/run \
  -H "Content-Type: application/json" \
  -d '{"query": "Analyze demo security scenario"}'
```

## Video Demo

[![Demo Video](https://img.shields.io/badge/Demo-YouTube-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=PLACEHOLDER)

> Record using `demos/RECORDING_SCRIPT.md` and replace PLACEHOLDER with your unlisted YouTube link.

## Evaluation

- Unit tests pass with `USE_MOCK_LLM=true` (no API keys required)
- See `eval/` for RAGAS or agent success metrics where applicable
- Target latency: &lt;5s per query on local Ollama (hardware dependent)

## Security & Ethics

Synthetic demo data only. See [SECURITY.md](SECURITY.md). No unauthorized scanning.

## Documentation

- [Architecture](docs/architecture.md)
- [Design Patterns](docs/design-patterns.md)
- [Demo Data](docs/demo-data.md)
- [Runbook](docs/runbook.md)
