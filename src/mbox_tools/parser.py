"""Read-only helpers for walking an mbox file.

This module intentionally wraps the standard library's ``mailbox`` and
adds a few utility functions that are handy for quick triage and CLI
use. No messages are parsed beyond what is needed for headers.
"""
from __future__ import annotations

import datetime as _dt
import mailbox
import os
from collections import Counter
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from typing import Iterable, Iterator, Optional


@dataclass
class MboxStats:
    path: str
    messages: int
    size_bytes: int
    earliest: Optional[_dt.datetime]
    latest: Optional[_dt.datetime]
    top_senders: list[tuple[str, int]]


def _iter_messages(path: str) -> Iterator[mailbox.Message]:
    mb = mailbox.mbox(path, create=False)
    try:
        for msg in mb:
            yield msg
    finally:
        mb.close()


def _parse_date(value: Optional[str]) -> Optional[_dt.datetime]:
    if not value:
        return None
    try:
        return parsedate_to_datetime(value)
    except Exception:  # pragma: no cover
        return None


def compute_stats(path: str, top: int = 5) -> MboxStats:
    size = os.path.getsize(path)
    count = 0
    earliest: Optional[_dt.datetime] = None
    latest: Optional[_dt.datetime] = None
    senders: Counter[str] = Counter()
    for msg in _iter_messages(path):
        count += 1
        from_ = (msg.get("From") or "(unknown)").strip()
        senders[from_] += 1
        d = _parse_date(msg.get("Date"))
        if d is not None:
            if earliest is None or d < earliest:
                earliest = d
            if latest is None or d > latest:
                latest = d
    return MboxStats(
        path=path,
        messages=count,
        size_bytes=size,
        earliest=earliest,
        latest=latest,
        top_senders=senders.most_common(top),
    )


def deduplicate(src: str, dst: str) -> int:
    """Write **dst** with duplicate Message-IDs removed. Returns kept count."""
    seen: set[str] = set()
    out = mailbox.mbox(dst, create=True)
    kept = 0
    try:
        for msg in _iter_messages(src):
            mid = (msg.get("Message-ID") or "").strip()
            if mid and mid in seen:
                continue
            if mid:
                seen.add(mid)
            out.add(msg)
            kept += 1
    finally:
        out.close()
    return kept


def split_by_date(
    src: str,
    dst: str,
    date_from: Optional[_dt.date] = None,
    date_to: Optional[_dt.date] = None,
) -> int:
    """Copy messages with Date in [date_from, date_to] into **dst**."""
    out = mailbox.mbox(dst, create=True)
    written = 0
    try:
        for msg in _iter_messages(src):
            d = _parse_date(msg.get("Date"))
            if d is None:
                continue
            donly = d.date()
            if date_from and donly < date_from:
                continue
            if date_to and donly > date_to:
                continue
            out.add(msg)
            written += 1
    finally:
        out.close()
    return written
