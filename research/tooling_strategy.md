# Tooling & MCP Strategy

## Developer MCP Servers (IDE-time)
These MCP servers assist humans during development and debugging:
- filesystem-mcp: safe file inspection/editing
- git-mcp: commit history inspection and diff reasoning
- sqlite-mcp (optional): local structured data experiments

These are NOT available to runtime agents.

## Runtime Capabilities
Runtime agents rely on:
- Skills (internal, versioned interfaces in `skills/`)
- MCP Servers (external world connectors)

## Skill vs MCP Rule
- Skills = “what the agent can do” (logic orchestration)
- MCP Servers = “how the agent touches the world” (I/O, APIs, wallets)

Agents must never bypass MCP to reach external systems.

## OpenClaw Alignment
Chimera agents will:
- Advertise available skills as capabilities
- Publish health/status signals
- Respect rate limits and revocation policies

This enables future agent-to-agent coordination and discovery.
