import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open("data/core_real_pools.json", "r", encoding="utf-8") as f:
    pools = json.load(f)

# High quality relevant Unsplash product photos
STATIONERY_IMGS = [
    "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1585776245991-cf89dd7fc73a?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1532012164546-f432f2e37272?w=500&auto=format&fit=crop&q=80",
]

CLEANING_IMGS = [
    "https://images.unsplash.com/photo-1585421514284-efb74c2b69ba?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1563245372-f21724e3856d?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=500&auto=format&fit=crop&q=80",
]

TOOL_IMGS = [
    "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1581783342308-f792dbdd27c5?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1530124566582-a618bc2615dc?w=500&auto=format&fit=crop&q=80",
]

JEWELRY_IMGS = [
    "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1602751584552-8ba73aad10e1?w=500&auto=format&fit=crop&q=80",
    "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=500&auto=format&fit=crop&q=80",
]

if "stationery_books" in pools:
    for i, it in enumerate(pools["stationery_books"]):
        it["image"] = STATIONERY_IMGS[i % len(STATIONERY_IMGS)]

if "home_cleaning" in pools:
    for i, it in enumerate(pools["home_cleaning"]):
        it["image"] = CLEANING_IMGS[i % len(CLEANING_IMGS)]

if "tools_hardware" in pools:
    for i, it in enumerate(pools["tools_hardware"]):
        it["image"] = TOOL_IMGS[i % len(TOOL_IMGS)]

if "jewelry_accessories" in pools:
    for i, it in enumerate(pools["jewelry_accessories"]):
        it["image"] = JEWELRY_IMGS[i % len(JEWELRY_IMGS)]

with open("data/core_real_pools.json", "w", encoding="utf-8") as f:
    json.dump(pools, f, ensure_ascii=False, indent=2)

print("Updated pool images to match categories perfectly!")
