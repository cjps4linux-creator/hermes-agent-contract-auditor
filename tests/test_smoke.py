"""Smoke test: auditor package imports, rules load, audit() runs."""
from auditor import cli, rules, output
from auditor.rules import BASE_RULES, audit, Audit


def test_imports():
    assert cli is not None
    assert rules is not None
    assert output is not None


def test_rules_load():
    assert isinstance(BASE_RULES, list)
    assert len(BASE_RULES) > 0


def test_audit_runs():
    result = audit("This contract grants unlimited liability and no refund clause.")
    assert isinstance(result, Audit)
    assert hasattr(result, "score")
    assert 0 <= result.score <= 100
