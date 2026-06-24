#!/usr/bin/env python3
"""One-command demo runner for screen recording (mock LLM, no Docker/Ollama)."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH when run as `python scripts/run_demo.py`
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ANSI colors for terminal recording
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def banner(text: str) -> None:
    print(f"\n{BOLD}{CYAN}{text}{RESET}")
    print(f"{DIM}{'=' * min(len(text), 60)}{RESET}")


def section(title: str) -> None:
    print(f"\n{BOLD}{YELLOW}▸ {title}{RESET}")


def main() -> int:
    os.environ.setdefault("USE_MOCK_LLM", "true")
    os.environ.setdefault("LLM_PROVIDER", "mock")

    banner("Secure Code Reflection Reviewer")
    print(f"{DIM}Pattern: Reflection / Self-Critique · USE_MOCK_LLM=true (no Ollama/Docker required){RESET}\n")
    section("Agent API demo")
    from fastapi.testclient import TestClient
    from src.api.main import app

    client = TestClient(app)
    request_body = {'query': 'review', 'context': {'snippet_id': 'SNIP-003'}}
    print(f"  POST /api/v1/agent/run")
    print(f"  {DIM}Request:{RESET}")
    print(json.dumps(request_body, indent=2))

    response = client.post("/api/v1/agent/run", json=request_body)
    print(f"\n  {GREEN}HTTP {response.status_code}{RESET}")
    body = response.json()
    print(json.dumps(body, indent=2))

    section("Agent trace excerpt")
    trace = body.get("trace", [])
    if trace:
        excerpt = trace[:3]
        print(json.dumps(excerpt, indent=2))
        if len(trace) > 3:
            print(f"  {DIM}… {len(trace) - 3} more trace entries{RESET}")
    else:
        print("  (no trace)")

    section("Captured output saved to demos/captured/")
    captured = Path(__file__).resolve().parent.parent / "demos" / "captured"
    print(f"  {DIM}{captured}{RESET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
