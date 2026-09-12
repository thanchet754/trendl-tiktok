import os
import json
import logging
from typing import Dict, Any, List
import requests

logger = logging.getLogger("SupabaseClient")
logging.basicConfig(level=logging.INFO)

# Supabase Credentials
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://jwkgzrzlsnfvuhumtdjy.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp3a2d6cnpsc25mdnVodW10ZGp5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE1OTEwMTgsImV4cCI6MjA5NzE2NzAxOH0.2iLifMZrloTtvlSNWdiIZ_Fj3UN2xELWC0ivPQho-Sg")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates"
}

import re
import hashlib

def clean_float(val, default=0.0) -> float:
    if isinstance(val, (int, float)):
        return float(val)
    if not val:
        return default
    matches = re.findall(r'(\d+(?:\.\d+)?)', str(val))
    if matches:
        return float(matches[0])
    return default

def clean_int(val, default=0) -> int:
    if isinstance(val, int):
        return val
    if isinstance(val, float):
        return int(val)
    if not val:
        return default
    cleaned = re.sub(r'[^\d]', '', str(val))
    return int(cleaned) if cleaned else default

def sync_trends_to_supabase(analyzed_data: Dict[str, Any]) -> bool:
    """
    Đồng bộ toàn bộ danh sách xu hướng, video và KOCs lên Supabase
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        logger.warning("Supabase URL hoặc Key chưa được cấu hình.")
        return False

    success = True
    
    # 1. Upsert TikTok Trends
    trends = analyzed_data.get("all_ideas", [])
    if trends:
        trends_payload = []
        for it in trends:
            raw_id = str(it.get("id") or "")
            if not raw_id or raw_id == "None":
                title_key = (it.get("title", "") + it.get("category", "")).strip()
                raw_id = f"trend_{hashlib.md5(title_key.encode('utf-8')).hexdigest()[:12]}"
            
            raw_sales = it.get("sales_24h", it.get("sales_count_24h", 0))
            sales_24h = clean_int(raw_sales, 0)
            price = clean_float(it.get("price", 0), 0.0)
            gmv_24h = clean_float(it.get("gmv_24h", round(sales_24h * price, 2)), 0.0)
            sales_30d = clean_int(it.get("sales_30d", sales_24h * 15), 0)
            gmv_30d = clean_float(it.get("gmv_30d", round(sales_30d * price, 2)), 0.0)
            is_new = bool(it.get("is_new_listing_24h", False))
            tags = it.get("tags", [])
            if not tags:
                tags = [it.get("classification", "VIRAL_SPIKE_24H")]
                if is_new:
                    tags.append("NEW_LISTING_24H")
            
            trends_payload.append({
                "id": raw_id,
                "title": it.get("title", ""),
                "category": it.get("category", "General"),
                "sub_niche": it.get("sub_niche", ""),
                "price": price,
                "rank_in_category": clean_int(it.get("rank_in_category", 999), 999),
                "rank_overall": clean_int(it.get("rank_overall", 9999), 9999),
                "sales_24h": sales_24h,
                "gmv_24h": gmv_24h,
                "sales_30d": sales_30d,
                "gmv_30d": gmv_30d,
                "classification": it.get("classification", "VIRAL_SPIKE_24H"),
                "velocity_score": clean_float(it.get("velocity_score", 0), 0.0),
                "is_new_listing_24h": is_new,
                "listing_time": it.get("listing_time", "2026-09-12T00:00:00Z"),
                "listing_age_hours": clean_float(it.get("listing_age_hours", 24.0), 24.0),
                "tags": tags,
                "keywords": it.get("keywords", []),
                "image_url": it.get("image", ""),
                "shop_url": it.get("tiktok_url", ""),
                "query_1688": it.get("query_1688", ""),
                "query_alibaba": it.get("query_alibaba", ""),
                "platform_sources": it.get("platform_sources", ["TikTok Shop US"]),
                "verification_24h": it.get("verification_24h", {}),
                "strategy": it.get("strategy", {})
            })
        
        # Deduplicate by id to avoid Postgres 21000 ON CONFLICT error
        unique_trends = {}
        for p in trends_payload:
            unique_trends[p["id"]] = p
        clean_payload = list(unique_trends.values())

        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_trends",
                headers=HEADERS,
                json=clean_payload,
                timeout=20
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(clean_payload)} sản phẩm xu hướng lên Supabase.")
            else:
                logger.warning(f"Lỗi đồng bộ trends lên Supabase ({res.status_code}): {res.text}")
                success = False
        except Exception as e:
            logger.error(f"Lỗi kết nối Supabase trends: {e}")
            success = False

    # 2. Upsert TikTok Creators
    creators = analyzed_data.get("top_influencers", [])
    if creators:
        creators_payload = []
        for c in creators:
            cid = str(c.get("id", c.get("handle")))
            creators_payload.append({
                "id": cid,
                "handle": c.get("handle", ""),
                "nickname": c.get("nickname", ""),
                "avatar_url": c.get("avatar", ""),
                "follower_count": clean_int(c.get("follower_count", 0), 0),
                "gmv_24h": clean_float(c.get("gmv_24h", 0), 0.0),
                "items_sold_24h": clean_int(c.get("items_sold_24h", 0), 0),
                "category": c.get("category", ""),
                "sub_niche": c.get("sub_niche", ""),
                "top_product_title": c.get("top_product_title", ""),
                "top_product_image": c.get("top_product_image", "")
            })
            
        unique_creators = {p["id"]: p for p in creators_payload}
        clean_creators = list(unique_creators.values())

        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_creators",
                headers=HEADERS,
                json=clean_creators,
                timeout=15
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(clean_creators)} creators lên Supabase.")
            else:
                logger.warning(f"Lỗi đồng bộ creators lên Supabase ({res.status_code}): {res.text}")
                success = False
        except Exception as e:
            logger.error(f"Lỗi kết nối Supabase creators: {e}")
            success = False

    # 3. Upsert TikTok Videos
    videos = analyzed_data.get("top_videos", [])
    if videos:
        videos_payload = []
        for v in videos:
            vid = str(v.get("id", v.get("video_id")))
            videos_payload.append({
                "id": vid,
                "video_id": str(v.get("video_id", "")),
                "author_handle": v.get("author_handle", ""),
                "title": v.get("title", ""),
                "cover_url": v.get("cover_url", ""),
                "views_24h": clean_int(v.get("views_24h", 0), 0),
                "est_items_sold": clean_int(v.get("est_items_sold", 0), 0),
                "est_gmv_24h": clean_float(v.get("est_gmv_24h", 0), 0.0),
                "sound_title": v.get("sound_title", ""),
                "category": v.get("category", "")
            })
            
        unique_videos = {p["id"]: p for p in videos_payload}
        clean_videos = list(unique_videos.values())

        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_videos",
                headers=HEADERS,
                json=clean_videos,
                timeout=15
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(clean_videos)} videos lên Supabase.")
            else:
                logger.warning(f"Lỗi đồng bộ videos lên Supabase ({res.status_code}): {res.text}")
                success = False
        except Exception as e:
            logger.error(f"Lỗi kết nối Supabase videos: {e}")
            success = False

    return success

def fetch_trends_from_supabase(limit: int = 1000) -> List[Dict[str, Any]]:
    """Lấy danh sách sản phẩm xu hướng từ Supabase xếp hạng theo GMV / Sales 24h"""
    try:
        url = f"{SUPABASE_URL}/rest/v1/tiktok_trends?select=*&order=sales_24h.desc&limit={limit}"
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            return res.json()
        return []
    except Exception as e:
        logger.error(f"Lỗi khi đọc trends từ Supabase: {e}")
        return []

def fetch_creators_from_supabase(limit: int = 50) -> List[Dict[str, Any]]:
    """Lấy danh sách top influencers từ Supabase"""
    try:
        url = f"{SUPABASE_URL}/rest/v1/tiktok_creators?select=*&order=gmv_24h.desc&limit={limit}"
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            return res.json()
        return []
    except Exception as e:
        logger.error(f"Lỗi khi đọc creators từ Supabase: {e}")
        return []

def fetch_videos_from_supabase(limit: int = 50) -> List[Dict[str, Any]]:
    """Lấy danh sách top viral videos từ Supabase"""
    try:
        url = f"{SUPABASE_URL}/rest/v1/tiktok_videos?select=*&order=est_gmv_24h.desc&limit={limit}"
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            return res.json()
        return []
    except Exception as e:
        logger.error(f"Lỗi khi đọc videos từ Supabase: {e}")
        return []
