# Hermes Agent Contract Auditor

Validate an agent contract against the Hermes contract schema and produce structured audit reports.

Built by Conrad CJ Wilson.

## What It Demonstrates

| Capability | Implementation |
|---|---|
| Contract validation | Validates agent contracts against the Hermes contract schema |
| Structured reporting | Produces JSON and text audit reports with scored findings |
| Rule-based auditing | Checks for required fields, valid values, and schema compliance |
| CI integration | Can be run in automated pipelines to enforce contract standards |

## Quick Start

```bash
git clone https://github.com/cjps4linux-creator/hermes-agent-contract-auditor.git
cd hermes-agent-contract-auditor

uv venv
uv pip install pydantic

# Validate a contract
uv run python -m auditor.cli agent/agent.spec.md

# JSON output
uv run python -m auditor.cli agent/agent.spec.md --json
```

## Requirements

- Python 3.11+
- pydantic

## License

MIT — use, modify, and ship freely.

**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
