import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import json
import pytest
from pathlib import Path
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_task_schema_is_valid_jsonschema():
    schema_path = REPO_ROOT / "specs" / "schemas" / "task.schema.json"
    assert schema_path.exists(), "Missing specs/schemas/task.schema.json"

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)  # raises if invalid


def test_sample_trend_scan_task_conforms_to_schema():
    schema_path = REPO_ROOT / "specs" / "schemas" / "task.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)

    sample_task = {
        "task_id": "00000000-0000-0000-0000-000000000000",
        "task_type": "trend_scan",
        "priority": "medium",
        "context": {
            "goal_description": "Find trending topics in Ethiopian fashion",
            "persona_constraints": ["No politics", "Positive tone"],
            "required_resources": ["news://ethiopia/fashion/trends"],
            "input_state_version": "state_v1"
        },
        "assigned_worker_id": "worker-1",
        "created_at": "2026-02-04T12:00:00Z",
        "status": "pending"
    }

    errors = sorted(validator.iter_errors(sample_task), key=lambda e: e.path)
    assert not errors, "Sample task failed schema validation:\n" + "\n".join(
        f"- {list(e.path)}: {e.message}" for e in errors
    )


def test_trend_fetcher_is_stub_and_should_fail_for_now():
    # This defines the empty slot. Implementation comes later.
    from skills.trend_fetcher import run

    payload = {
        "niche": "fashion",
        "locale": "en-ET",
        "time_window_hours": 4,
        "sources": ["news://ethiopia/fashion/trends"]
    }

    with pytest.raises(NotImplementedError):
        run(payload)
