import urllib.request
import json
import time

time.sleep(20)

req_main = urllib.request.Request("https://api.github.com/repos/thanchet754/trendl-tiktok/commits/main", headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req_main) as resp:
    main_commit = json.loads(resp.read().decode())
    sha = main_commit["sha"]

url2 = f"https://api.github.com/repos/thanchet754/trendl-tiktok/commits/{sha}/status"
req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req2) as resp:
    data2 = json.loads(resp.read().decode())
    print("Combined state:", data2.get("state"))
    for st in data2.get("statuses", []):
        print(f"{st['context']}: {st['state']} - {st.get('target_url', '')}")
