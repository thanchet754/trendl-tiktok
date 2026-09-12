"""
TikTok Shop US - Trend & Evergreen Intelligence
Direct Browser & 6-Hour Auto-Scheduler.
"""

import sys
import os

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

import time
import argparse
import webbrowser
from web.app import app, perform_full_scan
from scheduler import scheduler_instance

def run_main(open_browser: bool = True, daemon_scheduler: bool = True):
    print("=" * 75)
    print("🚀 BẮT ĐẦU CÀO DỮ LIỆU TIKTOK SHOP US TỪ 5 SÀN (PHIÊN BẢN NỀN SÁNG VUÔNG VỨC)")
    print("   Google Trends | TikTok Viral 24h | Amazon Movers | Etsy POD | eBay Deals")
    print("=" * 75)

    # 1. Start 6-Hour Auto-Scheduler
    if daemon_scheduler:
        scheduler_instance.start(perform_full_scan)
        sched_status = scheduler_instance.get_status()
        print(f"⏰ ĐÃ KÍCH HOẠT HẸN GIỜ TỰ ĐỘNG: Cứ 6 tiếng sẽ quét mới một lần.")
        print(f"   Lần quét kế tiếp dự kiến lúc: {sched_status.get('next_run_time', 'N/A')}")
        print("=" * 75)

    # 2. Perform initial scan
    data = perform_full_scan()
    stats = data["stats"]

    print("\n" + "=" * 75)
    print(f"📊 KẾT QUẢ THU THẬP & PHÂN TÍCH ({data['updated_at']})")
    print(f"- Tổng ý tưởng sản phẩm phân tích: {stats['total_analyzed']}")
    print(f"- 🔥 Top Bùng Nổ 24h (Viral Spikes): {stats['total_viral_24h']} (Kèm minh chứng 24h)")
    print(f"- 🌲 Top Bền Vững Quanh Năm (Evergreen): {stats['total_evergreen']}")
    print("=" * 75)

    html_file = os.path.abspath("dashboard.html")
    excel_file = os.path.abspath(data.get('latest_excel', 'exports/TikTok_Shop_US_Latest_Trends.xlsx'))

    print("=" * 75)
    print(f"✅ BẢNG ĐIỀU KHIỂN NỀN SÁNG VUÔNG VỨC: file:///{html_file.replace(os.sep, '/')}")
    print(f"✅ BÁO CÁO EXCEL ĐÃ XUẤT: {excel_file}")
    print("=" * 75)

    if open_browser and os.path.exists(html_file):
        print("\n🌐 Đang tự động mở bảng điều khiển trên trình duyệt web của bạn...")
        webbrowser.open(f"file:///{html_file.replace(os.sep, '/')}")

    # Keep alive if running with scheduler in foreground terminal
    if daemon_scheduler:
        print("\n💡 Hệ thống đang duy trì hẹn giờ tự động mỗi 6 tiếng một lần.")
        print("   Nhấn Ctrl + C để dừng hoặc cứ để cửa sổ chạy thu nhỏ.")
        try:
            while True:
                time.sleep(30)
        except KeyboardInterrupt:
            print("\nĐã dừng bộ hẹn giờ tự động.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TikTok Shop US Trends Scraper")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically open browser")
    parser.add_argument("--once", action="store_true", help="Run once without keeping 6-hour scheduler alive in console")
    args = parser.parse_args()

    run_main(open_browser=not args.no_browser, daemon_scheduler=not args.once)
