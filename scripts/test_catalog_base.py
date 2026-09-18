import sys, os, json, random, re
sys.path.insert(0, os.path.abspath("."))

from analyzer.category_taxonomy import TIKTOK_SHOP_28_CATEGORIES

# 1. Load existing ideas
with open("data/latest_trends.json", "r", encoding="utf-8") as f:
    trends_data = json.load(f)

with open("data/core_real_pools.json", "r", encoding="utf-8") as f:
    core_pools = json.load(f)

ideas = trends_data.get("all_ideas", [])
existing_titles = set(it["title"].lower().strip() for it in ideas)
print(f"Loaded {len(ideas)} existing ideas (unique: {len(existing_titles)})")

# Matcher rule for pool_id
def match_pool_for_item(title, sub_niche, category):
    t = title.lower()
    sn = (sub_niche or "").lower()
    cat = (category or "").lower()
    
    if "family matching" in t or "birthday family" in t:
        return "family_matching"
    if "steering wheel" in t or "desk tray" in t:
        return "steering_wheel_desk"
    if "led" in t or "ambient" in t or "strip" in t or "light" in t and ("car" in t or "interior" in t):
        return "led_ambient_strip"
    if "floor mat" in t or "rubber" in t or "weather" in t and "mat" in t:
        return "rubber_floor_mats"
    if "dash cam" in t or "camera" in t and "car" in t:
        return "dash_cam_4k"
    if "phone mount" in t or "magsafe" in t or "holder" in t and "car" in t:
        return "car_phone_mount"
    if "carplay" in t or "android auto" in t or "wireless adapter" in t:
        return "carplay_adapter"
    if "vacuum" in t or "cordless" in t and ("cleaner" in t or "car" in t):
        return "car_vacuum"
    if "inflator" in t or "tire" in t or "air compressor" in t:
        return "tire_inflator"
    if "foam cannon" in t or "pressure washer" in t:
        return "foam_cannon"
    if "obd2" in t or "scanner" in t or "code reader" in t:
        return "obd2_scanner"
    if "fm transmitter" in t or "bluetooth car adapter" in t:
        return "fm_transmitter"
    if "leather" in t or "interior cleaner" in t:
        return "leather_cleaner"
    if "towel" in t or "microfiber" in t or "drying towel" in t:
        return "microfiber_towels"
    if "ceramic" in t or "coating" in t or "wax" in t or "shine" in t:
        return "ceramic_coating_wax"
    if "swaddle" in t or "blanket" in t or "baby" in t and "wrap" in t:
        return "baby_swaddle"
    if "montessori" in t or "sensory" in t or "toddler toy" in t:
        return "montessori_toy"
    if "curler" in t or "hair" in t and ("wave" in t or "iron" in t):
        return "hair_curler"
    if "lip" in t and ("gloss" in t or "plump" in t or "oil" in t):
        return "lip_plump"
    if "candy" in t or "freeze dried" in t or "snack" in t:
        return "freeze_dried"
    if "figurine" in t or "blind box" in t or "smiski" in t or "toy" in t:
        return "smiski_figurine"
    if "cooler" in t or "ice chest" in t or "drinkware" in t:
        return "hard_cooler"
    if "keyboard" in t or "keycap" in t or "mechanical" in t:
        return "mechanical_keyboard"
    if "mic" in t or "microphone" in t or "lavalier" in t:
        return "lavalier_microphone"
    if "boot" in t or "platform" in t or "shoes" in cat:
        return "platform_boots"
    if "bodysuit" in t or "shapewear" in t or "legging" in t:
        return "sculpting_bodysuit"
    if "skincare" in t or "serum" in t or "sunscreen" in t or "beauty" in cat:
        return "korean_skincare"
    if "tumbler" in t or "bottle" in t or "mug" in t or "kitchen" in cat:
        return "tumbler_drinkware"
    if "grooming" in t or "dog" in t or "cat" in t or "pet" in cat:
        return "pet_grooming"
    
    return "tactical_backseat_organizer"

# Helper for 1688 search
from exporters.html_exporter import get_1688_query, get_alibaba_query

