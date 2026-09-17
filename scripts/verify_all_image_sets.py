import urllib.request
import json
import os

# Guaranteed working Unsplash product photos
RELIABLE_CAR_IMAGES = [
    "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=400",
    "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400",
    "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400",
    "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=400",
    "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?w=400",
    "https://images.unsplash.com/photo-150287733853-766e1452684a?w=400",
    "https://images.unsplash.com/photo-1563720223185-11003d516935?w=400",
    "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=400",
    "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=400",
    "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=400",
    "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=400",
    "https://images.unsplash.com/photo-1580273916550-e323be2ae537?w=400",
    "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=400",
    "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=400",
    "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?w=400",
    "https://images.unsplash.com/photo-1553440569-bcc63803a83d?w=400", # Replaced broken 16
    "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=400",
    "https://images.unsplash.com/photo-1508974239320-0a029497e820?w=400",
    "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=400",
    "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400",
    "https://images.unsplash.com/photo-1590362891991-f776e747a588?w=400",
    "https://images.unsplash.com/photo-1562911791-c7a97b729ec5?w=400",
    "https://images.unsplash.com/photo-1616422285623-13ff0162193c?w=400",
    "https://images.unsplash.com/photo-1526726538690-5cbf956ae2fd?w=400"
]

# Update data/latest_trends.json Drop Stop
with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for i, p in enumerate(d["all_ideas"][0]["child_products"]):
    p["image"] = RELIABLE_CAR_IMAGES[i % len(RELIABLE_CAR_IMAGES)]

with open("data/latest_trends.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Updated Drop Stop images!")
