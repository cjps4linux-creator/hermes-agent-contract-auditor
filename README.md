# Hermes Agent Contract Auditor

Validate an agent contract against the Hermes contract schema and produce structured audit reports.

## Install
```bash
git clone <repo-url>
cd hermes-agent-contract-auditor
uv venv
uv pip install pydantic
```

## Usage
```bash
uv run python -m auditor.cli agent/agent.spec.md
uv run python -m auditor.cli agent/agent.spec.md --json
```

## Sellable Assets
- Auditor CLI with JSON/text reports
- Example contract with filled schema
- README with install + usage

## Offered As
- Digital product / consulting add-on
