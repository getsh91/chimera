# OpenClaw Integration Plan (Conceptual)

## Purpose
This document outlines how Project Chimera can integrate with an Agent Social Network such as OpenClaw.

This is a design-level specification; no implementation is required at this stage.

---

## 1. Capability Advertisement

Each Chimera agent can publish:
- Supported skills (by name and version)
- Confidence thresholds
- Availability state (idle, busy, degraded)

This allows other agents to discover Chimera as a potential collaborator.

---

## 2. Status & Health Signals

Agents may publish:
- Last successful execution timestamp
- Error rate (rolling window)
- Budget utilization
- HITL queue depth

These signals allow external systems to assess reliability.

---

## 3. Task Negotiation (Future)

Chimera agents are designed to support:
- Incoming task proposals
- Budget-aware acceptance or rejection
- Confidence-based delegation

All accepted tasks are converted into internal `AgentTask` objects and governed by the Planner → Worker → Judge pipeline.

---

## 4. Identity & Revocation

- Agent identities are cryptographically verifiable
- Credentials are scoped and revocable
- Revocation occurs at the MCP or capability boundary

---

## 5. Safety Boundaries

- External agents cannot bypass Chimera governance
- All external requests are subject to:
  - Schema validation
  - Confidence scoring
  - HITL escalation rules

This ensures interoperability without sacrificing safety.
