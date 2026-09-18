import sys, os, json, random, re
sys.path.insert(0, os.path.abspath("."))

from analyzer.category_taxonomy import TIKTOK_SHOP_28_CATEGORIES

with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    current_data = json.load(f)

existing_ideas = current_data.get("all_ideas", [])
print(f"Current ideas count: {len(existing_ideas)}")

needed = 5000 - len(existing_ideas)
print(f"Needed new ideas: {needed}")
