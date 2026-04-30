#!/usr/bin/env python3
import sys
from collections import Counter
import re

WORD_RE = re.compile(r"\b\w[\w']*\b")


def top_words(path=None, n=10):
    if path is None:
        text = sys.stdin.read()
    else:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

    words = WORD_RE.findall(text.lower())
    return Counter(words).most_common(n)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else None
    for word, count in top_words(path):
        print(f"{word}\t{count}")
