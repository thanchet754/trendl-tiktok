import os
import sys
sys.path.append(os.getcwd())
import json
import urllib.request
from scripts.scrape_real_products import scrape_amazon_real_products

prods = scrape_amazon_real_products('tactical car backseat organizer', 24)
imgs = [p['image'] for p in prods]
print(f"Total: {len(prods)}, Unique images: {len(set(imgs))}")

# Check HTTP 200 on all images
for i, p in enumerate(prods):
    try:
        req = urllib.request.Request(p['image'], headers={'User-Agent': 'Mozilla/5.0'})
        code = urllib.request.urlopen(req).getcode()
        if code != 200:
            print(f"Warn: {i+1} got HTTP {code}")
    except Exception as e:
        print(f"Error {i+1}: {e}")

print("Verification of all 24 real product photos completed!")

# Save to data/real_car_products.json
with open("data/real_car_products.json", "w", encoding="utf-8") as f:
    json.dump(prods, f, ensure_ascii=False, indent=2)
print("Saved to data/real_car_products.json")
