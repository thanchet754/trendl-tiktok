"""
28 Core Categories & Sub-niches Taxonomy for TikTok Shop US.
Directly maps to leading analytics standards (Kalodata, FastMoss, EchoTik).
"""

from typing import Dict, List, Any

TIKTOK_SHOP_28_CATEGORIES = [
    {
        "name": "Automotive & Motorcycle",
        "name_vi": "Ô Tô & Xe Máy",
        "icon": "ph-car",
        "sub_niches": [
            {"name": "Car Interior Accessories", "name_vi": "Nội Thất & Phụ Kiện Ô Tô"},
            {"name": "Car Electronics & Mounts", "name_vi": "Giá Đỡ & Thiết Bị Điện Tử Ô Tô"},
            {"name": "Cleaning & Detailing", "name_vi": "Dụng Cụ Vệ Sinh & Chăm Sóc Xe"},
            {"name": "Motorcycle Gear & Parts", "name_vi": "Đồ Bảo Hộ & Phụ Tùng Xe Máy"}
        ]
    },
    {
        "name": "Baby & Maternity",
        "name_vi": "Mẹ & Bé",
        "icon": "ph-baby",
        "sub_niches": [
            {"name": "Baby Clothing & Shoes", "name_vi": "Quần Áo Trẻ Em"},
            {"name": "Feeding & Nursing", "name_vi": "Bình Sữa & Đồ Ăn Dặm"},
            {"name": "Teething & Sensory Toys", "name_vi": "Đồ Chơi Gặm Nướu & Phát Triển Trí Tuệ"},
            {"name": "Diapering & Potty", "name_vi": "Tã Bỉm & Chăm Sóc Bé"}
        ]
    },
    {
        "name": "Beauty & Personal Care",
        "name_vi": "Làm Đẹp & Chăm Sóc Cá Nhân",
        "icon": "ph-sparkle",
        "sub_niches": [
            {"name": "Skincare & Face Care", "name_vi": "Chăm Sóc Da Mặt (Toner, Khăn Lau, Serum)"},
            {"name": "Makeup & Cosmetics", "name_vi": "Trang Điểm & Mỹ Phẩm"},
            {"name": "Oral Care & Whitening", "name_vi": "Làm Trắng Răng & Chăm Sóc Răng Miệng"},
            {"name": "Hair Care & Styling Tools", "name_vi": "Dụng Cụ Uốn Tóc & Dưỡng Tóc"},
            {"name": "Beauty Tools & Accessories", "name_vi": "Dụng Cụ Làm Đẹp"}
        ]
    },
    {
        "name": "Books, Magazines & Audio",
        "name_vi": "Sách & Văn Phòng Phẩm",
        "icon": "ph-book-open",
        "sub_niches": [
            {"name": "Journaling & Stationery", "name_vi": "Sổ Tay & Bút Pastel"},
            {"name": "Self-Help & Business", "name_vi": "Sách Phát Triển Bản Thân"},
            {"name": "Children Books", "name_vi": "Sách Thiếu Nhi"}
        ]
    },
    {
        "name": "Collectibles",
        "name_vi": "Đồ Sưu Tầm",
        "icon": "ph-trophy",
        "sub_niches": [
            {"name": "Trading Cards", "name_vi": "Thẻ Bài Sưu Tầm"},
            {"name": "Blind Box & Figurines", "name_vi": "Hộp Mù Blind Box & Mô Hình"}
        ]
    },
    {
        "name": "Computers & Office Equipment",
        "name_vi": "Máy Tính & Thiết Bị Văn Phòng",
        "icon": "ph-desktop",
        "sub_niches": [
            {"name": "Keyboards & Mice", "name_vi": "Bàn Phím Cơ & Chuột"},
            {"name": "Desk Organizers & Stands", "name_vi": "Kệ Đỡ Màn Hình & Giá Đỡ"},
            {"name": "Cables & Adapters", "name_vi": "Dây Cáp & Cổng Chuyển"}
        ]
    },
    {
        "name": "Fashion Accessories",
        "name_vi": "Phụ Kiện Thời Trang",
        "icon": "ph-sunglasses",
        "sub_niches": [
            {"name": "Sunglasses & Eyewear", "name_vi": "Kính Mát Thời Trang"},
            {"name": "Hats & Caps", "name_vi": "Mũ Nón Streetwear"},
            {"name": "Belts & Scarves", "name_vi": "Thắt Lưng & Khăn Choàng"}
        ]
    },
    {
        "name": "Food & Beverages",
        "name_vi": "Thực Phẩm & Đồ Uống",
        "icon": "ph-cookie",
        "sub_niches": [
            {"name": "Freeze Dried Snacks", "name_vi": "Kẹo & Đồ Ăn Vặt Sấy Thăng Hoa"},
            {"name": "Coffee & Specialty Tea", "name_vi": "Cà Phê & Trà Thảo Mộc"},
            {"name": "Sauces & Condiments", "name_vi": "Gia Vị & Sốt Chấm Viral"}
        ]
    },
    {
        "name": "Furniture",
        "name_vi": "Nội Thất",
        "icon": "ph-armchair",
        "sub_niches": [
            {"name": "Ergonomic Chairs", "name_vi": "Ghế Công Thái Học"},
            {"name": "Bedside Tables & Racks", "name_vi": "Kệ Đầu Giường & Tủ Đồ Nhỏ"}
        ]
    },
    {
        "name": "Health",
        "name_vi": "Sức Khỏe & Thực Phẩm Chức Năng",
        "icon": "ph-heartbeat",
        "sub_niches": [
            {"name": "Vitamins & Dietary Supplements", "name_vi": "Vitamin & Gummies Giúp Ngủ Ngon"},
            {"name": "Pain Relief & Posture Support", "name_vi": "Đai Chống Gù & Giảm Đau Lưng"},
            {"name": "Fitness Nutrition", "name_vi": "Dinh Dưỡng Tập Gym & Giảm Cân"}
        ]
    },
    {
        "name": "Home Improvement",
        "name_vi": "Cải Tạo & Trang Trí Nhà Cửa",
        "icon": "ph-paint-brush",
        "sub_niches": [
            {"name": "Ambient LED Lighting", "name_vi": "Dây Đèn LED & Đèn Cảm Ứng"},
            {"name": "Wall Decals & Hardware", "name_vi": "Tranh Dán Tường & Móc Treo"}
        ]
    },
    {
        "name": "Home Supplies",
        "name_vi": "Đồ Dùng Gia Đình & Vệ Sinh",
        "icon": "ph-broom",
        "sub_niches": [
            {"name": "Cleaning & Organization", "name_vi": "Cọ Rửa Điện & Dọn Dẹp CleanTok"},
            {"name": "Laundry & Storage", "name_vi": "Túi Giặt & Hộp Lưu Trữ"},
            {"name": "Air Fresheners & Candles", "name_vi": "Nến Thơm & Tinh Dầu Khử Mùi"}
        ]
    },
    {
        "name": "Household Appliances",
        "name_vi": "Thiết Bị Điện Gia Dụng",
        "icon": "ph-plug",
        "sub_niches": [
            {"name": "Portable Steamers & Irons", "name_vi": "Bàn Ủi Hơi Nước Cầm Tay"},
            {"name": "Mini Blenders & Juicers", "name_vi": "Máy Xay Sinh Tố Mini Cầm Tay"},
            {"name": "Electric Kettles", "name_vi": "Ấm Đun Nước Siêu Tốc"}
        ]
    },
    {
        "name": "Jewelry Accessories & Derivatives",
        "name_vi": "Trang Sức & Quà Tặng Tùy Chỉnh",
        "icon": "ph-sketch-logo",
        "sub_niches": [
            {"name": "Custom Name Jewelry & POD", "name_vi": "Dây Chuyền Khắc Tên & Hoa Sinh"},
            {"name": "Earrings & Rings", "name_vi": "Khuyên Tai & Nhẫn Tinh Tế"},
            {"name": "Bracelets & Charms", "name_vi": "Lắc Tay & Hạt Charm"}
        ]
    },
    {
        "name": "Kids' Fashion",
        "name_vi": "Thời Trang Trẻ Em",
        "icon": "ph-t-shirt",
        "sub_niches": [
            {"name": "Toddler Outfits", "name_vi": "Set Đồ Bé Gái & Bé Trai"},
            {"name": "Costumes & Pajamas", "name_vi": "Đồ Ngủ & Đồ Hóa Trang Trẻ Em"}
        ]
    },
    {
        "name": "Kitchenware",
        "name_vi": "Dụng Cụ Nhà Bếp & Bàn Ăn",
        "icon": "ph-cooking-pot",
        "sub_niches": [
            {"name": "Drinkware & Tumblers", "name_vi": "Bình & Cốc Giữ Nhiệt (Owala, Stanley)"},
            {"name": "Cutting Boards & Charcuterie", "name_vi": "Thớt Gỗ Khắc Tên & Khay Phô Mai"},
            {"name": "Kitchen Gadgets & Peelers", "name_vi": "Dụng Cụ Gọt Tỉa & Nấu Ăn Đa Năng"}
        ]
    },
    {
        "name": "Luggage & Bags",
        "name_vi": "Balo, Vali & Túi Xách",
        "icon": "ph-tote",
        "sub_niches": [
            {"name": "Crossbody & Belt Bags", "name_vi": "Túi Đeo Chéo & Túi Bao Tử Lululemon Dupe"},
            {"name": "Travel Backpacks", "name_vi": "Balo Du Lịch Đa Năng"},
            {"name": "Tote Bags", "name_vi": "Túi Vải Canvas & Túi Công Sở"}
        ]
    },
    {
        "name": "Menswear & Underwear",
        "name_vi": "Thời Trang & Đồ Lót Nam",
        "icon": "ph-pants",
        "sub_niches": [
            {"name": "Streetwear & Cargo Pants", "name_vi": "Quần Túi Hộp & Quần Jean Ống Rộng"},
            {"name": "Graphic Tees & Hoodies", "name_vi": "Áo Thun In Hình & Áo Hoodie"},
            {"name": "Boxers & Underwear", "name_vi": "Quần Lót Thoáng Khí & Vớ Nam"}
        ]
    },
    {
        "name": "Modest Fashion",
        "name_vi": "Thời Trang Kín Đáo",
        "icon": "ph-coat-hanger",
        "sub_niches": [
            {"name": "Abayas & Hijabs", "name_vi": "Khăn Choàng & Đầm Kín Đáo"},
            {"name": "Maxi Dresses", "name_vi": "Đầm Dài Che Khuyết Điểm"}
        ]
    },
    {
        "name": "Pet Supplies",
        "name_vi": "Đồ Dùng & Chăm Sóc Thú Cưng",
        "icon": "ph-dog",
        "sub_niches": [
            {"name": "Pet Grooming & Care", "name_vi": "Lược Chải Lông Tự Nhả & Dưỡng Lông"},
            {"name": "Pet Toys & Interactive", "name_vi": "Đồ Chơi Thú Cưng Tương Tác"},
            {"name": "Collars, Leashes & Harnesses", "name_vi": "Yếm & Dây Dắt Chó Mèo"}
        ]
    },
    {
        "name": "Phones & Electronics",
        "name_vi": "Điện Thoại & Phụ Kiện Công Nghệ",
        "icon": "ph-device-mobile",
        "sub_niches": [
            {"name": "Printers & Gadgets", "name_vi": "Máy In Nhiệt Bỏ Túi & Sticker"},
            {"name": "Wireless Microphones & Audio", "name_vi": "Micro Thu Âm Không Dây Cài Áo"},
            {"name": "Phone Cases & Chargers", "name_vi": "Ốp Lưng Từ Tính & Củ Sạc Nhanh"},
            {"name": "Smartwatches & Wearables", "name_vi": "Đồng Hồ Thông Minh & Retro"}
        ]
    },
    {
        "name": "Pre-Owned",
        "name_vi": "Hàng Tuyển Secondhand",
        "icon": "ph-recycle",
        "sub_niches": [
            {"name": "Vintage Apparel", "name_vi": "Áo Khoác & Đồ Vintage Mỹ"},
            {"name": "Designer Accessories", "name_vi": "Phụ Kiện Hàng Hiệu Đã Qua Sử Dụng"}
        ]
    },
    {
        "name": "Shoes",
        "name_vi": "Giày Dép",
        "icon": "ph-sneaker",
        "sub_niches": [
            {"name": "Platform Clogs & Slides", "name_vi": "Dép Sục & Dép Đi Trong Nhà"},
            {"name": "Sneakers & Walking Shoes", "name_vi": "Giày Thể Thao Êm Chân"},
            {"name": "Boots & Ankle Shoes", "name_vi": "Bốt Cổ Thấp Thời Trang"}
        ]
    },
    {
        "name": "Sports & Outdoor",
        "name_vi": "Thể Thao & Dã Ngoại",
        "icon": "ph-barbell",
        "sub_niches": [
            {"name": "Gym & Yoga Accessories", "name_vi": "Thảm Yoga & Dây Kháng Lực"},
            {"name": "Outdoor Camping Gear", "name_vi": "Đèn Dã Ngoại & Bình Nước Sinh Tồn"}
        ]
    },
    {
        "name": "Textiles & Soft Furnishings",
        "name_vi": "Vải May & Đồ Dệt May Gia Đình",
        "icon": "ph-grid-four",
        "sub_niches": [
            {"name": "Aesthetic Rugs & Mats", "name_vi": "Thảm Chùi Chân ASMR"},
            {"name": "Pillows & Blankets", "name_vi": "Gối Tựa Lưng & Chăn Lông Cừu"}
        ]
    },
    {
        "name": "Tools and equipment",
        "name_vi": "Dụng Cụ Sửa Chữa & Đồ Nghề",
        "icon": "ph-wrench",
        "sub_niches": [
            {"name": "Cordless Screwdrivers", "name_vi": "Máy Bắt Vít Pin Mini"},
            {"name": "Multi-tool Sets", "name_vi": "Bộ Kìm Kéo Đa Năng"}
        ]
    },
    {
        "name": "Toys & Hobbies",
        "name_vi": "Đồ Chơi & Sở Thích",
        "icon": "ph-game-controller",
        "sub_niches": [
            {"name": "Squishy & Fidget Toys", "name_vi": "Đồ Chơi Bóp Giảm Stress (Dumpling)"},
            {"name": "Building Blocks & Puzzles", "name_vi": "Bộ Xếp Hình & Mô Hình Lắp Ráp"},
            {"name": "Plushies & Stuffed Toys", "name_vi": "Gấu Bông Cute"}
        ]
    },
    {
        "name": "Virtual Products",
        "name_vi": "Sản Phẩm Kỹ Thuật Số",
        "icon": "ph-file-code",
        "sub_niches": [
            {"name": "Digital Planners & Templates", "name_vi": "Template Notion & Kế Hoạch Số"},
            {"name": "Design Presets", "name_vi": "Bộ Màu Lightroom & Preset"}
        ]
    },
    {
        "name": "Womenswear & Underwear",
        "name_vi": "Thời Trang & Đồ Lót Nữ",
        "icon": "ph-dress",
        "sub_niches": [
            {"name": "Shapewear & Body Sculpting", "name_vi": "Đồ Định Hình Bodysuit Siêu Gọn"},
            {"name": "Dresses & Rompers", "name_vi": "Đầm Váy Dự Tiệc & Đi Chơi"},
            {"name": "Athleisure & Leggings", "name_vi": "Quần Legging Nâng Mông"},
            {"name": "Lounge & Pajamas", "name_vi": "Đồ Mặc Nhà & Pijama Lụa"}
        ]
    }
]

def get_all_categories() -> List[Dict[str, Any]]:
    return TIKTOK_SHOP_28_CATEGORIES
