@echo off
title Trendl TikTok - 6-Hour Auto Crawler Daemon
color 0A
cd /d "%~dp0"
:start
echo ========================================================
echo   TRENDL TIKTOK - 24/7 AUTOMATIC 6-HOUR SCANNER
echo ========================================================
echo  [+] Current Directory: %CD%
echo  [+] Starting Python scheduler engine...
echo  [+] Logs will update continuously every 6 hours
echo ========================================================
python scheduler.py
if %ERRORLEVEL% NEQ 0 (
    echo [!] Python error or stopped. Restarting in 15 seconds...
    timeout /t 15
    goto :start
)
pause
