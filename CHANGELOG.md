# Changelog

All notable changes to `mbox-tools` are documented in this file.

The format is loosely based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- `stats`: `--json` output mode (tracking in #1).
- `split`: support for multiple non-contiguous ranges (tracking in #2).

## [0.1.0] - unreleased

First working version. No tagged release yet; this entry describes the state of `main`.

### Added

- `mbox-tools stats`: count messages, print size, date range, and top senders for an mbox.
- `mbox-tools dedupe`: write a new mbox with duplicate `Message-ID` values removed.
- `mbox-tools split`: extract a `--from`/`--to` date range into a new mbox.
- Public package layout `src/mbox_tools` with `parser` and `cli` modules.
- Pytest suite covering stats, top-sender, dedupe, and date-range split.
- GitHub Actions CI against Python 3.10, 3.11, and 3.12.
- `docs/gmail-takeout.md` end-to-end walkthrough.
- `CONTRIBUTING.md` and `SECURITY.md`.

### Documented non-goals

- PST/OST/OLM formats.
- Message body parsing or attachment extraction.
- Any mutation of the source file.

[Unreleased]: https://github.com/leenadesq/mbox-tools/commits/main
[0.1.0]: https://github.com/leenadesq/mbox-tools

