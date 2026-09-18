import asyncio
from playwright.async_api import async_playwright
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        file_url = "file:///" + os.path.abspath("dashboard.html").replace("\\", "/")
        print("Loading " + file_url)
        await page.goto(file_url, wait_until="load")
        await page.wait_for_timeout(2000)

        # Scroll to top influencers pagination
        await page.evaluate("""() => {
            const el = document.getElementById('top-influencers-pagination-btns');
            if (el) el.scrollIntoView({ block: 'center' });
        }""")
        await page.wait_for_timeout(500)

        page_info = page.locator("#top-influencers-page-info")
        print("Page Info Text:", await page_info.text_content())

        pag_btns = page.locator("#top-influencers-pagination-btns")
        print("Pagination HTML:", await pag_btns.inner_html())

        # Click next button
        next_btn = pag_btns.locator("button[title='Trang sau']")
        if await next_btn.count() > 0:
            await next_btn.click()
            await page.wait_for_timeout(500)
            print("After click Next -> Page Info:", await page_info.text_content())

        # Click last page button
        last_btn = pag_btns.locator("button[title='Trang cuối']")
        if await last_btn.count() > 0:
            await last_btn.click()
            await page.wait_for_timeout(500)
            print("After click Last -> Page Info:", await page_info.text_content())

        # Click first page button to return to page 1
        first_btn = pag_btns.locator("button[title='Trang đầu']")
        if await first_btn.count() > 0:
            await first_btn.click()
            await page.wait_for_timeout(500)
            print("After click First -> Page Info:", await page_info.text_content())

        artifact_path = "C:/Users/Ngoc/.gemini/antigravity/brain/55e08546-d9ad-4004-abaf-f3e850339471/verified_fixed_koc_pagination.png"
        await page.screenshot(path=artifact_path)
        print("Screenshot saved to " + artifact_path)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
