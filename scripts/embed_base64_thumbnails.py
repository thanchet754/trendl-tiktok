import os
import json
import base64

# 1. Read all 24 shirt thumbnails and convert to base64
b64_list = []
for i in range(1, 25):
    img_path = f"assets/clusters/family_shirt_{i}.jpg"
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
        b64_list.append(f"data:image/jpeg;base64,{encoded}")

print(f"Loaded {len(b64_list)} base64 images.")

# 2. Update data/latest_trends.json
with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Update target cluster (Rank #7)
target_cluster = data["all_ideas"][6]
if target_cluster.get("child_products"):
    for idx, prod in enumerate(target_cluster["child_products"]):
        prod["image"] = b64_list[idx % len(b64_list)]
    target_cluster["image"] = b64_list[0]

with open("data/latest_trends.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated data/latest_trends.json with base64 images!")

# 3. Update exporters/html_exporter.py to include the base64 array in JS
with open("exporters/html_exporter.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace image fallback in getClusterProducts
js_b64_array = json.dumps(b64_list)

old_resolver_img = """let imgSrc = (it.image && it.image.startsWith('assets/')) 
                    ? `assets/clusters/family_shirt_${(i % 24) + 1}.jpg`
                    : (it.image || `assets/clusters/family_shirt_${(i % 24) + 1}.jpg`);"""

new_resolver_code = f"""const B64_SHIRTS = {js_b64_array};
                let imgSrc = (it.child_products && it.child_products[i] && it.child_products[i].image)
                    ? it.child_products[i].image
                    : B64_SHIRTS[i % B64_SHIRTS.length];"""

if "const B64_SHIRTS = " not in code:
    code = code.replace(old_resolver_img, new_resolver_code)
    with open("exporters/html_exporter.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("Updated exporters/html_exporter.py with B64_SHIRTS!")
else:
    print("B64_SHIRTS already present in html_exporter.py")

# 4. Also create vercel.json
vercel_config = {
    "cleanUrls": True,
    "trailingSlash": False
}
with open("vercel.json", "w", encoding="utf-8") as f:
    json.dump(vercel_config, f, indent=2)
print("Created vercel.json")
