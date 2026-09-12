@echo off
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
title TikTok Shop US - Radar Trend 24h & Evergreen (Hen Gio 6h Tu Dong)
cls
echo ======================================================================
echo    TIKTOK SHOP US - RADAR XAC THUC TREND 24H VA EVERGREEN BEN VUNG
echo    Ket hop 5 san: Google Trends + TikTok 24h + Amazon + Etsy + eBay
echo    Che do: Nen Sang - Vuong Vuc 100%% - Hen gio tu dong 6 tieng/lan
echo ======================================================================
echo.
echo [1/2] Dang kiem tra thu vien...
python -m pip install -r requirements.txt --quiet --no-warn-script-location

echo.
echo [2/2] Dang chay quet du lieu va mo bang dieu khien tren trinh duyet...
echo.
python main.py

pause
