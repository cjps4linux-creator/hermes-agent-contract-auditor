# Hermes Agent Contract Auditor

Validate an agent contract against the Hermes contract schema and produce structured audit reports with actionable findings.

## Install
```bash
cd hermes-agent-contract-auditor
uv venv
uv pip install pydantic
```

## Usage
```bash
uv run python -m auditor.cli agent/agent.spec.md
uv run python -m auditor.cli agent/agent.spec.md --json
```
