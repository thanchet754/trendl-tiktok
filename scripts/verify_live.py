import sys
import os
import time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1200})
    print("Navigating to https://trendl-tiktok-eight.vercel.app ...")
    page.goto("https://trendl-tiktok-eight.vercel.app", wait_until="domcontentloaded", timeout=45000)
    print("DOM loaded, waiting for table row...")
    
    page.wait_for_selector('tr:has-text("Drop Stop Multi-Pocket")', timeout=20000)
    time.sleep(2)
    
    # Check first 4 rows
    row1 = page.locator('tr:has-text("Drop Stop Multi-Pocket")').first
    row2 = page.locator('tr:has-text("Steering Wheel Desk Tray")').first
    row3 = page.locator('tr:has-text("LED Ambient Interior Light")').first
    row4 = page.locator('tr:has-text("Custom Fit All-Weather Deep Tray Rubber Floor Mats")').first
    
    img1 = row1.locator('img').first.get_attribute('src') if row1.count() > 0 else 'none'
    img2 = row2.locator('img').first.get_attribute('src') if row2.count() > 0 else 'none'
    img3 = row3.locator('img').first.get_attribute('src') if row3.count() > 0 else 'none'
    img4 = row4.locator('img').first.get_attribute('src') if row4.count() > 0 else 'none'
    
    print(f"Row 1 (Drop Stop) Thumbnail: {img1}")
    print(f"Row 2 (Steering Wheel Tray) Thumbnail: {img2}")
    print(f"Row 3 (LED Light) Thumbnail: {img3}")
    print(f"Row 4 (Floor Mats) Thumbnail: {img4}")
    
    # Capture overview of table rows showing distinct thumbnails
    overview_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_table_distinct_thumbnails.png"
    page.screenshot(path=overview_path, clip={"x": 0, "y": 450, "width": 1600, "height": 700})
    print("Saved live table overview screenshot to:", overview_path)
    
    # Test expanding Row 2 (Steering Wheel Desk Tray)
    print("\nClicking SP TikTok on Row 2 (Steering Wheel Desk Tray)...")
    btn = row2.locator('button:has-text("SP TikTok")').first
    btn.click()
    time.sleep(2)
    
    drawer = page.locator('tr[id^="cluster-drawer-"]:visible').first
    print("Drawer visible:", drawer.is_visible())
    if drawer.is_visible():
        cards = drawer.locator('a[class*="line-clamp-2"]').all()
        print(f"Products in Drawer: {len(cards)}")
        for c in cards[:3]:
            print("  - Product:", c.inner_text())
        drawer_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_steering_wheel_drawer.png"
        drawer.screenshot(path=drawer_path)
        print("Saved live drawer screenshot to:", drawer_path)
        
    b.close()
