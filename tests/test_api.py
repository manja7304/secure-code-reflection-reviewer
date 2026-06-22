from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_agent_run():
    r = client.post("/api/v1/agent/run", json={"query": "test query"})
    assert r.status_code == 200
    body = r.json()
    assert "answer" in body
    assert "trace" in body
