"""
Google Trends US Daily & Real-time Trends Collector
Fetches real-time breakout trends, rising search queries, and shopping-related trends in the US.
"""

import xml.etree.ElementTree as ET
import logging
from typing import List, Dict, Any
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Categories relevant to TikTok Shop & E-commerce
COMMERCE_KEYWORDS = {
    "Beauty & Personal Care": [
        "makeup", "skin", "hair", "lip", "lash", "serum", "perfume", "fragrance", 
        "nail", "cream", "shampoo", "glow", "oil", "sunscreen", "eyeliner", "cosmetics"
    ],
    "Home & Kitchen": [
        "cup", "tumbler", "bottle", "cleaning", "pillow", "blanket", "candle", 
        "kitchen", "cooker", "blender", "organizer", "rack", "pan", "gadget", "light", "lamp"
    ],
    "Fashion & Apparel": [
        "dress", "shoes", "jacket", "hoodie", "pants", "shirt", "outfit", "bag", 
        "jewelry", "necklace", "ring", "crocs", "sneakers", "hat", "leggings", "swimwear"
    ],
    "Gadgets & Electronics": [
        "phone", "charger", "case", "camera", "earbuds", "headphones", "bluetooth", 
        "led", "smart", "projector", "watch", "drone", "speaker", "powerbank", "cable"
    ],
    "Pets & Animals": [
        "dog", "cat", "pet", "puppy", "kitten", "collar", "leash", "feeder", "toy", "brush", "harness"
    ],
    "DIY, Craft & POD": [
        "gift", "custom", "mug", "shirt", "decor", "print", "craft", "stickers", 
        "personalized", "art", "canvas", "crochet", "poster"
    ],
    "Health & Fitness": [
        "gummies", "protein", "fitness", "workout", "weight", "massage", "posture", 
        "gym", "yoga", "supplement", "band", "roller"
    ]
}

def detect_category_and_commercial(title: str, snippet: str = "") -> tuple[str, bool]:
    combined = (title + " " + snippet).lower()
    for cat, kws in COMMERCE_KEYWORDS.items():
        for kw in kws:
            if kw in combined:
                return cat, True
    return "General Trend", False

def fetch_google_trends_us() -> List[Dict[str, Any]]:
    """
    Fetches real-time US daily search trends via official RSS feed.
    """
    url = "https://trends.google.com/trending/rss?geo=US"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "application/rss+xml, application/xml, text/xml, */*"
    }
    
    results = []
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code != 200:
            logger.error(f"Google Trends RSS returned status {resp.status_code}")
            return results
        
        # Parse XML
        root = ET.fromstring(resp.content)
        # Namespace for ht (Google Trends)
        namespaces = {
            'ht': 'https://trends.google.com/trending/rss'
        }
        
        items = root.findall('./channel/item')
        for item in items:
            title_el = item.find('title')
            title = title_el.text if title_el is not None and title_el.text else ""
            
            traffic_el = item.find('ht:approx_traffic', namespaces)
            traffic_str = traffic_el.text if traffic_el is not None and traffic_el.text else "10,000+"
            
            # Convert traffic string like '100,000+' to integer
            traffic_num = 10000
            try:
                clean_traffic = traffic_str.replace('+', '').replace(',', '').strip()
                traffic_num = int(clean_traffic)
            except Exception:
                pass
            
            pub_date_el = item.find('pubDate')
            pub_date = pub_date_el.text if pub_date_el is not None else ""
            
            # News title & snippet
            news_title = ""
            news_snippet = ""
            news_url = ""
            news_item_el = item.find('ht:news_item', namespaces)
            if news_item_el is not None:
                nt_el = news_item_el.find('ht:news_item_title', namespaces)
                if nt_el is not None and nt_el.text:
                    news_title = nt_el.text
                ns_el = news_item_el.find('ht:news_item_snippet', namespaces)
                if ns_el is not None and ns_el.text:
                    news_snippet = ns_el.text
                nu_el = news_item_el.find('ht:news_item_url', namespaces)
                if nu_el is not None and nu_el.text:
                    news_url = nu_el.text

            cat, is_commercial = detect_category_and_commercial(title, f"{news_title} {news_snippet}")
            
            # Google Trends direct link
            encoded_query = requests.utils.quote(title)
            trend_url = f"https://trends.google.com/trends/explore?geo=US&q={encoded_query}"
            
            results.append({
                "source": "Google Trends US",
                "title": title,
                "query": title,
                "traffic": traffic_str,
                "traffic_num": traffic_num,
                "pub_date": pub_date,
                "snippet": f"{news_title}: {news_snippet}".strip(": "),
                "news_url": news_url,
                "url": trend_url,
                "category": cat,
                "is_commercial": is_commercial,
                "raw_type": "breakout_search"
            })
            
        logger.info(f"Google Trends: Extracted {len(results)} search trends.")
    except Exception as e:
        logger.error(f"Error fetching Google Trends: {e}")
        
    return results

if __name__ == "__main__":
    trends = fetch_google_trends_us()
    print(f"Total Google trends: {len(trends)}")
    for t in trends[:5]:
        print(f"- [{t['traffic']}] {t['title']} | Cat: {t['category']} | Comm: {t['is_commercial']}")
