@echo off
chcp 65001 >nul
title TikTok Shop US - Trend Radar Pro
echo =======================================================================
echo   🚀 TIKTOK SHOP US TREND RADAR PRO - SERVER NỀN & BỘ CÀO DỮ LIỆU
echo =======================================================================
echo   - Khởi động backend API tại: http://127.0.0.1:8000
echo   - Tự động duy trì quét dữ liệu 6 tiếng/lần
echo   - Hỗ trợ bấm nút "QUÉT MỚI NGAY" trực tiếp trên trình duyệt
echo =======================================================================
echo.
start "" "http://127.0.0.1:8000"
python -m uvicorn web.app:app --host 127.0.0.1 --port 8000
pause
