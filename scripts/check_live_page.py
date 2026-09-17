import sys
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch()
    page = b.new_page()
    page.goto("https://trendl-tiktok-eight.vercel.app/?t=9999", wait_until="domcontentloaded")
    time.sleep(3)
    
    # Check for Drop stop row
    drop_stop = page.locator('tr:has-text("Drop Stop Multi-Pocket")')
    count = drop_stop.count()
    print("Drop stop row count on live:", count)
    
    if count > 0:
        row = drop_stop.first
        print("Found row! Text snippet:", row.inner_text()[:120].replace('\n', ' '))
        
        # Click button inside row
        btn = row.locator('button').first
        btn.click()
        time.sleep(2)
        
        # Look for visible drawer
        drawer = page.locator('tr[id^="cluster-drawer-"]:visible').first
        if drawer.is_visible():
            print("Live Drawer is visible!")
            links = drawer.locator('a[href*="tiktok.com/view/product/"]').all()
            print("TikTok shop links in drawer:", len(links))
            imgs = drawer.locator('img').all()
            print("Images in drawer:", len(imgs))
            unique_imgs = set([img.get_attribute('src') for img in imgs])
            print("Unique images:", len(unique_imgs))
            
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_tiktok_drawer.png"
            drawer.screenshot(path=artifact_path)
            print("Saved screenshot to:", artifact_path)
    else:
        print("Drop stop row not found! Checking why...")
        # Check all table rows
        all_tr = page.locator('table tr').all()
        print("Total tr elements:", len(all_tr))
    b.close()
