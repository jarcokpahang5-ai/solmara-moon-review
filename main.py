#!/usr/bin/env python3
"""One-star review of the Moon (max 120 characters).

Writes a single one-star review of the Moon to /output/entry.txt.
Pure Python standard library, deterministic, no network.
"""

import os


def build_line():
    return ("One star. Vanished for a week, came back a different shape, "
            "and stirred the ocean while I slept. Blocked.")


def main():
    line = build_line()
    assert 1 <= len(line) <= 120, "line must be 1-120 characters, got %d" % len(line)
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
