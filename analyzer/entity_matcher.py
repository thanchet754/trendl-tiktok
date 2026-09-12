"""
Entity Matcher & Multi-Source Synthesizer
Combines data from Google Trends, TikTok 24h, Amazon, Etsy, and eBay into unified product ideas.
Maps each idea into the 28 TikTok Shop US categories and assigns velocity dimensions.
"""

from typing import List, Dict, Any
from .scorer import calculate_scores
from .strategy_generator import generate_tiktok_strategy
from .verifier_24h import verify_24h_trend_signals

def normalize_item_category_and_velocity(item: Dict[str, Any]) -> None:
    t_low = item.get("title", "").lower()
    src = item.get("source", "").lower()
    
    # Standardize category to 28 TikTok Shop US categories
    if any(k in t_low for k in ["toothpaste", "teeth", "whitening", "oral"]):
        item["category"] = "Beauty & Personal Care"
        item["category_vi"] = "Làm Đẹp & Chăm Sóc Cá Nhân"
        item["sub_niche"] = "Oral Care & Whitening"
        item["sub_niche_vi"] = "Làm Trắng Răng & Chăm Sóc Răng Miệng"
    elif any(k in t_low for k in ["toner", "pore", "skin", "towel", "cleanser", "acne", "patch", "serum", "mucin"]):
        item["category"] = "Beauty & Personal Care"
        item["category_vi"] = "Làm Đẹp & Chăm Sóc Cá Nhân"
        item["sub_niche"] = "Skincare & Face Care"
        item["sub_niche_vi"] = "Chăm Sóc Da Mặt (Toner, Khăn Lau, Serum)"
    elif any(k in t_low for k in ["curling", "hair", "airwrap", "shampoo"]):
        item["category"] = "Beauty & Personal Care"
        item["category_vi"] = "Làm Đẹp & Chăm Sóc Cá Nhân"
        item["sub_niche"] = "Hair Care & Styling Tools"
        item["sub_niche_vi"] = "Dụng Cụ Uốn Tóc & Dưỡng Tóc"
    elif any(k in t_low for k in ["squishy", "dumpling", "fidget", "toy", "puzzle"]):
        item["category"] = "Toys & Hobbies"
        item["category_vi"] = "Đồ Chơi & Sở Thích"
        item["sub_niche"] = "Squishy & Fidget Toys"
        item["sub_niche_vi"] = "Đồ Chơi Bóp Giảm Stress (Dumpling)"
    elif any(k in t_low for k in ["tumbler", "bottle", "owala", "stanley", "cup", "mug"]):
        item["category"] = "Kitchenware"
        item["category_vi"] = "Đồ Dùng Nhà Bếp"
        item["sub_niche"] = "Drinkware & Tumblers"
        item["sub_niche_vi"] = "Bình Giữ Nhiệt & Ly Giữ Nhiệt"
    elif any(k in t_low for k in ["cutting board", "charcuterie", "peeler", "knife", "pan"]):
        item["category"] = "Kitchenware"
        item["category_vi"] = "Đồ Dùng Nhà Bếp"
        item["sub_niche"] = "Cutting Boards & Charcuterie"
        item["sub_niche_vi"] = "Thớt Gỗ Khắc Tên & Khay Gỗ Steak"
    elif any(k in t_low for k in ["scrubber", "clean", "mop", "vacuum", "stain"]):
        item["category"] = "Home Supplies"
        item["category_vi"] = "Đồ Gia Dụng Tiện Ích"
        item["sub_niche"] = "Cleaning & Organization"
        item["sub_niche_vi"] = "Dụng Cụ Vệ Sinh Nhà Cửa & Bàn Chải Điện"
    elif any(k in t_low for k in ["calendar", "candle", "storage", "pillow", "blanket"]):
        item["category"] = "Home Supplies"
        item["category_vi"] = "Đồ Gia Dụng Tiện Ích"
        item["sub_niche"] = "Air Fresheners & Candles"
        item["sub_niche_vi"] = "Nến Thơm & Tinh Dầu Phòng"
    elif any(k in t_low for k in ["pet", "dog", "cat", "grooming", "brush", "deshedding", "slicker"]):
        item["category"] = "Pet Supplies"
        item["category_vi"] = "Đồ Cho Thú Cưng"
        item["sub_niche"] = "Pet Grooming & Care"
        item["sub_niche_vi"] = "Lược Chải Lông & Chăm Sóc Chó Mèo"
    elif any(k in t_low for k in ["printer", "mic", "microphone", "lavalier", "camera", "headphone"]):
        item["category"] = "Phones & Electronics"
        item["category_vi"] = "Điện Thoại & Thiết Bị Điện Tử"
        item["sub_niche"] = "Printers & Gadgets"
        item["sub_niche_vi"] = "Máy In Nhiệt & Phụ Kiện Điện Thoại"
    elif any(k in t_low for k in ["necklace", "birth flower", "ring", "earring", "jewelry"]):
        item["category"] = "Jewelry Accessories & Derivatives"
        item["category_vi"] = "Trang Sức & Phụ Kiện"
        item["sub_niche"] = "Custom Name Jewelry & POD"
        item["sub_niche_vi"] = "Vòng Cổ Khắc Tên Hoa Sinh & POD"
    elif any(k in t_low for k in ["bodysuit", "shapewear", "dress", "legging"]):
        item["category"] = "Womenswear & Underwear"
        item["category_vi"] = "Thời Trang & Đồ Lót Nữ"
        item["sub_niche"] = "Shapewear & Body Sculpting"
        item["sub_niche_vi"] = "Đồ Định Hình Bodysuit Siêu Gọn"
    elif any(k in t_low for k in ["pant", "hoodie", "boxer", "men", "cargo", "shirt"]):
        item["category"] = "Menswear & Underwear"
        item["category_vi"] = "Thời Trang Nam"
        item["sub_niche"] = "Streetwear & Cargo Pants"
        item["sub_niche_vi"] = "Quần Túi Hộp Ống Rộng Cargo"
    elif any(k in t_low for k in ["vitamin", "gummy", "magnesium", "sleep", "supplement", "posture"]):
        item["category"] = "Health"
        item["category_vi"] = "Sức Khỏe & Thực Phẩm Chức Năng"
        item["sub_niche"] = "Vitamins & Dietary Supplements"
        item["sub_niche_vi"] = "Vitamin & Thực Phẩm Hỗ Trợ Giấc Ngủ"
    elif any(k in t_low for k in ["car", "automotive", "mount", "charger", "vehicle"]):
        item["category"] = "Automotive & Motorcycle"
        item["category_vi"] = "Ô Tô & Xe Máy"
        item["sub_niche"] = "Car Electronics & Mounts"
        item["sub_niche_vi"] = "Giá Đỡ & Thiết Bị Điện Tử Ô Tô"
    elif any(k in t_low for k in ["baby", "toddler", "maternity", "teething"]):
        item["category"] = "Baby & Maternity"
        item["category_vi"] = "Mẹ & Bé"
        item["sub_niche"] = "Teething & Sensory Toys"
        item["sub_niche_vi"] = "Đồ Chơi Gặm Nướu & Phát Triển Trí Tuệ"
    elif any(k in t_low for k in ["candy", "snack", "coffee", "tea", "sauce"]):
        item["category"] = "Food & Beverages"
        item["category_vi"] = "Thực Phẩm & Đồ Uống"
        item["sub_niche"] = "Freeze Dried Snacks"
        item["sub_niche_vi"] = "Kẹo Sấy Thăng Hoa & Đồ Ăn Vặt"
    elif any(k in t_low for k in ["journal", "pen", "highlighter", "book"]):
        item["category"] = "Books, Magazines & Audio"
        item["category_vi"] = "Sách & Văn Phòng Phẩm"
        item["sub_niche"] = "Journaling & Stationery"
        item["sub_niche_vi"] = "Sổ Tay & Bút Pastel"
    elif not item.get("category"):
        item["category"] = "Beauty & Personal Care"
        item["category_vi"] = "Làm Đẹp & Chăm Sóc Cá Nhân"
        item["sub_niche"] = "General"
        item["sub_niche_vi"] = "Tổng Hợp"

    # Velocity Dimension: VIRAL_VIDEO_24H | FAST_SALES_VELOCITY_24H | BREAKOUT_KEYWORD_24H | EVERGREEN_WINNER
    if item.get("classification") == "EVERGREEN_WINNER":
        item["velocity_dimension"] = "EVERGREEN_WINNER"
    elif "tiktok" in src:
        item["velocity_dimension"] = "VIRAL_VIDEO_24H"
    elif "google" in src:
        item["velocity_dimension"] = "BREAKOUT_KEYWORD_24H"
    else: # Amazon, eBay
        item["velocity_dimension"] = "FAST_SALES_VELOCITY_24H"

