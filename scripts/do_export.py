import json
import shutil
import os
from exporters.html_exporter import export_to_standalone_html

print("Loading data/latest_trends.json...")
with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Exporting {len(data.get('all_ideas', []))} ideas to dashboard.html...")
out = export_to_standalone_html(data, "dashboard.html")
print(f"Exported to dashboard.html, size: {os.path.getsize('dashboard.html') / (1024*1024):.2f} MB")

shutil.copyfile("dashboard.html", "index.html")
print(f"Copied to index.html, size: {os.path.getsize('index.html') / (1024*1024):.2f} MB")
