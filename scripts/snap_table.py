import os
import time
import sys
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1200})
    cwd = os.getcwd()
    file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
    page.goto(file_url, wait_until="domcontentloaded", timeout=20000)
    time.sleep(2)
    
    # Scroll to table
    table = page.locator('#ideas-table').first
    table.scroll_into_view_if_needed()
    time.sleep(1)
    
    artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_table_rows_with_real_images.png"
    table.screenshot(path=artifact_path)
    print("Saved table screenshot to:", artifact_path)
    b.close()
