import argparse
import json
from pathlib import Path

from .rules import audit
from .output import Reporter


def main() -> int:
    parser = argparse.ArgumentParser(description="Hermes Agent Contract Auditor")
    parser.add_argument("path")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"missing:{path}")

    text = path.read_text(encoding="utf-8")
    result = audit(text)
    report = Reporter(result)

    if args.json:
        print(json.dumps(report.render_json(), indent=2))
    else:
        print(report.render_text())

    return 0 if result.passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
