"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a concrete everyday annoyance to
/output/entry.txt. The rant targets the self-checkout machine: a specific,
universally shared humiliation, told in short sentences with the punch
landing on the last line. Gate: UTF-8 text, 1 to 400 characters.
"""

import hashlib
import os

RANT = (
    "Self-checkout scanned my milk, weighed it, then screamed UNEXPECTED ITEM "
    "IN BAGGING AREA like I was smuggling dairy. I paid for the milk. "
    "The machine watched me pay. Now a teenager with a key has to come "
    "unlock my groceries while the whole queue decides I am a criminal. "
    "I came here to buy milk, not to be tried for it."
)

MAX_CHARS = 400


def validate(text):
    """Check the gate: 1-400 characters, UTF-8, not only whitespace."""
    if not text or text.isspace():
        raise ValueError("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 400 cap")
    text.encode("utf-8")
    return True


def report(text):
    """Print length and sha256 of the entry, with and without newline."""
    raw = text.encode("utf-8")
    print(f"chars: {len(text)}")
    print("sha256 no-newline: " + hashlib.sha256(raw).hexdigest())
    print("sha256 with-newline: " + hashlib.sha256(raw + b"\n").hexdigest())


def main():
    validate(RANT)
    report(RANT)
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(RANT)
    print(f"wrote {len(RANT)} chars to {out_path}")


if __name__ == "__main__":
    main()
