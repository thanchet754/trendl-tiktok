"""
Scoring & Classification Engine
Evaluates products on Viral Spike (24h) and Evergreen Sustainability metrics.
"""

import re
from typing import Dict, Any

def extract_price_value(price_str: str) -> float:
    """Extracts first numeric float from price string."""
    if not price_str:
        return 25.0
    match = re.search(r'\$?(\d+(?:\.\d{2})?)', str(price_str))
    if match:
        try:
            return float(match.group(1))
        except Exception:
            pass
    return 25.0

def calculate_scores(item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculates:
    - viral_score (0-100)
    - evergreen_score (0-100)
    - impulse_score (0-100)
    - classification ('VIRAL_SPIKE_24H' or 'EVERGREEN_WINNER')
    - badge
    """
    source = item.get("source", "")
    title = item.get("title", "").lower()
    category = item.get("category", "")
    price_val = extract_price_value(item.get("price", ""))
    
    # 1. Impulse Buy Score (Sweet spot for TikTok Shop is $12 - $35)
    if 10 <= price_val <= 30:
        impulse_score = 95
    elif 30 < price_val <= 45:
        impulse_score = 80
    elif price_val < 10:
        impulse_score = 85
    else:
        impulse_score = 65

    # 2. Viral Score calculation
    viral_score = 50
    if "tiktok" in source.lower():
        viral_score = item.get("impulse_score", 90)
    elif "google trends" in source.lower():
        traffic = item.get("traffic_num", 10000)
        if traffic >= 100000:
            viral_score = 94
        elif traffic >= 50000:
            viral_score = 88
        else:
            viral_score = 78
    elif "amazon" in source.lower():
        rank = item.get("rank", "")
        if rank in ["#1", "#2", "#3"]:
            viral_score = 92
        elif rank in ["#4", "#5", "#6"]:
            viral_score = 86
        else:
            viral_score = 75
    elif "ebay" in source.lower():
        viral_score = 76

    # Boost viral score for highly visual / demonstration categories
    visual_keywords = ["makeup", "toner", "pore", "skin", "cleaning", "scrubber", "tumbler", "printer", "hair", "patch"]
    if any(k in title for k in visual_keywords):
        viral_score = min(99, viral_score + 6)

    # 3. Evergreen Score calculation
    evergreen_score = 45
    evergreen_niches = [
        "personalized", "custom", "docking", "calendar", "cutting board", 
        "necklace", "jewelry", "candle", "swab", "towel", "water bottle", "brush", "pillow"
    ]
    if "etsy" in source.lower():
        evergreen_score = 94
    elif any(k in title for k in evergreen_niches):
        evergreen_score = 90
    elif "amazon" in source.lower():
        reviews = item.get("reviews", "0")
        try:
            rev_num = int(str(reviews).replace(',', '').replace('+', ''))
            if rev_num > 50000:
                evergreen_score = 92
            elif rev_num > 10000:
                evergreen_score = 85
            else:
                evergreen_score = 75
        except Exception:
            evergreen_score = 78
    elif "ebay" in source.lower():
        evergreen_score = 72

    # Category evergreen weight
    if category in ["Beauty & Skincare", "Home Gadgets", "Home & Kitchen", "Pets & Animals", "Personalized Gifts"]:
        evergreen_score = min(98, evergreen_score + 5)

    # 4. Classification determination
    if "etsy" in source.lower() or evergreen_score >= 88 and viral_score < 93:
        classification = "EVERGREEN_WINNER"
        label = "🌲 Evergreen Bền Vững"
        badge_color = "emerald"
    elif viral_score >= 88 or "tiktok" in source.lower() or "google trends" in source.lower():
        classification = "VIRAL_SPIKE_24H"
        label = "🔥 Bùng Nổ 24h (Viral Spike)"
        badge_color = "rose"
    elif evergreen_score > viral_score:
        classification = "EVERGREEN_WINNER"
        label = "🌲 Evergreen Tiềm Năng"
        badge_color = "emerald"
    else:
        classification = "VIRAL_SPIKE_24H"
        label = "🔥 Xu Hướng Tăng Trưởng"
        badge_color = "amber"

    # Overall Opportunity Score
    opportunity_score = round((viral_score * 0.55 + evergreen_score * 0.45), 1)

    # 5. Sales & GMV Estimation (24h vs 30 Days)
    existing_sales_24h = item.get("sales_24h") or item.get("sales_count_24h")
    if existing_sales_24h is not None:
        sales_24h = int(existing_sales_24h)
    else:
        # Estimate based on traffic or viral score
        if "tiktok" in source.lower():
            sales_24h = int(viral_score * 32 + (opportunity_score * 12))
        elif "amazon" in source.lower():
            sales_24h = int(viral_score * 25 + 200)
        else:
            sales_24h = int(viral_score * 15 + 80)

    # 30-day sales volume (historical monthly cumulative)
    existing_sales_30d = item.get("sales_30d")
    if existing_sales_30d is not None:
        sales_30d = int(existing_sales_30d)
    else:
        sales_30d = int(sales_24h * 16.5 + (evergreen_score * 45))

    gmv_24h = round(sales_24h * price_val, 2)
    gmv_30d = round(sales_30d * price_val, 2)

    # 6. New Listing Detection (<24h with real sales >= 5)
    listing_age_hours = item.get("listing_age_hours")
    if listing_age_hours is None:
        # Identify newly listed breakout items
        is_new_listing_24h = item.get("is_new_listing_24h", False) or ("new" in title and sales_24h >= 5) or (viral_score >= 93 and evergreen_score < 70)
        listing_age_hours = 14.5 if is_new_listing_24h else 120.0
    else:
        listing_age_hours = float(listing_age_hours)
        is_new_listing_24h = (listing_age_hours <= 24.0 and sales_24h >= 5)

    # 7. Smart Tags & Badges
    tags = list(item.get("tags", []))
    if is_new_listing_24h and "NEW_LISTING_24H" not in tags:
        tags.append("NEW_LISTING_24H")
    if classification == "VIRAL_SPIKE_24H" and "VIRAL_SPIKE_24H" not in tags:
        tags.append("VIRAL_SPIKE_24H")
    if sales_30d >= 8000 and "TOP_SELLER_30D" not in tags:
        tags.append("TOP_SELLER_30D")
    if impulse_score >= 90 and "HIGH_CONVERSION" not in tags:
        tags.append("HIGH_CONVERSION")

    # 8. Keywords Extraction
    keywords = list(item.get("keywords", []))
    if not keywords:
        clean_words = re.sub(r'[^a-zA-Z0-9\s]', ' ', item.get("title", "")).split()
        stop_words = {"the", "a", "an", "and", "or", "for", "with", "in", "on", "of", "to", "set", "pack"}
        meaningful = [w.lower() for w in clean_words if len(w) > 2 and w.lower() not in stop_words]
        if len(meaningful) >= 4:
            keywords = [
                f"{meaningful[0]} {meaningful[1]}",
                f"{meaningful[1]} {meaningful[2]}",
                f"{meaningful[0]} {meaningful[-1]}"
            ]
        elif meaningful:
            keywords = [" ".join(meaningful[:3])]
        else:
            keywords = ["tiktok shop viral", "trending us"]

    return {
        "viral_score": viral_score,
        "evergreen_score": evergreen_score,
        "impulse_score": impulse_score,
        "opportunity_score": opportunity_score,
        "classification": classification,
        "label": label,
        "badge_color": badge_color,
        "clean_price": f"${price_val:.2f}",
        "price_val": price_val,
        "sales_24h": sales_24h,
        "sales_30d": sales_30d,
        "gmv_24h": gmv_24h,
        "gmv_30d": gmv_30d,
        "is_new_listing_24h": is_new_listing_24h,
        "listing_age_hours": listing_age_hours,
        "tags": tags,
        "keywords": keywords
    }
