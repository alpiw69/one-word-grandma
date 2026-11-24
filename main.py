"""make.fun bounty: One Word From Grandma.

Deterministic, no-network program. Writes exactly one word to
/output/entry.txt: the single word grandma would text about AI.
She read "AI" as a person's name. So she asks about Al. Running
twice writes identical bytes.
"""
from pathlib import Path

WORD = "Al"  # grandma thinks AI is a nice young man named Al

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(WORD, encoding="utf-8")
    print(f"Wrote {OUT} ({len(WORD)} chars)")


if __name__ == "__main__":
    main()
