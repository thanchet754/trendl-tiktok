import os
import sys
import json
import time
sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.getcwd())

from scripts.scrape_real_products import scrape_amazon_real_products

TARGET_CATEGORIES = {
    "Automotive & Motorcycle": "tactical car backseat organizer",
    "Beauty & Personal Care": "viral korean skincare toner serum",
    "Kitchenware": "insulated stainless steel tumbler with straw",
    "Pet Supplies": "self cleaning pet grooming brush",
    "Phones & Electronics": "wireless lavalier microphone for phone",
    "Shoes": "platform mini snow boots for women",
    "Womenswear & Underwear": "seamless tummy control sculpting bodysuit"
}

all_cat_products = {}

# If automotive already scraped, reuse it
if os.path.exists("data/real_car_products.json"):
    try:
        with open("data/real_car_products.json", "r", encoding="utf-8") as f:
            all_cat_products["Automotive & Motorcycle"] = json.load(f)
            print("Loaded 24 real Automotive products from cache.")
    except Exception as e:
        print("Error loading car cache:", e)

for cat, query in TARGET_CATEGORIES.items():
    if cat in all_cat_products and len(all_cat_products[cat]) >= 24:
        continue
    print(f"\n--- Scraping real products for {cat} ({query}) ---")
    try:
        prods = scrape_amazon_real_products(query, 24)
        print(f"Scraped {len(prods)} products for {cat}.")
        all_cat_products[cat] = prods
    except Exception as e:
        print(f"Error scraping {cat}: {e}")
    time.sleep(2)

with open("data/category_real_products.json", "w", encoding="utf-8") as f:
    json.dump(all_cat_products, f, ensure_ascii=False, indent=2)

print("\nSuccessfully saved all real category products to data/category_real_products.json!")