# Real commercial products catalog dictionary by category & sub_niche
REAL_US_CATALOG = {
    "Automotive & Motorcycle": [
        ("AstroAI Digital Tire Pressure Gauge 150 PSI with Lighted Nozzle", "Car Electronics & Mounts", 11.99),
        ("NOCO Boost Plus GB40 1000A UltraSafe Car Battery Jump Starter", "Car Electronics & Mounts", 99.95),
        ("Anker Roav SmartCharge F0 Bluetooth FM Transmitter Audio Adapter", "Car Electronics & Mounts", 16.99),
        ("Meguiar's Gold Class Car Wash Foam Shampoo & Conditioner 64oz", "Cleaning & Detailing", 13.99),
        ("Rain-X 2-in-1 Windshield Glass Cleaner with Water Repellent Spray", "Cleaning & Detailing", 7.49),
        ("WeatherTech Universal Trim-to-Fit Heavy Duty Rubber Cargo Liner", "Car Interior Accessories", 54.95),
        ("Drop Stop The Original Patented Car Seat Gap Filler 2-Pack", "Car Interior Accessories", 24.99),
        ("ThisWorx Portable High Power Car Vacuum Cleaner with Detail Kit", "Car Interior Accessories", 34.99),
        ("Garmin Dash Cam Mini 2 1080p Ultra-Compact Car Security Camera", "Car Electronics & Mounts", 129.99),
        ("Lamicall Car Air Vent Magnetic Cell Phone Mount Cradle", "Car Electronics & Mounts", 13.99),
        ("KMMOTORS Foldable Car Garbage Can with Waterproof Interior Liner", "Car Interior Accessories", 15.99),
        ("Chemical Guys Leather Cleaner and Leather Conditioner Complete Kit", "Cleaning & Detailing", 21.99),
        ("Zwipes Auto Professional Microfiber Drying Towels 12-Pack", "Cleaning & Detailing", 14.49),
        ("Turtle Wax Hybrid Solutions Ceramic Wet Wax Car Spray 26oz", "Cleaning & Detailing", 16.98),
        ("Fochier Heavy Duty Elastic Bungee Cargo Net for SUV Trunk Storage", "Car Interior Accessories", 19.99),
        ("ILM Motorcycle Full Face Modular Helmet with Dual Visor DOT", "Motorcycle Gear & Parts", 79.99),
        ("FreedConn T-COM VB Motorcycle Helmet Bluetooth 5.0 Intercom Headset", "Motorcycle Gear & Parts", 49.99),
        ("Nelson-Rigg Commuter Sport Motorcycle Tail Bag Luggage Pack", "Motorcycle Gear & Parts", 99.95),
        ("Oxford Aqua T30 Waterproof All-Weather Motorcycle Roll Bag 30L", "Motorcycle Gear & Parts", 59.95),
        ("Sedici Federico 2 Mesh Armored Breathable Motorcycle Riding Jacket", "Motorcycle Gear & Parts", 149.99),
        ("Alpinestars SMX-1 Air V2 Breathable Leather Motorcycle Gloves", "Motorcycle Gear & Parts", 44.95),
        ("Oxford Monster Ultra Heavy Duty 14mm Hardened Steel Chain Lock", "Motorcycle Gear & Parts", 69.95),
        ("Guardian Bell Legend Gremlin Bell for Motorcycle Frame Protection", "Motorcycle Gear & Parts", 12.99),
        ("Scottoiler vSystem Automatic Motorcycle Chain Oiler Lubrication Kit", "Motorcycle Gear & Parts", 139.95)
    ],
    "Beauty & Personal Care": [
        ("COSRX Advanced Snail 96 Mucin Power Essence Hydrating Serum 3.38oz", "Skincare & Face Care", 14.59),
        ("CeraVe Resurfacing Retinol Serum Post-Acne Marks Brightening Treatment", "Skincare & Face Care", 17.99),
        ("Anua Heartleaf 77% Soothing Toner Skin Barrier Calming Care 8.45oz", "Skincare & Face Care", 18.00),
        ("Beauty of Joseon Relief Sun Rice + Probiotics SPF50+ PA++++ Sunscreen", "Skincare & Face Care", 13.50),
        ("Medicube Zero Pore Pad 2.0 Dual Textured Exfoliating Toner Pads", "Skincare & Face Care", 23.00),
        ("TIRTIR Mask Fit Red Cushion Foundation Lightweight High Coverage SPF40", "Makeup & Cosmetics", 21.99),
        ("e.l.f. Halo Glow Liquid Filter Complexion Booster Radiant Glow Primer", "Makeup & Cosmetics", 14.00),
        ("NYX Professional Makeup Fat Oil Lip Drip Non-Sticky Glossy Lip Stain", "Makeup & Cosmetics", 9.00),
        ("Rare Beauty Soft Pinch Liquid Blush Dewy Finish Long-Lasting Pigment", "Makeup & Cosmetics", 23.00),
        ("Tarte Maracuja Juicy Lip Plump Hydrating Shimmer Gloss Balm", "Makeup & Cosmetics", 24.00),
        ("Listerine Total Care Anticavity Fluoride Mouthwash Fresh Mint 1L", "Oral Care & Whitening", 8.49),
        ("Crest 3D White Professional Effects Whitestrips Teeth Whitening Kit", "Oral Care & Whitening", 45.99),
        ("Waterpik Aquarius Water Flosser Professional Dental Plaque Remover", "Oral Care & Whitening", 79.99),
        ("GuruNanda Cocomint Pulling Oil with 7 Pure Essential Oils for Teeth", "Oral Care & Whitening", 13.99),
        ("TheraBreath Fresh Breath Dentist Recommended Oral Rinse Icy Mint 2-Pack", "Oral Care & Whitening", 15.98),
        ("Dyson Airwrap Multi-Styler Complete Long Nickel and Copper Edition", "Hair Care & Styling Tools", 599.99),
        ("Shark FlexStyle Air Drying & Styling System with Auto-Wrap Curlers", "Hair Care & Styling Tools", 299.99),
        ("Revlon One-Step Volumizer Plus 2.0 Ceramic Hot Air Blow Dry Brush", "Hair Care & Styling Tools", 39.99),
        ("Mielle Organics Rosemary Mint Scalp & Hair Strengthening Growth Oil", "Hair Care & Styling Tools", 9.99),
        ("Olaplex No. 7 Bonding Oil Weightless Heat Protection Hair Serum", "Hair Care & Styling Tools", 30.00),
        ("Sol de Janeiro Brazilian Bum Bum Body Cream Guaraná Firming Cream 8.1oz", "Beauty Tools & Accessories", 48.00),
        ("Hero Cosmetics Mighty Patch Original Hydrocolloid Blemish Dots 36-Count", "Beauty Tools & Accessories", 12.99),
        ("Finishing Touch Flawless Women's Painless Facial Hair Remover 18K Gold", "Beauty Tools & Accessories", 19.98),
        ("Ice Roller for Face and Eye Puffiness Relief Stainless Steel Massager", "Beauty Tools & Accessories", 9.99)
    ],
    "Baby & Maternity": [
        ("Momcozy S12 Pro Hands-Free Wearable Breast Pump Double Electric", "Feeding & Nursing", 119.99),
        ("Haakaa Manual Breast Pump Silicone Milk Collector with Suction Base 4oz", "Feeding & Nursing", 13.94),
        ("Dr. Brown's Natural Flow Anti-Colic Options+ Narrow Baby Bottles 4-Pack", "Feeding & Nursing", 21.99),
        ("Comotomo Natural Feel Silicone Baby Bottles Dual Anti-Colic Vents 8oz", "Feeding & Nursing", 23.99),
        ("Baby Brezza Formula Pro Advanced Automatic Baby Formula Dispenser", "Feeding & Nursing", 199.99),
        ("Frida Baby 3-in-1 Nose, Nail & Ear Picker Snot Cleaning Tool", "Diapering & Potty", 9.99),
        ("Ubbi Steel Odor Locking Diaper Pail Trash Can Special Edition Matte", "Diapering & Potty", 79.99),
        ("Aquaphor Baby Healing Ointment Advanced Therapy Skin Protectant 14oz", "Diapering & Potty", 17.47),
        ("Huggies Natural Care Sensitive Baby Wipes Hypoallergenic 560 Count", "Diapering & Potty", 17.98),
        ("Pampers Swaddlers Disposable Diapers Newborn Wetness Indicator 140-Pack", "Diapering & Potty", 44.99),
        ("Mushie Silicone Baby Bibs Set of 2 Waterproof Deep Food Catch Pocket", "Baby Clothing & Shoes", 12.99),
        ("Burt's Bees Baby 100% Organic Cotton Romper Jumpsuit Pajama 2-Pack", "Baby Clothing & Shoes", 19.95),
        ("Simple Joys by Carter's Cotton Footed Sleep and Play Onesie 3-Pack", "Baby Clothing & Shoes", 18.99),
        ("Hudson Baby Unisex Plush Animal Fleece Baby Bathrobe with Hood", "Baby Clothing & Shoes", 14.99),
        ("Kyte Baby Soft Bamboo Rayon Zippered Footie Sleeper Pajama 0-3M", "Baby Clothing & Shoes", 38.00),
        ("Lovevery The Play Gym Stage-Based Sensory Activity Play Mat for Baby", "Teething & Sensory Toys", 140.00),
        ("Manhattan Toy Winkel Rattle & Sensory Teether Activity Toy BPA Free", "Teething & Sensory Toys", 11.99),
        ("Fisher-Price Kick & Play Piano Deluxe Musical Gym with Smart Stages", "Teething & Sensory Toys", 39.99),
        ("Shashibo Shape Shifting Box Award Winning Patented Rare Earth Magnet Toy", "Teething & Sensory Toys", 24.99),
        ("Skip Hop Explore and More 3-Stage Interactive Activity Center Jumper", "Teething & Sensory Toys", 142.99)
    ],
    "Kitchenware": [
        ("Stanley Quencher H2.0 FlowState Stainless Steel Vacuum Tumbler 40oz", "Drinkware & Tumblers", 45.00),
        ("Owala FreeSip Insulated Stainless Steel Water Bottle with Straw 32oz", "Drinkware & Tumblers", 37.99),
        ("Hydro Flask All Around Travel Tumbler with Handle and Flex Straw 40oz", "Drinkware & Tumblers", 44.95),
        ("YETI Rambler 30oz Stainless Steel Vacuum Insulated MagSlider Lid Tumbler", "Drinkware & Tumblers", 42.00),
        ("Simple Modern 40oz Tumbler with Handle and Straw Lid Trek Insulated Cup", "Drinkware & Tumblers", 29.99),
        ("Ninja AF101 Air Fryer 4-Quart Capacity with Crisper Plate & Roaster", "Kitchen Appliances", 89.99),
        ("Cosori Pro LE 5.0-Quart Air Fryer Compact Quiet 450F High Heat Cooking", "Kitchen Appliances", 99.99),
        ("Magic Bullet Blender Small 11-Piece Set High-Speed Smoothie Blender", "Kitchen Appliances", 39.88),
        ("Keurig K-Express Single Serve K-Cup Pod Coffee Maker Quick Brew 42oz", "Kitchen Appliances", 69.99),
        ("Lodge Pre-Seasoned Cast Iron Skillet with Silicone Hot Handle Holder 10.25in", "Cookware & Bakeware", 24.90),
        ("Caraway Non-Toxic Ceramic Non-Stick Fry Pan 10.5in Chemical-Free Cookware", "Cookware & Bakeware", 95.00),
        ("HexClad Hybrid Nonstick 12-Inch Stainless Steel Wok with Stay-Cool Handle", "Cookware & Bakeware", 149.99),
        ("Cuisinart 12-Piece Ceramic Coated Printed Color Kitchen Knife Set", "Kitchen Utensils & Gadgets", 19.99),
        ("Fullstar Vegetable Chopper 4-in-1 Mandoline Spiralizer Onion Dicer 1.2L", "Kitchen Utensils & Gadgets", 29.99),
        ("ThermoPro TP19H Waterproof Digital Meat Thermometer Instant Read Backlit", "Kitchen Utensils & Gadgets", 15.99),
        ("Scrub Daddy Color Sponge 4-Pack Scratch-Free FlexTexture Kitchen Scrubber", "Kitchen Cleaning", 14.99),
        ("Rubbermaid Brilliance Leak-Proof Food Storage Containers 10-Piece Set", "Kitchen Storage", 34.99),
        ("Stasher Platinum Silicone Reusable Food Bag Leakproof Storage Dishwasher", "Kitchen Storage", 13.99),
        ("Vtopmart Airtight Pantry Food Storage Containers with Chalkboard Labels", "Kitchen Storage", 38.99),
        ("OXO Good Grips Pop Container Airtight Flour & Sugar Canister 4.4 Qt", "Kitchen Storage", 21.95)
    ],
    "Phones & Electronics": [
        ("Anker MagGo Qi2 Wireless Charging Station 3-in-1 Foldable Stand 15W", "Chargers & Cables", 89.99),
        ("UGREEN Nexode 100W USB-C GaN 4-Port Fast Wall Charger Compact Block", "Chargers & Cables", 54.99),
        ("Baseus 65W Power Bank 20000mAh Laptop Portable Fast Charger External Battery", "Chargers & Cables", 49.99),
        ("Apple AirTag 4-Pack Precision Finding Bluetooth Tracking Key Finder", "Phone Accessories", 79.99),
        ("TORRAS Magnetic Shockproof iPhone 16 Pro Max Case with Invisible Stand", "Phone Accessories", 29.99),
        ("LISEN MagSafe Car Mount Wireless Charger 15W Air Vent Qi2 Certified", "Phone Accessories", 32.99),
        ("DJI Osmo Pocket 3 Creator Combo 4K 120fps 1-Inch Sensor Gimbal Camera", "Cameras & Optics", 669.00),
        ("DJI Mic 2 Wireless Lavalier Microphone with Intelligent Noise Cancelling", "Microphones & Audio", 349.00),
        ("Rode Wireless PRO Dual Channel Compact Microphone System 32-Bit Float", "Microphones & Audio", 399.00),
        ("Sony WH-1000XM5 Wireless Industry Leading Noise Canceling Headphones", "Headphones & Earbuds", 398.00),
        ("Bose QuietComfort Ultra Wireless Noise Cancelling Over-Ear Headphones", "Headphones & Earbuds", 429.00),
        ("Beats Studio Pro Premium Wireless Bluetooth Spatial Audio Headphones", "Headphones & Earbuds", 249.99),
        ("JBL Flip 6 Portable Waterproof Bluetooth Speaker Deep Bass Output", "Speakers & Soundbars", 99.95),
        ("Marshall Emberton II Portable Compact Bluetooth Speaker 30+ Hours Battery", "Speakers & Soundbars", 149.99),
        ("Anker Soundcore Motion 300 Hi-Res Wireless Smart Portable Bluetooth Speaker", "Speakers & Soundbars", 79.99),
        ("Logitech MX Master 3S Wireless Performance Mouse Quiet Clicks 8K DPI", "Computer Accessories", 99.99),
        ("Keychron V1 QMK Custom Mechanical Keyboard Hot-Swappable RGB Frosted", "Computer Accessories", 84.00),
        ("SteelSeries Apex Pro TKL Wireless HyperMagnetic Gaming Keyboard", "Computer Accessories", 249.99),
        ("BenQ ScreenBar Halo LED Monitor Light Bar Wireless Controller No Glare", "Computer Accessories", 179.00),
        ("Elgato Stream Deck MK.2 Studio Controller 15 Customizable LCD Macro Keys", "Computer Accessories", 149.99)
    ],
    "Womenswear & Underwear": [
        ("SKIMS Fits Everybody Scoop Neck Sleeveless Bodysuit Second-Skin Comfort", "Bodysuits & Shapewear", 58.00),
        ("SPANX HigherPower High-Waisted Mid-Thigh Tummy Control Shaper Shorts", "Bodysuits & Shapewear", 38.00),
        ("Halara High Waisted Crossover 2-in-1 Side Pocket Flare Casual Leggings", "Activewear & Leggings", 39.95),
        ("Lululemon Align High-Rise Pant 25in Butter-Soft Weightless Yoga Tights", "Activewear & Leggings", 98.00),
        ("CRZ YOGA Butterluxe High Waisted Workout Leggings Naked Feeling 25in", "Activewear & Leggings", 32.00),
        ("Gymshark Vital Seamless 2.0 Long Sleeve Gym Crop Top Breathable Knit", "Activewear & Leggings", 40.00),
        ("Alo Yoga Airlift Line Up Bra Medium Impact Strappy Back Sports Bralette", "Bras & Underwear", 68.00),
        ("Calvin Klein Modern Cotton Wireless Bralette Unlined Racerback Soft Cup", "Bras & Underwear", 30.00),
        ("Warners Cloud 9 Super Soft Wireless Comfort Contour Everyday T-Shirt Bra", "Bras & Underwear", 21.99),
        ("Aerie Real Free Seamless Ribbed Boybrief Stretch Cotton Panty 5-Pack", "Bras & Underwear", 35.00),
        ("Eberjey Gisele TENCEL Modal Long PJ Set Contrast Piping Soft Sleepwear", "Sleepwear & Loungewear", 158.00),
        ("Stars Above Beautifully Soft Notch Collar Pajama Set Two-Piece Loungewear", "Sleepwear & Loungewear", 29.99),
        ("Orolay Women's Thickened Down Jacket Winter Warm Hooded Parka Coat", "Outerwear & Jackets", 149.99),
        ("Levi's Original Trucker Denim Jacket Classic Fit Vintage Washed Blue", "Outerwear & Jackets", 89.50),
        ("The Drop Women's Britt Tiered Maxi Tent Dress Relaxed Flowy Fit", "Dresses & Jumpsuits", 59.90),
        ("ANRABESS Casual Loose Sleeveless Jumpsuit Overalls with Pockets", "Dresses & Jumpsuits", 36.99)
    ],
    "Shoes": [
        ("UGG Classic Ultra Mini Platform Genuine Suede Sheepskin Ankle Boots", "Boots", 160.00),
        ("UGG Tazz Suede Platform Clog Slippers Embroidered Braid Trim", "Slippers", 130.00),
        ("HOKA Clifton 9 Neutral Lightweight Everyday Road Running Shoes", "Athletic Shoes", 145.00),
        ("HOKA Bondi 8 Maximum Cushion Road Running Shoes All-Day Comfort", "Athletic Shoes", 165.00),
        ("On Cloud 5 Lightweight All-Day Comfort Speed-Lacing Running Shoes", "Athletic Shoes", 139.99),
        ("Birkenstock Boston Soft Footbed Suede Leather Slip-On Mule Clogs", "Sandals & Clogs", 158.00),
        ("Crocs Classic Clog Slip-On Waterproof Lightweight Foam Sandal", "Sandals & Clogs", 39.99),
        ("New Balance 574 Core Classic Suede Mesh Cushion Heritage Sneakers", "Casual Sneakers", 89.99),
        ("New Balance 530 Retro Running Shoes Silver Metallic Sportstyle", "Casual Sneakers", 99.99),
        ("Adidas Samba OG Classic Low-Top Leather Gum Sole Streetwear Shoes", "Casual Sneakers", 100.00),
        ("Nike Air Force 1 07 Classic Leather Low Top Basketball Lifestyle Sneaker", "Casual Sneakers", 115.00),
        ("Brooks Ghost 15 Smooth Balanced Cushion Road Running Shoes Certified", "Athletic Shoes", 109.95),
        ("Asics Gel-Kayano 30 Stability Support Road Running Shoes FF Blast+", "Athletic Shoes", 160.00),
        ("Dr. Martens 1460 Smooth Leather 8-Eye Combat Ankle Boot Goodyear Welt", "Boots", 170.00),
        ("Blundstone 500 Original Chelsea Boot Rugged Water-Resistant Leather", "Boots", 219.95),
        ("Steve Madden Slinky30 Platform Slide Sandal Nostalgic 90s Stretch Band", "Sandals & Clogs", 89.95)
    ],
    "Pet Supplies": [
        ("ChomChom Roller Pet Hair Remover Lint Roller for Furniture and Carpet", "Pet Grooming", 24.99),
        ("Neakasa P1 Pro Pet Grooming Vacuum Kit with 5 Proven Suction Tools", "Pet Grooming", 129.99),
        ("Oneisall Low Noise Rechargeable Cordless Dog Hair Clippers Trimmer Kit", "Pet Grooming", 35.99),
        ("Hertzko Self-Cleaning Slicker Brush for Dogs and Cats Removes Loose Undercoat", "Pet Grooming", 15.99),
        ("FURminator deShedding Undercoat Tool for Medium and Large Dogs", "Pet Grooming", 32.99),
        ("KONG Classic Durable Natural Rubber Dog Chew Toy for Fetch and Stuffing", "Pet Toys & Play", 13.99),
        ("Outward Hound Interactive Treat Puzzle Game for Dogs Brain Enrichment", "Pet Toys & Play", 14.99),
        ("Catit Senses 2.0 Digger Interactive Slow Feed Cat Food Puzzle Toy", "Pet Toys & Play", 16.99),
        ("Petkit Eversweet 3 Pro Wireless Water Pump Ultra-Quiet Pet Fountain 1.8L", "Pet Feeding & Water", 49.99),
        ("WOPET Automatic Cat Feeder 6L Timed Dry Dog Food Dispenser Voice Recorder", "Pet Feeding & Water", 59.99),
        ("Bedsure Orthopedic Memory Foam Dog Bed with Removable Washable Cover", "Pet Beds & Furniture", 45.99),
        ("Furbo 360 Dog Camera Rotating Full HD Smart Treat Tossing Pet Cam", "Pet Cameras & Tech", 199.00),
        ("Earthbath All Natural Hypo-Allergenic Oatmeal Aloe Pet Shampoo 16oz", "Pet Bathing & Health", 14.99),
        ("Ruffwear Front Range Everyday Padded No-Pull Dog Harness Reflective", "Dog Collars & Leashes", 49.95)
    ]
}

print(f"Catalog template loaded with {sum(len(v) for v in REAL_US_CATALOG.values())} base product listings.")
