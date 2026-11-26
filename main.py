"""Print the one-line excuse from entry.txt, byte for byte."""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8")
    # write() on purpose: print() would append an extra newline.
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
