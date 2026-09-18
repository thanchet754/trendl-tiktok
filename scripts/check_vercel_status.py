import urllib.request
import json

url = "https://api.github.com/repos/thanchet754/trendl-tiktok/commits/43a97ce60e80d2cc5ba1faeb4f112eb7616ada7a/check-runs"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
        print("Total check runs:", data.get("total_count", 0))
        for cr in data.get("check_runs", []):
            print(f"{cr['name']}: {cr['status']} - {cr['conclusion']}")
except Exception as e:
    print("Error check-runs:", e)

# Also check statuses
url2 = "https://api.github.com/repos/thanchet754/trendl-tiktok/commits/43a97ce60e80d2cc5ba1faeb4f112eb7616ada7a/status"
req2 = urllib.request.Request(url2, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req2) as resp:
        data2 = json.loads(resp.read().decode())
        print("Combined state:", data2.get("state"))
        for st in data2.get("statuses", []):
            print(f"{st['context']}: {st['state']} - {st['target_url']}")
except Exception as e:
    print("Error status:", e)
