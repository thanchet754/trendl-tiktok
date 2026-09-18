import sys
import time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1300})
    file_url = "file:///" + __file__.replace("\\", "/").replace("scripts/test_drawer_dual.py", "dashboard.html")
    print(f"Loading {file_url} ...")
    page.goto(file_url, wait_until="domcontentloaded", timeout=30000)
    time.sleep(2)
    
    # Scroll to table
    page.evaluate("window.scrollTo(0, 950)")
    time.sleep(1)
    
    # Click 2nd row (Steering Wheel Desk Tray)
    row2 = page.locator('tr:has-text("Steering Wheel Desk Tray")').first
    btn = row2.locator("button:has-text('SP TikTok')").first
    print("Clicking SP TikTok button on Row 2...")
    btn.click()
    time.sleep(2)
    
    drawer = page.locator('tr[id^="cluster-drawer-"]:visible').first
    if drawer.count() > 0:
        drawer.scroll_into_view_if_needed()
        time.sleep(1)
        artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_drawer_dual_us_amazon_solution.png"
        drawer.screenshot(path=artifact_path)
        print("Saved dual solution drawer screenshot to:", artifact_path)
        
    b.close()
