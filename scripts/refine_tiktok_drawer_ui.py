with open('exporters/html_exporter.py', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Change button text from ASINs to SP TikTok
code = code.replace('${{asinCount}} ASINs', '${{asinCount}} SP TikTok')
code = code.replace('${asinCount} ASINs', '${asinCount} SP TikTok')
code = code.replace('(Direct ASINs)', '(TikTok Shop Products)')

# 2. Fix card badge from undefined (${p.asin}) to 'TikTok Shop'
old_badge = """<span class="absolute top-1 right-1 bg-slate-900/85 text-white font-mono text-[8.5px] px-1 py-0.2 font-bold shadow-xs">
                                                    ${{p.asin}}
                                                </span>"""

new_badge = """<span class="absolute top-1 right-1 bg-black/85 text-white font-mono text-[8.5px] px-1.5 py-0.5 font-bold shadow-xs">
                                                    TikTok Shop
                                                </span>"""

code = code.replace(old_badge, new_badge)

# Also replace in case of single brace
code = code.replace("${{p.asin}}", "TikTok Shop")
code = code.replace("${p.asin}", "TikTok Shop")

# 3. Make TikTok Shop buttons stylish red/rose
old_btn = 'bg-blue-50 hover:bg-blue-600 text-blue-700 hover:text-white border border-blue-200 hover:border-blue-600 transition shadow-2xs'
new_btn = 'bg-rose-600 hover:bg-rose-700 text-white border border-rose-700 transition shadow-xs'
code = code.replace(old_btn, new_btn)

# 4. Footer link text
code = code.replace('View all ${{asinCount}} products', 'Xem toàn bộ ${{asinCount}} sản phẩm trên TikTok Shop US')
code = code.replace('View all ${asinCount} products', 'Xem toàn bộ ${asinCount} sản phẩm trên TikTok Shop US')

with open('exporters/html_exporter.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Successfully refined TikTok Shop drawer UI!")
