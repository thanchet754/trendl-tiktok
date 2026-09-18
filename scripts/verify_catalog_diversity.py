import json
import sys
from collections import Counter

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('data/latest_trends.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

ideas = d['all_ideas']
print(f"Total ideas: {len(ideas)}")

titles = [it['title'].strip() for it in ideas]
counts = Counter(titles)
dups = {t: c for t, c in counts.items() if c > 1}
print(f"Duplicate titles count: {len(dups)}")

print("\n--- FIRST 25 ITEMS IN TABLE (PAGE 1) ---")
for i in range(25):
    it = ideas[i]
    print(f"{i+1:2d}. [{it['category']}] {it['title']} ({it['price']}) - 24h Sales: {it['sales_24h']:,}")

print("\n--- CATEGORY BREAKDOWN IN FIRST 100 ITEMS (PAGE 1) ---")
first_100_cats = Counter(it['category'] for it in ideas[:100])
print(f"Distinct categories on Page 1: {len(first_100_cats)} / 29 categories")
for cat, cnt in first_100_cats.most_common():
    print(f"  {cat}: {cnt} items")

print("\n--- CHECK REPEATED IMAGES ON PAGE 1 (FIRST 100 ITEMS) ---")
first_100_imgs = [it['image'] for it in ideas[:100]]
img_counts_100 = Counter(first_100_imgs)
repeated_imgs_100 = {k: v for k, v in img_counts_100.items() if v > 1}
print(f"Unique images in first 100 items: {len(img_counts_100)} / 100")
print(f"Number of repeated image URLs on page 1: {len(repeated_imgs_100)}")
