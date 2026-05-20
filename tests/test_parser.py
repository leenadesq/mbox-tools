"""Tests for mbox_tools.parser."""
from __future__ import annotations

import datetime as _dt
import shutil
from pathlib import Path

import pytest

from mbox_tools.parser import compute_stats, deduplicate, split_by_date

DATA = Path(__file__).parent / "data" / "sample.mbox"


@pytest.fixture
def mbox_copy(tmp_path: Path) -> Path:
    dst = tmp_path / "sample.mbox"
    shutil.copy(DATA, dst)
    return dst


def test_stats_counts_all_messages(mbox_copy: Path) -> None:
    s = compute_stats(str(mbox_copy))
    assert s.messages == 4
    assert s.size_bytes > 0


def test_stats_date_range(mbox_copy: Path) -> None:
    s = compute_stats(str(mbox_copy))
    assert s.earliest is not None and s.earliest.year == 2024
    assert s.latest is not None and s.latest.month == 3


def test_top_sender_is_alice(mbox_copy: Path) -> None:
    s = compute_stats(str(mbox_copy), top=1)
    assert s.top_senders[0][0] == "alice@example.com"


def test_dedupe_removes_duplicate(mbox_copy: Path, tmp_path: Path) -> None:
    out = tmp_path / "out.mbox"
    kept = deduplicate(str(mbox_copy), str(out))
    assert kept == 3
    s = compute_stats(str(out))
    assert s.messages == 3


def test_split_by_date_inclusive(mbox_copy: Path, tmp_path: Path) -> None:
    out = tmp_path / "feb.mbox"
    n = split_by_date(
        str(mbox_copy),
        str(out),
        date_from=_dt.date(2024, 2, 1),
        date_to=_dt.date(2024, 2, 28),
    )
    assert n == 2

