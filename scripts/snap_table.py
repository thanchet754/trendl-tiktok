import os
import time
import sys
from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1200})
    cwd = os.getcwd()
    file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
    page.goto(file_url, wait_until="domcontentloaded", timeout=25000)
    time.sleep(3)
    
    # Scroll to table
    page.evaluate("window.scrollTo(0, 950)")
    time.sleep(2)
    
    # Open drawer on row 1
    row1 = page.locator('#table-body tr').first
    if row1.count() > 0:
        btn = row1.locator('button:has-text("SP TikTok")').first
        if btn.count() > 0:
            btn.click()
            time.sleep(1)
            print("Opened drawer on Row 1 successfully.")
            
    artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_diverse_catalog_table.png"
    page.screenshot(path=artifact_path)
    print("Saved table screenshot to:", artifact_path)
    b.close()
