# Runbook

## Environment

| Variable | Default | Description |
|----------|---------|-------------|
| LLM_PROVIDER | ollama | ollama, openai, gemini, mock |
| OLLAMA_MODEL | llama3.2 | Local model name |
| USE_MOCK_LLM | false | Set true for tests |

## Troubleshooting

1. **Ollama model missing** — `docker exec -it <ollama> ollama pull llama3.2`
2. **Chroma connection** — verify CHROMA_HOST/PORT in `.env`
3. **Tests fail** — run with `USE_MOCK_LLM=true pytest`
