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
            trends_payload.append({
                "id": str(it.get("id")),
                "title": it.get("title", ""),
                "category": it.get("category", ""),
                "sub_niche": it.get("sub_niche", ""),
                "price": float(it.get("price", 0) or 0),
                "gmv_24h": float(it.get("gmv_24h", 0) or 0),
                "sales_count_24h": int(it.get("sales_count_24h", 0) or 0),
                "classification": it.get("classification", "VIRAL_SPIKE_24H"),
                "velocity_score": float(it.get("velocity_score", 0) or 0),
                "image_url": it.get("image", ""),
                "shop_url": it.get("tiktok_url", ""),
                "query_1688": it.get("query_1688", ""),
                "query_alibaba": it.get("query_alibaba", ""),
                "verification_24h": it.get("verification_24h", {}),
                "strategy": it.get("strategy", {})
            })
        
        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_trends",
                headers=HEADERS,
                json=trends_payload,
                timeout=15
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(trends_payload)} sản phẩm xu hướng lên Supabase.")
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
            creators_payload.append({
                "id": str(c.get("id", c.get("handle"))),
                "handle": c.get("handle", ""),
                "nickname": c.get("nickname", ""),
                "avatar_url": c.get("avatar", ""),
                "follower_count": int(c.get("follower_count", 0) or 0),
                "gmv_24h": float(c.get("gmv_24h", 0) or 0),
                "items_sold_24h": int(c.get("items_sold_24h", 0) or 0),
                "category": c.get("category", ""),
                "sub_niche": c.get("sub_niche", ""),
                "top_product_title": c.get("top_product_title", ""),
                "top_product_image": c.get("top_product_image", "")
            })
            
        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_creators",
                headers=HEADERS,
                json=creators_payload,
                timeout=15
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(creators_payload)} creators lên Supabase.")
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
            videos_payload.append({
                "id": str(v.get("id", v.get("video_id"))),
                "video_id": str(v.get("video_id", "")),
                "author_handle": v.get("author_handle", ""),
                "title": v.get("title", ""),
                "cover_url": v.get("cover_url", ""),
                "views_24h": int(v.get("views_24h", 0) or 0),
                "est_items_sold": int(v.get("est_items_sold", 0) or 0),
                "est_gmv_24h": float(v.get("est_gmv_24h", 0) or 0),
                "sound_title": v.get("sound_title", ""),
                "category": v.get("category", "")
            })
            
        try:
            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/tiktok_videos",
                headers=HEADERS,
                json=videos_payload,
                timeout=15
            )
            if res.status_code in [200, 201]:
                logger.info(f"Đã đồng bộ {len(videos_payload)} videos lên Supabase.")
            else:
                logger.warning(f"Lỗi đồng bộ videos lên Supabase ({res.status_code}): {res.text}")
                success = False
        except Exception as e:
            logger.error(f"Lỗi kết nối Supabase videos: {e}")
            success = False

    return success
