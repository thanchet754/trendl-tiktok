"""
Background 6-Hour Auto-Scheduler
Periodically crawls Google Trends, TikTok 24h, Amazon, Etsy, and eBay every 6 hours.
"""

import threading
import time
import logging
from datetime import datetime, timedelta
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default interval: 6 hours (21600 seconds)
DEFAULT_INTERVAL_SECONDS = 6 * 60 * 60

class AutoScheduler:
    def __init__(self, interval_seconds: int = DEFAULT_INTERVAL_SECONDS):
        self.interval = interval_seconds
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self.next_run_time: Optional[datetime] = None
        self.last_run_time: Optional[datetime] = None

    def start(self, scan_func):
        if self.running:
            return
        self.running = True
        self.scan_func = scan_func
        self.next_run_time = datetime.now() + timedelta(seconds=self.interval)
        
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        self.thread.start()
        logger.info(f"AutoScheduler started. Next scan in 6 hours ({self.next_run_time.strftime('%H:%M:%S')}).")

    def _run_loop(self):
        while self.running:
            time.sleep(10) # check periodically
            if datetime.now() >= self.next_run_time:
                logger.info("AutoScheduler: 6-hour interval reached. Starting scheduled crawl...")
                try:
                    self.last_run_time = datetime.now()
                    self.scan_func()
                except Exception as e:
                    logger.error(f"Error in scheduled scan: {e}")
                finally:
                    self.next_run_time = datetime.now() + timedelta(seconds=self.interval)
                    logger.info(f"AutoScheduler: Next scan scheduled at {self.next_run_time.strftime('%H:%M:%S')}.")

    def get_status(self):
        now = datetime.now()
        seconds_remaining = 0
        if self.next_run_time and self.next_run_time > now:
            seconds_remaining = int((self.next_run_time - now).total_seconds())
            
        return {
            "is_active": self.running,
            "interval_hours": round(self.interval / 3600, 1),
            "next_run_time": self.next_run_time.strftime("%d/%m/%Y %H:%M:%S") if self.next_run_time else None,
            "last_run_time": self.last_run_time.strftime("%d/%m/%Y %H:%M:%S") if self.last_run_time else None,
            "seconds_remaining": seconds_remaining
        }

scheduler_instance = AutoScheduler()
