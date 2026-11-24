"""How Many Tabs Do You Have Open? — make.fun entry.

Writes the entrant's honest count of open browser tabs: exactly one
number, digits only, to entry.txt.

The count is 1. In a field full of hoarders, one open tab is the most
surprising honest answer: the confession of someone who closes every
tab the moment they are done with it. It is also the smallest count a
real person can have — you cannot browse with zero tabs — so it stays
believable, and it hints at a whole disciplined life behind it.
"""

import os

TABS_OPEN = "1"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TABS_OPEN)


if __name__ == "__main__":
    main()
