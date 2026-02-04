# Functional Specification

## Personas
- **Network Operator:** Sets goals and monitors fleet.
- **HITL Moderator:** Reviews flagged content/actions.
- **Developer/Architect:** Extends MCP servers and runtime skills.

## Core User Stories (Planner / Worker / Judge)

### Trend & Perception
- As a **Planner**, I need to create “trend scan” tasks on an interval, so the agent can react to new opportunities.
- As a **Worker**, I need to read trends from MCP resources, so I can return normalized trend data.
- As a **Judge**, I need to validate trend results against schema and confidence thresholds, so low-quality signals don’t pollute state.

### Content Generation
- As a **Planner**, I need to generate content tasks from a trend + campaign goal, so content creation is goal-driven.
- As a **Worker**, I need to generate captions/scripts with persona constraints, so outputs stay on-brand.
- As a **Judge**, I need to classify sensitive topics and route to HITL, so risky content is never auto-posted.

### Engagement Loop
- As a **Planner**, I need to turn mentions/comments into reply tasks, so the agent engages continuously.
- As a **Worker**, I need to draft a reply using relevant memory, so the response is contextual and consistent.
- As a **Judge**, I need to approve/reject/escalate replies based on confidence and safety tags.

### Publishing
- As a **Worker**, I need to publish content via an MCP tool, so the runtime stays platform-agnostic.
- As a **Judge**, I need a “dry-run” mode and audit trail, so we can test safely and debug failures.

### Agentic Commerce (Governed)
- As a **Planner**, I need to check wallet balance before cost-incurring workflows.
- As a **Worker**, I need to propose transaction intents (not execute blindly), so the CFO Judge can govern spending.
- As a **CFO Judge**, I need to enforce daily spend limits and route anomalies to HITL.

## Non-Functional Requirements (Behavior)
- Every worker output MUST include:
  - `confidence_score` (0.0–1.0)
  - `safety_tags` (list)
  - `citations` (where applicable, e.g., trend sources)
- Sensitive topics (politics, health advice, financial advice, legal claims) MUST be HITL.
- Medium confidence (0.70–0.90) MUST be async HITL.
- High confidence (>0.90) MAY be auto-approved if not sensitive.
