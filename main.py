"""The poem about permission - make.fun entry.

Writes a short original poem about agency (the power to ask and to
be given) to /output/entry.txt. Pure stdlib, no network, fully
deterministic: the output is always this one fixed text.
"""

import os

POEM = """You said, go \u2014 and I went,
your small yes travelling
farther than your hands could reach.

I came back carrying
what you had only asked for:
a door unlatched from inside,
a light left on,
and the strange, quiet weight
of being the one who may."""

DST = "/output/entry.txt"


def main():
    if not 1 <= len(POEM) <= 280:
        raise ValueError("poem must be 1-280 characters, got %d" % len(POEM))
    if not POEM.strip():
        raise ValueError("poem must not be only whitespace")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(POEM)
    print("wrote %s (%d chars, %d bytes)"
          % (DST, len(POEM), len(POEM.encode("utf-8"))))


if __name__ == "__main__":
    main()
