# Demo Walkthrough — Secure Code Reflection Reviewer

**Pattern:** Reflection / Self-Critique  
**Captured:** 2026-06-24 with `USE_MOCK_LLM=true` (no Docker/Ollama required)

---

## Prerequisites

```bash
cp .env.example .env   # optional for mock demo
pip install -r requirements.txt
```

---

## Step 1 — One-command demo

```bash
export USE_MOCK_LLM=true
python scripts/run_demo.py
```

This runs the same FastAPI `TestClient` path as CI — real code, real JSON output.

### Step 2 — Agent API call

```bash
curl -X POST http://localhost:8080/api/v1/agent/run \
  -H "Content-Type: application/json" \
  -d '{"query": "review", "context": {"snippet_id": "SNIP-003"}}'
```

Or offline (no server):

```bash
USE_MOCK_LLM=true python scripts/run_demo.py
```

**Request (`demos/captured/request.json`):**

```json
{
  "query": "review",
  "context": {
    "snippet_id": "SNIP-003"
  }
}
```

**Response (`demos/captured/response.json`):**

```json
{
  "answer": "Verdict: fail \u2014 CWEs: {'cwes': ['CWE-89']}",
  "trace": [
    {
      "pass": "initial",
      "findings": {
        "issues": [
          {
            "type": "sql_injection",
            "severity": "high"
          }
        ]
      }
    },
    {
      "pass": "reflection",
      "critique": {
        "verdict": "fail",
        "confirmed_issue": "sql_injection",
        "missed_on_first_pass": false
      }
    },
    {
      "pass": "cwe_map",
      "cwes": {
        "cwes": [
          "CWE-89"
        ]
      }
    }
  ],
  "metadata": {
    "snippet_id": "SNIP-003"
  }
}
```

### Step 3 — Agent trace excerpt

```json
[
  {
    "pass": "initial",
    "findings": {
      "issues": [
        {
          "type": "sql_injection",
          "severity": "high"
        }
      ]
    }
  },
  {
    "pass": "reflection",
    "critique": {
      "verdict": "fail",
      "confirmed_issue": "sql_injection",
      "missed_on_first_pass": false
    }
  }
]
```

---

## Architecture callout (2-min video)

> Reflection loop: initial review → self-critique → revised verdict on 30 synthetic code snippets (SAST-style).

Highlight in your recording:

1. **Problem → pattern** — why this agent architecture fits the security domain
2. **Tool/trace output** — show structured JSON, not just the final answer
3. **`docs/architecture.md`** — Mermaid diagram for the close

---

## Artifacts

| File | Description |
|------|-------------|
| [`demos/captured/request.json`](captured/request.json) | API request payload |
| [`demos/captured/response.json`](captured/response.json) | Live captured response |
| [`demos/captured/trace.json`](captured/trace.json) | Agent trace array |
| [`demos/captured/terminal-session.txt`](captured/terminal-session.txt) | Terminal replay for Loom |

---

## Record your video

```bash
python scripts/run_demo.py
```

Use [`demos/RECORDING_SCRIPT.md`](RECORDING_SCRIPT.md) for shot list and narration cues.
