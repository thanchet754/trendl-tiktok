import time
import os
from playwright.sync_api import sync_playwright

def test_full_view():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1200})
        
        cwd = os.getcwd()
        file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
        page.goto(file_url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2)
        
        # Scroll to rank 7 row
        row7 = page.locator('tr:has-text("Family Matching")').first
        if row7:
            row7.scroll_into_view_if_needed()
            time.sleep(1)
            
            # Click keyword or ASINs button
            btn = row7.locator('button').first
            btn.click()
            time.sleep(1.5)
            
            # Screenshot of the row header and drawer
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_full_cluster_and_row.png"
            page.screenshot(path=artifact_path)
            print("Saved full screenshot to:", artifact_path)
            
        browser.close()

if __name__ == "__main__":
    test_full_view()
