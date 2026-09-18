import sys, os, time
sys.stdout.reconfigure(encoding='utf-8')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1600, "height": 1300})
    file_url = "file:///" + os.path.abspath("dashboard.html").replace("\\", "/")
    print(f"Loading {file_url} ...")
    page.goto(file_url, wait_until="domcontentloaded", timeout=40000)
    time.sleep(3)
    
    # Check Ideas count badge
    badge = page.locator("#ideas-count-badge").inner_text()
    print(f"Ideas Count Badge: '{badge}'")
    assert "5.000" in badge or "5,000" in badge, f"Expected 5,000 in badge, got '{badge}'"
    
    # Check pagination info
    page_info = page.locator("#ideas-table-page-info").inner_text()
    print(f"Ideas Table Page Info: '{page_info}'")
    assert "5.000" in page_info or "5,000" in page_info, f"Expected 5,000 in page_info, got '{page_info}'"
    
    # Scroll to table and take screenshot
    page.evaluate("window.scrollTo(0, 950)")
    time.sleep(1)
    artifact_table = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_5000_ideas_table.png"
    page.screenshot(path=artifact_table)
    print("Saved 5,000 ideas table screenshot to:", artifact_table)
    
    # Scroll back up to Top Leaders section
    page.evaluate("window.scrollTo(0, 300)")
    time.sleep(1)
    
    # Check Top Videos count
    vid_info = page.locator("#top-videos-page-info").inner_text()
    print(f"Top Videos Page Info: '{vid_info}'")
    assert "2000" in vid_info or "2.000" in vid_info, f"Expected 2,000 in vid_info, got '{vid_info}'"
    
    # Check Top Influencers count
    creator_info = page.locator("#top-influencers-page-info").inner_text()
    print(f"Top Influencers Page Info: '{creator_info}'")
    assert "2000" in creator_info or "2.000" in creator_info, f"Expected 2,000 in creator_info, got '{creator_info}'"
    
    artifact_leaders = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_2000_leaders.png"
    page.screenshot(path=artifact_leaders)
    print("Saved 2,000 leaders screenshot to:", artifact_leaders)
    
    # Test jumping to page 50 of ideas table
    print("Jumping to page 50 of ideas table...")
    page.evaluate("changeMainIdeasPage(50)")
    time.sleep(1)
    page_info_50 = page.locator("#ideas-table-page-info").inner_text()
    print(f"Page 50 Info: '{page_info_50}'")
    assert "Trang 50/50" in page_info_50 or "Page 50/50" in page_info_50, f"Expected Page 50/50, got '{page_info_50}'"
    
    page.evaluate("window.scrollTo(0, 950)")
    time.sleep(1)
    artifact_page50 = r"C:\Users\Ngoc\.gemini\antigravity\brain\55e08546-d9ad-4004-abaf-f3e850339471\verified_page_50_ideas.png"
    page.screenshot(path=artifact_page50)
    print("Saved page 50 ideas screenshot to:", artifact_page50)
    
    # Test jumping to page 20 of top videos
    print("Jumping to page 20 of top videos...")
    page.evaluate("changeTopVideosPage(20)")
    time.sleep(1)
    vid_info_20 = page.locator("#top-videos-page-info").inner_text()
    print(f"Top Videos Page 20 Info: '{vid_info_20}'")
    assert "Trang 20/20" in vid_info_20 or "Page 20/20" in vid_info_20, f"Expected Page 20/20, got '{vid_info_20}'"
    
    b.close()
    print("\nALL VERIFICATIONS PASSED SUCCESSFULLY!")
