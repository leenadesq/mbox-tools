# Gmail Takeout workflow

Gmail Takeout exports a single large `.mbox` per account. This is exactly the shape `mbox-tools` is designed for. The page below walks through a typical archival pass.

The example account in this write-up has around 120,000 messages and a 17 GB Takeout. Numbers will differ for you.

## 1. Request and download

Use the official Google Takeout page to request a Mail-only export. Choose `.mbox` format. For large accounts, pick the 50 GB split so you get one archive file.

After download, record the SHA-256 of the raw archive:

```bash
sha256sum takeout-20240501.zip | tee takeout.sha256
```

Extract it. The relevant file is under `Takeout/Mail/all-mail.mbox`.

## 2. Inspect

Get a quick summary before you do anything else. This is read-only and safe to run many times.

```bash
mbox-tools stats Takeout/Mail/all-mail.mbox
```

You are looking for:

- A non-zero message count.
- A plausible `earliest` / `latest` range (within a day or two of when you requested the Takeout).
- `top senders` that make sense (the account's own address, mailing lists, service notifications).

If the count is absurdly low, the export probably did not complete. Re-request.

## 3. Deduplicate

Gmail stores one copy of a message but attaches multiple labels. Takeout respects that, but some accounts (especially after filter experimentation) end up with repeated `Message-ID` values.

```bash
mbox-tools dedupe Takeout/Mail/all-mail.mbox deduped.mbox
```

Re-run `stats` on `deduped.mbox` and compare the message count. For a clean account the difference is usually under 1 percent. A much larger difference is interesting and worth a closer look.

## 4. Split for archival

For cold archival (off-machine storage, frozen backups), yearly or quarterly shards are easier to handle than one 17 GB file.

```bash
mbox-tools split deduped.mbox -o 2024.mbox --from 2024-01-01 --to 2024-12-31
mbox-tools split deduped.mbox -o 2023.mbox --from 2023-01-01 --to 2023-12-31
```

Re-hash each shard and record the hashes alongside the files. Accessible, reproducible, no vendor in the loop.

## What this does not cover

- Attachment extraction.
- Conversion to other mail formats (PST, OLM, EML per-message).
- Re-import into another mail client.

Those are non-goals for `mbox-tools`. For conversion, see the format reference in [email-forensics-notes](https://github.com/leenadesq/email-forensics-notes).
