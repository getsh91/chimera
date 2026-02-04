.PHONY: setup test spec-check docker-test

setup:
	uv sync

test:
	uv run pytest -q

spec-check:
	uv run python -m json.tool specs/schemas/task.schema.json > NUL
	uv run python -m json.tool specs/schemas/mcp_tool.schema.json > NUL

docker-test:
	docker build -f docker/Dockerfile -t chimera:dev .
	docker run --rm chimera:dev
