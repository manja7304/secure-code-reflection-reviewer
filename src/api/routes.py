"""API routes for agent invocation."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.agents.runner import run_agent

router = APIRouter(prefix="/api/v1")


class AgentRequest(BaseModel):
    query: str = Field(..., min_length=1, description="User or security analyst query")
    context: dict | None = None


class AgentResponse(BaseModel):
    answer: str
    trace: list[dict]
    metadata: dict = {}


@router.post("/agent/run", response_model=AgentResponse)
def agent_run(request: AgentRequest) -> AgentResponse:
    result = run_agent(request.query, context=request.context or {})
    return AgentResponse(**result)
