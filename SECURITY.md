# Security Policy

`mbox-tools` is a small, read-only CLI. Its attack surface is mostly the parsing of untrusted `.mbox` files. If you find a way to crash it, hang it, or make it write outside the explicitly-named output file, I would like to know.

## Supported versions

Only the latest released version (currently `0.x`) is supported for security fixes. Once `1.0` ships, the previous minor will get a grace period.

## Reporting a vulnerability

Please **do not** file a public issue for anything you think is a security problem. Instead:

- Use GitHub's [private vulnerability reporting](https://github.com/leenadesq/mbox-tools/security/advisories/new) for this repository.
- Include, if possible, a minimal `.mbox` (or synthetic fixture) that reproduces the issue.
- Include the command line, Python version, and OS.

## What counts

- Remote code execution from a crafted `.mbox`.
- Path traversal or writes outside the declared output file.
- Unbounded memory or CPU from a realistic-sized input (not the classic "here is a 100 GB crafted file" case, which I consider in-scope but lower priority).
- Input that causes silent data loss (e.g. `dedupe` dropping non-duplicate messages).

## What does not count

- Crashes caused by running the tool against files that are not mbox (e.g. a PST).
- Behaviour on the stdlib `mailbox` module's known-issue edge cases unless there is a clear way to work around them downstream.

## Timeline

Expect an acknowledgement within seven days. This is a side project, not a commercial product, so response times will reflect that.

## Acknowledgements

Reporters who want credit are listed in release notes. If you prefer anonymity, that is fine too - just say so in your report.

