# Design Patterns

## Primary: Reflection / Self-Critique

Implemented with **LangChain** for explicit control flow and testability.

### Why this pattern?

- Maps to real security ops workflows
- Tool calls provide auditable steps
- Mock LLM enables CI without GPU

### Tradeoffs

| Pros | Cons |
|------|------|
| Traceable steps | More boilerplate than single prompt |
| Testable tools | Requires good demo data |
