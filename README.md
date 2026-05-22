# mbox-tools

Small Python CLI utilities for working with **mbox** mail archives. Built for forensic and archival workflows where you need read-only inspection, deduplication, and date-range splitting of large mailbox files.

## Why

.mbox files are common exports from Thunderbird, Apple Mail, Gmail Takeout, and many archival tools. They are also large, opaque, and awkward to inspect without loading them back into a mail client. `mbox-tools` gives you a few small, composable commands so you can answer basic questions and prepare subsets for review.

## What it does

- `mbox-tools stats <file>` - count messages, date range, top senders, total size.
- `mbox-tools dedupe <in> <out>` - write a new mbox with duplicate Message-IDs removed.
- `mbox-tools split <file> --from YYYY-MM-DD --to YYYY-MM-DD` - extract a date range into a new mbox.

All operations are read-only on the input file. Output is written to a new file you specify.

## Install (dev)

```bash
git clone https://github.com/leenadesq/mbox-tools.git
cd mbox-tools
pip install -e .
```

## Usage

```bash
mbox-tools stats path/to/archive.mbox
mbox-tools dedupe input.mbox deduped.mbox
mbox-tools split input.mbox --from 2024-01-01 --to 2024-06-30 -o q1q2.mbox
```

## Documentation

- [Gmail Takeout workflow](docs/gmail-takeout.md) - end-to-end inspection, dedupe, and split.

More walkthroughs will land under `docs/` as the issues in this repo get picked up.

## Status

Early. The current focus is correctness on the three commands above and a small pytest suite that runs in CI. See `tests/` for fixtures.

## Scope (and non-scope)

This project intentionally does not touch:

- PST / OST / OLM formats - use libpff or specialised tools.
- Mail body rendering, attachment extraction, or HTML sanitisation.
- Anything that mutates the source file.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue before starting any non-trivial change.

## Security

See [SECURITY.md](SECURITY.md) for private disclosure instructions.

## License

MIT. See [LICENSE](LICENSE).
