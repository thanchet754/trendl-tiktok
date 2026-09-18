import sys
import time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1200})
    print("Navigating to https://trendl-tiktok-eight.vercel.app ...")
    page.goto("https://trendl-tiktok-eight.vercel.app", wait_until="networkidle", timeout=60000)
    time.sleep(3)
    
    # Check if nav-btn-all is active or click it
    nav_all = page.locator("#nav-btn-all").first
    if nav_all.count() > 0:
        print("Clicking #nav-btn-all...")
        nav_all.click()
        time.sleep(2)
        
    # Check table rows
    rows = page.locator("#ideas-table-body tr").all()
    print(f"Total rows in #ideas-table-body: {len(rows)}")
    
    for i in range(min(5, len(rows))):
        r = rows[i]
        txt = r.inner_text().replace("\n", " ")[:60]
        imgs = [img.get_attribute("src") for img in r.locator("img").all()]
        print(f"Row {i+1}: {txt} -> Imgs: {imgs}")
        
    overview_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_table_distinct_thumbnails.png"
    page.screenshot(path=overview_path, clip={"x": 0, "y": 450, "width": 1600, "height": 700})
    print("Saved live overview screenshot to:", overview_path)
    
    # Click 2nd row SP TikTok button
    if len(rows) > 1:
        row2 = rows[1]
        btn = row2.locator("button:has-text('SP TikTok')").first
        if btn.count() > 0:
            print("Clicking SP TikTok button on Row 2...")
            btn.click()
            time.sleep(2)
            
            # Find open drawer
            drawer = page.locator("tr[id^='cluster-drawer-']:visible").first
            if drawer.count() > 0:
                print("Drawer visible!")
                cards = drawer.locator("a[class*='line-clamp-2']").all()
                print(f"Products in Drawer: {len(cards)}")
                for c in cards[:3]:
                    print("  -", c.inner_text())
                drawer_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_steering_wheel_drawer.png"
                drawer.screenshot(path=drawer_path)
                print("Saved live drawer screenshot to:", drawer_path)
    b.close()
