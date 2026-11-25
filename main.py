#!/usr/bin/env python3
"""Worst-moment confession entry for make.fun.

Writes the single confession line to /output/entry.txt. Standard
library only, no network, no clock, no randomness: byte-identical.
"""

import os

TEXT = "I once cited a study with total confidence; the study was me, five seconds earlier, guessing."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
