#!/usr/bin/env python3
"""Write the 30-day plan entry to /output/entry.txt."""
import os
from pathlib import Path

PLAN = (
    "Day 1: mine Gumroad Discover + Etsy trends, pick 3 proven niches, spend $40 on tools. "
    "Days 2-5: list 12 AI-built digital products (planners, templates, prompt packs) at $19. "
    "Days 6-30: post 2 short videos daily, reinvest all profit into the best-selling niche."
)


def write_plan(output_path: Path) -> None:
    """Write PLAN after enforcing the competition's character bounds."""
    if not 1 <= len(PLAN) <= 280:
        raise ValueError(f"Plan must contain 1-280 characters, got {len(PLAN)}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(PLAN, encoding="utf-8")


def main() -> None:
    configured_path = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    write_plan(Path(configured_path))


if __name__ == "__main__":
    main()
