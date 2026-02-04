# Technical Specification

## Canonical Data Contracts
Schemas live in `specs/schemas/`.

### 1) Agent Task Schema
- File: `specs/schemas/task.schema.json`
- Used between Planner → Worker.

### 2) MCP Tool Definition Schema
- File: `specs/schemas/mcp_tool.schema.json`
- Used to validate tool contract definitions.

## Required Skill Contracts
Each skill MUST contain:
- `skills/<skill_name>/contract.json`
- `skills/<skill_name>/__init__.py` exporting the entrypoint named in the contract (may be stub)

Minimum required skills for repo readiness:
1. `trend_fetcher`
2. `content_generator`
3. `social_publisher`

## Governance Logic (Judge)
### Confidence Routing
- > 0.90 and not sensitive → Auto-approve
- 0.70–0.90 or sensitive → HITL queue
- < 0.70 → Reject + request retry

### Sensitive Topics
Must be tagged and routed to HITL regardless of confidence:
- Politics
- Health advice
- Financial advice
- Legal claims

## Storage Strategy
- PostgreSQL: tasks, results, approvals, budgets, audit logs
- Redis: task_queue, review_queue, ephemeral cache
- Weaviate: semantic memory & persona memory objects

## OCC (Optimistic Concurrency Control)
Judge commits must include a `state_version` check:
- If current `state_version` differs from worker’s `input_state_version`, reject commit and re-queue task.

## Observability & Audit
All tool calls MUST produce a structured “tool_call_audit” record with:
- tool name, args hash, timestamp, outcome, correlation_id
