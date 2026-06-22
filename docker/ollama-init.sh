#!/bin/sh
set -e
echo "Pulling Ollama models..."
ollama pull llama3.2 || true
ollama pull nomic-embed-text || true
echo "Ollama init complete"
