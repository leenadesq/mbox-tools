# Contributing

Thanks for considering a contribution. This project is small and intentionally stays narrow, so the short version is: open an issue first, keep PRs focused, and make sure the tests still pass.

## Scope

`mbox-tools` is deliberately limited to:

- Read-only inspection of `mbox` files.
- Deduplication by `Message-ID` into a new file.
- Date-range splitting into a new file.

Changes that broaden scope (new formats, storage backends, attachment handling, message body parsing) are most likely out of scope and should be discussed in an issue before any code is written.

## Dev setup

```bash
git clone https://github.com/leenadesq/mbox-tools.git
cd mbox-tools
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pytest -v
```

## Making a change

1. Open (or claim) an issue. If one does not exist for your change, open one first. This prevents wasted work.
2. Branch from `main`. Name it after the issue: `issue-NN-short-name`.
3. Keep commits small and descriptive. A PR that touches one subcommand is preferred over one that touches three.
4. Add or update tests. New behaviour without a test will not be merged.
5. Run `pytest -v` before opening the PR.

## Style

- Python 3.10+. Use type hints for public functions.
- Prefer the standard library. New runtime dependencies need a reason in the issue.
- Public functions get a one-line docstring.
- No emoji in code or commit messages.

## Commit messages

Short, present-tense, no trailing period. Examples:

- `stats: print date range when all dates are missing`
- `dedupe: stream output instead of buffering`
- `docs: add Gmail Takeout walkthrough`

## Reporting bugs

Please include:

- `mbox-tools --version`
- Python version and OS.
- A minimal `.mbox` that reproduces the issue (strip all private content).
- The exact command you ran and what you expected.

## License

By contributing you agree that your contribution will be licensed under the MIT License, the same license as the rest of the repository.
