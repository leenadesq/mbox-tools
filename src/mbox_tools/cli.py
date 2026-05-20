"""Command-line interface for mbox-tools."""
from __future__ import annotations

import argparse
import datetime as _dt
import sys

from . import __version__
from .parser import compute_stats, deduplicate, split_by_date


def _parse_date(s: str) -> _dt.date:
    return _dt.datetime.strptime(s, "%Y-%m-%d").date()


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="mbox-tools", description="Small CLI utilities for mbox files.")
    p.add_argument("--version", action="version", version=f"mbox-tools {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_stats = sub.add_parser("stats", help="Print basic stats about an mbox.")
    p_stats.add_argument("file")
    p_stats.add_argument("--top", type=int, default=5)

    p_dedupe = sub.add_parser("dedupe", help="Write a new mbox with duplicate Message-IDs removed.")
    p_dedupe.add_argument("src")
    p_dedupe.add_argument("dst")

    p_split = sub.add_parser("split", help="Extract a date range into a new mbox.")
    p_split.add_argument("src")
    p_split.add_argument("-o", "--out", required=True)
    p_split.add_argument("--from", dest="date_from", type=_parse_date, default=None)
    p_split.add_argument("--to", dest="date_to", type=_parse_date, default=None)

    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if args.cmd == "stats":
        s = compute_stats(args.file, top=args.top)
        print(f"file:     {s.path}")
        print(f"messages: {s.messages}")
        print(f"size:     {s.size_bytes} bytes")
        print(f"earliest: {s.earliest}")
        print(f"latest:   {s.latest}")
        print("top senders:")
        for sender, n in s.top_senders:
            print(f"  {n:5}  {sender}")
        return 0
    if args.cmd == "dedupe":
        kept = deduplicate(args.src, args.dst)
        print(f"kept {kept} messages (deduped by Message-ID)")
        return 0
    if args.cmd == "split":
        n = split_by_date(args.src, args.out, args.date_from, args.date_to)
        print(f"wrote {n} messages to {args.out}")
        return 0
    return 2


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))

