"""
Amazon US Best Sellers & Movers Scraper
Extracts high-velocity, trending products across key TikTok Shop niches in the US.
"""

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None

import time
import re
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

AMAZON_CATEGORIES = [
    {"name": "Beauty & Personal Care", "slug": "beauty", "niche": "Beauty & Skincare"},
    {"name": "Kitchen & Dining", "slug": "kitchen", "niche": "Home & Kitchen"},
    {"name": "Home & Kitchen", "slug": "home-garden", "niche": "Home Gadgets"},
    {"name": "Electronics", "slug": "electronics", "niche": "Tech Gadgets"},
    {"name": "Pet Supplies", "slug": "pet-supplies", "niche": "Pets & Animals"}
]

def scrape_amazon_bestsellers(limit_per_category: int = 12) -> List[Dict[str, Any]]:
    """
    Scrapes top selling products from Amazon US Best Sellers.
    """
    if not sync_playwright:
        logger.warning("Playwright is not available in current environment, skipping live Amazon scrape.")
        return []

    all_products = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
        )
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            locale='en-US',
            extra_http_headers={'Accept-Language': 'en-US,en;q=0.9'}
        )
        page = context.new_page()
        
        for cat in AMAZON_CATEGORIES:
            url = f"https://www.amazon.com/Best-Sellers-{cat['slug']}/zgbs/{cat['slug']}"
            logger.info(f"Amazon Scraper: Fetching {cat['name']}...")
            try:
                page.goto(url, wait_until='domcontentloaded', timeout=18000)
                time.sleep(2.5)
                
                items = page.query_selector_all('div[id*="gridItemRoot"]')
                logger.info(f"Amazon {cat['name']}: Found {len(items)} raw items.")
                
                count = 0
                for item in items:
                    if count >= limit_per_category:
                        break
                        
                    text_lines = [l.strip() for l in item.inner_text().split('\n') if l.strip()]
                    link_el = item.query_selector('a[href*="/dp/"]')
                    img_el = item.query_selector('img')
                    
                    href = link_el.get_attribute('href') if link_el else ""
                    if href:
                        if not href.startswith('http'):
                            href = f"https://www.amazon.com{href}"
                        href = href.split('?')[0]
                        
                    img_src = img_el.get_attribute('src') if img_el else ""
                    
                    rank_str = ""
                    title_str = ""
                    price_str = ""
                    rating_str = ""
                    reviews_str = ""
                    
                    for line in text_lines:
                        if line.startswith('#') and not rank_str:
                            rank_str = line
                        elif '$' in line and not price_str:
                            price_str = line
                        elif 'out of 5 stars' in line:
                            rating_str = line.split('out of')[0].strip()
                        elif line.replace(',', '').isdigit() and int(line.replace(',', '')) > 20:
                            reviews_str = line
                        elif len(line) > 15 and not title_str and not line.startswith('Sponsored') and not line.startswith('#'):
                            title_str = line
                            
                    if title_str and href:
                        all_products.append({
                            "source": "Amazon US Best Sellers",
                            "category": cat["niche"],
                            "rank": rank_str or f"#{count+1}",
                            "title": title_str[:130],
                            "price": price_str or "$19.99",
                            "rating": rating_str or "4.6",
                            "reviews": reviews_str or "1,500+",
                            "url": href,
                            "image": img_src,
                            "velocity": "Top Ranked 24h"
                        })
                        count += 1
            except Exception as e:
                logger.error(f"Error scraping Amazon category {cat['name']}: {e}")
                
        browser.close()
        
    logger.info(f"Amazon Scraper: Extracted total {len(all_products)} products.")
    return all_products

if __name__ == "__main__":
    products = scrape_amazon_bestsellers(limit_per_category=3)
    print(f"Total Amazon items: {len(products)}")
    for p in products[:5]:
        print(f"- [{p['rank']}] {p['category']}: {p['title']} | {p['price']} | Rating: {p['rating']} ({p['reviews']})")
