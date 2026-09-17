import time
import os
from playwright.sync_api import sync_playwright

def test_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1100})
        
        cwd = os.getcwd()
        file_url = f"file:///{cwd}/dashboard.html".replace('\\', '/')
        print("Navigating to:", file_url)
        page.goto(file_url, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2)
        
        # Look for the cluster button
        rank7_btn = page.query_selector('button[onclick*="cluster_family_matching_7"]')
        print("Found Rank #7 button:", bool(rank7_btn))
        
        if rank7_btn:
            rank7_btn.scroll_into_view_if_needed()
            time.sleep(1)
            
            # Click to toggle drawer
            print("Clicking to expand cluster drawer...")
            rank7_btn.click()
            time.sleep(1.5)
            
            # Check drawer element
            drawer = page.query_selector('#cluster-drawer-cluster_family_matching_7')
            print("Drawer element found:", bool(drawer))
            if drawer:
                is_hidden = "hidden" in (drawer.get_attribute("class") or "")
                print("Drawer hidden class present:", is_hidden)
                
                cards = drawer.query_selector_all('div[class*="group bg-white border"]')
                print(f"Products inside drawer: {len(cards)}")
                
                first_link = drawer.query_selector('a[href*="amazon.com/dp/"]')
                if first_link:
                    href = first_link.get_attribute('href')
                    print(f"Verified Direct Product URL: {href}")
            
            # Scroll drawer into center view
            drawer.scroll_into_view_if_needed()
            time.sleep(1)
            
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_cluster_drawer.png"
            page.screenshot(path=artifact_path)
            print("Saved artifact screenshot to:", artifact_path)
            
        browser.close()

if __name__ == "__main__":
    test_ui()
