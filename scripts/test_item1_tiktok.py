import time
import os
from playwright.sync_api import sync_playwright

def test_item1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1200})
        
        cwd = os.getcwd()
        file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
        page.goto(file_url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2)
        
        # Look for the first row (Drop Stop)
        row1 = page.locator('tr:has-text("Drop Stop Multi-Pocket")').first
        print("Found Item #1 (Drop Stop) row:", bool(row1))
        
        if row1:
            row1.scroll_into_view_if_needed()
            time.sleep(1)
            
            # Click keyword or SP TikTok button
            btn = row1.locator('button').first
            btn.click()
            time.sleep(2)
            
            # Check drawer
            drawer = page.locator('tr[id^="cluster-drawer-"]:visible').first
            print("Visible Drawer found:", bool(drawer))
            
            # Verify images inside drawer
            imgs = drawer.locator('img').all()
            print(f"Images in drawer: {len(imgs)}")
            img_srcs = [img.get_attribute('src') for img in imgs]
            unique_imgs = set(img_srcs)
            print(f"Unique images count in 24 cards: {len(unique_imgs)} (Should be 24)")
            
            # Verify links inside drawer
            links = drawer.locator('a[href*="tiktok.com/view/product/"]').all()
            print(f"TikTok Shop direct links found in drawer: {len(links)}")
            if links:
                first_href = links[0].get_attribute('href')
                print(f"Verified First TikTok Shop URL: {first_href}")
            
            # Take screenshot of Item #1 expanded
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_item1_tiktok_drawer.png"
            try:
                drawer.screenshot(path=artifact_path, timeout=5000)
                print("Saved artifact drawer screenshot to:", artifact_path)
            except Exception as e:
                print("Drawer screenshot error:", e)
                try:
                    page.screenshot(path=artifact_path, timeout=5000, animations="disabled")
                    print("Saved page screenshot to:", artifact_path)
                except Exception as e2:
                    print("Page screenshot error:", e2)
            
        browser.close()

if __name__ == "__main__":
    test_item1()
