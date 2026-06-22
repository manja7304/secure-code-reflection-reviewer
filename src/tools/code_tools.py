"""Code review tools with reflection."""

from __future__ import annotations

import ast
import json

from langchain_core.tools import tool

RULES = {
    "sql_injection": ["execute(", "format(", 'f"SELECT'],
    "xss": ["innerHTML", "dangerouslySetInnerHTML"],
    "hardcoded_secret": ["password =", "api_key =", "SECRET"],
}


@tool
def analyze_snippet(snippet_json: str) -> str:
    """Run static analysis heuristics on a code snippet."""
    snippet = json.loads(snippet_json)
    code = snippet.get("code", "")
    issues = []
    for name, patterns in RULES.items():
        if any(p in code for p in patterns):
            issues.append({"type": name, "severity": "high"})
    if snippet.get("lang") == "python":
        try:
            ast.parse(code)
        except SyntaxError as e:
            issues.append({"type": "syntax_error", "detail": str(e)})
    return json.dumps({"issues": issues})


@tool
def reflection_critique(payload_json: str) -> str:
    """Second-pass reflection to catch missed vulnerabilities."""
    payload = json.loads(payload_json)
    initial = payload.get("initial", {})
    snippet = payload.get("snippet", {})
    issues = initial.get("issues", [])
    # Reflection catches SQLi if only XSS was found initially
    code = snippet.get("code", "")
    confirmed = "injection"
    if any(i["type"] == "sql_injection" for i in issues):
        confirmed = "sql_injection"
    elif "innerHTML" in code:
        confirmed = "xss"
    return json.dumps({
        "verdict": "fail" if issues else "pass",
        "confirmed_issue": confirmed,
        "missed_on_first_pass": confirmed == "sql_injection" and len(issues) == 0,
    })


@tool
def map_cwe(issue_type: str) -> str:
    """Map issue type to CWE identifiers."""
    mapping = {"sql_injection": ["CWE-89"], "xss": ["CWE-79"], "injection": ["CWE-74"], "hardcoded_secret": ["CWE-798"]}
    return json.dumps({"cwes": mapping.get(issue_type, ["CWE-OTHER"])})
