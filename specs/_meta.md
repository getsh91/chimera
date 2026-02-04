# Project Chimera — Specs Meta

## Vision
Project Chimera is an autonomous influencer network. It operates a fleet of persistent AI influencer agents that:
- Research trends and opportunities
- Generate multimodal content (text/image/video)
- Manage engagement loops (mentions/comments/replies)
- Execute governed economic actions (agentic commerce)

## Non-Negotiable Constraints
1. **Spec-first:** Implementation code MUST NOT be written until specs and schemas exist.
2. **MCP-only I/O:** The core agent runtime MUST NOT call third-party APIs directly. All external interaction MUST occur via MCP Tools/Resources.
3. **Swarm architecture:** Planner → Worker → Judge pattern is mandatory.
4. **HITL governance:** Sensitive topics and medium-confidence outputs MUST route to human review.
5. **Traceability:** All critical actions MUST emit structured logs and tool-call audits (for MCP Sense + repo auditability).
6. **Security:** No secrets in git. Wallet keys must be injected via environment/secrets manager (never logged).

## Definition of Done (Repo Readiness)
A repository is “ready for AI swarm implementation” when it contains:
- Full specs in `specs/` including JSON schemas
- Skills scaffolding in `skills/` with contracts
- Failing tests in `tests/` that enforce contracts
- Dockerfile + Makefile + GitHub Actions CI
- AI governance policy (.cursor/rules + .coderabbit.yaml)

## Out of Scope (for this repo phase)
- Real social posting to production accounts
- Real wallet transfers on mainnet
- Media generation integrations beyond mocked/stubbed skill interfaces
