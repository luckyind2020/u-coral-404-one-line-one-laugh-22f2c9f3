"""One line, one laugh — print the single submitted line.

Reads entry.txt next to this file, checks it is exactly one line of
1-140 characters, then prints it.
"""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"
OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"
MAX_CHARS = 140
MIN_CHARS = 1


def load_line(path=ENTRY_PATH):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError(f"expected exactly 1 line, found {len(lines)}")
    line = lines[0].strip()
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}")
    return line


def save_copy(line, path=OUTPUT_PATH):
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(line + "\n", encoding="utf-8")
    except OSError:
        pass


def main():
    line = load_line()
    save_copy(line)
    print(line)


if __name__ == "__main__":
    main()
