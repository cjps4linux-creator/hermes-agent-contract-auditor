# Example Agent Contract

## Identity
- Name: Example Agent
- Status: testing

## Mission
One sentence.

## Scope
### Responsibilities
1. First responsibility
2. Second responsibility

### Non-responsibilities
1. Out of scope item

## Inputs
| Field | Rule | Required |
|-------|------|----------|
| email | valid email | yes |

## Outputs
| Field | Rule |
|-------|------|
| status | pass | fail |

## Constraints
- Performance limits:
- Memory limits:
- Tool limits:
- Security restrictions:
- Operational assumptions:

## Dependencies
| Dependency | Purpose | Version | Fallback |
|------------|---------|---------|----------|
| python | runtime | 3.11+ | none |

## Tools
| Tool | Purpose | Allowed Operations | Max Rate | Timeout | Fallback |
|------|---------|-------------------|----------|---------|----------|
| read_file | inspect files | read | 10/s | 5s | manual review |

## Memory Model
| Layer | Purpose | Retention |
|-------|---------|-----------|
| Working | current task | ephemeral |
| Session | conversation | while useful |
| Project | persistent knowledge | indefinite |
| Organizational | shared platform knowledge | indefinite |

## Failure Taxonomy
| Failure Mode | Detection | Recovery | Escalation |
|--------------|-----------|----------|------------|
| User input failure | bad values | clarify | request correction |
| Tool failure | tool unavailable | retry | manual mode |

## Observability
- [x] Version
- [x] Health status

## Evaluation
| Metric | Target | Review Cadence |
|--------|--------|----------------|
| Task success rate | >95% | weekly |

## Versioning Policy
- MAJOR: breaking change
- MINOR: enhancement
- PATCH: fix

## Changelog
| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-07-08 | Initial contract |
