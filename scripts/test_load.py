import sys, os, json, random, re
sys.path.insert(0, os.path.abspath("."))

from analyzer.category_taxonomy import TIKTOK_SHOP_28_CATEGORIES

# 1. Load data
with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    trends_data = json.load(f)

with open("data/core_real_pools.json", "r", encoding="utf-8") as f:
    core_pools = json.load(f)

ideas = trends_data.get("all_ideas", [])
videos = trends_data.get("top_videos", [])
creators = trends_data.get("top_influencers", [])

print(f"Initial: {len(ideas)} ideas, {len(videos)} videos, {len(creators)} creators")
