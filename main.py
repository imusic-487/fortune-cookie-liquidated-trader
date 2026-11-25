"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt.

The fortune (19 words, one line, plain text):
    Fortune favors the liquidated trader who laughs at 3 a.m.:
    your wallet is empty, your story is finally rich.

Why this line: it keeps the oracular fortune voice ("Fortune favors..."),
names the trader and the loss outright ("liquidated", "wallet is empty"),
stays rueful and warm instead of cruel, and lands its fresh turn on the
last word -- "rich" flips from money, which is gone, to the story, which
is finally worth telling.

Verified 2026-11-25: output is 1 line, 19 words (limit 20), 108 characters
stripped / 109 with the trailing newline (gate: 1-160), UTF-8 plain text.
"""

import os

FORTUNE = (
    "Fortune favors the liquidated trader who laughs at 3 a.m.: "
    "your wallet is empty, your story is finally rich."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
