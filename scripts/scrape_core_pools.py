import os
import sys
import json
import time
sys.path.append(os.getcwd())
sys.stdout.reconfigure(encoding='utf-8')

from scripts.scrape_real_products import scrape_amazon_real_products

CORE_PRODUCT_QUERIES = {
    "steering_wheel_desk": "car steering wheel desk tray table for laptop eating",
    "led_ambient_strip": "car led ambient interior light strip app control",
    "rubber_floor_mats": "all weather rubber car floor mats custom fit",
    "dash_cam_4k": "4k front and rear dual dash cam with wifi gps",
    "car_phone_mount": "magsafe wireless car charger mount air vent",
    "carplay_adapter": "wireless carplay android auto adapter dongle",
    "car_vacuum": "cordless handheld high power car vacuum cleaner",
    "tire_inflator": "portable air compressor tire inflator 12v digital",
    "foam_cannon": "high pressure snow foam cannon gun car wash",
    "obd2_scanner": "bluetooth obd2 scanner car diagnostic tool app",
    "fm_transmitter": "bluetooth fm transmitter for car radio bass boost",
    "leather_cleaner": "car interior leather cleaner and conditioner kit",
    "microfiber_towels": "ultra plush car detailing microfiber drying towels 1200gsm",
    "ceramic_coating_wax": "car ceramic coating spray intense gloss wax"
}

# Load existing if available
real_pools = {}
if os.path.exists("data/core_real_pools.json"):
    try:
        with open("data/core_real_pools.json", "r", encoding="utf-8") as f:
            real_pools = json.load(f)
            print(f"Loaded {len(real_pools)} existing product pools.")
    except Exception as e:
        print("Error loading existing:", e)

for key, query in CORE_PRODUCT_QUERIES.items():
    if key in real_pools and len(real_pools[key]) >= 20:
        print(f"Pool '{key}' already has {len(real_pools[key])} products, skipping.")
        continue
    print(f"\nScraping real products for: '{key}' ({query})...")
    try:
        prods = scrape_amazon_real_products(query, 24)
        if prods:
            real_pools[key] = prods
            print(f"-> Scraped {len(prods)} products for '{key}'.")
            # Save incrementally
            with open("data/core_real_pools.json", "w", encoding="utf-8") as f:
                json.dump(real_pools, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error scraping '{key}': {e}")
    time.sleep(1.5)

print("\nDone! Total pools saved:", len(real_pools))
