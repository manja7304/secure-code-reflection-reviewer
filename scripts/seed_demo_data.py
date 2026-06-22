#!/usr/bin/env python3
import json
from pathlib import Path

snippets = []
for i in range(1, 31):
    lang = "python" if i % 2 else "javascript"
    if i % 3 == 0:
        code = 'query = f"SELECT * FROM users WHERE id={user_id}"\ncursor.execute(query)'
    elif i % 3 == 1:
        code = 'element.innerHTML = userInput'
    else:
        code = 'api_key = "sk-demo-not-real"'
    snippets.append({"id": f"SNIP-{i:03d}", "lang": lang, "code": code})
DEMO = Path(__file__).resolve().parent.parent / "demo-data"
DEMO.mkdir(parents=True, exist_ok=True)
(DEMO / "vulnerable_snippets.json").write_text(json.dumps(snippets, indent=2), encoding="utf-8")
print(f"Seeded {len(snippets)} snippets")
