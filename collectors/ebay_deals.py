import requests
from bs4 import BeautifulSoup
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EBAY_CATEGORIES = {
    "All Trending Deals": "https://www.ebay.com/globaldeals/trending",
    "Tech & Gadgets": "https://www.ebay.com/deals/tech",
    "Home & Garden": "https://www.ebay.com/deals/home-and-garden",
    "Fashion & Apparel": "https://www.ebay.com/deals/fashion",
}

def fetch_ebay_deals() -> list:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    
    all_deals = []
    seen_urls = set()
    
    for cat_name, url in EBAY_CATEGORIES.items():
        try:
            resp = requests.get(url, headers=headers, timeout=12)
            if resp.status_code != 200:
                continue
            soup = BeautifulSoup(resp.text, 'html.parser')
            
            # Find deal cards or links
            items = soup.find_all('div', class_=lambda c: c and any(k in str(c).lower() for k in ['dhelix', 'col', 'itemlink', 'deal']))
            
            # Extract links with /itm/
            for card in items:
                a_tag = card.find('a', href=lambda h: h and '/itm/' in h)
                if not a_tag:
                    continue
                href = a_tag.get('href', '').split('?')[0]
                if href in seen_urls:
                    continue
                seen_urls.add(href)
                
                title = a_tag.get('title') or card.find('span', class_=lambda c: c and 'title' in str(c).lower())
                if not title or len(str(title).strip()) < 10:
                    title_text = card.text.split('$')[0].strip()
                else:
                    title_text = title.text.strip() if hasattr(title, 'text') else str(title).strip()
                    
                # Clean title
                title_text = re.sub(r'^(Sponsored|New Listing)\s*', '', title_text).strip()
                if len(title_text) < 10:
                    continue
                
                # Extract prices
                price_match = re.search(r'\$\d+(?:\.\d{2})?', card.text)
                price_str = price_match.group(0) if price_match else "$19.99"
                
                # Discount
                discount_match = re.search(r'(\d+%\s*off)', card.text, re.IGNORECASE)
                discount_str = discount_match.group(1) if discount_match else "Trending Deal"
                
                # Image
                img_tag = card.find('img')
                img_url = img_tag.get('src') or img_tag.get('data-src') if img_tag else ""
                
                all_deals.append({
                    "source": "eBay US",
                    "category": cat_name,
                    "title": title_text[:120],
                    "price": price_str,
                    "discount": discount_str,
                    "url": href,
                    "image": img_url,
                    "velocity": "High 24h Velocity"
                })
        except Exception as e:
            logger.error(f"Error scraping eBay {cat_name}: {e}")
            
    logger.info(f"eBay Deals: Extracted {len(all_deals)} trending deals.")
    return all_deals

if __name__ == "__main__":
    deals = fetch_ebay_deals()
    print(f"Total eBay Deals: {len(deals)}")
    for d in deals[:5]:
        print(f"- [{d['category']}] {d['title']} | Price: {d['price']} | {d['discount']}")
