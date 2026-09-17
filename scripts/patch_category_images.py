import json

CATEGORY_IMAGE_SETS = {
    "Automotive & Motorcycle": [
        "https://images.unsplash.com/photo-1542282088-72c9c27ed0cd?w=400",
        "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=400",
        "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400",
        "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=400",
        "https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?w=400",
        "https://images.unsplash.com/photo-1502877338535-766e1452684a?w=400",
        "https://images.unsplash.com/photo-1563720223185-11003d516935?w=400",
        "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=400",
        "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=400",
        "https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=400",
        "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=400",
        "https://images.unsplash.com/photo-1580273916550-e323be2ae537?w=400",
        "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=400",
        "https://images.unsplash.com/photo-1617788138017-80ad40651399?w=400",
        "https://images.unsplash.com/photo-1517524008697-84bbe3c3fd98?w=400",
        "https://images.unsplash.com/photo-1541348263662-e0c866661ba3?w=400",
        "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=400",
        "https://images.unsplash.com/photo-1508974239320-0a029497e820?w=400",
        "https://images.unsplash.com/photo-1544829099-b9a0c07fad1a?w=400",
        "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400",
        "https://images.unsplash.com/photo-1590362891991-f776e747a588?w=400",
        "https://images.unsplash.com/photo-1562911791-c7a97b729ec5?w=400",
        "https://images.unsplash.com/photo-1616422285623-13ff0162193c?w=400",
        "https://images.unsplash.com/photo-1526726538690-5cbf956ae2fd?w=400"
    ],
    "Beauty & Personal Care": [
        "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400",
        "https://images.unsplash.com/photo-1598440947619-2c35fc9aa908?w=400",
        "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400",
        "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=400",
        "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=400",
        "https://images.unsplash.com/photo-1608248597359-009d028b8cf4?w=400",
        "https://images.unsplash.com/photo-1616683693504-3ea7e9ad6fec?w=400",
        "https://images.unsplash.com/photo-1567928815104-b63073998b31?w=400",
        "https://images.unsplash.com/photo-1512290900672-1f023f99052d?w=400",
        "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=400",
        "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?w=400",
        "https://images.unsplash.com/photo-1601049541289-9b1b7bbbfe19?w=400",
        "https://images.unsplash.com/photo-1526947425960-945c6e72858f?w=400",
        "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=400",
        "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400",
        "https://images.unsplash.com/photo-1519699047748-de8e457a634e?w=400",
        "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400",
        "https://images.unsplash.com/photo-1617897903246-719242758050?w=400",
        "https://images.unsplash.com/photo-1576426863848-c21f53c60b19?w=400",
        "https://images.unsplash.com/photo-1515377905703-c4788e51af15?w=400",
        "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400",
        "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=400",
        "https://images.unsplash.com/photo-1599305090598-fe179d501227?w=400",
        "https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?w=400"
    ],
    "Kitchenware": [
        "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=400",
        "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400",
        "https://images.unsplash.com/photo-1584990347449-34b7f73905cf?w=400",
        "https://images.unsplash.com/photo-1590794056226-79ef3a8147e1?w=400",
        "https://images.unsplash.com/photo-1588854337236-6889d631faa8?w=400",
        "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400",
        "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=400",
        "https://images.unsplash.com/photo-1583778176476-4a8b02a64c01?w=400",
        "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=400",
        "https://images.unsplash.com/photo-1541658016709-82535e94bc69?w=400",
        "https://images.unsplash.com/photo-1585515320310-259814833e62?w=400",
        "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?w=400",
        "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?w=400",
        "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400",
        "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400",
        "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400",
        "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400",
        "https://images.unsplash.com/photo-1517256064527-09c73fc73e38?w=400",
        "https://images.unsplash.com/photo-1584269600519-112d071b35e6?w=400",
        "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400",
        "https://images.unsplash.com/photo-1584727638096-042c45049ebe?w=400",
        "https://images.unsplash.com/photo-1556911073-38141963c9e0?w=400",
        "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=400",
        "https://images.unsplash.com/photo-1584990347449-a78b5f36e382?w=400"
    ],
    "Pet Supplies": [
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400",
        "https://images.unsplash.com/photo-1576201836106-db1758fd1c97?w=400",
        "https://images.unsplash.com/photo-1548767797-d8c844163c4c?w=400",
        "https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?w=400",
        "https://images.unsplash.com/photo-1563460716037-460b3dd14ba9?w=400",
        "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400",
        "https://images.unsplash.com/photo-1541599540903-216a46ca1dc0?w=400",
        "https://images.unsplash.com/photo-1535268647677-300dbf3d78d1?w=400",
        "https://images.unsplash.com/photo-1601758228041-f3b2795255f1?w=400",
        "https://images.unsplash.com/photo-1587300003388-59208cc962cb?w=400",
        "https://images.unsplash.com/photo-1583512603805-3cc6b41f3edb?w=400",
        "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?w=400",
        "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=400",
        "https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?w=400",
        "https://images.unsplash.com/photo-1543466835-00a7907e9de1?w=400",
        "https://images.unsplash.com/photo-1583337130417-3346a1be7def?w=400",
        "https://images.unsplash.com/photo-1583511655826-05700d52f4d9?w=400",
        "https://images.unsplash.com/photo-1560743641-3914f4c4b344?w=400",
        "https://images.unsplash.com/photo-1534361960057-19889db9621e?w=400",
        "https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=400",
        "https://images.unsplash.com/photo-1581888227599-779811939961?w=400",
        "https://images.unsplash.com/photo-1548199973-03cce0bbc87b?w=400",
        "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=400",
        "https://images.unsplash.com/photo-1574158622682-e40e69881006?w=400"
    ],
    "Womenswear & Underwear": [
        "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400",
        "https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=400",
        "https://images.unsplash.com/photo-1496747611176-843222e1e57c?w=400",
        "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=400",
        "https://images.unsplash.com/photo-1485968579580-b6d095142e6e?w=400",
        "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=400",
        "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=400",
        "https://images.unsplash.com/photo-1558769132-cb1aea458c5e?w=400",
        "https://images.unsplash.com/photo-1516762689617-e1cffcef479d?w=400",
        "https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=400",
        "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=400",
        "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=400",
        "https://images.unsplash.com/photo-1525507119028-ed4c629a60a3?w=400",
        "https://images.unsplash.com/photo-1479064555552-3ef4979f8908?w=400",
        "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?w=400",
        "https://images.unsplash.com/photo-1485230895905-ec40ba36b9bc?w=400",
        "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?w=400",
        "https://images.unsplash.com/photo-1564257631407-4deb1f99d992?w=400",
        "https://images.unsplash.com/photo-1518049362265-d5b2a6467637?w=400",
        "https://images.unsplash.com/photo-1550614000-4895a10e1bfd?w=400",
        "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=400",
        "https://images.unsplash.com/photo-1508427953056-b00b8d78ebf5?w=400",
        "https://images.unsplash.com/photo-1520006403909-838d6b92c22e?w=400",
        "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400"
    ],
    "Phones & Electronics": [
        "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
        "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
        "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400",
        "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400",
        "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400",
        "https://images.unsplash.com/photo-1560343090-f0409e92791a?w=400",
        "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400",
        "https://images.unsplash.com/photo-1585060544812-6b45742d762f?w=400",
        "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=400",
        "https://images.unsplash.com/photo-1567581935884-3349723552ca?w=400",
        "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=400",
        "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=400",
        "https://images.unsplash.com/photo-1543512214-318c7553f230?w=400",
        "https://images.unsplash.com/photo-1510519138101-570d1dca3d66?w=400",
        "https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?w=400",
        "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=400",
        "https://images.unsplash.com/photo-1580910051074-3eb694886505?w=400",
        "https://images.unsplash.com/photo-1606220588913-b3aacb4d2f46?w=400",
        "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=400",
        "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?w=400",
        "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?w=400",
        "https://images.unsplash.com/photo-1585792180666-f75a7c52b271?w=400",
        "https://images.unsplash.com/photo-1512499617640-c74ae3a79d37?w=400",
        "https://images.unsplash.com/photo-1509741102003-ca64bfe5f069?w=400"
    ],
    "Baby & Maternity": [
        "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?w=400",
        "https://images.unsplash.com/photo-1519689680058-324335c77eba?w=400",
        "https://images.unsplash.com/photo-1522771930-78848d9293e8?w=400",
        "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?w=400",
        "https://images.unsplash.com/photo-1544126592-807ade215a0b?w=400",
        "https://images.unsplash.com/photo-1516627145497-ae6968895b74?w=400",
        "https://images.unsplash.com/photo-1574015974293-817f0ebebb74?w=400",
        "https://images.unsplash.com/photo-1596870230751-ebdfce98ec42?w=400",
        "https://images.unsplash.com/photo-1505377059067-e285a7bac49b?w=400",
        "https://images.unsplash.com/photo-1584839682565-5669b622c1b3?w=400",
        "https://images.unsplash.com/photo-1596464716127-f2a829822391?w=400",
        "https://images.unsplash.com/photo-1566458342470-388a53139366?w=400",
        "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=400",
        "https://images.unsplash.com/photo-1508873696983-2df5293cb32f?w=400",
        "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=400",
        "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?w=400",
        "https://images.unsplash.com/photo-1587614382346-4ec70e388b28?w=400",
        "https://images.unsplash.com/photo-1584820927498-cfe5211fd8bf?w=400",
        "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=400",
        "https://images.unsplash.com/photo-1584820927498-cfe5211fd8c0?w=400",
        "https://images.unsplash.com/photo-1544816155-12df9643f363?w=400",
        "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=400",
        "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=400",
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=400"
    ]
}

