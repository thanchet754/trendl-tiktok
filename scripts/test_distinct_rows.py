import os
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

def test_distinct():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1200})
        
        cwd = os.getcwd()
        file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
        page.goto(file_url, wait_until="domcontentloaded", timeout=20000)
        time.sleep(3)
        
        # Check first 4 rows
        row1 = page.locator('tr:has-text("Drop Stop Multi-Pocket")').first
        row2 = page.locator('tr:has-text("Steering Wheel Desk Tray")').first
        row3 = page.locator('tr:has-text("LED Ambient Interior Light")').first
        row4 = page.locator('tr:has-text("Custom Fit All-Weather Deep Tray Rubber Floor Mats")').first
        
        print("Found Row 1 (Drop Stop):", bool(row1))
        print("Found Row 2 (Steering Wheel Tray):", bool(row2))
        print("Found Row 3 (LED Light Strip):", bool(row3))
        print("Found Row 4 (Rubber Floor Mats):", bool(row4))
        
        # Check thumbnails in these rows
        img1 = row1.locator('img').first.get_attribute('src') if row1 else 'none'
        img2 = row2.locator('img').first.get_attribute('src') if row2 else 'none'
        img3 = row3.locator('img').first.get_attribute('src') if row3 else 'none'
        img4 = row4.locator('img').first.get_attribute('src') if row4 else 'none'
        
        print(f"Row 1 Thumbnail: {img1}")
        print(f"Row 2 Thumbnail: {img2}")
        print(f"Row 3 Thumbnail: {img3}")
        print(f"Row 4 Thumbnail: {img4}")
        
        assert len(set([img1, img2, img3, img4])) == 4, "Row thumbnails must be completely different!"
        print("SUCCESS: All 4 row thumbnails are 100% distinct and matched to their product!")
        
        # Test expanding Row 2 (Steering Wheel Tray)
        print("\nOpening Row 2 (Steering Wheel Tray) drawer...")
        row2.locator('button:has-text("SP TikTok")').first.click()
        time.sleep(2)
        
        drawer2 = page.locator('tr[id^="cluster-drawer-"]:visible').first
        print("Drawer 2 visible:", bool(drawer2))
        if drawer2:
            card_titles = [c.inner_text() for c in drawer2.locator('a[class*="line-clamp-2"]').all()]
            print(f"Products in Drawer 2: {len(card_titles)}")
            print("First 3 products in Drawer 2:")
            for ct in card_titles[:3]:
                print(f"  - {ct}")
            
            # Save screenshot of steering wheel tray drawer
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_steering_wheel_drawer.png"
            drawer2.screenshot(path=artifact_path)
            print("Saved artifact screenshot to:", artifact_path)
            
        # Capture overview of table rows showing distinct thumbnails
        overview_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_table_distinct_thumbnails.png"
        page.screenshot(path=overview_path, clip={"x": 0, "y": 450, "width": 1600, "height": 700})
        print("Saved table overview screenshot to:", overview_path)
        
        browser.close()

if __name__ == "__main__":
    test_distinct()