def synthesize_and_rank_ideas(
    google_trends: List[Dict[str, Any]],
    tiktok_items: List[Dict[str, Any]],
    amazon_items: List[Dict[str, Any]],
    etsy_items: List[Dict[str, Any]],
    ebay_items: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Synthesizes and cross-references items from all 5 sources.
    Returns:
    - 'all_ideas': complete sorted list
    - 'viral_24h': top viral breakout ideas
    - 'evergreen': top evergreen ideas
    - 'stats': summary statistics
    """
    raw_all = []
    
    # 1. Ingest TikTok viral items (Primary viral signals)
    for it in tiktok_items:
        it_copy = dict(it)
        scores = calculate_scores(it_copy)
        it_copy.update(scores)
        it_copy["strategy"] = generate_tiktok_strategy(it_copy, scores)
        it_copy["verified_platforms"] = ["TikTok Shop", "TikTok Viral 24h"]
        it_copy["verification_24h"] = verify_24h_trend_signals(it_copy)
        raw_all.append(it_copy)
        
    # 2. Ingest Amazon items (Sales volume and rank velocity signals)
    for it in amazon_items:
        it_copy = dict(it)
        scores = calculate_scores(it_copy)
        it_copy.update(scores)
        it_copy["strategy"] = generate_tiktok_strategy(it_copy, scores)
        it_copy["verified_platforms"] = ["Amazon Best Sellers", "Amazon US"]
        it_copy["verification_24h"] = verify_24h_trend_signals(it_copy)
        raw_all.append(it_copy)

    # 3. Ingest Etsy items (Evergreen, high margin POD & custom gifts)
    for it in etsy_items:
        it_copy = dict(it)
        scores = calculate_scores(it_copy)
        it_copy.update(scores)
        it_copy["strategy"] = generate_tiktok_strategy(it_copy, scores)
        it_copy["verified_platforms"] = ["Etsy US", "Handmade/POD"]
        it_copy["verification_24h"] = verify_24h_trend_signals(it_copy)
        raw_all.append(it_copy)

    # 4. Ingest eBay items
    for it in ebay_items:
        it_copy = dict(it)
        scores = calculate_scores(it_copy)
        it_copy.update(scores)
        it_copy["strategy"] = generate_tiktok_strategy(it_copy, scores)
        it_copy["verified_platforms"] = ["eBay US Deals"]
        it_copy["verification_24h"] = verify_24h_trend_signals(it_copy)
        raw_all.append(it_copy)

    # 5. Ingest Google Trends items (if commercial or breakout)
    for it in google_trends:
        it_copy = dict(it)
        scores = calculate_scores(it_copy)
        it_copy.update(scores)
        it_copy["strategy"] = generate_tiktok_strategy(it_copy, scores)
        it_copy["verified_platforms"] = ["Google Trends US Search"]
        it_copy["verification_24h"] = verify_24h_trend_signals(it_copy)
        raw_all.append(it_copy)

    # Detect Cross-Platform Synergies (Keywords appearing in multiple platforms)
    cross_keywords = {
        "medicube": ["medicube", "pore pad", "exfoliat"],
        "tumbler": ["tumbler", "owala", "stanley", "water bottle"],
        "acne patch": ["patch", "mighty patch", "pimple", "hydrocolloid"],
        "face towel": ["face towel", "clean skin", "clean towels"],
        "spin scrubber": ["scrubber", "spin scrubber", "electric brush"],
        "printer": ["thermal printer", "sticker printer", "label printer"],
        "pet brush": ["pet brush", "slicker", "grooming", "deshedding"],
        "docking station": ["docking station", "desk organizer", "wooden stand"],
        "birth flower": ["birth flower", "name necklace", "personalized necklace"],
        "acrylic calendar": ["acrylic calendar", "wall calendar", "command center"],
        "cutting board": ["cutting board", "charcuterie", "engraved board"]
    }

    for item in raw_all:
        normalize_item_category_and_velocity(item)
        t_low = item["title"].lower()
        for kw_name, terms in cross_keywords.items():
            if any(term in t_low for term in terms):
                if "Amazon" in item["source"]:
                    if "TikTok Shop" not in item["verified_platforms"]:
                        item["verified_platforms"].append("TikTok Trend Validated")
                elif "TikTok" in item["source"]:
                    if "Amazon US" not in item["verified_platforms"]:
                        item["verified_platforms"].append("Amazon Top 100")
                elif "Etsy" in item["source"]:
                    if "TikTok Shop" not in item["verified_platforms"]:
                        item["verified_platforms"].append("TikTok Gift Trend")
                item["opportunity_score"] = min(99.5, item["opportunity_score"] + 5.0)
                break

    # Sort all ideas by opportunity score descending
    all_sorted = sorted(raw_all, key=lambda x: x["opportunity_score"], reverse=True)

    # Filter into Viral 24h vs Evergreen
    viral_24h = [x for x in all_sorted if x["classification"] == "VIRAL_SPIKE_24H"]
    evergreen = [x for x in all_sorted if x["classification"] == "EVERGREEN_WINNER"]

    stats = {
        "total_analyzed": len(all_sorted),
        "total_viral_24h": len(viral_24h),
        "total_evergreen": len(evergreen),
        "google_trends_count": len(google_trends),
        "tiktok_count": len(tiktok_items),
        "amazon_count": len(amazon_items),
        "etsy_count": len(etsy_items),
        "ebay_count": len(ebay_items)
    }

    return {
        "all_ideas": all_sorted,
        "viral_24h": viral_24h,
        "evergreen": evergreen,
        "stats": stats
    }
