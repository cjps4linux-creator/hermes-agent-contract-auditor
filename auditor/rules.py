from dataclasses import dataclass, field
from typing import List, Dict


@dataclass(frozen=True)
class Rule:
    id: str
    title: str
    severity: str
    check: str


BASE_RULES: List[Rule] = [
    Rule("R-001", "Identity present", "blocker", "Identity"),
    Rule("R-002", "Mission present", "blocker", "Mission"),
    Rule("R-003", "Scope present", "major", "Scope"),
    Rule("R-004", "Inputs present", "major", "Inputs"),
    Rule("R-005", "Outputs present", "major", "Outputs"),
    Rule("R-006", "Constraints present", "major", "Constraints"),
    Rule("R-007", "Dependencies present", "minor", "Dependencies"),
    Rule("R-008", "Tools present", "major", "Tools"),
    Rule("R-009", "Memory Model present", "minor", "Memory Model"),
    Rule("R-010", "Failure Taxonomy present", "blocker", "Failure Taxonomy"),
    Rule("R-011", "Observability present", "major", "Observability"),
    Rule("R-012", "Evaluation present", "major", "Evaluation"),
]


@dataclass
class Finding:
    rule_id: str
    title: str
    severity: str
    detail: str


@dataclass
class Audit:
    passed: bool
    score: float
    findings: List[Finding] = field(default_factory=list)
    summary: Dict[str, int] = field(default_factory=dict)


def audit(text: str) -> Audit:
    findings: List[Finding] = []
    counts: Dict[str, int] = {"blocker": 0, "major": 0, "minor": 0}

    for rule in BASE_RULES:
        missing = rule.check not in text
        if missing:
            finding = Finding(
                rule_id=rule.id,
                title=rule.title,
                severity=rule.severity,
                detail=f"Missing required section: {rule.check}",
            )
            findings.append(finding)
            counts[rule.severity] += 1

    total = len(BASE_RULES)
    failed = len(findings)
    passed = failed == 0
    score = round(((total - failed) / total) * 100, 2)

    return Audit(passed=passed, score=score, findings=findings, summary=counts)
