"""
FastAPI Application for TikTok Shop US Trend Radar
Serves Web Dashboard, triggers collectors, and handles Excel exports.
"""

import os
import json
import logging
from datetime import datetime, timedelta
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from collectors.google_trends import fetch_google_trends_us
from collectors.tiktok_viral import fetch_tiktok_viral_24h
from collectors.amazon_movers import scrape_amazon_bestsellers
from collectors.etsy_trending import fetch_etsy_trending
from collectors.ebay_deals import fetch_ebay_deals
from collectors.tiktok_shop_leaders import fetch_tiktok_shop_leaders

from analyzer.category_taxonomy import get_all_categories
from analyzer.entity_matcher import synthesize_and_rank_ideas
from exporters.excel_exporter import export_to_excel
from exporters.html_exporter import export_to_standalone_html
from scheduler import scheduler_instance

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="TikTok Shop US Trend Radar Pro")

# Cho phép gọi API từ file:// hoặc bất kỳ trình duyệt local nào
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = os.path.join("data", "latest_trends.json")
os.makedirs("data", exist_ok=True)
os.makedirs("exports", exist_ok=True)

latest_cache = None

def perform_full_scan():
    global latest_cache
    logger.info("Starting Full 5-Platform Scan...")
    
    # 1. Google Trends
    try:
        g_trends = fetch_google_trends_us()
    except Exception as e:
        logger.error(f"Google trends scan error: {e}")
        g_trends = []

    # 2. TikTok Viral 24h
    try:
        tt_items = fetch_tiktok_viral_24h()
    except Exception as e:
        logger.error(f"TikTok scan error: {e}")
        tt_items = []

    # 3. Amazon Movers & Best Sellers
    try:
        amz_items = scrape_amazon_bestsellers(limit_per_category=6)
    except Exception as e:
        logger.error(f"Amazon scan error: {e}")
        amz_items = []

    # 4. Etsy Evergreen
    try:
        etsy_items = fetch_etsy_trending()
    except Exception as e:
        logger.error(f"Etsy scan error: {e}")
        etsy_items = []

    # 5. eBay Deals
    try:
        ebay_items = fetch_ebay_deals()
    except Exception as e:
        logger.error(f"eBay scan error: {e}")
        ebay_items = []

    # Synthesize
    analyzed = synthesize_and_rank_ideas(
        google_trends=g_trends,
        tiktok_items=tt_items,
        amazon_items=amz_items,
        etsy_items=etsy_items,
        ebay_items=ebay_items
    )
    # 6. TikTok Shop US Leaders (Top Videos 24h GMV & Top Influencers)
    try:
        leaders_data = fetch_tiktok_shop_leaders()
        analyzed["top_videos"] = leaders_data.get("top_videos", [])
        analyzed["top_influencers"] = leaders_data.get("top_influencers", [])
    except Exception as e:
        logger.error(f"TikTok Shop leaders scan error: {e}")
        analyzed["top_videos"] = []
        analyzed["top_influencers"] = []

    try:
        analyzed["categories_taxonomy"] = get_all_categories()
    except Exception as e:
        logger.error(f"Category taxonomy error: {e}")
        analyzed["categories_taxonomy"] = []

    now_dt = datetime.now()
    analyzed["updated_at"] = now_dt.strftime("%d/%m/%Y %H:%M:%S")
    analyzed["last_scan_timestamp"] = int(now_dt.timestamp())
    analyzed["next_scan_timestamp"] = int((now_dt + timedelta(hours=6)).timestamp())
    analyzed["next_scan_time"] = (now_dt + timedelta(hours=6)).strftime("%H:%M:%S (%d/%m)")

    # Generate Excel
    latest_excel_path = os.path.join("exports", "TikTok_Shop_US_Latest_Trends.xlsx")
    export_to_excel(analyzed, latest_excel_path)
    analyzed["latest_excel"] = latest_excel_path

    # Generate Standalone HTML
    export_to_standalone_html(analyzed, "dashboard.html")
    export_to_standalone_html(analyzed, "index.html")

    # Sync to Supabase Cloud Database
    try:
        from database.supabase_client import sync_trends_to_supabase
        sync_trends_to_supabase(analyzed)
    except Exception as e:
        logger.error(f"Lỗi đồng bộ Supabase: {e}")

    # Save to disk
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(analyzed, f, ensure_ascii=False, indent=2)

    latest_cache = analyzed
    logger.info("Scan completed, Excel and standalone HTML updated successfully.")
    return analyzed

@app.on_event("startup")
def on_startup():
    if not os.environ.get("VERCEL"):
        scheduler_instance.start(perform_full_scan)
        logger.info("AutoScheduler initialized on local app startup.")
    else:
        logger.info("Running on Vercel Serverless. AutoScheduler deactivated for serverless worker.")

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    for fpath in ["index.html", "dashboard.html"]:
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                return f.read()
    template_path = os.path.join("web", "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse("<h1>TikTok Shop US Trend Radar Pro</h1>")

@app.get("/dashboard", response_class=HTMLResponse)
async def serve_dashboard_page():
    return await serve_dashboard()

@app.get("/api/data")
async def get_data():
    global latest_cache
    if latest_cache is not None:
        return latest_cache
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                latest_cache = json.load(f)
                return latest_cache
        except Exception:
            pass

    # Initial fast scan if empty
    return perform_full_scan()

@app.get("/api/supabase-trends")
async def get_supabase_trends(limit: int = 100):
    try:
        from database.supabase_client import fetch_trends_from_supabase
        return fetch_trends_from_supabase(limit=limit)
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/scan")
async def scan_trends():
    data = perform_full_scan()
    return data

@app.get("/api/export-excel")
async def download_excel():
    excel_path = os.path.join("exports", "TikTok_Shop_US_Latest_Trends.xlsx")
    if not os.path.exists(excel_path):
        perform_full_scan()
    return FileResponse(
        excel_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=f"TikTok_Shop_US_Trends_{datetime.now().strftime('%Y%m%d')}.xlsx"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web.app:app", host="127.0.0.1", port=8000, reload=False)
