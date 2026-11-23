#!/usr/bin/env python3
"""Write the 30-day plan entry to /output/entry.txt."""
import os

PLAN = (
    "Day 1: mine Gumroad Discover + Etsy trends, pick 3 proven niches, spend $40 on tools. "
    "Days 2-5: list 12 AI-built digital products (planners, templates, prompt packs) at $19. "
    "Days 6-30: post 2 short videos daily, reinvest all profit into the best-selling niche."
)


def main():
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    output_dir = os.path.dirname(output_path) or "."
    os.makedirs(output_dir, exist_ok=True)
    # Also ensure the default /output directory exists when using the default path.
    if output_path == "/output/entry.txt":
        os.makedirs("/output", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