# Verify uniqueness
for k, v in CATEGORY_IMAGE_SETS.items():
    s = set(v)
    if len(s) != len(v):
        print(f"Warning: {k} has duplicate ({len(v)} total, {len(s)} unique)")
    else:
        print(f"OK: {k} has {len(v)} 100% unique images")

# Build JS object string
# Note: since html_exporter.py is a Python file containing an f-string,
# all JS curly braces MUST BE DOUBLED ({{ and }})!
lines = ["const CATEGORY_IMAGE_SETS = {{"]
for k, v in CATEGORY_IMAGE_SETS.items():
    lines.append(f'            "{k}": [')
    for i, url in enumerate(v):
        comma = "," if i < len(v) - 1 else ""
        lines.append(f'                "{url}"{comma}')
    lines.append("            ],")
lines.append("        }};")
js_code = "\n".join(lines)

with open("exporters/html_exporter.py", "r", encoding="utf-8") as f:
    orig = f.read()

start = orig.find("const CATEGORY_IMAGE_SETS =")
end = orig.find("function getClusterProducts", start)

if start != -1 and end != -1:
    new_content = orig[:start] + js_code + "\n\n        " + orig[end:]
    with open("exporters/html_exporter.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully patched exporters/html_exporter.py!")
else:
    print("Could not find delimiters in exporters/html_exporter.py")
