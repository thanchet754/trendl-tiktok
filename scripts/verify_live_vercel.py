import time
from playwright.sync_api import sync_playwright

def verify_live():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1200})
        
        url = "https://trendl-tiktok-eight.vercel.app"
        print("Visiting live Vercel URL:", url)
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(3)
        
        # Look for the cluster button for Rank 7
        row7 = page.locator('tr:has-text("Family Matching")').first
        print("Found Rank #7 row on live site:", bool(row7))
        
        if row7:
            row7.scroll_into_view_if_needed()
            time.sleep(1)
            
            # Click to toggle drawer
            btn = row7.locator('button').first
            btn.click()
            time.sleep(2)
            
            # Check drawer element
            drawer = page.query_selector('#cluster-drawer-cluster_family_matching_7')
            print("Live Drawer found:", bool(drawer))
            if drawer:
                is_hidden = "hidden" in (drawer.get_attribute("class") or "")
                print("Live Drawer is visible (not hidden):", not is_hidden)
                
                cards = drawer.query_selector_all('div[class*="group bg-white border"]')
                print(f"Products inside live drawer: {len(cards)}")
                
                first_link = drawer.query_selector('a[href*="amazon.com/dp/"]')
                if first_link:
                    href = first_link.get_attribute('href')
                    print(f"Verified Live Direct Product URL: {href}")
            
            # Scroll drawer into center view and take artifact screenshot
            artifact_path = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_live_vercel_cluster_drawer.png"
            page.screenshot(path=artifact_path)
            print("Saved live artifact screenshot to:", artifact_path)
            
        browser.close()

if __name__ == "__main__":
    verify_live()
