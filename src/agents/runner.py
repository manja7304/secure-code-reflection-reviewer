"""Reflection agent: initial review → critique → final verdict."""

from __future__ import annotations

import json
from pathlib import Path

from src.tools.code_tools import analyze_snippet, map_cwe, reflection_critique

DEMO = Path(__file__).resolve().parent.parent.parent / "demo-data"


def run_agent(query: str, context: dict | None = None) -> dict:
    snippet_id = (context or {}).get("snippet_id", "SNIP-001")
    snippets = json.loads((DEMO / "vulnerable_snippets.json").read_text(encoding="utf-8"))
    snippet = next((s for s in snippets if s["id"] == snippet_id), snippets[0])
    trace = []
    initial = json.loads(analyze_snippet.invoke(json.dumps(snippet)))
    trace.append({"pass": "initial", "findings": initial})
    critique = json.loads(reflection_critique.invoke(json.dumps({"snippet": snippet, "initial": initial})))
    trace.append({"pass": "reflection", "critique": critique})
    cwes = json.loads(map_cwe.invoke(critique.get("confirmed_issue", "injection")))
    trace.append({"pass": "cwe_map", "cwes": cwes})
    answer = f"Verdict: {critique.get('verdict', 'review')} — CWEs: {cwes}"
    return {"answer": answer, "trace": trace, "metadata": {"snippet_id": snippet_id}}
