# Chimera Skills (Runtime)

A **Skill** is a runtime capability package the Chimera agent can call.
Skills are not MCP servers. Skills may call MCP tools/resources internally (later), but their interface is stable and versioned.

## Contract Standard
Every skill MUST include:
- `contract.json` — declares the skill API (input/output schema + entrypoint)
- `__init__.py` — exports the entrypoint function declared in the contract

## Required Contract Fields
- `name` (string)
- `version` (string, semver)
- `entrypoint` (string, python function name)
- `description` (string)
- `input_schema` (JSON Schema object)
- `output_schema` (JSON Schema object)

## Design Rules
- Skills must be pure interfaces in this phase (stubs only).
- No network calls here yet.
- Tests will enforce that contracts exist and exports match entrypoints.
