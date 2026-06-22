"""FastAPI application entrypoint."""

from fastapi import FastAPI

from src.api.routes import router
from src.config import settings

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "project": "secure-code-reflection-reviewer"}


@app.get("/metrics")
def metrics() -> dict:
    return {"requests_total": 0, "agent_runs_total": 0}
