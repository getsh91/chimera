import json
import importlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"

REQUIRED_CONTRACT_FIELDS = {
    "name",
    "version",
    "entrypoint",
    "description",
    "input_schema",
    "output_schema",
}


def test_each_skill_has_contract_and_entrypoint_exported():
    assert SKILLS_DIR.exists(), "skills/ directory missing"

    skill_dirs = [p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("__")]
    assert skill_dirs, "No skill folders found under skills/"

    for skill_dir in skill_dirs:
        contract_path = skill_dir / "contract.json"
        assert contract_path.exists(), f"Missing contract.json for skill: {skill_dir.name}"

        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        missing = REQUIRED_CONTRACT_FIELDS - set(contract.keys())
        assert not missing, f"{skill_dir.name} contract missing fields: {sorted(missing)}"

        entrypoint = contract["entrypoint"]
        module_name = f"skills.{skill_dir.name}"

        mod = importlib.import_module(module_name)
        assert hasattr(mod, entrypoint), (
            f"{skill_dir.name} must export entrypoint '{entrypoint}' in {module_name}"
        )
