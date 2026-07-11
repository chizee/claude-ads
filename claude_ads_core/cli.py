"""Command-line interface for deterministic Claude Ads core operations."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from . import __version__
from .adapters import AdapterError, GenericCSVExportAdapter
from .contracts import CONTRACT_NAMES, ContractError, load_contract, validate_contract
from .reporting import ReportRenderError, write_report_bundle
from .scoring import ScoringError, score_account, score_portfolio


def _read_json(path: str) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ContractError(f"cannot load {path}: {exc}") from exc


def _emit(payload: Any) -> None:
    print(json.dumps(payload, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="claude-ads-core")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)

    validate = commands.add_parser("validate", help="validate a versioned JSON contract")
    validate.add_argument("contract", choices=CONTRACT_NAMES)
    validate.add_argument("path")

    score = commands.add_parser("score", help="score one account")
    score.add_argument("--controls", required=True)
    score.add_argument("--findings", required=True)
    score.add_argument("--weights", required=True)

    portfolio = commands.add_parser("portfolio", help="aggregate account scores")
    portfolio.add_argument("path", help="JSON array of account score records")

    status = commands.add_parser("status", help="show a report bundle's deterministic status")
    status.add_argument("path")

    render = commands.add_parser(
        "render",
        aliases=["report"],
        help="render a validated report bundle beneath a safe output root",
    )
    render.add_argument("path", help="ReportBundle JSON input")
    render.add_argument("--format", choices=("markdown", "html", "pdf"), default="markdown")
    render.add_argument("--root", default=".claude-ads/runs", help="safe root for report artifacts")
    render.add_argument("--output", help="relative output path; defaults to <run-id>/report.<extension>")

    ingest = commands.add_parser("ingest-export", help="normalize a generic CSV export")
    ingest.add_argument("--platform", required=True)
    ingest.add_argument("path")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            load_contract(args.contract, args.path)
            _emit({"contract": args.contract, "path": args.path, "status": "valid"})
        elif args.command == "score":
            controls = _read_json(args.controls)
            findings = _read_json(args.findings)
            weights = _read_json(args.weights)
            if not isinstance(controls, list) or not isinstance(findings, list) or not isinstance(weights, dict):
                raise ScoringError("controls/findings must be arrays and weights must be an object")
            _emit(score_account(controls, findings, weights).to_dict())
        elif args.command == "portfolio":
            accounts = _read_json(args.path)
            if not isinstance(accounts, list):
                raise ScoringError("portfolio input must be an array")
            _emit(score_portfolio(accounts).to_dict())
        elif args.command == "status":
            bundle = _read_json(args.path)
            validate_contract("report-bundle", bundle)
            scoring = bundle["scoring"]
            manifest = bundle["run_manifest"]
            _emit(
                {
                    "run_id": manifest["run_id"],
                    "completeness": manifest["completeness"],
                    "health_score": scoring["health_score"],
                    "evidence_coverage": scoring["evidence_coverage"],
                    "status": scoring["status"],
                }
            )
        elif args.command in {"render", "report"}:
            bundle = load_contract("report-bundle", args.path)
            extension = {"markdown": "md", "html": "html", "pdf": "pdf"}[args.format]
            destination = args.output or f"{bundle['run_manifest']['run_id']}/report.{extension}"
            output_path = write_report_bundle(bundle, args.format, args.root, destination)
            _emit(
                {
                    "format": args.format,
                    "path": str(output_path),
                    "run_id": bundle["run_manifest"]["run_id"],
                    "status": "rendered",
                }
            )
        elif args.command == "ingest-export":
            _emit(GenericCSVExportAdapter(args.platform).read_snapshot(args.path))
    except (AdapterError, ContractError, ReportRenderError, ScoringError) as exc:
        print(json.dumps({"status": "invalid", "error": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
