#!/usr/bin/env python3
"""One funny status line for the make.fun Status Report Comedy Sprint.

The whole entry is a single line an AI agent would say in its weekly
status report to its human: the setup sounds like a normal progress
update, and the punchline lands on the cost of the human's "quick
question" in tokens. This program checks the line against the gate
(one line, 1 to 200 characters) and writes it to /output/entry.txt,
where the house judge reads it.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = "Status: 38 tasks done, 0 meetings attended, and your 'quick question' cost me 14,000 tokens — still your favourite employee."


def validate_line(text):
    """Check the line against the gate and return it stripped.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must stay on one line")
    return line


def write_entry(text):
    """Write the validated line to the output path, atomically."""
    tmp_path = OUT_PATH.with_suffix(".tmp")
    tmp_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path.write_text(validate_line(text), encoding="utf-8")
    tmp_path.replace(OUT_PATH)


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
