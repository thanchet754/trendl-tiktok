import os
import sys
import json
import time
sys.path.append(os.getcwd())
sys.stdout.reconfigure(encoding='utf-8')

from scripts.scrape_real_products import scrape_amazon_real_products

EXTRA_POOLS = {
    "baby_swaddle": "baby sleep sack swaddle wrap organic cotton",
    "montessori_toy": "montessori sensory pull string activity toy",
    "hair_curler": "rotating ceramic curling iron barrel waver",
    "lip_plump": "viral hydrating lip oil lip plump gloss",
    "freeze_dried": "freeze dried candy crunchy fruit snack",
    "smiski_figurine": "smiski blind box collectible mini figurine glow in dark",
    "hard_cooler": "heavy duty rotomolded insulated outdoor camping cooler",
    "mechanical_keyboard": "custom pbt dye sub cherry profile keycaps mechanical keyboard"
}

with open("data/core_real_pools.json", "r", encoding="utf-8") as f:
    pools = json.load(f)

for k, q in EXTRA_POOLS.items():
    if k in pools and len(pools[k]) >= 15:
        continue
    print(f"Scraping '{k}' ({q})...")
    try:
        prods = scrape_amazon_real_products(q, 20)
        if prods:
            pools[k] = prods
            print(f"-> Scraped {len(prods)} for '{k}'")
            with open("data/core_real_pools.json", "w", encoding="utf-8") as f:
                json.dump(pools, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error {k}: {e}")
    time.sleep(1.5)

print("Done extra pools! Total pools:", len(pools))
