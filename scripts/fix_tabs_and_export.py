import os
import json
from datetime import datetime

EXPORTER_PATH = "exporters/html_exporter.py"

with open(EXPORTER_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Set currentTab = 'all' by default
code = code.replace("let currentTab = 'viral';", "let currentTab = 'all';")

# 2. Fix active styles for nav-btn-all vs nav-btn-viral in HTML
old_nav_all = 'id="nav-btn-all" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent"'
new_nav_all = 'id="nav-btn-all" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-rose-600 text-white border-l-4 border-rose-900"'

old_nav_viral = 'id="nav-btn-viral" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-rose-600 text-white border-l-4 border-rose-900"'
new_nav_viral = 'id="nav-btn-viral" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent"'

code = code.replace(old_nav_all, new_nav_all)
code = code.replace(old_nav_viral, new_nav_viral)

# 3. Ensure viral_24h and evergreen are populated in export_to_standalone_html
export_prep = """def export_to_standalone_html(analyzed_data: Dict[str, Any], output_path: str = "dashboard.html") -> str:
    # Ensure viral_24h and evergreen are populated
    if "viral_24h" not in analyzed_data or not analyzed_data["viral_24h"]:
        analyzed_data["viral_24h"] = [x for x in analyzed_data.get("all_ideas", []) if x.get("classification") == "VIRAL_SPIKE_24H" or x.get("surge_type") == "BREAKOUT_V3"]
    if "evergreen" not in analyzed_data or not analyzed_data["evergreen"]:
        analyzed_data["evergreen"] = [x for x in analyzed_data.get("all_ideas", []) if x.get("classification") != "VIRAL_SPIKE_24H"]
"""

code = code.replace('def export_to_standalone_html(analyzed_data: Dict[str, Any], output_path: str = "dashboard.html") -> str:', export_prep)

with open(EXPORTER_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("Updated exporters/html_exporter.py with default 'all' tab!")
