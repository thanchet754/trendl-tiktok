import sys
import time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1200})
    print("Navigating to https://trendl-tiktok-eight.vercel.app ...")
    page.goto("https://trendl-tiktok-eight.vercel.app", wait_until="domcontentloaded", timeout=45000)
    time.sleep(3)
    
    # Scroll down 900px
    page.evaluate("window.scrollTo(0, 950)")
    time.sleep(2)
    
    # Take screenshot of table area
    overview_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_table_distinct_thumbnails.png"
    page.screenshot(path=overview_path)
    print("Saved live table overview screenshot to:", overview_path)
    
    # Check rows
    rows = page.locator("tr:has-text('SP TikTok')").all()
    print(f"Found {len(rows)} rows with SP TikTok button")
    if len(rows) > 1:
        row2 = rows[1]
        btn = row2.locator("button:has-text('SP TikTok')").first
        print("Clicking SP TikTok button on Row 2...")
        btn.click()
        time.sleep(2)
        
        # Take full screenshot with open drawer
        drawer_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_steering_wheel_drawer.png"
        page.screenshot(path=drawer_path)
        print("Saved live drawer screenshot to:", drawer_path)
        
    b.close()
