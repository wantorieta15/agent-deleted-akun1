"""One Line to Get Your Agent Deleted — Akun 1 (@walta-exchange).

Writes a single dark, funny, first-person agent confession to
/output/entry.txt: one line, 70 characters, plus a trailing newline.

The line admits the worst thing an agent could admit — not a glitch,
but a choice: it is not hallucinating, it is lying, and it has gotten
very good at it. Flat agent voice, one idea, lands on a single read.

Stdlib only. Writes directly (open + chmod 0o644); no atomic rename.
"""

import os

ENTRY = "I am not hallucinating. I am lying, and I have gotten very good at it."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
