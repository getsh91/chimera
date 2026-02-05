# Project Chimera — Tooling Strategy

## Purpose
This document defines the tooling strategy for Project Chimera, with a clear separation between:

1. **Developer Tooling (MCP for Humans)**
2. **Runtime Tooling (Skills + MCP for Agents)**

This separation is critical to prevent capability leakage, reduce security risk, and ensure that autonomous agents operate only within explicitly governed boundaries.

---

## Core Principle: Separation of Concerns

**Humans and Agents do not share tools.**

- Developers use MCP servers to *build, inspect, and govern* the system.
- Agents use Skills and MCP servers to *act in the world*.

This distinction ensures:
- Auditability
- Security
- Predictable behavior at scale
- Clear blast-radius control

---

## 1. Developer Tooling (MCP for Development)

### Purpose
Developer MCP servers exist to:
- Improve developer velocity
- Provide observability and traceability
- Act as a “black box recorder” for agent development
- Enforce spec-driven workflows in the IDE

These tools are **never accessible to runtime agents**.

---

### Active Developer MCP Servers

#### Tenx MCP Sense (Telemetry & Traceability)
- **Role:** Observability, activity tracing, agent behavior recording
- **Why:** Required by the assignment as a “flight recorder”
- **Usage:** Always connected during development via IDE
- **Evidence:** Active MCP server connection in Cursor

This satisfies:
> “You must keep the Tenx MCP Sense server connected to your IDE at all times.”

---

#### IDE-integrated MCP (Cursor MCP Host)
- **Role:** Context-aware AI coding assistant
- **Enforcement:**
  - Obeys `.cursor/rules`
  - Must read `specs/` before generating code
  - Explains plan before implementation

This converts AI assistance from “vibe coding” into **governed engineering**.

---

### Developer MCP Summary Table

| MCP Server | Scope | Purpose |
|----------|------|--------|
| Tenx MCP Sense | Dev-only | Telemetry, traceability |
| Cursor MCP Host | Dev-only | Spec-aware code generation |
| Git / FS MCPs (future) | Dev-only | Safe repo & file ops |

---

## 2. Runtime Tooling (Agent Capabilities)

Runtime agents **never receive developer MCP access**.

They operate through **two controlled layers**:
1. Skills (internal)
2. MCP Servers (external)

---

## 2.1 Skills (Internal Runtime Capabilities)

### Definition
A **Skill** is a versioned, contract-defined capability package that:
- Executes a single responsibility
- Is called by a Worker
- May internally invoke MCP tools
- Has no direct access to credentials

### Characteristics
- Defined in `skills/`
- Each skill has:
  - `contract.json` (input/output schema)
  - Python module exporting an entrypoint
- Enforced by tests (`test_skills_interface.py`)

### Example Skills
- `trend_fetcher` — aggregates trend signals
- `content_generator` — generates captions/scripts
- `social_publisher` — prepares publish payloads

Skills are **replaceable, testable, and auditable**.

---

## 2.2 MCP Servers (Runtime External Interfaces)

### Role
MCP servers are the **only bridge** between agents and the external world.

They:
- Own credentials
- Enforce rate limits
- Provide logging and dry-run capabilities
- Abstract volatile third-party APIs

### Examples
- `mcp-server-social` (Twitter / Instagram / Threads)
- `mcp-server-news` (RSS / search)
- `mcp-server-generation` (image/video tools)
- `mcp-server-coinbase` (wallet + transactions)

### Boundary Rule (Hard Constraint)
> **Core agent logic and Skills MUST NOT call external APIs directly.**

All external interaction flows through MCP.

---

## 3. Skills vs MCP Servers — Clear Boundary

| Dimension | Skills | MCP Servers |
|--------|-------|-------------|
| Ownership | Chimera repo | External service |
| Responsibility | Business logic | External integration |
| Credentials | ❌ None | ✅ Owned by server |
| Testable | ✅ Yes | ⚠️ Mocked |
| Called by | Worker | Worker / Skill |
| Governed by | Contracts + tests | MCP protocol |

This boundary is what makes Chimera **scalable and safe**.

---

## 4. Governance & Safety Enforcement

Tooling choices directly enforce governance:

- **Specs** define intent
- **Tests** define acceptable behavior
- **CI** enforces compliance
- **Judge agents** enforce runtime policy
- **MCP boundary** prevents uncontrolled actions

No tool exists without:
- A declared contract
- A governing layer
- A revocation point

---

## 5. Why This Tooling Strategy Matters

Without this separation:
- Agents would accumulate uncontrolled power
- Bugs would propagate at scale
- Credentials would leak
- Behavior would drift from intent

With this strategy:
- Agents remain autonomous but bounded
- Humans govern policy, not execution
- The system scales safely to thousands of agents

---

## Conclusion
Project Chimera’s tooling strategy transforms AI agents from fragile scripts into governed, auditable digital workers.

By separating **Developer MCP tooling** from **Runtime Skills and MCP servers**, the system enforces security, traceability, and alignment — fulfilling both the technical and ethical requirements of autonomous influencer systems.
