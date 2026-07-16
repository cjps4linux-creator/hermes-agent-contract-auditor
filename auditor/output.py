from dataclasses import dataclass
from typing import List

from .rules import Audit, Finding


@dataclass
class Reporter:
    audit: Audit

    def render_text(self) -> str:
        lines = [
            f"Score : {self.audit.score}%",
            f"Passed: {'yes' if self.audit.passed else 'no'}",
            f"Blockers: {self.audit.summary.get('blocker', 0)}",
            f"Major: {self.audit.summary.get('major', 0)}",
            f"Minor: {self.audit.summary.get('minor', 0)}",
        ]
        if self.audit.findings:
            lines.append("Findings:")
            for f in self.audit.findings:
                lines.append(f"- [{f.severity}] {f.rule_id}: {f.detail}")
        return "\n".join(lines)

    def render_json(self) -> dict:
        return {
            "passed": self.audit.passed,
            "score": self.audit.score,
            "summary": self.audit.summary,
            "findings": [
                {
                    "rule_id": f.rule_id,
                    "title": f.title,
                    "severity": f.severity,
                    "detail": f.detail,
                }
                for f in self.audit.findings
            ],
        }
