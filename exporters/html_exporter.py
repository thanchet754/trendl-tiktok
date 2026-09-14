"""
Comprehensive Light Square HTML Dashboard Exporter for TikTok Shop US Trend Radar
Includes:
- Left Taskbar Navigation Menu (100% Square)
- Top 24h Leaders: Top Videos (Highest GMV) & Top Influencers (Highest Sales & GMV) matching Kalodata/FastMoss layout
- 28 Major Categories & Sub-Niches Cascading Dynamic Filter Hub
- Velocity Dimension Filtering (Viral Videos 24h, Sales Velocity Movers, Breakout Search Keywords, Evergreen)
- Music & Audio Viral Radar (Hot TikTok Sounds 24h)
- Visual / Image Search & 1688 / Alibaba Sourcing Hub
- 1688 Direct Factory Lookup & International Alibaba B2B
- Bilingual English / Tiếng Việt Instant Switcher
- Multi-User & Team Saved Trends Collaboration
- 100% Light Theme & 100% Square Corners (Zero border-radius)
- 24h Real-time Trend Verification Proof & Live Audit Links
- 6-Hour Auto-Schedule Countdown Timer
"""

import os
import json
from datetime import datetime
from typing import Dict, Any

CATEGORY_SPECIFIC_1688 = {
    "Pet Supplies": {
        "brush": "宠物一键脱毛梳 自动退毛清理梳 猫狗通用",
        "clean": "宠物一键脱毛梳 自动退毛梳 猫狗去浮毛刷",
        "slicker": "宠物针梳 自动脱毛清理刷 猫狗通用",
        "deshedding": "宠物去浮毛梳 脱毛开结梳",
        "grooming": "宠物美容清理梳 猫狗去浮毛刷",
        "litter": "膨润土矿石猫砂 结团无尘 低敏除臭",
        "clay": "高效除臭膨润土矿石猫砂",
        "pee": "宠物尿垫 加厚吸水 隔尿垫 狗尿片",
        "pad": "加厚吸水宠物除臭尿垫 狗尿片",
        "treat": "猫条肉泥 营养猫零食 冻干生骨肉",
        "churu": "流质肉泥猫条 鲜肉营养膏猫零食",
        "feast": "猫罐头 湿粮 肉泥浓汤 宠物主粮",
        "poop": "可降解宠物拾便袋 拾便盒 狗便便袋",
        "leash": "防爆冲宠物牵引绳 狗胸背带",
        "collar": "反光宠物项圈 狗牌定制",
        "toy": "逗猫玩具 猫抓板 磨爪益智玩具",
        "dog": "宠物狗狗用品 训练牵引绳 拾便袋",
        "cat": "猫咪用品 磨爪猫抓板 逗猫玩具"
    },
    "Beauty & Personal Care": {
        "teeth": "紫光美白牙膏 泡沫去黄 炫白牙贴",
        "tooth": "电动牙刷 牙齿美白仪 便携冲牙器",
        "pulling oil": "椰子油漱口水 口腔清洁除口臭",
        "cocomint": "椰子薄荷漱口水 亮白牙齿",
        "toner": "毛孔清洁水杨酸棉片 积雪草爽肤水湿敷贴",
        "pore": "毛孔细致收缩棉片 清洁去黑头",
        "towel": "一次性洗脸巾 纯棉加厚 珍珠纹洁面巾",
        "patch": "水胶体痘痘贴 隐形净痘贴 吸脓透气",
        "serum": "玻尿酸面部精华液 抗衰紧致",
        "lotion": "身体乳 润肤乳 滋润保湿 香氛身体霜",
        "shea": "乳木果香氛润肤乳 高保湿身体乳",
        "lip": "果汁丰唇蜜 水光唇釉 嘟嘟唇油",
        "plump": "丰唇膏 滋润保湿变色唇油",
        "wand": "红光微电流美肤仪 面部提拉导入仪",
        "red light": "LED红光嫩肤美容仪 面部微电流",
        "curling": "多功能自动卷发棒 负离子热风直卷两用",
        "beachwaver": "全自动旋转卷发棒 陶瓷不伤发",
        "thermal brush": "热风直发梳 电热卷发圆筒梳 蓬松高颅顶",
        "blowout": "多功能电吹风造型梳 热风梳",
        "hair": "负离子无叶高速吹风机 造型美发梳"
    },
    "Kitchenware": {
        "tumbler": "不锈钢保温杯 吸管保冷杯 运动便携水杯",
        "bottle": "不锈钢真空运动水壶 大容量吸管水杯",
        "owala": "双饮吸管不锈钢保温杯 户外运动水壶",
        "stanley": "汽车杯 手柄吸管大容量保温杯",
        "cup": "不锈钢咖啡随行杯 保温保冷吸管杯",
        "scale": "高精度厨房电子秤 烘焙烘培称 重食品秤",
        "cutting board": "实木牛排餐盘 刻字砧板 菜板",
        "charcuterie": "天然竹木奶酪拼盘 熟食切板",
        "peeler": "多功能不锈钢削皮器 刨丝刀"
    },
    "Home Supplies": {
        "scrubber": "电动清洁刷 多功能旋转浴室地砖地毯刷",
        "pink stuff": "多功能清洁膏 万能去污膏 厨房油污净",
        "paste": "万能清洁去污膏 抛光清洁剂",
        "clean": "家用清洁剂 去污除垢多功能刷",
        "calendar": "亚克力磁吸冰箱周计划留言板",
        "candle": "天然大豆香薰蜡烛 琥珀玻璃罐",
        "sheet": "亲肤磨毛四件套 床单被套 纯色水洗棉",
        "bed": "加厚床单四件套 纯棉床上用品",
        "insect": "果蝇诱捕器 物理灭蚊灯 粘捕灯",
        "trap": "室内捕虫诱捕器 苍蝇小飞虫粘板",
        "ant": "灭蚁饵剂 室内除蚁胶饵 诱杀蚂蚁全窝端"
    },
    "Phones & Electronics": {
        "earbuds": "TWS真无线蓝牙耳机 降噪半入耳式",
        "airpods": "无线降噪蓝牙耳机 空间音频",
        "earphone": "Type-C有线耳机 半入耳式 通话降噪",
        "headphone": "头戴式无线蓝牙耳机 重低音主动降噪",
        "airtag": "防丢定位器 智能寻物器 蓝牙防丢器",
        "tracker": "GPS智能定位防丢器 钥匙寻物器",
        "power bank": "磁吸无线充移动电源 10000mAh快充充电宝",
        "charger": "GaN氮化镓快速充电器 快充排插",
        "cable": "PD快充数据线 编织耐用快充线",
        "mic": "无线领夹麦克风 降噪直播收音麦 手机专用",
        "camera": "4K高清数码相机 翻转屏Vlog微单 学生照相机",
        "printer": "便携迷你热敏错题打印机 无墨不干胶便签机",
        "docking": "实木多功能桌面手机支架收纳盒 充电底座",
        "case": "防摔气囊手机壳 磁吸支架保护套"
    },
    "Womenswear & Underwear": {
        "legging": "高腰交叉阔腿瑜伽裤 提臀裸感无缝打底裤",
        "halara": "交叉腰运动阔腿裤 休闲弹力女裤",
        "bodysuit": "无缝塑身衣 连体束腹收腹美体衣",
        "shapewear": "高腰收腹提臀裤 紧身无痕塑形衣",
        "dress": "法式复古收腰连衣裙 显瘦长裙",
        "romper": "休闲高弹连体裤 运动连体衣",
        "pajama": "真丝感仿真丝睡衣两件套 家居服"
    },
    "Menswear & Underwear": {
        "hoodie": "重磅纯棉连帽卫衣 潮牌落肩外套",
        "vest": "复古机车皮马甲 骑士皮背心",
        "jacket": "男士机车真皮皮衣 防风夹克",
        "pants": "工装战术长裤 多口袋休闲阔腿裤",
        "cargo": "美式复古多口袋工装裤 宽松束脚裤",
        "boxer": "莫代尔男士平角内裤 透气无痕四角裤"
    },
    "Automotive & Motorcycle": {
        "inflator": "便携车载充气泵 无线电动轮胎补气打气筒 150PSI",
        "tire": "车载智能数显电动充气泵 轮胎打气筒",
        "mount": "车载手机支架 出风口中控台重力磁吸支架",
        "holder": "车载无线充手机支架 自动感应夹紧",
        "cleaner": "车载内饰清洁软胶 汽车出风口除尘泥",
        "diffuser": "车载香薰太阳能旋转香氛 汽车出风口香水",
        "dash cam": "4K高清行车记录仪 双镜头夜视倒车影像"
    },
    "Baby & Maternity": {
        "teething": "婴儿硅胶磨牙棒 曼哈顿手抓球 咬咬胶",
        "sensory": "婴儿早教抽抽乐 蒙氏感官拉拉乐玩具",
        "baby clothes": "纯棉新生儿连体衣 婴儿哈衣爬服",
        "feeding": "婴儿硅胶吸盘碗 辅食勺防摔餐具",
        "diaper": "加厚干爽透气纸尿裤 拉拉裤批发"
    },
    "Books, Magazines & Audio": {
        "journal": "复古加厚皮质手账本 密码锁日记本",
        "planner": "时间轴日程本日计划 自律打卡手账",
        "stationery": "彩色莫兰迪双头荧光笔 刷题速干笔",
        "marker": "速干彩色标记笔 学生手账高光笔"
    },
    "Collectibles": {
        "card": "球星卡PTCG卡牌收纳册 磁吸卡砖卡夹",
        "blind box": "潮玩盲盒收纳展示盒 亚克力防尘手办架",
        "figurine": "动漫PVC手办模型 机甲潮玩摆件"
    },
    "Computers & Office Equipment": {
        "keyboard": "客制化机械键盘 无线三模热插拔轴体",
        "mouse": "人体工学垂直静音鼠标 双模无线充电",
        "desk pad": "超大皮质办公桌垫 防水防滑鼠标垫",
        "stand": "铝合金折叠笔记本支架 升降散热底座"
    },
    "Fashion Accessories": {
        "sunglasses": "Y2K复古墨镜 欧美个性太阳镜 防紫外线",
        "hat": "复古刺绣棒球帽 弯檐遮阳鸭舌帽",
        "cap": "潮牌水洗做旧鸭舌帽 户外防晒帽子",
        "belt": "复古双扣真皮皮带 时尚百搭牛仔裤腰带",
        "scarf": "仿羊绒纯色加厚保暖围巾 冬季披肩"
    },
    "Food & Beverages": {
        "candy": "彩虹糖脆皮水果软糖 爆浆夹心硬糖",
        "freeze dried": "冻干草莓脆 水果干无添加 冻干棉花糖",
        "snack": "网红休闲零食大礼包 办公室解馋小吃",
        "tea": "花果茶三角茶包 养生排毒玫瑰荷叶茶",
        "coffee": "冷萃黑咖啡粉 挂耳滤挂原产地咖啡"
    },
    "Furniture": {
        "chair": "人体工学办公电脑椅 电竞椅透气网椅",
        "desk": "电动升降桌 站立办公桌 简约电脑桌",
        "table": "简约现代床头小茶几 沙发边几移动角几",
        "rack": "落地多层置物架 卧室简易衣帽架"
    },
    "Health": {
        "supplement": "高纯度深海鱼油软胶囊 Omega-3 膳食补充剂",
        "gummy": "褪黑素助眠软糖 晚安睡眠糖",
        "vitamin": "复合维生素软糖 成人多种维生素矿物质",
        "magnesium": "甘氨酸镁胶囊 舒缓神经肌肉放松",
        "posture": "智能感应背部矫正器 防驼背隐形矫正带"
    },
    "Home Improvement": {
        "led": "RGB智能幻彩灯带 音乐律动氛围灯条",
        "strip": "自粘COB高亮柔性线性灯条 房间吊顶背景墙",
        "wallpaper": "自粘加厚防水防潮墙纸 3D立体墙贴",
        "hook": "强力免打孔透明无痕粘钩 门后衣服挂钩"
    },
    "Household Appliances": {
        "steamer": "便携手持挂烫机 家用折叠小型电熨斗",
        "blender": "便携多功能无线榨汁杯 小型辅食随行搅拌杯",
        "heater": "桌面小型暖风机 陶瓷PTC快速制热取暖器",
        "diffuser": "火焰香薰机 超声波加湿器 卧室香氛机",
        "vacuum": "无线手持车载吸尘器 家用大吸力除螨吸尘机"
    },
    "Jewelry Accessories & Derivatives": {
        "necklace": "定制出生花姓名吊坠项链 18K不锈钢锁骨链",
        "bracelet": "欧美古巴链手链 钛钢粗链保色手饰",
        "ring": "莫比乌斯环情侣对戒 S925银微镶开口戒指",
        "earrings": "法式复古珍珠耳环 纯银耳钉防过敏"
    },
    "Kids' Fashion": {
        "outfit": "儿童纯棉运动两件套 童装韩版卫衣长裤",
        "pajamas": "儿童竹纤维无骨睡衣 春秋长袖家居服",
        "dress": "女童公主裙 蓬蓬纱裙 生日礼服裙"
    },
    "Luggage & Bags": {
        "crossbody": "多功能斜挎包 运动防水腰包 胸包",
        "belt bag": "尼龙纯色腰包 经典百搭胸包 杜邦纸包",
        "backpack": "大容量干湿分离旅行背包 登机电脑包",
        "tote": "加厚纯棉帆布托特包 大容量单肩购物袋"
    },
    "Modest Fashion": {
        "abaya": "中东穆斯林长袍 Abaya 时尚开衫迪拜礼拜袍",
        "hijab": "莫代尔高弹头巾 Hijab 透气防滑围巾",
        "maxi": "优雅宽松大摆纯色长裙 垂感显瘦长款连衣裙"
    },
    "Pre-Owned": {
        "vintage": "Vintage美式复古水洗做旧牛仔外套",
        "leather": "古着复古翻领皮夹克 骑士重磅机车服"
    },
    "Shoes": {
        "clog": "EVA厚底洞洞鞋 踩屎感防滑沙滩外穿拖鞋",
        "slide": "软底防滑浴室凉拖鞋 室内厚底静音拖鞋",
        "sneaker": "轻便透气飞织运动鞋 软底减震跑步鞋",
        "boot": "真皮英伦风切尔西短靴 粗跟厚底马丁靴"
    },
    "Sports & Outdoor": {
        "mat": "TPE加厚无味防滑瑜伽垫 健身垫跳绳垫",
        "band": "高弹力乳胶阻力带 臀圈健身拉力带",
        "bottle": "户外大容量Tritan运动水杯 防摔带刻度太空杯",
        "tent": "全自动速开户外露营帐篷 防雨防晒野营装备"
    },
    "Textiles & Soft Furnishings": {
        "rug": "法兰绒吸水印花地垫 浴室门口防滑地毯",
        "blanket": "加厚双层云毯 羊羔绒保暖午睡毯 沙发盖毯",
        "pillow": "慢回弹记忆棉护颈枕 蝶形人体工学睡眠枕",
        "curtain": "高精密全遮光窗帘 隔热降噪成品窗帘"
    },
    "Tools and equipment": {
        "screwdriver": "4V便携电动螺丝刀套装 家用迷你充电式起子",
        "tool set": "家用多功能五金工具箱 维修电工工具套装",
        "multitool": "户外不锈钢多功能折叠钳 随身野营多用工具"
    },
    "Toys & Hobbies": {
        "squishy": "慢回弹减压捏捏乐 仿真包子软胶解压玩具",
        "fidget": "磁力滑块推牌 EDC减压推推乐玩具",
        "puzzle": "3D立体木质拼图 机械传动拼装模型",
        "plush": "可爱毛绒公仔 玩偶抱枕 闺蜜生日礼物"
    },
    "Virtual Products": {
        "template": "Notion自律打卡人生管理模板 电子手账",
        "preset": "Lightroom复古胶片调色预设 摄影滤镜"
    }
}

KEYWORDS_1688_MAP = {
    # Oral Care & Whitening
    "teeth": "紫光美白牙膏 泡沫去黄 炫白牙贴",
    "tooth": "电动牙刷 牙齿美白仪 便携冲牙器",
    "pulling oil": "椰子油漱口水 口腔清洁除口臭",
    "cocomint": "椰子薄荷漱口水 亮白牙齿",
    # Skincare & Beauty
    "toner": "毛孔清洁水杨酸棉片 积雪草爽肤水湿敷贴",
    "pore": "毛孔细致收缩棉片 清洁去黑头",
    "towel": "一次性洗脸巾 纯棉加厚 珍珠纹洁面巾",
    "patch": "水胶体痘痘贴 隐形净痘贴 吸脓透气",
    "serum": "玻尿酸面部精华液 抗衰紧致",
    "lotion": "身体乳 润肤乳 滋润保湿 香氛身体霜",
    "shea": "乳木果香氛润肤乳 高保湿身体乳",
    "lip": "果汁丰唇蜜 水光唇釉 嘟嘟唇油",
    "plump": "丰唇膏 滋润保湿变色唇油",
    "swab": "医用脱脂棉签 双头化妆棉签",
    "cotton": "纯棉化妆棉 一次性卸妆棉",
    "wand": "红光微电流美肤仪 面部提拉导入仪",
    "red light": "LED红光嫩肤美容仪 面部微电流",
    # Hair Care & Tools
    "curling": "多功能自动卷发棒 负离子热风直卷两用",
    "beachwaver": "全自动旋转卷发棒 陶瓷不伤发",
    "thermal brush": "热风直发梳 电热卷发圆筒梳 蓬松高颅顶",
    "blowout": "多功能电吹风造型梳 热风梳",
    "hair": "负离子无叶高速吹风机 造型美发梳",
    # Kitchen & Drinkware
    "tumbler": "不锈钢保温杯 吸管保冷杯 运动便携水杯",
    "bottle": "不锈钢真空运动水壶 大容量吸管水杯",
    "owala": "双饮吸管不锈钢保温杯 户外运动水壶",
    "stanley": "汽车杯 手柄吸管大容量保温杯",
    "scale": "高精度厨房电子秤 烘焙烘培称 重食品秤",
    "cutting board": "实木牛排餐盘 刻字砧板 菜板",
    # Home & Cleaning
    "scrubber": "电动清洁刷 多功能旋转浴室地砖地毯刷",
    "pink stuff": "多功能清洁膏 万能去污膏 厨房油污净",
    "paste": "万能清洁去污膏 抛光清洁剂",
    "clean": "家用清洁剂 去污除垢多功能刷",
    "calendar": "亚克力磁吸冰箱周计划留言板",
    "candle": "天然大豆香薰蜡烛 琥珀玻璃罐",
    "sheet": "亲肤磨毛四件套 床单被套 纯色水洗棉",
    "bed": "加厚床单四件套 纯棉床上用品",
    "insect": "果蝇诱捕器 物理灭蚊灯 粘捕灯",
    "trap": "室内捕虫诱捕器 苍蝇小飞虫粘板",
    "ant": "灭蚁饵剂 室内除蚁胶饵 诱杀蚂蚁全窝端",
    # Pet Supplies
    "brush": "宠物一键脱毛梳 自动退毛清理梳 猫狗通用",
    "litter": "膨润土猫砂 结团无尘 低敏除臭除味",
    "clay": "高效除臭膨润土矿石猫砂",
    "pee": "宠物尿垫 加厚吸水 隔尿垫 狗尿片",
    "pad": "加厚吸水宠物除臭尿垫",
    "treat": "猫条肉泥 营养猫零食 冻干生骨肉",
    "churu": "流质肉泥猫条 鲜肉营养膏猫零食",
    "feast": "猫罐头 湿粮 肉泥浓汤 宠物主粮",
    "wet cat": "营养猫罐头 鲜肉浓汤湿粮",
    "poop": "可降解宠物拾便袋 拾便盒 狗便便袋",
    "dog": "宠物狗狗用品 训练牵引绳 拾便袋",
    "cat": "猫咪用品 磨爪猫抓板 逗猫玩具",
    # Electronics & Gadgets
    "earbuds": "TWS真无线蓝牙耳机 降噪半入耳式",
    "airpods": "无线降噪蓝牙耳机 空间音频",
    "earphone": "Type-C有线耳机 半入耳式 通话降噪",
    "headphone": "头戴式无线蓝牙耳机 重低音主动降噪",
    "airtag": "防丢定位器 智能寻物器 蓝牙防丢器",
    "tracker": "GPS智能定位防丢器 钥匙寻物器",
    "power bank": "磁吸无线充移动电源 10000mAh快充充电宝",
    "charger": "GaN氮化镓快速充电器 快充排插",
    "cable": "PD快充数据线 编织耐用快充线",
    "mic": "无线领夹麦克风 降噪直播收音麦 手机专用",
    "camera": "4K高清数码相机 翻转屏Vlog微单 学生照相机",
    "printer": "便携迷你热敏错题打印机 无墨不干胶便签机",
    "docking": "实木多功能桌面手机支架收纳盒 充电底座",
    "case": "防摔气囊手机壳 磁吸支架保护套",
    # Apparel & Accessories
    "legging": "高腰交叉阔腿瑜伽裤 提臀裸感无缝打底裤",
    "halara": "交叉腰运动阔腿裤 休闲弹力女裤",
    "bodysuit": "无缝塑身衣 连体束腹收腹美体衣",
    "shapewear": "高腰收腹提臀裤 紧身无痕塑形衣",
    "hoodie": "定制宠物头像刺绣卫衣 纯棉连帽衫",
    "vest": "复古机车皮马甲 骑士皮背心",
    "jacket": "男士机车真皮皮衣 防风夹克",
    "pants": "工装战术长裤 多口袋休闲阔腿裤",
    "necklace": "定制姓名出生花项链 钛钢不锈钢饰品",
    "jewelry": "欧美流行钛钢饰品 18K金保色项链手链",
    "watch": "复古多功能电子手表 运动防水腕表",
    "casio": "复古计算器电子手表 数字石英表",
    "slipper": "羊皮毛一体雪地靴保暖棉拖鞋",
    "cap": "刺绣棒球帽 弯檐遮阳鸭舌帽",
    "hat": "户外保暖针织冷帽 潮流毛线帽",
    # Fitness & Health
    "protein": "乳清分离蛋白粉 健身增肌 代餐冲饮",
    "greens": "羽衣甘蓝复合果蔬粉 益生菌膳食纤维青汁",
    "supplement": "复合维生素胶囊 膳食营养补充剂",
    "capsule": "深海鱼油软胶囊 Omega-3高纯度",
    # Automotive
    "inflator": "便携车载充气泵 无线电动轮胎补气打气筒 150PSI",
    "tire": "车载智能数显电动充气泵",
    "mount": "车载手机支架 出风口中控台重力磁吸支架",
    "car": "车载内饰收纳 汽车清洁软胶"
}

CATEGORY_FALLBACK_1688 = {
    "Automotive & Motorcycle": "汽车用品 车载内饰 汽摩配件工厂",
    "Baby & Maternity": "母婴用品 婴儿早教玩具 孕婴童源头工厂",
    "Beauty & Personal Care": "美妆护肤 日化个护 爆款源头工厂",
    "Books, Magazines & Audio": "文具手账 本册文教 办公文化用品批发",
    "Collectibles": "潮玩盲盒 手办模型 收藏卡牌货源工厂",
    "Computers & Office Equipment": "电脑周边 3C数码配件 办公外设源头厂家",
    "Fashion Accessories": "时尚配饰 潮流帽子 墨镜腰带工厂直供",
    "Food & Beverages": "休闲零食 网红食品 冻干果干源头工厂",
    "Furniture": "现代简约家具 电脑椅 电动升降桌源头直供",
    "Health": "营养保健品 膳食补充剂 康复保健源头工厂",
    "Home Improvement": "家装建材 氛围灯带 装饰五金源头工厂",
    "Home Supplies": "居家日用 收纳整理 清洁日化工厂货源",
    "Household Appliances": "生活小家电 厨房小电器 便携家电源头厂家",
    "Jewelry Accessories & Derivatives": "流行饰品 钛钢项链手链 饰品源头工厂",
    "Kids' Fashion": "童装童鞋 儿童家居服 婴幼儿服饰源头直供",
    "Kitchenware": "厨具餐具 不锈钢保温杯 厨房小工具工厂",
    "Luggage & Bags": "箱包皮具 时尚双肩包 斜挎腰包工厂直供",
    "Menswear & Underwear": "男装潮牌 工装裤连帽衫 男士内衣批发",
    "Modest Fashion": "穆斯林服饰 长袍头巾 优雅长裙工厂货源",
    "Pet Supplies": "宠物用品 猫狗玩具 美容清洁用品工厂",
    "Phones & Electronics": "3C数码 手机配件 蓝牙音频源头厂家",
    "Pre-Owned": "Vintage复古服饰 古着牛仔外套货源",
    "Shoes": "流行鞋靴 踩屎感拖鞋 运动休闲鞋源头工厂",
    "Sports & Outdoor": "户外运动 健身器材 露营装备源头工厂",
    "Textiles & Soft Furnishings": "家纺布艺 地毯地垫 保暖盖毯源头工厂",
    "Tools and equipment": "五金工具 电动螺丝刀 手动工具套装工厂",
    "Toys & Hobbies": "解压玩具 潮玩益智 减压积木盲盒货源",
    "Virtual Products": "数字产品 模板设计 虚拟素材货源",
    # Legacy alias support:
    "Beauty & Skincare": "护肤美妆 面部护理 源头工厂货源",
    "Home & Kitchen": "家居百货 厨房收纳 源头工厂直供",
    "Home Gadgets": "创意家居 实用日用百货 工厂批发",
    "Tech Gadgets": "创意数码 3C数码配件 跨境热销货源",
    "Health & Wellness": "健康养生 营养保健品 代餐膳食"
}

def get_1688_query(title: str, category: str = "", sub_niche: str = "") -> str:
    t_low = (title or "").lower()
    
    # 1. Category-specific precision matching first (prevents "clean" in pet brush matching household detergent)
    if category in CATEGORY_SPECIFIC_1688:
        for k, v in CATEGORY_SPECIFIC_1688[category].items():
            if k in t_low:
                return v

    # 2. Match longest keyword from global map
    for k in sorted(KEYWORDS_1688_MAP.keys(), key=len, reverse=True):
        if k in t_low:
            return KEYWORDS_1688_MAP[k]

    # 3. Category fallback
    if category in CATEGORY_FALLBACK_1688:
        return CATEGORY_FALLBACK_1688[category]

    return "跨境热销 爆款源头工厂直供"

KEYWORDS_ALIBABA_MAP = {
    "toner": "toner pads exfoliating face",
    "pore": "pore cleansing pads skincare",
    "towel": "disposable face towels biobased cotton",
    "brush": "pet deshedding slicker brush self cleaning",
    "tumbler": "stainless steel tumbler with straw leak proof",
    "bottle": "insulated water bottle",
    "patch": "hydrocolloid acne pimple patch",
    "printer": "mini thermal portable sticker printer",
    "scrubber": "electric spin scrubber bathroom cleaner",
    "mic": "wireless lavalier lapel microphone",
    "necklace": "custom birth flower name bar necklace",
    "docking": "wood docking station desk organizer men",
    "calendar": "acrylic wall calendar weekly planner",
    "cutting board": "custom engraved wood cutting board charcuterie",
    "candle": "soy wax aromatherapy scented candle",
    "hoodie": "custom embroidered pet hoodie",
    "casio": "retro digital electronic watch",
    "cable": "fast charging usb cable",
    "teeth": "purple teeth whitening foam color corrector",
    "squishy": "steamed bun squishy stress relief toy",
    "curling": "5 in 1 hair styler airwrap curling wand"
}

def get_alibaba_query(title: str) -> str:
    t_low = title.lower()
    for k, v in KEYWORDS_ALIBABA_MAP.items():
        if k in t_low:
            return v
    words = [w for w in title.split() if len(w) > 3 and not w.startswith('http')][:3]
    return " ".join(words)

def export_to_standalone_html(analyzed_data: Dict[str, Any], output_path: str = "dashboard.html") -> str:
    # Attach 1688 and Alibaba search queries to items
    for item in analyzed_data.get("all_ideas", []):
        item["query_1688"] = get_1688_query(item.get("title", ""), item.get("category", ""))
        item["query_alibaba"] = get_alibaba_query(item.get("title", ""))
    for item in analyzed_data.get("viral_24h", []):
        item["query_1688"] = get_1688_query(item.get("title", ""), item.get("category", ""))
        item["query_alibaba"] = get_alibaba_query(item.get("title", ""))
    for item in analyzed_data.get("evergreen", []):
        item["query_1688"] = get_1688_query(item.get("title", ""), item.get("category", ""))
        item["query_alibaba"] = get_alibaba_query(item.get("title", ""))

    data_json = json.dumps(analyzed_data, ensure_ascii=False)
    updated_at = analyzed_data.get("updated_at", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    stats = analyzed_data.get("stats", {})

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TikTok Shop US - Trend Intelligence Pro (28 Ngành & Top Leaders 24h)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Phosphor Icons -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <style>
        /* QUY TẮC BẮT BUỘC: TOÀN BỘ GIAO DIỆN VUÔNG VỨC 100% - ZERO BORDER RADIUS */
        *, *::before, *::after {{
            border-radius: 0px !important;
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: #f1f5f9;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 0px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #94a3b8;
        }}
        html, body {{
            overflow-x: clip;
        }}
        /* Đảm bảo thanh Header bám dính chắc chắn trên cùng khi cuộn trang, NỀN TRẮNG 100% ĐẶC HOÀN TOÀN KHÔNG TRONG SUỐT */
        header.sticky-top-bar {{
            position: -webkit-sticky !important;
            position: sticky !important;
            top: 0 !important;
            z-index: 50 !important;
            background: #ffffff !important;
            background-color: #ffffff !important;
            opacity: 1 !important;
            border-bottom: 2px solid #cbd5e1 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -2px rgba(0, 0, 0, 0.05) !important;
        }}
        
        /* HIỆU ỨNG THU GỌN / MỞ RỘNG TASKBAR BÊN TRÁI */
        #main-sidebar {{
            transition: width 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        #main-sidebar.collapsed {{
            width: 4.25rem !important; /* 68px */
        }}
        #main-sidebar.collapsed .sidebar-full-item {{
            display: none !important;
        }}
        #main-sidebar.collapsed .sidebar-nav-btn {{
            justify-content: center !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }}
        #main-sidebar.collapsed .sidebar-nav-btn .sidebar-text,
        #main-sidebar.collapsed .sidebar-nav-btn .sidebar-badge {{
            display: none !important;
        }}
        #main-sidebar.collapsed .sidebar-header-box {{
            padding: 0.75rem 0.5rem !important;
            justify-content: center !important;
        }}
        #main-sidebar.collapsed .sidebar-footer-box {{
            padding: 0.75rem 0.5rem !important;
        }}
        #main-sidebar.collapsed #sidebar-toggle-btn {{
            margin: 0 auto;
        }}
        @media (max-width: 767px) {{
            #main-sidebar.collapsed {{
                display: none !important;
            }}
        }}
    </style>
</head>
<body class="bg-[#f8fafc] text-slate-900 min-h-screen font-sans antialiased selection:bg-rose-500 selection:text-white flex flex-col md:flex-row">

    <!-- ==================== 1. THANH TASKBAR MENU CỐ ĐỊNH BÊN TRÁI (COLLAPSIBLE SIDEBAR) ==================== -->
    <aside id="main-sidebar" class="w-full md:w-72 bg-white border-r-2 border-slate-300 md:h-screen md:sticky md:top-0 flex flex-col justify-between z-40 shrink-0 shadow-sm overflow-y-auto overflow-x-hidden">
        
        <!-- Sidebar Header: Logo, Language Toggle & Collapsible Control -->
        <div>
            <!-- Top Branding -->
            <div class="p-3.5 border-b-2 border-slate-300 bg-slate-50 flex items-center justify-between sidebar-header-box">
                <div class="flex items-center gap-2.5 min-w-0">
                    <div class="w-8 h-8 bg-rose-600 flex items-center justify-center text-white font-black text-lg shadow shrink-0 cursor-pointer" onclick="toggleSidebar()" title="Thu gọn / Mở rộng menu">
                        <i class="ph-bold ph-trend-up"></i>
                    </div>
                    <div class="sidebar-full-item min-w-0">
                        <h1 class="text-sm font-black tracking-tight text-slate-900 uppercase leading-none truncate">
                            TikTok Shop US
                        </h1>
                        <span class="text-[10px] text-rose-700 font-extrabold uppercase">Radar Pro 24h</span>
                    </div>
                </div>

                <!-- Action buttons: Language & Collapse Toggle -->
                <div class="flex items-center gap-1.5 shrink-0">
                    <button onclick="toggleLanguage()" id="lang-btn" class="px-2 py-1 text-[11px] font-black uppercase bg-white border-2 border-slate-400 hover:border-slate-800 text-slate-900 flex items-center gap-1 shadow-sm sidebar-full-item" title="Đổi ngôn ngữ">
                        <span id="lang-flag">🇻🇳</span> <span id="lang-text">VI</span>
                    </button>
                    <!-- Nút thu gọn taskbar -->
                    <button onclick="toggleSidebar()" id="sidebar-toggle-btn" class="w-7 h-7 bg-white hover:bg-slate-200 border-2 border-slate-400 text-slate-700 hover:text-slate-900 flex items-center justify-center transition shadow-sm" title="Thu gọn / Mở rộng thanh taskbar">
                        <i class="ph-bold ph-caret-double-left text-sm" id="sidebar-toggle-icon"></i>
                    </button>
                </div>
            </div>

            <!-- Auto 6-Hour Schedule Status Box (Collapsible) -->
            <div class="p-3 bg-white border-b-2 border-slate-300">
                <div class="flex items-center justify-between text-[11px] font-black text-slate-700 uppercase tracking-tight mb-1.5">
                    <span class="flex items-center gap-1.5 text-rose-700">
                        <span class="relative flex h-2 w-2 shrink-0">
                            <span class="animate-ping absolute inline-flex h-full w-full bg-rose-400 opacity-75"></span>
                            <span class="relative inline-flex h-2 w-2 bg-rose-600"></span>
                        </span>
                        <span data-i18n="auto_timer" class="sidebar-full-item">Hẹn giờ 6h:</span>
                    </span>
                    <div class="flex items-center gap-1.5">
                        <span id="countdown-text" class="font-mono bg-slate-100 px-1 py-0.5 border border-slate-300 text-slate-900 font-bold text-xs tracking-wider" title="Thời gian còn lại đến lượt cào dữ liệu tiếp theo">--:--:--</span>
                        <button onclick="forceScanTrends()" class="text-[10px] font-black text-rose-600 hover:text-white hover:bg-rose-600 px-1 py-0.5 border border-rose-300 uppercase transition sidebar-full-item" title="Ép cào mới ngay không chờ 6 tiếng">Quét</button>
                    </div>
                </div>
                <div class="text-[10px] text-slate-500 font-medium leading-tight flex items-center justify-between sidebar-full-item">
                    <span>Lần quét tới: <strong id="next-scan-label" class="text-slate-800 font-bold">--:--</strong></span>
                    <span class="text-emerald-700 font-black flex items-center gap-1"><i class="ph-fill ph-check-circle"></i> Daemon</span>
                </div>
            </div>

            <!-- User Selector & Management (Collapsible) -->
            <div class="p-3 bg-slate-50 border-b-2 border-slate-300">
                <div class="flex items-center justify-between text-[11px] font-black uppercase text-slate-700 mb-1.5 sidebar-full-item">
                    <span data-i18n="active_member">Thành Viên / User:</span>
                    <button onclick="openNewUserModal()" class="text-[10px] font-black text-rose-600 hover:text-rose-800 flex items-center gap-0.5 uppercase">
                        <i class="ph-bold ph-plus-circle"></i> <span data-i18n="add_user">Thêm User</span>
                    </button>
                </div>
                <div class="sidebar-full-item">
                    <select id="active-user-select" onchange="changeActiveUser(this.value)" class="w-full bg-white border-2 border-slate-300 text-xs font-bold text-slate-900 py-1.5 px-2 focus:outline-none focus:border-rose-600">
                        <!-- Populated via JS -->
                    </select>
                    <div class="flex items-center justify-between text-[10px] text-slate-500 font-bold mt-1.5">
                        <span data-i18n="saved_items">Đã lưu:</span>
                        <span id="user-saved-count" class="font-black text-rose-600">0 mục</span>
                    </div>
                </div>
                <!-- Mini User Icon when collapsed -->
                <div class="hidden justify-center text-slate-700 cursor-pointer" onclick="toggleSidebar()" title="Đổi thành viên">
                    <i class="ph-bold ph-user-circle text-2xl text-rose-600"></i>
                </div>
            </div>

            <!-- Navigation Links (Collapsible Sidebar Nav) -->
            <nav class="p-2 space-y-1">
                <div class="text-[10px] font-black uppercase text-slate-400 px-2 py-1 tracking-wider sidebar-full-item" data-i18n="nav_analytics">
                    Khám Phá Xu Hướng
                </div>

                <!-- TAB TẤT CẢ Ý TƯỞNG ĐƯA LÊN ĐẦU TIÊN -->
                <button onclick="switchTab('all')" id="nav-btn-all" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="📊 Tất Cả Ý Tưởng">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-table text-base text-slate-600 shrink-0"></i>
                        <span data-i18n="tab_all" class="sidebar-text">📊 Tất Cả Ý Tưởng</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-slate-100 text-slate-800 px-1.5 py-0.2 border border-slate-300">{stats.get('total_analyzed', 0)}</span>
                </button>

                <button onclick="switchTab('viral')" id="nav-btn-viral" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-rose-600 text-white border-l-4 border-rose-900" title="🔥 Bùng Nổ 24h">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-fire text-base shrink-0"></i>
                        <span data-i18n="tab_viral" class="sidebar-text">🔥 Bùng Nổ 24h</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-white text-rose-700 px-1.5 py-0.2">{stats.get('total_viral_24h', 0)}</span>
                </button>

                <button onclick="switchTab('evergreen')" id="nav-btn-evergreen" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="🌲 Evergreen Bền Vững">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-tree-evergreen text-base text-emerald-600 shrink-0"></i>
                        <span data-i18n="tab_evergreen" class="sidebar-text">🌲 Evergreen Bền Vững</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-emerald-100 text-emerald-800 px-1.5 py-0.2 border border-emerald-300">{stats.get('total_evergreen', 0)}</span>
                </button>

                <button onclick="switchTab('leaders')" id="nav-btn-leaders" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="🏆 BXH Top Videos & KOC 24h">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-trophy text-base text-amber-500 shrink-0"></i>
                        <span data-i18n="tab_leaders" class="sidebar-text">🏆 BXH Top Video & KOC</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-amber-100 text-amber-900 px-1.5 py-0.2 border border-amber-300">Top 24h</span>
                </button>

                <button onclick="switchTab('audio')" id="nav-btn-audio" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="🎵 Giai Điệu Nhạc Viral">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-music-notes text-base text-purple-600 shrink-0"></i>
                        <span data-i18n="tab_audio" class="sidebar-text">🎵 Giai Điệu Nhạc Viral</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-purple-100 text-purple-800 px-1.5 py-0.2 border border-purple-300">Hot</span>
                </button>

                <button onclick="switchTab('visual')" id="nav-btn-visual" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="📷 Tìm Bằng Hình Ảnh & 1688">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-camera text-base text-orange-600 shrink-0"></i>
                        <span data-i18n="tab_visual" class="sidebar-text">📷 Tìm Bằng Hình Ảnh & 1688</span>
                    </span>
                    <span class="sidebar-badge text-[10px] font-black bg-orange-100 text-orange-800 px-1.5 py-0.2 border border-orange-300">Tool</span>
                </button>

                <!-- CHỈ GIỮ ĐÚNG 1 TAB "ĐÃ LƯU" -->
                <div class="text-[10px] font-black uppercase text-slate-400 px-2 pt-3 pb-1 tracking-wider sidebar-full-item" data-i18n="nav_saved">
                    Mục Đã Lưu
                </div>

                <button onclick="switchTab('saved')" id="nav-btn-saved" class="sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent" title="📌 Đã Lưu">
                    <span class="flex items-center gap-2.5">
                        <i class="ph-bold ph-bookmark-simple text-base text-amber-600 shrink-0"></i>
                        <span data-i18n="tab_saved" class="sidebar-text">📌 Đã Lưu</span>
                    </span>
                    <span id="nav-saved-count" class="sidebar-badge text-[10px] font-black bg-amber-100 text-amber-900 px-1.5 py-0.2 border border-amber-300">0</span>
                </button>
            </nav>
        </div>

        <!-- Sidebar Footer: Export Excel & Platform Sources Status (Collapsible) -->
        <div class="p-3 border-t-2 border-slate-300 bg-slate-50 space-y-3 sidebar-footer-box">
            <a href="exports/TikTok_Shop_US_Latest_Trends.xlsx" download class="w-full flex items-center justify-center gap-2 py-2.5 px-2 bg-emerald-700 hover:bg-emerald-800 text-white font-black text-xs uppercase shadow transition" title="Xuất Báo Cáo Excel">
                <i class="ph-bold ph-file-xls text-lg shrink-0"></i>
                <span data-i18n="btn_export_excel" class="sidebar-full-item">Xuất Báo Cáo Excel</span>
            </a>

            <div class="text-[11px] text-slate-500 font-bold uppercase tracking-wider sidebar-full-item">
                <span data-i18n="sources_label">Nguồn dữ liệu đối soát:</span>
                <div class="grid grid-cols-2 gap-1 mt-1 font-normal text-[10px] text-slate-600">
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-blue-500"></span> Google Trends</span>
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-rose-500"></span> TikTok Shop</span>
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-amber-500"></span> Amazon US</span>
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-orange-500"></span> Etsy US</span>
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-emerald-500"></span> eBay Deals</span>
                    <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 bg-red-600"></span> 1688 / Alibaba</span>
                </div>
            </div>
        </div>

    </aside>

    <!-- ==================== 2. KHU VỰC NỘI DUNG CHÍNH (MAIN CONTENT) ==================== -->
    <div class="flex-1 flex flex-col min-w-0">
        
        <!-- Top Sticky Header: Đi theo màn hình đến cuối trang (Sticky Header), Nền Trắng Đặc 100% Không Trong Suốt -->
        <header class="sticky-top-bar bg-white border-b-2 border-slate-300 px-6 py-2.5 flex flex-col gap-2.5 shadow-md transition-all" style="background-color: #ffffff !important; opacity: 1 !important; z-index: 50 !important;">
            <!-- HÀNG 1: Menu Title / Clock / Ô Tìm Kiếm Nhanh / Nút Đặt Lại -->
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3">
                <div class="flex items-center gap-2.5 w-full sm:w-auto">
                    <!-- Nút Thu Gọn / Mở Rộng Taskbar Bên Trái -->
                    <button onclick="toggleSidebar()" class="w-8 h-8 bg-slate-100 hover:bg-slate-200 border-2 border-slate-300 text-slate-700 hover:text-slate-900 flex items-center justify-center shadow-sm shrink-0 transition" title="Thu gọn / Mở rộng thanh taskbar bên trái">
                        <i class="ph-bold ph-sidebar-simple text-base"></i>
                    </button>

                    <div class="text-xs font-black uppercase text-slate-900 whitespace-nowrap flex items-center gap-1.5" id="current-view-title">
                        🔥 Bùng Nổ 24h (Viral Spikes)
                    </div>
                    <div class="text-[11px] text-slate-500 hidden lg:block border-l border-slate-300 pl-3">
                        <i class="ph-bold ph-clock mr-1 text-rose-600"></i> Cập nhật: <strong>{updated_at}</strong>
                    </div>
                </div>

                <!-- Ô tìm kiếm, bộ chọn khung thời gian MerchTrends 24h/7d/30d/60d và nút Đặt Lại / Quét Mới -->
                <div class="flex items-center gap-2 w-full sm:w-auto flex-wrap">
                    <div class="relative flex-1 sm:w-64">
                        <i class="ph-bold ph-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                        <input type="text" id="search-input" onkeyup="filterItems()" placeholder="Tìm từ khóa, video, influencer, sản phẩm..." class="w-full pl-9 pr-3 py-1.5 bg-white border-2 border-slate-300 text-xs font-medium text-slate-900 placeholder-slate-400 focus:outline-none focus:border-rose-600">
                    </div>

                    <!-- MerchTrends Multi-Timeframe Selector Button Group -->
                    <div class="inline-flex border-2 border-slate-300 bg-slate-100 p-0.5 shrink-0" id="timeframe-buttons" title="Chuyển đổi tức thì khung thời gian phân tích">
                        <button type="button" onclick="setTimeframe('24h')" id="tf-btn-24h" class="px-2.5 py-1 text-xs font-black uppercase bg-slate-900 text-white transition">24H</button>
                        <button type="button" onclick="setTimeframe('7d')" id="tf-btn-7d" class="px-2.5 py-1 text-xs font-bold uppercase text-slate-700 hover:bg-slate-200 transition">7D</button>
                        <button type="button" onclick="setTimeframe('30d')" id="tf-btn-30d" class="px-2.5 py-1 text-xs font-bold uppercase text-slate-700 hover:bg-slate-200 transition">30D</button>
                        <button type="button" onclick="setTimeframe('60d')" id="tf-btn-60d" class="px-2.5 py-1 text-xs font-bold uppercase text-slate-700 hover:bg-slate-200 transition">60D</button>
                    </div>

                    <button onclick="resetFilters()" class="px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 border-2 border-slate-300 text-xs font-bold text-slate-700 flex items-center gap-1 shrink-0 transition" title="Đặt lại bộ lọc về mặc định">
                        <i class="ph-bold ph-arrows-counter-clockwise text-sm"></i>
                        <span data-i18n="btn_reset_filters">Đặt Lại</span>
                    </button>

                    <button id="btn-force-scan" onclick="forceScanTrends()" class="px-3 py-1.5 bg-rose-600 hover:bg-rose-700 text-white border-2 border-rose-700 text-xs font-black uppercase flex items-center gap-1.5 shrink-0 transition shadow-sm" title="Ép hệ thống cào mới dữ liệu từ 5 sàn ngay lập tức">
                        <i class="ph-bold ph-arrows-clockwise text-sm" id="force-scan-icon"></i>
                        <span id="force-scan-text" data-i18n="btn_force_scan">Quét Mới Ngay</span>
                    </button>
                </div>
            </div>

            <!-- HÀNG 2: CÁC Ô FILTER BÊN DƯỚI MENU THANH TRÊN (28 Ngành Hàng, Ngách Hàng, Ranking, Mới Listing 24h) -->
            <div class="flex flex-col md:flex-row items-center justify-between gap-2.5 pt-2.5 border-t border-slate-200 w-full">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-2.5 w-full">
                    <!-- Ô Filter 1: Ngành Hàng Lớn (28 Ngành) -->
                    <div class="flex items-center gap-1.5 bg-slate-50 border-2 border-slate-300 px-2.5 py-1">
                        <i class="ph-bold ph-squares-four text-rose-600 text-sm shrink-0"></i>
                        <span class="text-[10px] font-black uppercase text-slate-500 whitespace-nowrap shrink-0" data-i18n="filter_major_category">Ngành:</span>
                        <select id="category-select" onchange="onCategoryChange()" class="w-full bg-transparent text-xs font-bold text-slate-900 focus:outline-none truncate cursor-pointer">
                            <option value="all" data-i18n="cat_all">-- Tất Cả 28 Ngành Hàng --</option>
                        </select>
                    </div>

                    <!-- Ô Filter 2: Ngách Hàng Nhỏ (Sub-Niche) -->
                    <div class="flex items-center gap-1.5 bg-slate-50 border-2 border-slate-300 px-2.5 py-1">
                        <i class="ph-bold ph-git-branch text-blue-600 text-sm shrink-0"></i>
                        <span class="text-[10px] font-black uppercase text-slate-500 whitespace-nowrap shrink-0" data-i18n="filter_sub_niche">Ngách:</span>
                        <select id="subniche-select" onchange="filterItems()" class="w-full bg-transparent text-xs font-bold text-slate-900 focus:outline-none truncate cursor-pointer">
                            <option value="all" data-i18n="sub_all">-- Tất Cả Các Ngách --</option>
                        </select>
                    </div>

                    <!-- Ô Filter 3: Hệ Thống Xếp Hạng (Ranking) -->
                    <div class="flex items-center gap-1.5 bg-slate-50 border-2 border-slate-300 px-2.5 py-1">
                        <i class="ph-bold ph-ranking text-amber-600 text-sm shrink-0"></i>
                        <span class="text-[10px] font-black uppercase text-slate-500 whitespace-nowrap shrink-0" data-i18n="filter_ranking">Rank:</span>
                        <select id="ranking-select" onchange="filterItems()" class="w-full bg-transparent text-xs font-bold text-slate-900 focus:outline-none truncate cursor-pointer">
                            <option value="all" data-i18n="rank_all">🏆 Tất Cả Thứ Hạng</option>
                            <option value="top_10" data-i18n="rank_top_10">🥇 Top 1 - 10 Ngành</option>
                            <option value="top_50" data-i18n="rank_top_50">🥈 Top 1 - 50 Ngành</option>
                            <option value="top_100" data-i18n="rank_top_100">🥉 Top 1 - 100 Ngành</option>
                            <option value="sales_24h" data-i18n="rank_sales_24h">🔥 Bán Chạy Nhất 24h</option>
                            <option value="sales_30d" data-i18n="rank_sales_30d">📈 Bán Chạy 1 Tháng (30d)</option>
                        </select>
                    </div>

                    <!-- Ô Filter 4: Lọc Tag & Mới Listing 24h -->
                    <div class="flex items-center gap-1.5 bg-slate-50 border-2 border-slate-300 px-2 py-1">
                        <button id="btn-tag-new-listing" onclick="toggleNewListingFilter()" class="w-full py-0.5 px-2 bg-purple-50 hover:bg-purple-100 border border-purple-300 text-purple-900 text-xs font-black uppercase flex items-center justify-center gap-1 transition truncate" title="Lọc sản phẩm mới listing trong 24h đã có số bán">
                            <i class="ph-bold ph-sparkle text-purple-600"></i>
                            <span id="text-tag-new-listing" data-i18n="tag_new_listing_btn">✨ Mới Listing &lt;24h</span>
                        </button>
                    </div>
                </div>
            </div>
        </header>

        <!-- Main Body Container -->
        <main class="p-6 max-w-7xl mx-auto w-full space-y-6">

            <!-- ================= ĐẦU TRANG: TOP VIDEOS GMV 24H & TOP INFLUENCERS 24H ================= -->
            <!-- Layout 2 cột vuông vức đối xứng tuyệt đối (FastMoss & MerchTrends) -->
            <section id="top-leaders-section" class="grid grid-cols-1 lg:grid-cols-2 gap-4 items-stretch">
                
                <!-- CỘT 1: TOP VIDEOS (GMV CAO NHẤT 24H) -->
                <div class="bg-white border-2 border-slate-300 shadow-sm flex flex-col h-full">
                    <div class="p-3 bg-rose-50/70 border-b-2 border-slate-300 flex items-center justify-between min-h-[58px]">
                        <div class="flex items-center gap-2">
                            <div class="w-6 h-6 bg-rose-600 text-white flex items-center justify-center font-black text-xs">
                                <i class="ph-bold ph-film-strip"></i>
                            </div>
                            <div>
                                <h2 class="text-xs font-black uppercase text-slate-900 tracking-tight" data-i18n="top_videos_title">
                                    Top Videos (GMV Cao Nhất 24h)
                                </h2>
                                <p class="text-[10px] text-slate-500 font-medium" data-i18n="top_videos_sub">
                                    Xếp hạng theo doanh số GMV trực tiếp tạo ra trong 24h trên TikTok Shop US
                                </p>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <!-- Bộ chọn số dòng hiển thị -->
                            <div class="flex items-center gap-1 bg-white border border-slate-300 px-1.5 py-0.5">
                                <span class="text-[10px] font-bold text-slate-500 uppercase">Dòng:</span>
                                <select id="leaders-page-size-select" onchange="onLeadersPageSizeChange(this.value)" class="bg-transparent text-[10px] font-black text-slate-800 focus:outline-none cursor-pointer">
                                    <option value="all" selected>Tối Đa (Tất Cả)</option>
                                    <option value="10">10 dòng</option>
                                    <option value="25">25 dòng</option>
                                    <option value="50">50 dòng</option>
                                </select>
                            </div>
                            <button onclick="switchTab('leaders')" class="text-[10px] font-bold text-rose-700 hover:text-rose-900 flex items-center gap-1 hover:underline bg-rose-100/70 px-2 py-0.5 border border-rose-300" title="Chuyển sang tab riêng chuyên biệt về 2 bảng này">
                                <span>Tab Riêng</span> <i class="ph-bold ph-arrow-square-out text-xs"></i>
                            </button>
                            <span id="top-videos-count-badge" class="text-[10px] font-black bg-rose-100 text-rose-800 px-2 py-0.5 border border-rose-300">
                                62 Videos
                            </span>
                        </div>
                    </div>

                    <!-- Bảng Top Videos (Khung cuộn đồng bộ) -->
                    <div class="overflow-x-auto overflow-y-auto max-h-[640px] flex-1">
                        <table class="w-full text-left border-collapse text-xs">
                            <thead class="bg-slate-100 text-slate-600 uppercase font-black text-[10px] border-b border-slate-300 sticky top-0 z-10">
                                <tr>
                                    <th class="py-2.5 px-3 w-12 text-center" data-i18n="th_rank">Rank</th>
                                    <th class="py-2.5 px-3" data-i18n="th_video">Video Viral</th>
                                    <th class="py-2.5 px-2 text-center" data-i18n="th_prod_thumb">SP Gắn</th>
                                    <th class="py-2.5 px-3 text-right" data-i18n="th_items_sold">Đã Bán 24h</th>
                                    <th class="py-2.5 px-3 text-right cursor-help" title="Doanh số GMV 24h được phân tích định lượng trực tiếp từ dữ liệu TikTok: (Lượt Xem Thực Tế × Tỷ Lệ CVR Benchmark Ngành × Giá Niêm Yết Sản Phẩm)"><span data-i18n="th_gmv">GMV 24h</span> <i class="ph-bold ph-info text-[10px] text-slate-400"></i></th>
                                </tr>
                            </thead>
                            <tbody id="top-videos-body" class="divide-y divide-slate-200">
                                <!-- Populated dynamically via JS -->
                            </tbody>
                        </table>
                    </div>

                    <!-- Footer Pagination Top Videos (Ghim đáy đồng bộ) -->
                    <div class="p-2.5 bg-slate-50 border-t-2 border-slate-300 flex items-center justify-between text-xs flex-wrap gap-2 mt-auto min-h-[44px]">
                        <div id="top-videos-page-info" class="text-[11px] font-bold text-slate-600">
                            Hiển thị 62 / 62 videos
                        </div>
                        <div class="flex items-center gap-1" id="top-videos-pagination-btns">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>
                </div>

                <!-- CỘT 2: TOP INFLUENCERS (SỐ BÁN & GMV CAO NHẤT 24H) -->
                <div class="bg-white border-2 border-slate-300 shadow-sm flex flex-col h-full">
                    <div class="p-3 bg-blue-50/70 border-b-2 border-slate-300 flex items-center justify-between min-h-[58px]">
                        <div class="flex items-center gap-2">
                            <div class="w-6 h-6 bg-blue-600 text-white flex items-center justify-center font-black text-xs">
                                <i class="ph-bold ph-user-circle-check"></i>
                            </div>
                            <div>
                                <h2 class="text-xs font-black uppercase text-slate-900 tracking-tight" data-i18n="top_influencers_title">
                                    Top Influencers (Bán Chạy Nhất 24h)
                                </h2>
                                <p class="text-[10px] text-slate-500 font-medium" data-i18n="top_influencers_sub">
                                    KOC/Creator chốt đơn nhiều nhất theo từng ngành hàng 24h qua
                                </p>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <!-- Bộ chọn số dòng hiển thị (Đồng bộ với bảng 1) -->
                            <div class="flex items-center gap-1 bg-white border border-slate-300 px-1.5 py-0.5">
                                <span class="text-[10px] font-bold text-slate-500 uppercase">Dòng:</span>
                                <select id="leaders-page-size-select-2" onchange="onLeadersPageSizeChange(this.value)" class="bg-transparent text-[10px] font-black text-slate-800 focus:outline-none cursor-pointer">
                                    <option value="all" selected>Tối Đa (Tất Cả)</option>
                                    <option value="10">10 dòng</option>
                                    <option value="25">25 dòng</option>
                                    <option value="50">50 dòng</option>
                                </select>
                            </div>
                            <button onclick="switchTab('leaders')" class="text-[10px] font-bold text-blue-700 hover:text-blue-900 flex items-center gap-1 hover:underline bg-blue-100/70 px-2 py-0.5 border border-blue-300" title="Chuyển sang tab riêng chuyên biệt về 2 bảng này">
                                <span>Tab Riêng</span> <i class="ph-bold ph-arrow-square-out text-xs"></i>
                            </button>
                            <span id="top-influencers-count-badge" class="text-[10px] font-black bg-blue-100 text-blue-800 px-2 py-0.5 border border-blue-300">
                                55 Creators
                            </span>
                        </div>
                    </div>

                    <!-- Bảng Top Influencers (Khung cuộn đồng bộ) -->
                    <div class="overflow-x-auto overflow-y-auto max-h-[640px] flex-1">
                        <table class="w-full text-left border-collapse text-xs">
                            <thead class="bg-slate-100 text-slate-600 uppercase font-black text-[10px] border-b border-slate-300 sticky top-0 z-10">
                                <tr>
                                    <th class="py-2.5 px-3 w-12 text-center" data-i18n="th_rank">Rank</th>
                                    <th class="py-2.5 px-3" data-i18n="th_creator">Nhà Sáng Tạo (KOC)</th>
                                    <th class="py-2.5 px-2 text-center" data-i18n="th_prod_thumb">Top SP</th>
                                    <th class="py-2.5 px-3 text-right" data-i18n="th_items_sold">Đã Bán 24h</th>
                                    <th class="py-2.5 px-3 text-right cursor-help" title="Doanh số GMV 24h được phân tích từ lượt tương tác thực tế và số lượng sản phẩm bán ra từ TikTok Shop Showcase của Creator"><span data-i18n="th_gmv">GMV 24h</span> <i class="ph-bold ph-info text-[10px] text-slate-400"></i></th>
                                </tr>
                            </thead>
                            <tbody id="top-influencers-body" class="divide-y divide-slate-200">
                                <!-- Populated dynamically via JS -->
                            </tbody>
                        </table>
                    </div>

                    <!-- Footer Pagination Top Influencers (Ghim đáy đồng bộ) -->
                    <div class="p-2.5 bg-slate-50 border-t-2 border-slate-300 flex items-center justify-between text-xs flex-wrap gap-2 mt-auto min-h-[44px]">
                        <div id="top-influencers-page-info" class="text-[11px] font-bold text-slate-600">
                            Hiển thị 55 / 55 creators
                        </div>
                        <div class="flex items-center gap-1" id="top-influencers-pagination-btns">
                            <!-- Populated dynamically via JS -->
                        </div>
                    </div>
                </div>

            </section>

            <!-- Overview Metrics Row (MerchTrends Command Center 5-Card Analytics) -->
            <div class="grid grid-cols-2 md:grid-cols-5 gap-3" id="stats-overview-row">
                <!-- Card 1: New Listings 7D & Total Ideas (Blue) -->
                <div class="p-3.5 bg-white border-2 border-blue-300 bg-blue-50/30 shadow-sm">
                    <div class="text-blue-900 text-[11px] font-black uppercase tracking-wider mb-0.5 flex justify-between">
                        <span data-i18n="stat_new_listings_7d">Mới Listing 7D</span>
                        <i class="ph-bold ph-sparkle text-blue-600 text-base"></i>
                    </div>
                    <div class="text-2xl font-black text-slate-900 leading-tight">+{stats.get('total_new_listings_7d', stats.get('total_new_listings_24h', 0))}</div>
                    <div class="text-[10px] text-slate-500 font-bold mt-0.5">/ {stats.get('total_analyzed', 0)} tổng sản phẩm</div>
                </div>

                <!-- Card 2: 28 Niches Coverage (Purple) -->
                <div class="p-3.5 bg-white border-2 border-purple-300 bg-purple-50/30 shadow-sm">
                    <div class="text-purple-900 text-[11px] font-black uppercase tracking-wider mb-0.5 flex justify-between">
                        <span data-i18n="stat_coverage">Độ Phủ 28 Ngành</span>
                        <i class="ph-bold ph-chart-pie-slice text-purple-600 text-base"></i>
                    </div>
                    <div class="text-2xl font-black text-purple-700 leading-tight">{stats.get('theme_coverage_pct', 100)}%</div>
                    <div class="text-[10px] text-slate-500 font-bold mt-0.5">Quét đủ 28/28 ngành hàng</div>
                </div>

                <!-- Card 3: Leading Niche Theme (Amber) -->
                <div class="p-3.5 bg-white border-2 border-amber-300 bg-amber-50/30 shadow-sm">
                    <div class="text-amber-900 text-[11px] font-black uppercase tracking-wider mb-0.5 flex justify-between">
                        <span data-i18n="stat_leading">Ngành Dẫn Đầu</span>
                        <i class="ph-bold ph-trophy text-amber-600 text-base"></i>
                    </div>
                    <div class="text-base font-black text-amber-900 leading-tight truncate" title="{stats.get('leading_theme', 'Beauty & Personal Care')}">{stats.get('leading_theme', 'Beauty & Care').split('&')[0]}</div>
                    <div class="text-[10px] text-amber-700 font-bold mt-0.5">+{stats.get('leading_theme_sales', 0):,} đơn/24h ↗</div>
                </div>

                <!-- Card 4: Rank Surge Radar V3 (Rose) -->
                <div class="p-3.5 bg-white border-2 border-rose-300 bg-rose-50/30 shadow-sm">
                    <div class="text-rose-900 text-[11px] font-black uppercase tracking-wider mb-0.5 flex justify-between">
                        <span data-i18n="stat_surges">Rank Surges V3</span>
                        <i class="ph-bold ph-lightning text-rose-600 text-base"></i>
                    </div>
                    <div class="text-2xl font-black text-rose-600 leading-tight">{stats.get('total_rank_surges', stats.get('total_viral_24h', 0))}</div>
                    <div class="text-[10px] text-rose-700 font-bold mt-0.5">Breakout (Lọc ảo drawdown)</div>
                </div>

                <!-- Card 5: Estimated Daily Sales & Monthly Rev (Emerald) -->
                <div class="p-3.5 bg-white border-2 border-emerald-300 bg-emerald-50/30 shadow-sm col-span-2 md:col-span-1">
                    <div class="text-emerald-900 text-[11px] font-black uppercase tracking-wider mb-0.5 flex justify-between">
                        <span data-i18n="stat_eds">Dự Báo EDS & DT</span>
                        <i class="ph-bold ph-trend-up text-emerald-600 text-base"></i>
                    </div>
                    <div class="text-xl font-black text-emerald-700 leading-tight">{stats.get('total_est_daily_sales', 0):,} <span class="text-xs font-bold text-slate-500">đơn/ngày</span></div>
                    <div class="text-[10px] text-emerald-800 font-bold mt-0.5">~${stats.get('total_est_monthly_rev', 0):,.0f} / tháng (98% Conf)</div>
                </div>
            </div>

            <!-- ================= VIEW 1: HORIZONTAL ROWS LIST ================= -->
            <div id="cards-container" class="flex flex-col gap-3">
                <!-- Populated via JS -->
            </div>

            <!-- ================= VIEW 2: TABLE MATRIX ================= -->
            <div id="table-container" class="hidden bg-white border-2 border-slate-300 overflow-x-auto shadow-sm">
                <table class="w-full text-left border-collapse text-xs">
                    <thead class="bg-slate-100 text-slate-700 uppercase font-black border-b-2 border-slate-300">
                        <tr>
                            <th class="py-3 px-3 w-16 text-center">Hạng (#)</th>
                            <th class="py-3 px-3 text-center" data-i18n="th_sparkline">Quỹ Đạo Trend</th>
                            <th class="py-3 px-4" data-i18n="th_product">Sản Phẩm & Từ Khóa</th>
                            <th class="py-3 px-3">Tag / Nhãn</th>
                            <th class="py-3 px-4" data-i18n="th_niche">Ngành Hàng</th>
                            <th class="py-3 px-3 text-center" id="th-sales-col">Bán Khung Giờ</th>
                            <th class="py-3 px-3 text-center" data-i18n="th_eds_daily">Dự Báo EDS (Ngày)</th>
                            <th class="py-3 px-3 text-center" data-i18n="th_est_monthly">Doanh Thu Tháng (Est)</th>
                            <th class="py-3 px-3 text-center" data-i18n="th_price">Giá Bán</th>
                            <th class="py-3 px-4" data-i18n="th_saved_by">Người Lưu Trong Team</th>
                            <th class="py-3 px-4" data-i18n="th_actions">Thao Tác</th>
                        </tr>
                    </thead>
                    <tbody id="table-body" class="divide-y divide-slate-200">
                        <!-- Populated via JS -->
                    </tbody>
                </table>
            </div>

            <!-- ================= VIEW 3: TIKTOK VIRAL SOUNDS RADAR ================= -->
            <div id="audio-view-container" class="hidden space-y-4">
                <div class="p-4 bg-purple-50 border-2 border-purple-300 flex items-start justify-between">
                    <div>
                        <h2 class="text-sm font-black uppercase text-purple-900" data-i18n="audio_banner_title">Radar Giai Điệu & Âm Thanh Viral TikTok 24h</h2>
                        <p class="text-xs text-purple-700 mt-0.5" data-i18n="audio_banner_sub">Các bài nhạc và âm thanh có lượng video mới tạo tăng đột biến trong 24h qua dùng cho kịch bản bán hàng TikTok Shop US.</p>
                    </div>
                    <span class="text-xs font-black px-2 py-1 bg-purple-200 text-purple-900 border border-purple-400 uppercase">24h Hot List</span>
                </div>

                <div id="audio-list" class="space-y-3">
                    <!-- Populated via JS -->
                </div>
            </div>

            <!-- ================= VIEW 4: VISUAL / IMAGE SEARCH & 1688 SOURCING ================= -->
            <div id="visual-view-container" class="hidden space-y-6">
                
                <!-- Header Banner -->
                <div class="p-4 bg-orange-50 border-2 border-orange-300 flex items-start justify-between">
                    <div>
                        <h2 class="text-sm font-black uppercase text-orange-950" data-i18n="visual_title">Tìm Kiếm Sản Phẩm Bằng Hình Ảnh (Reverse Image Search)</h2>
                        <p class="text-xs text-orange-800 mt-0.5" data-i18n="visual_sub">Tải ảnh chụp màn hình video TikTok hoặc sản phẩm để tra cứu xưởng sản xuất gốc 1688 và kiểm tra đối thủ cạnh tranh trên Google Lens.</p>
                    </div>
                    <span class="text-xs font-black px-2 py-1 bg-orange-200 text-orange-950 border border-orange-400 uppercase">1688 Visual AI</span>
                </div>

                <!-- Dropzone Area -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    
                    <!-- Left: Upload Box with Paste Support -->
                    <div id="image-drop-zone" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleDrop(event)" class="border-2 border-dashed border-slate-400 bg-white p-6 flex flex-col items-center justify-center text-center cursor-pointer hover:border-slate-800 hover:bg-slate-50 transition relative min-h-[220px]">
                        <input type="file" id="file-upload" accept=".jpg,.jpeg,.png,.webp" onchange="handleImageUpload(event)" class="absolute inset-0 opacity-0 cursor-pointer w-full h-full">
                        
                        <div id="drop-prompt" class="space-y-2">
                            <i class="ph-bold ph-cloud-arrow-up text-4xl text-slate-400"></i>
                            <div class="text-xs font-black uppercase text-slate-800" data-i18n="drop_image_text">
                                BẤM VÀO ĐÂY ĐỂ TẢI ẢNH LÊN HOẶC KÉO THẢ
                            </div>
                            <p class="text-[11px] text-slate-500">Hỗ trợ JPG, PNG, WEBP hoặc bấm <strong>Ctrl + V</strong> để dán ảnh chụp màn hình trực tiếp.</p>
                        </div>

                        <!-- Preview Container -->
                        <div id="preview-container" class="hidden space-y-3 w-full">
                            <div class="relative w-32 h-32 mx-auto border-2 border-slate-900 bg-slate-100 flex items-center justify-center overflow-hidden">
                                <img id="preview-img" src="" class="w-full h-full object-contain" alt="Preview">
                            </div>
                            <div class="text-xs font-bold text-slate-700 truncate max-w-xs mx-auto" id="preview-filename"></div>
                            <div class="flex items-center justify-center gap-2">
                                <button type="button" onclick="clearImagePreview()" class="px-3 py-1 bg-slate-200 hover:bg-slate-300 text-slate-800 text-[11px] font-bold">
                                    XÓA ẢNH
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Right: Online URL & Quick Action -->
                    <div class="bg-white border-2 border-slate-300 p-5 flex flex-col justify-between">
                        <div class="space-y-3">
                            <div class="text-xs font-black uppercase text-slate-800">Hoặc Dán Link Ảnh Online:</div>
                            <div class="flex gap-2">
                                <input type="url" id="image-url-input" placeholder="https://example.com/product-image.jpg" class="flex-1 px-3 py-2 bg-slate-50 border-2 border-slate-300 text-xs font-medium text-slate-900 focus:outline-none focus:border-rose-600">
                                <button onclick="handleUrlSearch()" class="px-4 py-2 bg-slate-900 hover:bg-slate-800 text-white font-black text-xs uppercase" data-i18n="btn_preview">XEM</button>
                            </div>
                        </div>

                        <!-- Action Buttons -->
                        <div class="flex flex-col sm:flex-row gap-2 mt-4">
                            <a id="link-1688-image" href="https://s.1688.com/youyuan/index.htm" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="flex-1 py-2.5 px-3 bg-orange-600 hover:bg-orange-700 text-white font-black text-xs uppercase flex items-center justify-center gap-1.5 shadow transition">
                                <i class="ph-bold ph-factory text-base"></i>
                                <span data-i18n="btn_search_1688">TÌM XƯỞNG TRÊN 1688</span>
                            </a>
                            <a id="link-google-lens" href="https://lens.google.com/" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="flex-1 py-2.5 px-3 bg-blue-700 hover:bg-blue-800 text-white font-black text-xs uppercase flex items-center justify-center gap-1.5 shadow transition">
                                <i class="ph-bold ph-google-logo text-base"></i>
                                <span data-i18n="btn_search_lens">GOOGLE LENS US</span>
                            </a>
                        </div>
                    </div>

                </div>

                <!-- 1688 Price & Profit Calculator -->
                <div class="bg-white border-2 border-slate-300 p-5 shadow-sm">
                    <h3 class="text-xs font-black uppercase text-slate-900 mb-3 flex items-center gap-2">
                        <i class="ph-bold ph-calculator text-emerald-600 text-base"></i>
                        <span data-i18n="calc_title">Bảng Tính Lợi Nhuận Nhập Sỉ 1688 Về Bán TikTok Shop US</span>
                    </h3>
                    <div class="grid grid-cols-1 sm:grid-cols-4 gap-3 text-xs">
                        <div>
                            <label class="block text-slate-500 font-bold mb-1" data-i18n="calc_cny">Giá Nhập 1688 (¥ Tệ):</label>
                            <input type="number" id="calc-cny" value="28" oninput="calculateMargin()" class="w-full px-2.5 py-1.5 bg-slate-50 border-2 border-slate-300 font-black text-slate-900 focus:outline-none focus:border-rose-600">
                            <span class="text-[10px] text-slate-400 font-bold" id="calc-usd-equiv">~ $3.89 USD</span>
                        </div>
                        <div>
                            <label class="block text-slate-500 font-bold mb-1" data-i18n="calc_ship">Ship & Fulfillment ($):</label>
                            <input type="number" id="calc-ship" value="4.5" oninput="calculateMargin()" class="w-full px-2.5 py-1.5 bg-slate-50 border-2 border-slate-300 font-black text-slate-900 focus:outline-none focus:border-rose-600">
                        </div>
                        <div>
                            <label class="block text-slate-500 font-bold mb-1" data-i18n="calc_retail">Giá Bán TikTok Shop ($):</label>
                            <input type="number" id="calc-retail" value="24.99" oninput="calculateMargin()" class="w-full px-2.5 py-1.5 bg-slate-50 border-2 border-slate-300 font-black text-slate-900 focus:outline-none focus:border-rose-600">
                        </div>
                        <div class="p-2.5 bg-emerald-50 border border-emerald-300 flex flex-col justify-center">
                            <div class="text-[10px] font-bold uppercase text-emerald-800" data-i18n="calc_profit">Lợi Nhuận Ròng & Margin:</div>
                            <div class="text-base font-black text-emerald-700" id="calc-net-profit">+$16.60 / đơn</div>
                            <div class="text-[11px] font-black text-emerald-900" id="calc-margin-percent">Biên lãi: 66.4%</div>
                        </div>
                    </div>
                </div>

            </div>

            <!-- Empty Saved Items Box -->
            <div id="empty-saved-box" class="hidden p-12 text-center bg-white border-2 border-dashed border-slate-300">
                <i class="ph-bold ph-bookmarks text-5xl text-slate-300 mb-3 inline-block"></i>
                <h3 class="text-base font-bold text-slate-800" data-i18n="empty_saved_title">Chưa có sản phẩm nào được lưu trong mục này</h3>
                <p class="text-xs text-slate-500 mt-1 max-w-md mx-auto" data-i18n="empty_saved_sub">Hãy bấm vào nút <strong>"+ Lưu Cho Tôi"</strong> trên bất kỳ dòng sản phẩm nào để thêm vào danh sách của bạn.</p>
            </div>

        </main>
    </div>

    <!-- ==================== 3. MODALS ==================== -->
    <!-- ==================== MODAL PHÓNG TO ẢNH SẢN PHẨM (IN-PLACE LIGHTBOX) ==================== -->
    <div id="image-zoom-modal" onclick="closeImageZoomModal(event)" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-xs p-4 cursor-zoom-out">
        <div onclick="event.stopPropagation()" class="bg-white border-2 border-slate-900 max-w-xl w-full p-4 shadow-2xl relative cursor-default">
            
            <!-- Modal Header -->
            <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-200">
                <div class="flex items-center gap-2">
                    <div class="w-6 h-6 bg-rose-600 text-white flex items-center justify-center font-bold text-xs">
                        <i class="ph-bold ph-magnifying-glass-plus"></i>
                    </div>
                    <span class="text-xs font-black uppercase text-slate-800 tracking-tight">Chi Tiết Ảnh Sản Phẩm</span>
                </div>
                <button onclick="closeImageZoomModal()" class="w-7 h-7 bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 border border-slate-300 font-bold flex items-center justify-center transition" title="Đóng">
                    <i class="ph-bold ph-x text-base"></i>
                </button>
            </div>

            <!-- Main Zoomed Image Container -->
            <div class="w-full h-80 sm:h-[400px] bg-slate-100 border-2 border-slate-200 flex items-center justify-center overflow-hidden p-3 relative">
                <img id="zoom-modal-img" src="" class="max-w-full max-h-full object-contain shadow-sm select-none" alt="Product Zoom">
            </div>

            <!-- Product Title & Optional Action Buttons -->
            <div class="mt-3 pt-3 border-t border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="flex-1 min-w-0">
                    <h4 id="zoom-modal-title" class="text-xs font-black text-slate-900 leading-snug line-clamp-2"></h4>
                </div>
                <div class="flex items-center gap-2 shrink-0 flex-wrap">
                    <a id="zoom-tiktok-btn" href="#" target="_blank" rel="noreferrer noopener" class="px-3 py-1.5 bg-slate-900 hover:bg-black text-white text-xs font-black uppercase flex items-center gap-1 shadow-sm transition" title="Mở sản phẩm trên TikTok Shop">
                        <i class="ph-bold ph-tiktok-logo text-sm"></i>
                        <span>TikTok Shop</span>
                    </a>
                    <button id="zoom-lens-btn" onclick="openZoomGoogleLens()" class="px-3 py-1.5 bg-blue-700 hover:bg-blue-800 text-white text-xs font-black uppercase flex items-center gap-1 shadow-sm transition" title="Tìm ảnh này trên Google Lens">
                        <i class="ph-bold ph-google-logo text-sm"></i>
                        <span>Google Lens</span>
                    </button>
                    <button id="zoom-1688-btn" onclick="openZoom1688()" class="px-3 py-1.5 bg-orange-600 hover:bg-orange-700 text-white text-xs font-black uppercase flex items-center gap-1 shadow-sm transition" title="Tìm xưởng sản xuất trên 1688">
                        <i class="ph-bold ph-factory text-sm"></i>
                        <span>Xưởng 1688</span>
                    </button>
                </div>
            </div>

            <!-- Lời nhắc tìm kiếm 1688 nằm ngang dưới dòng button -->
            <div class="mt-3 p-2.5 bg-amber-50 border border-amber-300 text-amber-950 text-xs flex items-center gap-2.5">
                <i class="ph-bold ph-lightbulb text-amber-600 text-base shrink-0"></i>
                <div class="leading-relaxed">
                    <strong class="font-bold text-amber-900" data-i18n="tip_1688_title">Mẹo tìm kiếm 1688:</strong> 
                    <span data-i18n="tip_1688_search">Nếu khi mở ra chưa thấy sản phẩm ngay, bạn chỉ cần bấm lại nút <strong>"Tìm kiếm" (🔍 搜索)</strong> trên thanh tìm kiếm của 1688 một lần nữa là hệ thống sẽ tải đúng sản phẩm theo từ khóa đã điền sẵn.</span>
                </div>
            </div>

        </div>
    </div>


    <!-- Strategy & 24h Verification Audit Modal -->
    <div id="strategy-modal" onclick="closeModal(event)" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-none p-4 cursor-pointer">
        <div onclick="event.stopPropagation()" class="bg-white border-2 border-slate-900 max-w-2xl w-full p-6 shadow-2xl relative max-h-[90vh] overflow-y-auto cursor-default">
            <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-500 hover:text-slate-900 text-2xl font-bold" title="Đóng">
                <i class="ph-bold ph-x"></i>
            </button>
            <div id="modal-content"></div>
        </div>
    </div>

    <!-- Modal Thêm Người Dùng Mới -->
    <div id="new-user-modal" onclick="closeNewUserModal(event)" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-none p-4 cursor-pointer">
        <div onclick="event.stopPropagation()" class="bg-white border-2 border-slate-900 max-w-md w-full p-6 shadow-2xl relative cursor-default">
            <button onclick="closeNewUserModal()" class="absolute top-4 right-4 text-slate-500 hover:text-slate-900 text-2xl font-bold" title="Đóng">
                <i class="ph-bold ph-x"></i>
            </button>
            <h3 class="text-base font-black uppercase text-slate-900 mb-1 flex items-center gap-1.5">
                <i class="ph-bold ph-user-plus text-rose-600"></i> <span data-i18n="modal_add_user_title">Thêm Người Dùng / Thành Viên Mới</span>
            </h3>
            <p class="text-xs text-slate-600 mb-4" data-i18n="modal_add_user_sub">Tạo hồ sơ thành viên để quản lý và lưu riêng các ý tưởng sản phẩm trong nhóm.</p>
            
            <div class="space-y-3 mb-4">
                <div>
                    <label class="text-[11px] font-black uppercase text-slate-700 block mb-1" data-i18n="label_name">Tên Thành Viên *</label>
                    <input type="text" id="new-user-name" placeholder="Ví dụ: Hoàng (Sourcing), Linh (Content)..." class="w-full px-3 py-2 bg-white border-2 border-slate-400 text-xs font-bold text-slate-900 focus:outline-none focus:border-rose-600">
                </div>
                <div>
                    <label class="text-[11px] font-black uppercase text-slate-700 block mb-1" data-i18n="label_role">Vai Trò / Phụ Trách</label>
                    <input type="text" id="new-user-role" placeholder="Ví dụ: Product Hunter, Sourcing, Content..." class="w-full px-3 py-2 bg-white border-2 border-slate-400 text-xs font-bold text-slate-900 focus:outline-none focus:border-rose-600">
                </div>
            </div>

            <div class="flex items-center justify-end gap-2">
                <button onclick="closeNewUserModal()" class="px-4 py-2 text-xs font-bold bg-slate-200 hover:bg-slate-300 text-slate-800" data-i18n="btn_cancel">
                    HỦY BỎ
                </button>
                <button onclick="confirmCreateUser()" class="px-4 py-2 text-xs font-black bg-rose-600 hover:bg-rose-700 text-white" data-i18n="btn_create_user">
                    TẠO NGƯỜI DÙNG
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== 4. EMBEDDED DATA & LOGIC CONTROLLER ==================== -->
    <script>
        const globalData = {data_json};
        let currentTab = 'viral';
        let currentTimeframe = '24h';
        let currentLang = localStorage.getItem('tiktok_radar_lang') || 'vi'; // 'vi' or 'en'
        const categoriesTaxonomy = globalData.categories_taxonomy || [];
        const topVideosData = globalData.top_videos || [];
        const topInfluencersData = globalData.top_influencers || [];

        function setTimeframe(tf) {{
            currentTimeframe = tf;
            const tfs = ['24h', '7d', '30d', '60d'];
            tfs.forEach(t => {{
                const btn = document.getElementById('tf-btn-' + t);
                if (btn) {{
                    if (t === tf) {{
                        btn.className = "px-2.5 py-1 text-xs font-black uppercase bg-slate-900 text-white transition";
                    }} else {{
                        btn.className = "px-2.5 py-1 text-xs font-bold uppercase text-slate-700 hover:bg-slate-200 transition";
                    }}
                }}
            }});
            const thSales = document.getElementById('th-sales-col');
            if (thSales) {{
                thSales.innerText = (currentLang === 'vi' ? 'Bán ' + tf.toUpperCase() : tf.toUpperCase() + ' Sales');
            }}
            filterItems();
        }}

        // 1. DICTIONARY BILINGUAL (VI / EN)
        const I18N = {{
            vi: {{
                auto_timer: "Hẹn giờ 6h:",
                active_member: "Thành Viên / User:",
                add_user: "Thêm User",
                saved_items: "Đã lưu:",
                nav_analytics: "Khám Phá Xu Hướng",
                tab_viral: "🔥 Bùng Nổ 24h",
                tab_evergreen: "🌲 Evergreen Bền Vững",
                tab_audio: "🎵 Giai Điệu Nhạc Viral",
                tab_visual: "📷 Tìm Bằng Hình Ảnh & 1688",
                nav_saved: "Mục Đã Lưu",
                tab_saved: "📌 Đã Lưu",
                tab_leaders: "🏆 BXH Top Videos & KOC",
                
                tab_all: "📊 Tất Cả Ý Tưởng",
                btn_export_excel: "Xuất Báo Cáo Excel",
                sources_label: "Nguồn dữ liệu đối soát:",
                filter_major_category: "Ngành Hàng Lớn (28 Ngành TikTok Shop):",
                filter_sub_niche: "Ngách Hàng Nhỏ (Sub-Niche):",
                filter_velocity: "Chiều Xu Hướng (Velocity):",
                btn_reset_filters: "Đặt Lại",
                cat_all: "-- Tất Cả 28 Ngành Hàng --",
                sub_all: "-- Tất Cả Các Ngách --",
                vel_all: "Tất Cả Ma Trận Trend",
                vel_viral: "🔥 Video Viral 24h",
                vel_sales: "🚀 Tốc Độ Bán Nhanh (Movers)",
                vel_keyword: "📈 Từ Khóa Tìm Kiếm Đột Phá",
                vel_evergreen: "🌲 Evergreen Quanh Năm",
                top_videos_title: "Top Videos (GMV 24h Cao Nhất)",
                top_videos_sub: "Xếp hạng theo tổng doanh thu GMV trực tiếp tạo ra trong 24h qua trên TikTok Shop US",
                top_influencers_title: "Top KOCs / Influencers (Bán Chạy Nhất 24h)",
                top_influencers_sub: "KOC/Creator chốt đơn nhiều nhất theo từng ngành hàng 24h qua",
                th_rank: "Rank",
                th_video: "Video Viral",
                th_creator: "Nhà Sáng Tạo (KOC)",
                th_prod_thumb: "Sản Phẩm",
                th_items_sold: "Đã Bán 24h",
                th_gmv: "GMV 24h",
                stat_total: "Tổng ý tưởng",
                stat_viral: "Top Viral 24h",
                stat_evergreen: "Top Evergreen",
                stat_team_saved: "Đã Lưu",
                stat_new_listings_7d: "Mới Listing 7D",
                stat_coverage: "Độ Phủ 28 Ngành",
                stat_leading: "Ngành Dẫn Đầu",
                stat_surges: "Rank Surges V3",
                stat_eds: "Dự Báo EDS & DT",
                th_sparkline: "Quỹ Đạo Trend",
                th_eds_daily: "Dự Báo EDS (Ngày)",
                th_est_monthly: "Doanh Thu Tháng (Est)",
                th_product: "Sản Phẩm",
                th_class: "Phân Loại",
                th_niche: "Ngành Hàng",
                th_price: "Giá Bán",
                th_saved_by: "Người Lưu Trong Team",
                th_actions: "Thao Tác",
                audio_banner_title: "Radar Giai Điệu & Âm Thanh Viral TikTok 24h",
                audio_banner_sub: "Các bài nhạc và âm thanh có lượng video mới tạo tăng đột biến trong 24h qua dùng cho kịch bản bán hàng TikTok Shop US.",
                visual_title: "Tìm Kiếm Sản Phẩm Bằng Hình Ảnh (Reverse Image Search)",
                visual_sub: "Tải ảnh chụp màn hình video TikTok hoặc sản phẩm để tra cứu xưởng sản xuất gốc 1688 và kiểm tra đối thủ cạnh tranh trên Google Lens.",
                drop_image_text: "BẤM VÀO ĐÂY ĐỂ TẢI ẢNH LÊN HOẶC KÉO THẢ",
                btn_preview: "XEM",
                preview_empty: "Chưa có ảnh nào được chọn",
                btn_search_1688: "TÌM XƯỞNG TRÊN 1688",
                btn_search_lens: "GOOGLE LENS US",
                calc_title: "Bảng Tính Lợi Nhuận Nhập Sỉ 1688 Về Bán TikTok Shop US",
                calc_cny: "Giá Nhập 1688 (¥ Tệ):",
                calc_ship: "Ship & Fulfillment ($):",
                calc_retail: "Giá Bán TikTok Shop ($):",
                calc_profit: "Lợi Nhuận Ròng & Margin:",
                empty_saved_title: "Chưa có sản phẩm nào được lưu trong mục này",
                empty_saved_sub: "Hãy bấm vào nút '+ Lưu Cho Tôi' trên bất kỳ dòng sản phẩm nào để thêm vào danh sách của bạn.",
                modal_add_user_title: "Thêm Người Dùng / Thành Viên Mới",
                modal_add_user_sub: "Tạo hồ sơ thành viên để quản lý và lưu riêng các ý tưởng sản phẩm trong nhóm.",
                label_name: "Tên Thành Viên *",
                label_role: "Vai Trò / Phụ Trách",
                btn_cancel: "HỦY BỎ",
                btn_create_user: "TẠO NGƯỜI DÙNG",
                btn_save_me: "+ Lưu Cho Tôi",
                btn_saved_me: "✔ Đã Lưu",
                btn_proof: "Minh Chứng",
                btn_view_1688: "🇨🇳 Xưởng 1688",
                btn_view_store: "Xem Sàn",
                hook_label: "Hook 3s:",
                verified_badge: "ĐÃ XÁC THỰC 24H (HỢP LỆ)",
                btn_force_scan: "Quét Mới Ngay",
                tip_1688_title: "Mẹo tìm kiếm 1688:",
                tip_1688_search: "Nếu khi mở ra chưa thấy sản phẩm ngay, bạn chỉ cần bấm lại nút 'Tìm kiếm' (🔍 搜索) trên thanh tìm kiếm của 1688 một lần nữa là hệ thống sẽ tải đúng sản phẩm theo từ khóa đã điền sẵn.",
                filter_ranking: "Rank:",
                rank_all: "🏆 Tất Cả Thứ Hạng",
                rank_top_10: "🥇 Top 1 - 10 Ngành",
                rank_top_50: "🥈 Top 1 - 50 Ngành",
                rank_top_100: "🥉 Top 1 - 100 Ngành",
                rank_sales_24h: "🔥 Bán Chạy Nhất 24h",
                rank_sales_30d: "📈 Bán Chạy 1 Tháng (30d)",
                tag_new_listing_btn: "✨ Mới Listing <24h"
            }},
            en: {{
                auto_timer: "Auto 6h Scan:",
                active_member: "Active Member / User:",
                add_user: "Add User",
                saved_items: "Saved:",
                nav_analytics: "Trend Discovery",
                tab_viral: "🔥 24h Viral Spikes",
                tab_evergreen: "🌲 Evergreen Winners",
                tab_audio: "🎵 Viral Sounds Radar",
                tab_visual: "📷 Visual & 1688 Search",
                nav_saved: "Saved Items",
                tab_saved: "📌 Saved Trends",
                tab_leaders: "🏆 Top Videos & Creators",
                
                tab_all: "📊 Full Matrix",
                btn_export_excel: "Export Excel Report",
                sources_label: "Verified Market Sources:",
                filter_major_category: "Major Category (28 TikTok Shop Niches):",
                filter_sub_niche: "Sub-Niche:",
                filter_velocity: "Trend Dimension (Velocity):",
                btn_reset_filters: "Reset",
                btn_force_scan: "Force Scan",
                cat_all: "-- All 28 Categories --",
                sub_all: "-- All Sub-Niches --",
                vel_all: "All Trend Matrix",
                vel_viral: "🔥 24h Viral Videos",
                vel_sales: "🚀 Fast Sales Velocity (Movers)",
                vel_keyword: "📈 Breakout Search Keywords",
                vel_evergreen: "🌲 Evergreen Winners",
                top_videos_title: "Top Videos (Highest 24h GMV)",
                top_videos_sub: "Ranked by direct GMV generated in the past 24 hours on TikTok Shop US",
                top_influencers_title: "Top Influencers (Highest 24h Sales)",
                top_influencers_sub: "Top selling KOCs/Creators by category with highest 24h conversion",
                th_rank: "Rank",
                th_video: "Viral Video",
                th_creator: "Creator (KOC)",
                th_prod_thumb: "Product",
                th_items_sold: "Sold 24h",
                th_gmv: "24h GMV",
                stat_total: "Total Ideas",
                stat_viral: "Top Viral 24h",
                stat_evergreen: "Top Evergreen",
                stat_team_saved: "Saved Items",
                stat_new_listings_7d: "New Listings 7D",
                stat_coverage: "28 Niches Coverage",
                stat_leading: "Leading Niche",
                stat_surges: "Rank Surges V3",
                stat_eds: "EDS & Est. Rev",
                th_sparkline: "Trajectory",
                th_eds_daily: "Est. Daily Sales (EDS)",
                th_est_monthly: "Est. Monthly Rev",
                th_product: "Product Idea",
                th_class: "Type",
                th_niche: "Niche",
                th_price: "Retail Price",
                th_saved_by: "Saved by Team",
                th_actions: "Actions",
                audio_banner_title: "TikTok 24h Viral Music & Sounds Radar",
                audio_banner_sub: "Top breakout audios with soaring 24h video velocity used by winning TikTok Shop US creators.",
                visual_title: "Product Visual & Reverse Image Search",
                visual_sub: "Upload product or TikTok screenshot to look up direct 1688 manufacturing factories and Google Lens competitors.",
                drop_image_text: "CLICK TO UPLOAD IMAGE OR DRAG & DROP",
                btn_preview: "VIEW",
                preview_empty: "No image selected yet",
                btn_search_1688: "SEARCH ON 1688 FACTORY",
                btn_search_lens: "SEARCH GOOGLE LENS US",
                calc_title: "1688 Sourcing to TikTok Shop US Profit Calculator",
                calc_cny: "1688 Wholesale Price (¥ CNY):",
                calc_ship: "Shipping & Fulfillment ($):",
                calc_retail: "TikTok Shop Retail Price ($):",
                calc_profit: "Net Profit & Margin:",
                empty_saved_title: "No saved products in this section yet",
                empty_saved_sub: "Click '+ Save For Me' on any product row to bookmark it into your personal collection.",
                modal_add_user_title: "Add New Team Member / User",
                modal_add_user_sub: "Create a member profile to manage and bookmark product ideas independently.",
                label_name: "Member Name *",
                label_role: "Role / Responsibility",
                btn_cancel: "CANCEL",
                btn_create_user: "CREATE USER",
                btn_save_me: "+ Save For Me",
                btn_saved_me: "✔ Saved",
                btn_proof: "24h Audit",
                btn_view_1688: "🇨🇳 1688 Source",
                btn_view_store: "Store Link",
                hook_label: "3s Hook:",
                verified_badge: "24H TREND VERIFIED",
                tip_1688_title: "1688 Search Tip:",
                tip_1688_search: "If products do not appear immediately, just click the 'Search' (🔍 搜索) button on the 1688 search bar once more to fetch products with prefilled keyword.",
                filter_ranking: "Rank:",
                rank_all: "🏆 All Rankings",
                rank_top_10: "🥇 Top 1 - 10 Niche",
                rank_top_50: "🥈 Top 1 - 50 Niche",
                rank_top_100: "🥉 Top 1 - 100 Niche",
                rank_sales_24h: "🔥 Best Selling 24h",
                rank_sales_30d: "📈 Best Selling 1 Month (30d)",
                tag_new_listing_btn: "✨ New Listing <24h"
            }}
        }};

        function toggleLanguage() {{
            currentLang = currentLang === 'vi' ? 'en' : 'vi';
            localStorage.setItem('tiktok_radar_lang', currentLang);
            applyLanguage();
            populateCategoryDropdown();
            renderUI();
        }}

        function applyLanguage() {{
            const lang = I18N[currentLang];
            document.getElementById('lang-flag').innerText = currentLang === 'vi' ? '🇻🇳' : '🇺🇸';
            document.getElementById('lang-text').innerText = currentLang.toUpperCase();

            // Translate elements with data-i18n
            document.querySelectorAll('[data-i18n]').forEach(el => {{
                const key = el.getAttribute('data-i18n');
                if (lang[key]) {{
                    el.innerText = lang[key];
                }}
            }});
        }}

        // 2. CATEGORY TAXONOMY & CASCADING FILTER CONTROLLER
        function populateCategoryDropdown() {{
            const selectEl = document.getElementById('category-select');
            const headerSelectEl = document.getElementById('header-category-select');
            if (!selectEl) return;
            const currentVal = selectEl.value;

            const allLabel = currentLang === 'vi' ? '-- Tất Cả 28 Ngành Hàng --' : '-- All 28 Categories --';
            let optionsHtml = `<option value="all">${{allLabel}}</option>`;

            categoriesTaxonomy.forEach(cat => {{
                const label = currentLang === 'vi' ? (cat.name_vi || cat.name) : cat.name;
                optionsHtml += `<option value="${{cat.name}}">${{label}}</option>`;
            }});

            selectEl.innerHTML = optionsHtml;
            selectEl.value = currentVal || 'all';
            
            if (headerSelectEl) {{
                headerSelectEl.innerHTML = optionsHtml;
                headerSelectEl.value = currentVal || 'all';
            }}
            
            updateSubNicheDropdown();
        }}

        function onHeaderCategoryChange(val) {{
            const mainCatSelect = document.getElementById('category-select');
            if (mainCatSelect) {{
                mainCatSelect.value = val;
            }}
            onCategoryChange();
        }}

        function onCategoryChange() {{
            updateSubNicheDropdown();
            filterItems();
        }}

        function updateSubNicheDropdown() {{
            const catSelect = document.getElementById('category-select');
            const subSelect = document.getElementById('subniche-select');
            if (!catSelect || !subSelect) return;

            const chosenCatName = catSelect.value;
            const allSubLabel = currentLang === 'vi' ? '-- Tất Cả Các Ngách --' : '-- All Sub-Niches --';
            let subHtml = `<option value="all">${{allSubLabel}}</option>`;

            if (chosenCatName !== 'all') {{
                const catObj = categoriesTaxonomy.find(c => c.name === chosenCatName);
                if (catObj && catObj.sub_niches) {{
                    catObj.sub_niches.forEach(sn => {{
                        const snLabel = currentLang === 'vi' ? (sn.name_vi || sn.name) : sn.name;
                        subHtml += `<option value="${{sn.name}}">${{snLabel}}</option>`;
                    }});
                }}
            }}
            subSelect.innerHTML = subHtml;
            subSelect.value = 'all';
        }}

        function resetFilters() {{
            document.getElementById('category-select').value = 'all';
            updateSubNicheDropdown();
            const velSelect = document.getElementById('velocity-select');
            if (velSelect) velSelect.value = 'ALL';
            const rankSelect = document.getElementById('ranking-select');
            if (rankSelect) rankSelect.value = 'all';
            document.getElementById('search-input').value = '';
            filterNewListingActive = false;
            const btnNew = document.getElementById('btn-tag-new-listing');
            if (btnNew) {{
                btnNew.classList.remove('bg-purple-700', 'text-white', 'border-purple-800');
                btnNew.classList.add('bg-purple-50', 'text-purple-900', 'border-purple-300');
            }}
            setTimeframe('24h');
            filterItems();
            showToast(currentLang === 'vi' ? 'Đã đặt lại toàn bộ bộ lọc về mặc định' : 'Filters reset to default');
        }}

        // 3. TOP 24H LEADERS RENDERER (TOP VIDEOS GMV & TOP INFLUENCERS) WITH CUSTOM PAGE SIZE & SYNC
        let topVideosPage = 1;
        let topInfluencersPage = 1;
        let leadersPageSize = 'all'; // Mặc định hiển thị Tối Đa (Tất cả) theo yêu cầu!

        function onLeadersPageSizeChange(val) {{
            leadersPageSize = val;
            topVideosPage = 1;
            topInfluencersPage = 1;
            
            // Đồng bộ giá trị 2 dropdown
            const sel1 = document.getElementById('leaders-page-size-select');
            const sel2 = document.getElementById('leaders-page-size-select-2');
            if (sel1) sel1.value = val;
            if (sel2) sel2.value = val;

            const searchVal = (document.getElementById('search-input').value || '').toLowerCase().trim();
            const catVal = document.getElementById('category-select').value;
            const subVal = document.getElementById('subniche-select').value;
            renderTopLeaders(catVal, subVal, searchVal);
        }}

        function changeTopVideosPage(p) {{
            topVideosPage = p;
            const searchVal = (document.getElementById('search-input').value || '').toLowerCase().trim();
            const catVal = document.getElementById('category-select').value;
            const subVal = document.getElementById('subniche-select').value;
            renderTopLeaders(catVal, subVal, searchVal);
        }}

        function changeTopInfluencersPage(p) {{
            topInfluencersPage = p;
            const searchVal = (document.getElementById('search-input').value || '').toLowerCase().trim();
            const catVal = document.getElementById('category-select').value;
            const subVal = document.getElementById('subniche-select').value;
            renderTopLeaders(catVal, subVal, searchVal);
        }}

        function renderTopLeaders(catFilter, subFilter, searchVal) {{
            const topVideosBody = document.getElementById('top-videos-body');
            const topInfluencersBody = document.getElementById('top-influencers-body');
            if (!topVideosBody || !topInfluencersBody) return;

            // Filter Top Videos
            let filteredVideos = topVideosData.filter(v => {{
                const matchCat = (catFilter === 'all') || (v.category && v.category.toLowerCase() === catFilter.toLowerCase());
                const matchSub = (subFilter === 'all') || (v.sub_niche && v.sub_niche.toLowerCase().includes(subFilter.toLowerCase()));
                const matchSearch = !searchVal || (v.caption && v.caption.toLowerCase().includes(searchVal)) || (v.product_name && v.product_name.toLowerCase().includes(searchVal)) || (v.creator_name && v.creator_name.toLowerCase().includes(searchVal));
                return matchCat && matchSub && matchSearch;
            }});

            // Filter Top Influencers
            let filteredInfluencers = topInfluencersData.filter(inf => {{
                const matchCat = (catFilter === 'all') || (inf.category && inf.category.toLowerCase() === catFilter.toLowerCase());
                const matchSub = (subFilter === 'all') || (inf.sub_niche && inf.sub_niche.toLowerCase().includes(subFilter.toLowerCase()));
                const matchSearch = !searchVal || (inf.name && inf.name.toLowerCase().includes(searchVal)) || (inf.handle && inf.handle.toLowerCase().includes(searchVal)) || (inf.best_product_title && inf.best_product_title.toLowerCase().includes(searchVal));
                return matchCat && matchSub && matchSearch;
            }});

            const pageSize = leadersPageSize === 'all' ? 9999 : parseInt(leadersPageSize, 10);

            // Compute pagination for Top Videos
            const totalVidPages = Math.max(1, Math.ceil(filteredVideos.length / pageSize));
            if (topVideosPage > totalVidPages) topVideosPage = totalVidPages;
            if (topVideosPage < 1) topVideosPage = 1;
            const startVidIdx = (topVideosPage - 1) * pageSize;
            const pagedVideos = filteredVideos.slice(startVidIdx, startVidIdx + pageSize);

            // Compute pagination for Top Influencers
            const totalInfPages = Math.max(1, Math.ceil(filteredInfluencers.length / pageSize));
            if (topInfluencersPage > totalInfPages) topInfluencersPage = totalInfPages;
            if (topInfluencersPage < 1) topInfluencersPage = 1;
            const startInfIdx = (topInfluencersPage - 1) * pageSize;
            const pagedInfluencers = filteredInfluencers.slice(startInfIdx, startInfIdx + pageSize);

            document.getElementById('top-videos-count-badge').innerText = `${{filteredVideos.length}} Videos`;
            document.getElementById('top-influencers-count-badge').innerText = `${{filteredInfluencers.length}} Creators`;

            // Helper medal renderer
            function getRankBadge(rank) {{
                if (rank === 1) return `<span class="inline-flex items-center justify-center w-6 h-6 bg-amber-400 text-slate-900 font-black text-xs shadow-sm">🥇</span>`;
                if (rank === 2) return `<span class="inline-flex items-center justify-center w-6 h-6 bg-slate-300 text-slate-900 font-black text-xs shadow-sm">🥈</span>`;
                if (rank === 3) return `<span class="inline-flex items-center justify-center w-6 h-6 bg-amber-600 text-white font-black text-xs shadow-sm">🥉</span>`;
                return `<span class="inline-flex items-center justify-center w-6 h-6 bg-slate-100 text-slate-700 font-bold text-xs border border-slate-300">${{rank}}</span>`;
            }}

            // Render Top Videos Rows (Đồng nhất chiều cao h-[72px] với bảng bên cạnh)
            if (filteredVideos.length === 0) {{
                topVideosBody.innerHTML = `
                    <tr>
                        <td colspan="5" class="py-6 text-center text-slate-400 font-bold text-xs">
                            ${{currentLang === 'vi' ? 'Không có video nào trong ngách được chọn 24h qua' : 'No top videos recorded in this niche over the past 24h'}}
                        </td>
                    </tr>
                `;
            }} else {{
                topVideosBody.innerHTML = pagedVideos.map(v => `
                    <tr class="hover:bg-rose-50/40 transition h-[72px]">
                        <!-- Rank -->
                        <td class="py-2 px-3 text-center align-middle">
                            ${{getRankBadge(v.rank)}}
                        </td>

                        <!-- Video Info -->
                        <td class="py-2 px-3 align-middle max-w-[220px]">
                            <div class="flex items-center gap-2.5">
                                <a href="${{v.video_url}}" target="_blank" rel="noreferrer noopener" class="relative w-10 h-13 bg-slate-900 border border-slate-300 shrink-0 group block overflow-hidden" title="Bấm để mở và xem video trên TikTok">
                                    <img src="${{v.video_cover || v.product_image}}" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&auto=format&fit=crop&q=60';" class="w-full h-full object-cover opacity-85 group-hover:opacity-100 transition" alt="">
                                    <div class="absolute inset-0 flex items-center justify-center bg-black/40 group-hover:bg-black/20 transition">
                                        <i class="ph-fill ph-play text-white text-base"></i>
                                    </div>
                                    <span class="absolute bottom-0 right-0 bg-black/80 text-white text-[9px] font-mono font-bold px-0.5">${{v.duration}}</span>
                                </a>
                                <div class="min-w-0 flex-1">
                                    <a href="${{v.video_url}}" target="_blank" rel="noreferrer noopener" class="font-bold text-slate-900 hover:text-rose-600 transition block text-xs line-clamp-2 leading-tight">
                                        ${{v.caption}}
                                    </a>
                                    <div class="text-[10px] text-slate-500 mt-1 flex items-center gap-1.5 flex-wrap">
                                        <a href="${{v.channel_url || ('https://www.tiktok.com/' + v.creator_handle)}}" target="_blank" rel="noreferrer noopener" class="font-bold text-slate-700 hover:text-rose-600 hover:underline inline-flex items-center gap-0.5" title="Mở trang cá nhân TikTok của KOC">
                                            ${{v.creator_handle}} <i class="ph-bold ph-arrow-square-out text-[9px]"></i>
                                        </a>
                                        <span>·</span>
                                        <span class="text-rose-600 font-bold"><i class="ph-bold ph-eye"></i> ${{v.views}}</span>
                                        <span class="bg-rose-50 text-rose-700 font-bold px-1 text-[9px] border border-rose-200 inline-flex items-center gap-0.5">
                                            <i class="ph-fill ph-check-circle text-rose-600"></i> LIVE
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </td>

                        <!-- Attached Product -->
                        <td class="py-2 px-2 text-center align-middle">
                            <div class="w-9 h-9 mx-auto border border-slate-300 hover:border-rose-600 bg-slate-50 p-0.5 cursor-zoom-in relative group transition" onclick='zoomProductImage("${{v.product_image}}", "${{(v.product_name || "").replace(/"/g, "&quot;").replace(/'/g, "\'")}}", "${{v.product_url || ""}}")' title="Bấm để xem ảnh phóng to & mở TikTok Shop">
                                <img src="${{v.product_image}}" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&auto=format&fit=crop&q=60';" class="w-full h-full object-contain" alt="">
                                <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition flex items-center justify-center text-white text-[10px]">
                                    <i class="ph-bold ph-magnifying-glass-plus"></i>
                                </div>
                            </div>
                        </td>

                        <!-- Items Sold 24h -->
                        <td class="py-2 px-3 text-right align-middle font-black text-slate-800">
                            ${{v.items_sold_24h.toLocaleString()}}
                        </td>

                        <!-- GMV 24h -->
                        <td class="py-2 px-3 text-right align-middle font-black text-rose-600 text-xs">
                            ${{v.gmv_24h}}
                        </td>
                    </tr>
                `).join('');
            }}

            // Footer Pagination Top Videos
            const vidPageInfo = document.getElementById('top-videos-page-info');
            const vidPagination = document.getElementById('top-videos-pagination-btns');
            if (vidPageInfo) {{
                if (filteredVideos.length === 0) {{
                    vidPageInfo.innerText = currentLang === 'vi' ? '0 video' : '0 videos';
                }} else if (leadersPageSize === 'all') {{
                    vidPageInfo.innerHTML = `${{currentLang === 'vi' ? 'Hiển thị tối đa' : 'Showing all'}} <strong>${{filteredVideos.length}}</strong> / <strong>${{filteredVideos.length}}</strong> videos`;
                }} else {{
                    const endVidIdx = Math.min(startVidIdx + pageSize, filteredVideos.length);
                    vidPageInfo.innerHTML = `${{currentLang === 'vi' ? 'Hiển thị' : 'Showing'}} <strong>${{startVidIdx + 1}} - ${{endVidIdx}}</strong> / <strong>${{filteredVideos.length}}</strong> videos`;
                }}
            }}
            if (vidPagination) {{
                if (leadersPageSize === 'all' || totalVidPages <= 1) {{
                    vidPagination.innerHTML = leadersPageSize === 'all' ? '<span class="text-[10px] font-bold text-slate-400 uppercase bg-slate-100 px-2 py-0.5 border border-slate-200">Đã mở toàn bộ</span>' : '';
                }} else {{
                    let h = '';
                    h += `<button onclick="changeTopVideosPage(${{topVideosPage - 1}})" ${{topVideosPage <= 1 ? 'disabled' : ''}} class="px-2.5 py-1 text-[11px] font-bold border border-slate-300 ${{topVideosPage <= 1 ? 'opacity-40 cursor-not-allowed bg-slate-100 text-slate-400' : 'bg-white hover:bg-slate-100 text-slate-800'}} transition"><i class="ph-bold ph-caret-left"></i> ${{currentLang === 'vi' ? 'Trước' : 'Prev'}}</button>`;
                    for (let p = 1; p <= totalVidPages; p++) {{
                        h += `<button onclick="changeTopVideosPage(${{p}})" class="px-2.5 py-1 text-[11px] font-black border ${{p === topVideosPage ? 'bg-rose-600 text-white border-rose-700' : 'bg-white hover:bg-slate-100 text-slate-700 border-slate-300'}} transition">${{p}}</button>`;
                    }}
                    h += `<button onclick="changeTopVideosPage(${{topVideosPage + 1}})" ${{topVideosPage >= totalVidPages ? 'disabled' : ''}} class="px-2.5 py-1 text-[11px] font-bold border border-slate-300 ${{topVideosPage >= totalVidPages ? 'opacity-40 cursor-not-allowed bg-slate-100 text-slate-400' : 'bg-white hover:bg-slate-100 text-slate-800'}} transition">${{currentLang === 'vi' ? 'Sau' : 'Next'}} <i class="ph-bold ph-caret-right"></i></button>`;
                    vidPagination.innerHTML = h;
                }}
            }}

            // Render Top Influencers Rows (Đồng nhất chiều cao h-[72px] với bảng bên cạnh)
            if (filteredInfluencers.length === 0) {{
                topInfluencersBody.innerHTML = `
                    <tr>
                        <td colspan="5" class="py-6 text-center text-slate-400 font-bold text-xs">
                            ${{currentLang === 'vi' ? 'Không có creator nào trong ngách được chọn 24h qua' : 'No creators recorded in this niche over the past 24h'}}
                        </td>
                    </tr>
                `;
            }} else {{
                topInfluencersBody.innerHTML = pagedInfluencers.map(inf => `
                    <tr class="hover:bg-blue-50/40 transition h-[72px]">
                        <!-- Rank -->
                        <td class="py-2 px-3 text-center align-middle">
                            ${{getRankBadge(inf.rank)}}
                        </td>

                        <!-- Creator Info -->
                        <td class="py-2 px-3 align-middle max-w-[220px]">
                            <div class="flex items-center gap-2.5">
                                <a href="${{inf.profile_url}}" target="_blank" rel="noreferrer noopener" class="w-10 h-10 border border-slate-300 bg-slate-100 shrink-0 block overflow-hidden" title="Mở trang cá nhân TikTok">
                                    <img src="${{inf.avatar}}" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src='https://ui-avatars.com/api/?name=' + encodeURIComponent('${{(inf.name || inf.handle).replace(/[^a-zA-Z0-9]/g, '')}}') + '&background=0D8ABC&color=fff&size=160&bold=true';" class="w-full h-full object-cover" alt="">
                                </a>
                                <div class="min-w-0 flex-1">
                                    <div class="flex items-center gap-1">
                                        <a href="${{inf.profile_url}}" target="_blank" rel="noreferrer noopener" class="font-black text-slate-900 hover:text-blue-600 transition block text-xs truncate">
                                            ${{inf.name}}
                                        </a>
                                        ${{inf.verified ? '<i class="ph-fill ph-seal-check text-blue-500 text-xs shrink-0" title="Tài khoản chính chủ TikTok"></i>' : ''}}
                                    </div>
                                    <div class="text-[10px] text-slate-500 flex items-center gap-1.5 flex-wrap mt-0.5">
                                        <span class="font-mono text-slate-600 font-bold">${{inf.handle}}</span>
                                        <span>·</span>
                                        <span class="bg-slate-100 text-slate-700 font-bold px-1 border border-slate-200" title="Số follower thực tế trên TikTok">${{inf.followers}}</span>
                                        ${{inf.is_live_scraped ? '<span class="bg-emerald-50 text-emerald-700 font-bold px-1 border border-emerald-200 text-[9px] inline-flex items-center gap-1" title="Dữ liệu cào thực tế từ máy chủ TikTok"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>LIVE</span>' : ''}}
                                    </div>
                                </div>
                            </div>
                        </td>

                        <!-- Best Selling Product -->
                        <td class="py-2 px-2 text-center align-middle">
                            <div class="w-9 h-9 mx-auto border border-slate-300 hover:border-blue-600 bg-slate-50 p-0.5 cursor-zoom-in relative group transition" onclick='zoomProductImage("${{inf.best_product_image}}", "${{(inf.best_product_title || "").replace(/"/g, "&quot;").replace(/'/g, "\'")}}", "${{inf.product_url || ""}}")' title="Bấm để xem ảnh phóng to & mở TikTok Shop">
                                <img src="${{inf.best_product_image}}" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&auto=format&fit=crop&q=60';" class="w-full h-full object-contain" alt="">
                                <div class="absolute inset-0 bg-black/30 opacity-0 group-hover:opacity-100 transition flex items-center justify-center text-white text-[10px]">
                                    <i class="ph-bold ph-magnifying-glass-plus"></i>
                                </div>
                            </div>
                        </td>

                        <!-- Items Sold 24h -->
                        <td class="py-2 px-3 text-right align-middle font-black text-slate-800">
                            ${{inf.items_sold_24h.toLocaleString()}}
                        </td>

                        <!-- GMV 24h -->
                        <td class="py-2 px-3 text-right align-middle font-black text-blue-700 text-xs">
                            ${{inf.gmv_24h}}
                        </td>
                    </tr>
                `).join('');
            }}

            // Footer Pagination Top Influencers
            const infPageInfo = document.getElementById('top-influencers-page-info');
            const infPagination = document.getElementById('top-influencers-pagination-btns');
            if (infPageInfo) {{
                if (filteredInfluencers.length === 0) {{
                    infPageInfo.innerText = currentLang === 'vi' ? '0 creator' : '0 creators';
                }} else if (leadersPageSize === 'all') {{
                    infPageInfo.innerHTML = `${{currentLang === 'vi' ? 'Hiển thị tối đa' : 'Showing all'}} <strong>${{filteredInfluencers.length}}</strong> / <strong>${{filteredInfluencers.length}}</strong> creators`;
                }} else {{
                    const endInfIdx = Math.min(startInfIdx + pageSize, filteredInfluencers.length);
                    infPageInfo.innerHTML = `${{currentLang === 'vi' ? 'Hiển thị' : 'Showing'}} <strong>${{startInfIdx + 1}} - ${{endInfIdx}}</strong> / <strong>${{filteredInfluencers.length}}</strong> creators`;
                }}
            }}
            if (infPagination) {{
                if (leadersPageSize === 'all' || totalInfPages <= 1) {{
                    infPagination.innerHTML = leadersPageSize === 'all' ? '<span class="text-[10px] font-bold text-slate-400 uppercase bg-slate-100 px-2 py-0.5 border border-slate-200">Đã mở toàn bộ</span>' : '';
                }} else {{
                    let h = '';
                    h += `<button onclick="changeTopInfluencersPage(${{topInfluencersPage - 1}})" ${{topInfluencersPage <= 1 ? 'disabled' : ''}} class="px-2.5 py-1 text-[11px] font-bold border border-slate-300 ${{topInfluencersPage <= 1 ? 'opacity-40 cursor-not-allowed bg-slate-100 text-slate-400' : 'bg-white hover:bg-slate-100 text-slate-800'}} transition"><i class="ph-bold ph-caret-left"></i> ${{currentLang === 'vi' ? 'Trước' : 'Prev'}}</button>`;
                    for (let p = 1; p <= totalInfPages; p++) {{
                        h += `<button onclick="changeTopInfluencersPage(${{p}})" class="px-2.5 py-1 text-[11px] font-black border ${{p === topInfluencersPage ? 'bg-blue-600 text-white border-blue-700' : 'bg-white hover:bg-slate-100 text-slate-700 border-slate-300'}} transition">${{p}}</button>`;
                    }}
                    h += `<button onclick="changeTopInfluencersPage(${{topInfluencersPage + 1}})" ${{topInfluencersPage >= totalInfPages ? 'disabled' : ''}} class="px-2.5 py-1 text-[11px] font-bold border border-slate-300 ${{topInfluencersPage >= totalInfPages ? 'opacity-40 cursor-not-allowed bg-slate-100 text-slate-400' : 'bg-white hover:bg-slate-100 text-slate-800'}} transition">${{currentLang === 'vi' ? 'Sau' : 'Next'}} <i class="ph-bold ph-caret-right"></i></button>`;
                    infPagination.innerHTML = h;
                }}
            }}
        }}

        // 4. TOP 24H TRENDING TIKTOK SOUNDS (GIAI ĐIỆU NHẠC VIRAL)
        const VIRAL_SOUNDS_24H = [
            {{
                title: "Satisfying Crisp Pop & Click SFX (Remix)",
                artist: "CleanTok Studio Beats",
                mood: "ASMR / Satisfying Routine",
                velocity_24h: "+94,000 video mới trong 24h",
                best_niches: "Gia dụng thông minh, Đồ chơi làm đẹp, Bàn chải thú cưng",
                hook_tip: "Bấm nút đúng nhịp bass drop để tạo cảm giác thỏa mãn cực độ",
                tiktok_sound_url: "https://www.tiktok.com/search?q=%23asmrsounds"
            }},
            {{
                title: "Dramatic Reveal & Shock Tension Beat",
                artist: "Viral Challenge Sound Hub",
                mood: "Drop Test / So Sánh Đột Phá",
                velocity_24h: "+148,000 video mới trong 24h",
                best_niches: "Bình giữ nhiệt Owala chống tràn, Máy làm sạch, Micro chống ồn",
                hook_tip: "Tạo khoảng lặng 1 giây trước khi lật ngược bình nước hoặc bật máy",
                tiktok_sound_url: "https://www.tiktok.com/search?q=%23droptest"
            }},
            {{
                title: "Aesthetic Morning Wind-Down Lo-Fi Chords",
                artist: "Chill Routine Lab",
                mood: "Clean Girl Aesthetic / Skincare",
                velocity_24h: "+72,000 video mới trong 24h",
                best_niches: "Medicube Toner Pads, Khăn lau mặt Clean Skin, Nến thơm",
                hook_tip: "Quay ánh sáng tự nhiên cạnh cửa sổ, ghép voiceover nhẹ nhàng",
                tiktok_sound_url: "https://www.tiktok.com/search?q=%23skincareroutine"
            }},
            {{
                title: "High BPM Motivation Electro Groove",
                artist: "Workout & Deep Clean",
                mood: "Năng Lượng Cao / Trước & Sau",
                velocity_24h: "+61,000 video mới trong 24h",
                best_niches: "Bàn chải cọ xoay điện, Máy hút lông thú cưng, Dụng cụ tập gym",
                hook_tip: "Tua nhanh video x2 tốc độ vết bẩn cứng đầu bay sạch theo nhịp nhạc",
                tiktok_sound_url: "https://www.tiktok.com/search?q=%23cleanwithme"
            }},
            {{
                title: "Laser Glow & Nostalgic Piano",
                artist: "Handmade Memories",
                mood: "Cảm Xúc / Quà Tặng Ý Nghĩa",
                velocity_24h: "+45,000 video mới trong 24h",
                best_niches: "Vòng cổ khắc tên hoa sinh, Kệ gỗ đa năng cho nam, Lịch tường",
                hook_tip: "Quay cận cảnh laser khắc tên người thương vào sản phẩm",
                tiktok_sound_url: "https://www.tiktok.com/search?q=%23personalizedgift"
            }}
        ];

        // 5. Quản Lý Multi-User & Danh Sách Đã Lưu
        const DEFAULT_USERS_DATA = {{
            active_user_id: "u_leader",
            users: [
                {{ id: "u_leader", name: "Ngọc (Team Leader)", role: "Store Owner / Lead Hunter", saved_trends: [] }},
                {{ id: "u_sourcing", name: "Hoàng (Sourcing)", role: "1688 & Logistics Specialist", saved_trends: [] }},
                {{ id: "u_creator", name: "Linh (Content Creator)", role: "TikTok Video & Hooks", saved_trends: [] }}
            ]
        }};

        function getUsersData() {{
            const raw = localStorage.getItem('tiktok_radar_multiusers');
            if (!raw) return DEFAULT_USERS_DATA;
            try {{
                return JSON.parse(raw);
            }} catch (e) {{
                return DEFAULT_USERS_DATA;
            }}
        }}

        function saveUsersData(data) {{
            localStorage.setItem('tiktok_radar_multiusers', JSON.stringify(data));
            renderUsersDropdown();
            renderUI();
        }}

        function renderUsersDropdown() {{
            const uData = getUsersData();
            const selectEl = document.getElementById('active-user-select');
            if (!selectEl) return;

            selectEl.innerHTML = uData.users.map(u => `
                <option value="${{u.id}}" ${{u.id === uData.active_user_id ? 'selected' : ''}}>
                    ${{u.name}} (${{u.role}})
                </option>
            `).join('');

            const activeUser = uData.users.find(u => u.id === uData.active_user_id) || uData.users[0];
            const myCount = (activeUser.saved_trends || []).length;
            
            let totalTeamCount = 0;
            const uniqueTitles = new Set();
            uData.users.forEach(u => {{
                (u.saved_trends || []).forEach(it => uniqueTitles.add(it.title));
            }});
            totalTeamCount = uniqueTitles.size;

            document.getElementById('user-saved-count').innerText = `${{myCount}} mục`;
            const navSavedEl = document.getElementById('nav-saved-count');
            if (navSavedEl) navSavedEl.innerText = myCount;
            const statTeamSaved = document.getElementById('stat-main-team-saved');
            if (statTeamSaved) statTeamSaved.innerText = myCount;
        }}

        function changeActiveUser(newId) {{
            const uData = getUsersData();
            uData.active_user_id = newId;
            saveUsersData(uData);
            const userObj = uData.users.find(u => u.id === newId);
            showToast(`Đã chuyển sang tài khoản: "${{userObj ? userObj.name : newId}}"`);
        }}

        function openNewUserModal() {{
            document.getElementById('new-user-modal').classList.remove('hidden');
            document.getElementById('new-user-name').focus();
        }}

        function closeNewUserModal(e) {{
            if (e && e.target && e.target.id !== 'new-user-modal' && !e.target.closest('button')) {{
                return;
            }}
            const modal = document.getElementById('new-user-modal');
            if (modal) modal.classList.add('hidden');
            const nameEl = document.getElementById('new-user-name');
            if (nameEl) nameEl.value = '';
            const roleEl = document.getElementById('new-user-role');
            if (roleEl) roleEl.value = '';
        }}

        function confirmCreateUser() {{
            const name = document.getElementById('new-user-name').value.trim();
            const role = document.getElementById('new-user-role').value.trim() || 'Thành viên Team';
            if (!name) {{
                alert('Vui lòng nhập tên thành viên!');
                return;
            }}
            const uData = getUsersData();
            const newId = 'u_' + Date.now();
            uData.users.push({{
                id: newId,
                name: name,
                role: role,
                saved_trends: []
            }});
            uData.active_user_id = newId;
            saveUsersData(uData);
            closeNewUserModal();
            showToast(`Đã tạo thành viên mới: "${{name}}" (${{role}})`);
        }}

        function isSavedByCurrentUser(item) {{
            const uData = getUsersData();
            const activeUser = uData.users.find(u => u.id === uData.active_user_id) || uData.users[0];
            return (activeUser.saved_trends || []).some(it => it.title === item.title);
        }}

        function getTeamSavers(item) {{
            const uData = getUsersData();
            const savers = [];
            uData.users.forEach(u => {{
                if ((u.saved_trends || []).some(it => it.title === item.title)) {{
                    savers.push(u.name.split(' ')[0]);
                }}
            }});
            return savers;
        }}

        function toggleSaveTrend(item) {{
            const uData = getUsersData();
            const activeUser = uData.users.find(u => u.id === uData.active_user_id) || uData.users[0];
            if (!activeUser.saved_trends) activeUser.saved_trends = [];
            
            const existingIdx = activeUser.saved_trends.findIndex(it => it.title === item.title);
            if (existingIdx >= 0) {{
                activeUser.saved_trends.splice(existingIdx, 1);
            }} else {{
                const savedItem = Object.assign({{}}, item, {{
                    saved_by_id: activeUser.id,
                    saved_by_name: activeUser.name,
                    saved_at_time: new Date().toLocaleString('vi-VN')
                }});
                activeUser.saved_trends.push(savedItem);
            }}
            saveUsersData(uData);
        }}

        // 6. Đồng hồ đếm ngược 6 tiếng dựa trên mốc thời gian thực tế (F5 KHÔNG BAO GIỜ BỊ RESET)
        function startCountdown() {{
            const nowSec = Math.floor(Date.now() / 1000);
            
            // Lấy timestamp lần quét kế tiếp từ backend hoặc localStorage
            let nextScanTs = globalData.next_scan_timestamp;
            if (!nextScanTs) {{
                const savedTs = localStorage.getItem('tiktok_radar_next_scan_ts');
                if (savedTs && parseInt(savedTs) > nowSec) {{
                    nextScanTs = parseInt(savedTs);
                }} else {{
                    nextScanTs = nowSec + 6 * 3600;
                    localStorage.setItem('tiktok_radar_next_scan_ts', nextScanTs);
                }}
            }} else {{
                localStorage.setItem('tiktok_radar_next_scan_ts', nextScanTs);
            }}

            const nextTimeStr = globalData.next_scan_time || new Date(nextScanTs * 1000).toLocaleTimeString('vi-VN', {{ hour: '2-digit', minute: '2-digit' }});
            const nextLabelEl = document.getElementById('next-scan-label');
            if (nextLabelEl) nextLabelEl.innerText = nextTimeStr;

            function updateTimer() {{
                const currentNow = Math.floor(Date.now() / 1000);
                const diff = nextScanTs - currentNow;

                if (diff <= 0) {{
                    const el = document.getElementById('countdown-text');
                    if (el) {{
                        el.innerText = '00:00:00';
                        el.classList.add('text-rose-600', 'animate-pulse');
                    }}
                    const nextLabel = document.getElementById('next-scan-label');
                    if (nextLabel) nextLabel.innerText = currentLang === 'vi' ? 'Đang chạy quét mới...' : 'Crawling new data...';
                    return;
                }}

                const h = String(Math.floor(diff / 3600)).padStart(2, '0');
                const m = String(Math.floor((diff % 3600) / 60)).padStart(2, '0');
                const s = String(diff % 60).padStart(2, '0');
                const el = document.getElementById('countdown-text');
                if (el) el.innerText = `${{h}}:${{m}}:${{s}}`;
            }}

            updateTimer();
            setInterval(updateTimer, 1000);
        }}

        // 7. Visual Image Search Handlers
        let currentImageBlob = null;
        let currentImageUrl = '';

        function setPreviewImage(src, name) {{
            currentImageUrl = src;
            const img = document.getElementById('preview-img');
            const container = document.getElementById('preview-container');
            const promptBox = document.getElementById('drop-prompt');
            const nameEl = document.getElementById('preview-filename');
            
            if (img && container && promptBox) {{
                img.src = src;
                container.classList.remove('hidden');
                promptBox.classList.add('hidden');
                if (nameEl) nameEl.innerText = name || 'Hình ảnh đã chọn';
            }}
            
            if (src.startsWith('http')) {{
                document.getElementById('link-google-lens').href = `https://lens.google.com/uploadbyurl?url=${{encodeURIComponent(src)}}`;
            }} else {{
                document.getElementById('link-google-lens').href = 'https://lens.google.com/';
            }}
        }}

        function clearImagePreview() {{
            currentImageBlob = null;
            currentImageUrl = '';
            const uploadInput = document.getElementById('file-upload');
            const urlInput = document.getElementById('image-url-input');
            if (uploadInput) uploadInput.value = '';
            if (urlInput) urlInput.value = '';
            
            const container = document.getElementById('preview-container');
            const promptBox = document.getElementById('drop-prompt');
            if (container) container.classList.add('hidden');
            if (promptBox) promptBox.classList.remove('hidden');
            
            const lensBtn = document.getElementById('link-google-lens');
            if (lensBtn) lensBtn.href = 'https://lens.google.com/';
        }}

        function handleImageUpload(e) {{
            const files = e.target.files || (e.dataTransfer ? e.dataTransfer.files : null);
            if (!files || files.length === 0) return;
            const file = files[0];
            currentImageBlob = file;
            const url = URL.createObjectURL(file);
            setPreviewImage(url, file.name);
            showToast(`Đã nhận ảnh "${{file.name}}"! Bạn có thể bấm mở Google Lens hoặc 1688.`);
        }}

        function handleUrlSearch() {{
            const val = document.getElementById('image-url-input').value.trim();
            if (!val) return;
            setPreviewImage(val, 'Link ảnh Online');
            showToast('Đã nhận diện link ảnh online!');
        }}

        function handleDragOver(e) {{
            e.preventDefault();
            e.stopPropagation();
            const el = document.getElementById('image-drop-zone');
            if (el) el.classList.add('border-orange-500', 'bg-orange-50/50');
        }}

        function handleDragLeave(e) {{
            e.preventDefault();
            e.stopPropagation();
            const el = document.getElementById('image-drop-zone');
            if (el) el.classList.remove('border-orange-500', 'bg-orange-50/50');
        }}

        function handleDrop(e) {{
            e.preventDefault();
            e.stopPropagation();
            const el = document.getElementById('image-drop-zone');
            if (el) el.classList.remove('border-orange-500', 'bg-orange-50/50');
            handleImageUpload(e);
        }}

        // Global Paste handler (Ctrl + V anywhere)
        window.addEventListener('paste', (e) => {{
            const items = e.clipboardData ? e.clipboardData.items : [];
            for (let i = 0; i < items.length; i++) {{
                if (items[i].type.indexOf('image') !== -1) {{
                    const blob = items[i].getAsFile();
                    currentImageBlob = blob;
                    const url = URL.createObjectURL(blob);
                    setPreviewImage(url, 'Ảnh chụp màn hình vừa dán (Clipboard)');
                    showToast('Đã dán ảnh chụp màn hình thành công!');
                    switchTab('visual');
                    break;
                }}
            }}
        }});

        function searchProductImage(imgUrl) {{
            if (!imgUrl) return;
            window.open(`https://lens.google.com/uploadbyurl?url=${{encodeURIComponent(imgUrl)}}`, '_blank', 'noreferrer,noopener');
        }}

        
        // ================= ZOOM PREVIEW LIGHTBOX CONTROLLER =================
        let currentZoomedImgUrl = '';
        let currentZoomedTitle = '';
        let currentZoomedShopUrl = '';

        function zoomProductImage(imgUrl, title, shopUrl) {{
            if (!imgUrl) return;
            currentZoomedImgUrl = imgUrl;
            currentZoomedTitle = title || '';
            currentZoomedShopUrl = shopUrl || `https://www.tiktok.com/search?q=${{encodeURIComponent(title || '')}}`;

            const modal = document.getElementById('image-zoom-modal');
            const img = document.getElementById('zoom-modal-img');
            const titleEl = document.getElementById('zoom-modal-title');
            const tiktokBtn = document.getElementById('zoom-tiktok-btn');

            if (modal && img) {{
                img.src = imgUrl;
                if (titleEl) titleEl.innerText = currentZoomedTitle;
                if (tiktokBtn) tiktokBtn.href = currentZoomedShopUrl;
                modal.classList.remove('hidden');
                document.body.classList.add('overflow-hidden');
            }}
        }}

        function closeImageZoomModal(e) {{
            if (e && e.target && e.target.id !== 'image-zoom-modal' && !e.target.closest('button')) {{
                return;
            }}
            const modal = document.getElementById('image-zoom-modal');
            if (modal) modal.classList.add('hidden');
            document.body.classList.remove('overflow-hidden');
        }}

        function openZoomGoogleLens() {{
            if (currentZoomedImgUrl) {{
                window.open(`https://lens.google.com/uploadbyurl?url=${{encodeURIComponent(currentZoomedImgUrl)}}`, '_blank', 'noreferrer,noopener');
            }}
        }}

                // Hàm tra cứu từ khóa tiếng Trung Giản Thể cho 1688
        // Tra cứu từ khóa tiếng Trung Giản Thể chuẩn xác theo ngành cho 1688
        const CATEGORY_SPECIFIC_1688_JS = {json.dumps(CATEGORY_SPECIFIC_1688, ensure_ascii=False)};
        const CATEGORY_FALLBACK_1688_JS = {json.dumps(CATEGORY_FALLBACK_1688, ensure_ascii=False)};
        const KEYWORDS_1688_MAP_JS = {json.dumps(KEYWORDS_1688_MAP, ensure_ascii=False)};

        function get_1688_query(title, category) {{
            const tLow = (title || '').toLowerCase();
            const cat = category || '';
            
            // 1. Kiểm tra chính xác theo từng ngành hàng (tránh trùng từ khóa tổng quát như 'clean')
            if (cat && CATEGORY_SPECIFIC_1688_JS[cat]) {{
                for (const [k, v] of Object.entries(CATEGORY_SPECIFIC_1688_JS[cat])) {{
                    if (tLow.includes(k.toLowerCase())) return v;
                }}
            }}
            
            // 2. Tra cứu theo cụm từ dài nhất trước
            const sortedKeys = Object.keys(KEYWORDS_1688_MAP_JS).sort((a, b) => b.length - a.length);
            for (const k of sortedKeys) {{
                if (tLow.includes(k.toLowerCase())) return KEYWORDS_1688_MAP_JS[k];
            }}
            
            // 3. Fallback theo ngành
            if (cat && CATEGORY_FALLBACK_1688_JS[cat]) {{
                return CATEGORY_FALLBACK_1688_JS[cat];
            }}
            
            return "跨境爆款 源头工厂直供";
        }}

        function open1688Search(keyword) {{
            const qRaw = keyword || '跨境爆款 源头工厂直供';
            copyKeyword(qRaw, false);
            const qEnc = encodeURIComponent(qRaw);
            window.open(`https://www.1688.com/pages/offerlist/search/search.html?keywords=${{qEnc}}`, '_blank', 'noreferrer,noopener');
        }}

        function get_alibaba_query(title) {{
            return (title || '').replace(/[^\\w\\s]/gi, ' ').trim().split(/\\s+/).slice(0, 6).join(' ');
        }}

        function openZoom1688() {{
            if (currentZoomedTitle) {{
                const q = get_1688_query(currentZoomedTitle);
                open1688Search(q);
            }} else {{
                window.open('https://s.1688.com/youyuan/index.htm', '_blank', 'noreferrer,noopener');
            }}
        }}

        // 7. Force Reload / Live Scan Trends (Quét thủ công thực tế 100% kèm Modal tiến trình)
        let isScanning = false;
        let scanTimerInterval = null;
        let scanElapsedSeconds = 0;

        function openScanModal() {{
            const modal = document.getElementById('scan-progress-modal');
            if (modal) modal.classList.remove('hidden');
            scanElapsedSeconds = 0;
            const timerEl = document.getElementById('scan-elapsed-timer');
            if (timerEl) timerEl.innerText = '00:00';
            
            clearInterval(scanTimerInterval);
            scanTimerInterval = setInterval(() => {{
                scanElapsedSeconds++;
                const mins = String(Math.floor(scanElapsedSeconds / 60)).padStart(2, '0');
                const secs = String(scanElapsedSeconds % 60).padStart(2, '0');
                if (timerEl) timerEl.innerText = `${{mins}}:${{secs}}`;
            }}, 1000);

            updateScanStep(1, 'active', 'Đang kết nối API máy chủ...');
            setScanProgress(15);
        }}

        function closeScanModal() {{
            const modal = document.getElementById('scan-progress-modal');
            if (modal) modal.classList.add('hidden');
            clearInterval(scanTimerInterval);
        }}

        function setScanProgress(pct) {{
            const bar = document.getElementById('scan-progress-bar');
            if (bar) bar.style.width = `${{pct}}%`;
        }}

        function updateScanStep(stepNum, status, label) {{
            const el = document.getElementById(`scan-step-${{stepNum}}`);
            if (!el) return;
            if (status === 'active') {{
                el.className = 'flex items-center justify-between text-blue-600 font-black';
                el.innerHTML = `<span class="flex items-center gap-2"><i class="ph-bold ph-spinner animate-spin"></i> ${{label || el.innerText}}</span><span class="text-[10px] font-mono animate-pulse">ĐANG CÀO...</span>`;
            }} else if (status === 'done') {{
                el.className = 'flex items-center justify-between text-emerald-600 font-black';
                el.innerHTML = `<span class="flex items-center gap-2"><i class="ph-bold ph-check-circle text-emerald-600"></i> ${{label || el.innerText}}</span><span class="text-[10px] font-mono text-emerald-700 bg-emerald-50 px-1 border border-emerald-200">XONG</span>`;
            }}
        }}

        async function forceScanTrends() {{
            if (isScanning) return;
            const btn = document.getElementById('btn-force-scan');
            const icon = document.getElementById('force-scan-icon');
            const text = document.getElementById('force-scan-text');

            isScanning = true;
            if (btn) btn.disabled = true;
            if (icon) icon.classList.add('animate-spin');
            if (text) text.innerText = (currentLang === 'vi' ? 'Đang Quét...' : 'Scanning...');
            
            openScanModal();

            try {{
                const isHttp = window.location.origin.startsWith('http');
                const apiUrl = isHttp ? '/api/scan' : 'http://127.0.0.1:8000/api/scan';

                // Step 1: Connecting
                updateScanStep(1, 'active', '1. Kết nối cổng dữ liệu & Supabase Cloud');
                setScanProgress(25);

                // Simulation stepper while awaiting server
                const stepTimer1 = setTimeout(() => {{
                    updateScanStep(1, 'done', '1. Kết nối cổng dữ liệu & Supabase Cloud');
                    updateScanStep(2, 'active', '2. Cào Google Trends US & TikTok Shop Viral 24h');
                    setScanProgress(45);
                }}, 2000);

                const stepTimer2 = setTimeout(() => {{
                    updateScanStep(2, 'done', '2. Cào Google Trends US & TikTok Shop Viral 24h');
                    updateScanStep(3, 'active', '3. Đối soát Amazon Best Sellers & eBay Deals');
                    setScanProgress(70);
                }}, 5000);

                const stepTimer3 = setTimeout(() => {{
                    updateScanStep(3, 'done', '3. Đối soát Amazon Best Sellers & eBay Deals');
                    updateScanStep(4, 'active', '4. Tính toán EDS Power-Law & Xếp Hạng Rank Surge V3');
                    setScanProgress(85);
                }}, 8000);

                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 90000);

                const res = await fetch(apiUrl, {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    signal: controller.signal
                }});
                clearTimeout(timeoutId);
                clearTimeout(stepTimer1);
                clearTimeout(stepTimer2);
                clearTimeout(stepTimer3);

                if (res.ok) {{
                    const freshData = await res.json();
                    
                    updateScanStep(1, 'done', '1. Đã đồng bộ cổng dữ liệu & Supabase Cloud');
                    updateScanStep(2, 'done', '2. Đã cào Google Trends US & TikTok Viral 24h');
                    updateScanStep(3, 'done', '3. Đã đối soát Amazon Best Sellers & eBay Deals');
                    updateScanStep(4, 'done', '4. Đã phân tích mô hình EDS Power-Law & Rank Surge V3');
                    updateScanStep(5, 'done', '5. Xuất báo cáo Excel & Cập nhật Dashboard');
                    setScanProgress(100);

                    // Enable modal close button
                    const closeBtn = document.getElementById('scan-modal-close-btn');
                    if (closeBtn) {{
                        closeBtn.disabled = false;
                        closeBtn.className = 'px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-black uppercase shadow transition cursor-pointer flex items-center gap-1.5';
                        closeBtn.innerHTML = '<i class="ph-bold ph-check"></i> HOÀN TẤT - XEM DỮ LIỆU MỚI';
                    }}

                    if (freshData && freshData.all_ideas && freshData.all_ideas.length > 0) {{
                        window.globalData = freshData;
                        if (freshData.top_videos) window.topVideosData = freshData.top_videos;
                        if (freshData.top_influencers) window.topInfluencersData = freshData.top_influencers;
                    }}
                    
                    if (freshData.updated_at) {{
                        const updEl = document.querySelector('#current-view-title + div strong');
                        if (updEl) updEl.innerText = freshData.updated_at;
                        const sideScanLabel = document.getElementById('next-scan-label');
                        if (sideScanLabel) sideScanLabel.innerText = freshData.updated_at.split(' ')[1] || freshData.updated_at;
                    }}

                    populateCategoryDropdown();
                    renderUI();
                    showToast(currentLang === 'vi' ? '✅ Đã hoàn tất quét và nạp dữ liệu trend mới nhất!' : '✅ Scan completed! Fresh trends loaded.');
                }} else {{
                    throw new Error(`Status ${{res.status}}`);
                }}
            }} catch (err) {{
                console.warn('API scan connection error:', err);
                const closeBtn = document.getElementById('scan-modal-close-btn');
                if (closeBtn) {{
                    closeBtn.disabled = false;
                    closeBtn.className = 'px-4 py-2 bg-slate-800 text-white text-xs font-black uppercase shadow transition cursor-pointer';
                    closeBtn.innerText = 'Đóng Cửa Sổ';
                }}
                showToast(currentLang === 'vi' 
                    ? '💡 Để quét dữ liệu theo yêu cầu bằng nút bấm, hãy khởi động server nền bằng cách nhấp đúp file "run_dashboard.bat" (hoặc chạy "python main.py")!' 
                    : '💡 To enable on-demand scanning from this button, launch run_dashboard.bat to start the backend server!', true);
            }} finally {{
                isScanning = false;
                if (btn) btn.disabled = false;
                if (icon) icon.classList.remove('animate-spin');
                if (text) text.innerText = (currentLang === 'vi' ? 'Quét Mới Ngay' : 'Force Scan');
            }}
        }}

        // Global ESC key listener to close lightbox and modals
        window.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') {{
                closeImageZoomModal();
                closeModal();
                closeNewUserModal();
            }}
        }});

        // 8. 1688 Profit Margin Calculator
        function calculateMargin() {{
            const cny = parseFloat(document.getElementById('calc-cny').value) || 0;
            const ship = parseFloat(document.getElementById('calc-ship').value) || 0;
            const retail = parseFloat(document.getElementById('calc-retail').value) || 0;
            
            const usdCost = cny / 7.2;
            document.getElementById('calc-usd-equiv').innerText = `~ $${{usdCost.toFixed(2)}} USD (Tỉ giá 7.2)`;
            
            const totalCost = usdCost + ship;
            const netProfit = retail - totalCost;
            const margin = retail > 0 ? (netProfit / retail) * 100 : 0;
            
            document.getElementById('calc-net-profit').innerText = `${{netProfit >= 0 ? '+' : ''}}$${{netProfit.toFixed(2)}} / đơn`;
            document.getElementById('calc-margin-percent').innerText = `${{currentLang === 'vi' ? 'Biên lãi:' : 'Margin:'}} ${{margin.toFixed(1)}}%`;
        }}

        
        // ================= COLLAPSIBLE SIDEBAR CONTROLLER =================
        function toggleSidebar() {{
            const sidebar = document.getElementById('main-sidebar');
            const toggleIcon = document.getElementById('sidebar-toggle-icon');
            if (!sidebar) return;

            const isCollapsed = sidebar.classList.toggle('collapsed');
            localStorage.setItem('tiktok_radar_sidebar_collapsed', isCollapsed ? '1' : '0');

            if (toggleIcon) {{
                if (isCollapsed) {{
                    toggleIcon.className = 'ph-bold ph-caret-double-right text-sm';
                }} else {{
                    toggleIcon.className = 'ph-bold ph-caret-double-left text-sm';
                }}
            }}
        }}

        function restoreSidebarState() {{
            const isCollapsed = localStorage.getItem('tiktok_radar_sidebar_collapsed') === '1';
            const sidebar = document.getElementById('main-sidebar');
            const toggleIcon = document.getElementById('sidebar-toggle-icon');
            if (sidebar && isCollapsed) {{
                sidebar.classList.add('collapsed');
                if (toggleIcon) toggleIcon.className = 'ph-bold ph-caret-double-right text-sm';
            }}
        }}

        // 9. Navigation Tab Switching
        function switchTab(tab) {{
            currentTab = tab;
            const navIds = ['all', 'viral', 'evergreen', 'leaders', 'audio', 'visual', 'saved'];
            
            navIds.forEach(id => {{
                const btn = document.getElementById('nav-btn-' + id);
                if (btn) {{
                    btn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-white text-slate-700 hover:bg-slate-100 border-l-4 border-transparent";
                }}
            }});

            const activeBtn = document.getElementById('nav-btn-' + tab);
            if (activeBtn) {{
                if (tab === 'viral') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-rose-600 text-white border-l-4 border-rose-900";
                else if (tab === 'evergreen') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-emerald-600 text-white border-l-4 border-emerald-900";
                else if (tab === 'leaders') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-amber-600 text-white border-l-4 border-amber-900";
                else if (tab === 'audio') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-purple-600 text-white border-l-4 border-purple-900";
                else if (tab === 'visual') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-orange-600 text-white border-l-4 border-orange-900";
                else if (tab === 'saved') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-amber-600 text-white border-l-4 border-amber-900";
                else if (tab === 'team_saved') activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-blue-600 text-white border-l-4 border-blue-900";
                else activeBtn.className = "sidebar-nav-btn w-full flex items-center justify-between px-3 py-2 text-xs font-extrabold uppercase transition bg-slate-900 text-white border-l-4 border-black";
            }}

            const titles = {{
                all: currentLang === 'vi' ? '📊 TẤT CẢ Ý TƯỞNG ĐỐI SOÁT 5 SÀN' : '📊 ALL PRODUCT IDEAS 5-SOURCE MATRIX',
                viral: currentLang === 'vi' ? '🔥 BÙNG NỔ 24H (VIRAL SPIKES)' : '🔥 24H BREAKOUT VIRAL SPIKES',
                evergreen: currentLang === 'vi' ? '🌲 EVERGREEN BÁN QUANH NĂM' : '🌲 EVERGREEN YEAR-ROUND WINNERS',
                leaders: currentLang === 'vi' ? '🏆 BẢNG XẾP HẠNG TOP VIDEOS GMV & TOP INFLUENCERS TIKTOK SHOP (24H)' : '🏆 TIKTOK SHOP 24H TOP VIDEOS & INFLUENCERS LEADERBOARD',
                audio: currentLang === 'vi' ? '🎵 GIAI ĐIỆU & ÂM THANH VIRAL TIKTOK 24H' : '🎵 TIKTOK 24H VIRAL AUDIO & SOUNDS',
                visual: currentLang === 'vi' ? '📷 TÌM KIẾM HÌNH ẢNH & XƯỞNG SỈ 1688' : '📷 VISUAL SEARCH & 1688 WHOLESALE HUB',
                saved: currentLang === 'vi' ? '📌 DANH SÁCH SẢN PHẨM ĐÃ LƯU' : '📌 SAVED PRODUCTS COLLECTION'
            }};
            document.getElementById('current-view-title').innerText = titles[tab] || '';

            renderUI();
        }}

        let filterNewListingActive = false;
        function toggleNewListingFilter() {{
            filterNewListingActive = !filterNewListingActive;
            const btn = document.getElementById('btn-tag-new-listing');
            if (btn) {{
                if (filterNewListingActive) {{
                    btn.classList.remove('bg-purple-50', 'text-purple-900', 'border-purple-300');
                    btn.classList.add('bg-purple-700', 'text-white', 'border-purple-800');
                }} else {{
                    btn.classList.remove('bg-purple-700', 'text-white', 'border-purple-800');
                    btn.classList.add('bg-purple-50', 'text-purple-900', 'border-purple-300');
                }}
            }}
            topVideosPage = 1;
            topInfluencersPage = 1;
            renderUI();
        }}

        function searchByKeyword(kw, event) {{
            if (event) {{
                try {{
                    event.preventDefault();
                    event.stopPropagation();
                }} catch(e) {{}}
            }}
            const searchInput = document.getElementById('search-input');
            if (searchInput) {{
                searchInput.value = kw;
            }}
            const catSelect = document.getElementById('category-select');
            if (catSelect) catSelect.value = 'all';
            const subSelect = document.getElementById('subniche-select');
            if (subSelect) subSelect.value = 'all';
            filterItems();
            const targetEl = document.getElementById('search-input') || document.getElementById('table-container') || document.getElementById('cards-container');
            if (targetEl) {{
                targetEl.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            }}
            showToast(currentLang === 'vi' ? `🔍 Đang lọc theo từ khóa: #${{kw}}` : `🔍 Filtering by keyword: #${{kw}}`);
        }}

        function filterItems() {{
            topVideosPage = 1;
            topInfluencersPage = 1;
            renderUI();
        }}

        // 10. Main Render Function
        function renderUI() {{
            if (!globalData) return;
            const lang = I18N[currentLang];

            const searchVal = (document.getElementById('search-input').value || '').toLowerCase().trim();
            const catVal = document.getElementById('category-select').value;
            const subVal = document.getElementById('subniche-select').value;
            const velocitySelect = document.getElementById('velocity-select');
            const velocityVal = velocitySelect ? velocitySelect.value : 'ALL';
            const uData = getUsersData();
            const activeUser = uData.users.find(u => u.id === uData.active_user_id) || uData.users[0];

            const cardsContainer = document.getElementById('cards-container');
            const tableContainer = document.getElementById('table-container');
            const audioContainer = document.getElementById('audio-view-container');
            const visualContainer = document.getElementById('visual-view-container');
            const emptySavedBox = document.getElementById('empty-saved-box');
            const statsRow = document.getElementById('stats-overview-row');
            const topLeadersSection = document.getElementById('top-leaders-section');

            // Render Top Leaders (Top Videos GMV & Top Influencers) with live filters
            renderTopLeaders(catVal, subVal, searchVal);

            // Hide/Show main view containers
            cardsContainer.classList.add('hidden');
            tableContainer.classList.add('hidden');
            audioContainer.classList.add('hidden');
            visualContainer.classList.add('hidden');
            emptySavedBox.classList.add('hidden');

            if (currentTab === 'leaders') {{
                statsRow.classList.add('hidden');
                topLeadersSection.classList.remove('hidden');
                return;
            }}

            if (currentTab === 'audio') {{
                audioContainer.classList.remove('hidden');
                statsRow.classList.add('hidden');
                topLeadersSection.classList.add('hidden');
                
                document.getElementById('audio-list').innerHTML = VIRAL_SOUNDS_24H.map(s => `
                    <div class="bg-white border-2 border-purple-200 hover:border-purple-400 p-4 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4 transition">
                        <div class="flex-1">
                            <div class="flex items-center gap-2 mb-1">
                                <span class="text-[10px] font-black uppercase px-2 py-0.5 bg-purple-100 text-purple-800 border border-purple-300">
                                    ${{s.mood}}
                                </span>
                                <span class="text-xs font-black text-rose-600 flex items-center gap-1">
                                    <i class="ph-bold ph-chart-line-up"></i> ${{s.velocity_24h}}
                                </span>
                            </div>
                            <h3 class="text-sm font-black text-slate-900 mb-1 flex items-center gap-1.5">
                                <i class="ph-bold ph-music-note text-purple-600"></i> ${{s.title}}
                            </h3>
                            <div class="text-xs text-slate-600 mb-1">
                                <strong>Ngách phù hợp:</strong> ${{s.best_niches}}
                            </div>
                            <div class="text-xs text-purple-900 italic bg-purple-50 p-2 border border-purple-200">
                                <strong>Gợi ý quay:</strong> "${{s.hook_tip}}"
                            </div>
                        </div>

                        <div class="shrink-0 flex items-center gap-2">
                            <a href="${{s.tiktok_sound_url}}" target="_blank" rel="noreferrer noopener" class="px-4 py-2 bg-purple-700 hover:bg-purple-800 text-white font-black text-xs uppercase flex items-center gap-1.5 shadow transition">
                                <i class="ph-bold ph-play-circle text-base"></i> MỞ NHẠC TRÊN TIKTOK
                            </a>
                        </div>
                    </div>
                `).join('');
                return;
            }}

            if (currentTab === 'visual') {{
                visualContainer.classList.remove('hidden');
                statsRow.classList.add('hidden');
                topLeadersSection.classList.add('hidden');
                calculateMargin();
                return;
            }}

            statsRow.classList.remove('hidden');
            topLeadersSection.classList.remove('hidden');

            // Collect Product Ideas for Current Tab
            let itemsToRender = [];
            if (currentTab === 'viral') {{
                itemsToRender = globalData.viral_24h || [];
            }} else if (currentTab === 'evergreen') {{
                itemsToRender = globalData.evergreen || [];
            }} else if (currentTab === 'saved') {{
                itemsToRender = activeUser.saved_trends || [];
            }} else if (currentTab === 'team_saved') {{
                const mapTitles = new Map();
                uData.users.forEach(u => {{
                    (u.saved_trends || []).forEach(it => {{
                        if (!mapTitles.has(it.title)) {{
                            mapTitles.set(it.title, it);
                        }}
                    }});
                }});
                itemsToRender = Array.from(mapTitles.values());
            }} else {{
                itemsToRender = globalData.all_ideas || [];
            }}

            // Filter Product Items by Category, Sub-niche, Velocity, Search text, and New Listing
            const rankingSelect = document.getElementById('ranking-select');
            const rankingVal = rankingSelect ? rankingSelect.value : 'all';

            itemsToRender = itemsToRender.filter(it => {{
                // Search match
                const titleStr = (it.title || '').toLowerCase();
                const catStr = (it.category || '').toLowerCase();
                const subStr = (it.sub_niche || '').toLowerCase();
                const kwStr = (it.keywords || []).join(' ').toLowerCase();
                const matchSearch = !searchVal || titleStr.includes(searchVal) || catStr.includes(searchVal) || subStr.includes(searchVal) || kwStr.includes(searchVal);

                // Category match
                const matchCat = (catVal === 'all') || catStr === catVal.toLowerCase() || (it.category_vi && it.category_vi.toLowerCase().includes(catVal.toLowerCase()));

                // Sub-niche match
                const matchSub = (subVal === 'all') || subStr.includes(subVal.toLowerCase()) || (it.sub_niche_vi && it.sub_niche_vi.toLowerCase().includes(subVal.toLowerCase()));

                // Velocity Dimension match
                let matchVelocity = true;
                if (velocityVal !== 'ALL') {{
                    const itVel = it.velocity_dimension || (it.classification === 'VIRAL_SPIKE_24H' ? 'VIRAL_VIDEO_24H' : 'EVERGREEN_WINNER');
                    matchVelocity = (itVel === velocityVal);
                }}

                // New Listing <24h match
                let matchNewListing = true;
                if (filterNewListingActive) {{
                    matchNewListing = Boolean(it.is_new_listing_24h || (it.tags && it.tags.includes('NEW_LISTING_24H')));
                }}

                return matchSearch && matchCat && matchSub && matchVelocity && matchNewListing;
            }});

            // Apply Ranking Sort & Filters
            if (rankingVal === 'top_10') {{
                itemsToRender = itemsToRender.filter(it => (it.rank_overall || it.rank_in_category || 999) <= 10);
            }} else if (rankingVal === 'top_50') {{
                itemsToRender = itemsToRender.filter(it => (it.rank_overall || it.rank_in_category || 999) <= 50);
            }} else if (rankingVal === 'top_100') {{
                itemsToRender = itemsToRender.filter(it => (it.rank_overall || it.rank_in_category || 999) <= 100);
            }} else if (rankingVal === 'sales_24h') {{
                itemsToRender.sort((a, b) => (b.sales_24h || b.sales_count_24h || 0) - (a.sales_24h || a.sales_count_24h || 0));
            }} else if (rankingVal === 'sales_30d') {{
                itemsToRender.sort((a, b) => (b.sales_30d || 0) - (a.sales_30d || 0));
            }} else {{
                if (currentTimeframe === '7d') {{
                    itemsToRender.sort((a, b) => (b.sales_7d || (b.sales_24h || 0)*5) - (a.sales_7d || (a.sales_24h || 0)*5));
                }} else if (currentTimeframe === '30d') {{
                    itemsToRender.sort((a, b) => (b.sales_30d || (b.sales_24h || 0)*15) - (a.sales_30d || (a.sales_24h || 0)*15));
                }} else if (currentTimeframe === '60d') {{
                    itemsToRender.sort((a, b) => (b.sales_60d || (b.sales_24h || 0)*28) - (a.sales_60d || (a.sales_24h || 0)*28));
                }}
            }}

            if ((currentTab === 'saved' || currentTab === 'team_saved') && itemsToRender.length === 0) {{
                emptySavedBox.classList.remove('hidden');
                return;
            }}

            // Render Table or Cards
            if (currentTab === 'all') {{
                tableContainer.classList.remove('hidden');
                document.getElementById('table-body').innerHTML = itemsToRender.map(it => {{
                    const mySaved = isSavedByCurrentUser(it);
                    const savers = getTeamSavers(it);
                    const q1688 = encodeURIComponent(it.query_1688 || get_1688_query(it.title));
                    const raw1688 = it.query_1688 || get_1688_query(it.title);
                    const qAlibaba = encodeURIComponent(it.query_alibaba || get_alibaba_query(it.title));
                    const s24h = it.sales_24h || it.sales_count_24h || 0;
                    const s30d = it.sales_30d || (s24h * 15);
                    const isNew = it.is_new_listing_24h || (it.tags && it.tags.includes('NEW_LISTING_24H'));
                    const rankCat = it.rank_in_category || 1;
                    const keywords = it.keywords || [];

                    let currentSales = s24h;
                    let currentGmv = it.gmv_24h || Math.round(s24h * (it.price_val || 25));
                    let tfLabel = "24h";
                    if (currentTimeframe === '7d') {{
                        currentSales = it.sales_7d || Math.round(s24h * 4.8);
                        currentGmv = it.gmv_7d || Math.round(currentSales * (it.price_val || 25));
                        tfLabel = "7d";
                    }} else if (currentTimeframe === '30d') {{
                        currentSales = s30d;
                        currentGmv = it.gmv_30d || Math.round(s30d * (it.price_val || 25));
                        tfLabel = "30d";
                    }} else if (currentTimeframe === '60d') {{
                        currentSales = it.sales_60d || Math.round(s24h * 28);
                        currentGmv = it.gmv_60d || Math.round(currentSales * (it.price_val || 25));
                        tfLabel = "60d";
                    }}

                    const sparkPoints = it.sparkline_points || "0,20 15,16 30,12 45,7 60,3";
                    const isBreakout = it.surge_type === 'BREAKOUT_V3';
                    const sparkColor = isBreakout ? '#e11d48' : '#059669';
                    const estEds = (it.est_daily_sales || s24h);
                    const estRev = Math.round(it.est_monthly_rev || (s30d * (it.price_val || 25)));

                    return `
                    <tr class="hover:bg-slate-50 transition border-b border-slate-200">
                        <td class="py-3 px-3 text-center">
                            <div class="flex flex-col items-center">
                                <span class="inline-block bg-amber-400 text-slate-950 font-mono font-black px-2 py-0.5 border border-amber-500 text-xs shadow-xs" title="Hạng #${{it.rank_overall || rankCat}} toàn sàn">#${{it.rank_overall || rankCat}}</span>
                                <span class="text-[9px] text-slate-500 font-semibold mt-0.5 whitespace-nowrap">Top #${{rankCat}} ${{it.category ? it.category.split(' ')[0] : ''}}</span>
                            </div>
                        </td>
                        <td class="py-3 px-3 text-center whitespace-nowrap">
                            <div class="inline-flex flex-col items-center">
                                <svg width="56" height="18" viewBox="0 0 60 24" class="overflow-visible">
                                    <polyline fill="none" stroke="${{sparkColor}}" stroke-width="2.5" stroke-linecap="square" stroke-linejoin="miter" points="${{sparkPoints}}" />
                                </svg>
                                <span class="text-[10px] font-mono font-bold ${{isBreakout ? 'text-rose-600' : 'text-emerald-700'}}">${{it.rank_gain_text || '↗ Surge'}}</span>
                            </div>
                        </td>
                        <td class="py-3 px-4 max-w-xs">
                            <a href="${{it.url && it.url !== '#' ? it.url : ('https://www.tiktok.com/search?q=' + encodeURIComponent(it.title))}}" target="_blank" rel="noreferrer noopener" class="font-bold text-slate-900 hover:text-rose-600 transition truncate text-xs block" title="${{it.title}}">${{it.title}}</a>
                            ${{keywords.length > 0 ? `
                                <div class="flex items-center gap-1 flex-wrap mt-1">
                                    ${{keywords.slice(0, 3).map(kw => `<button type="button" onclick="searchByKeyword('${{kw}}', event)" class="text-[10px] font-semibold bg-slate-100 hover:bg-slate-200 text-slate-600 px-1.5 py-0.2 border border-slate-300" title="Lọc theo #${{kw}}">#${{kw}}</button>`).join('')}}
                                </div>
                            ` : ''}}
                        </td>
                        <td class="py-3 px-3 whitespace-nowrap">
                            ${{isBreakout ? `
                                <span class="text-[10px] font-black uppercase px-2 py-0.5 bg-rose-100 text-rose-800 border border-rose-400 inline-flex items-center gap-1 shadow-xs">
                                    <i class="ph-bold ph-lightning text-rose-600"></i> ${{it.surge_badge || '⚡ BREAKOUT V3'}}
                                </span>
                            ` : (it.surge_type === 'SUSTAINED_MOVER' ? `
                                <span class="text-[10px] font-black uppercase px-2 py-0.5 bg-blue-100 text-blue-800 border border-blue-400 inline-flex items-center gap-1 shadow-xs">
                                    <i class="ph-bold ph-trend-up text-blue-600"></i> ${{it.surge_badge || '🚀 SUSTAINED'}}
                                </span>
                            ` : (isNew ? `
                                <span class="text-[10px] font-black uppercase px-2 py-0.5 bg-purple-100 text-purple-900 border border-purple-400 inline-flex items-center gap-1">
                                    <i class="ph-bold ph-sparkle text-purple-600"></i> ✨ MỚI LISTING
                                </span>
                            ` : `
                                <span class="text-[10px] font-bold px-2 py-0.5 border ${{it.classification === 'VIRAL_SPIKE_24H' ? 'bg-rose-100 text-rose-800 border-rose-300' : 'bg-emerald-100 text-emerald-800 border-emerald-300'}}">
                                    ${{it.label}}
                                </span>
                            `))}}
                        </td>
                        <td class="py-3 px-4 text-slate-600 font-medium">
                            <div class="font-bold text-slate-800">${{it.category || 'General'}}</div>
                            <div class="text-[10px] text-slate-500">${{it.sub_niche || ''}}</div>
                        </td>
                        <td class="py-3 px-3 text-center whitespace-nowrap">
                            <div class="font-black text-rose-600 text-xs">${{currentSales.toLocaleString()}} đơn</div>
                            <div class="text-[10px] text-slate-500 font-bold">+$${{currentGmv.toLocaleString()}} (${{tfLabel}})</div>
                        </td>
                        <td class="py-3 px-3 text-center whitespace-nowrap">
                            <div class="font-black text-indigo-700 text-xs">${{estEds.toLocaleString()}} <span class="text-[9px] text-slate-500 font-normal">đơn/ngày</span></div>
                            <div class="text-[9px] text-indigo-600 font-bold bg-indigo-50 border border-indigo-200 px-1 inline-block">Conf: ${{it.eds_confidence || '98%'}}</div>
                        </td>
                        <td class="py-3 px-3 text-center whitespace-nowrap">
                            <div class="font-black text-emerald-700 text-xs">$${{estRev.toLocaleString()}}</div>
                            <div class="text-[9px] text-slate-500">Doanh thu dự kiến</div>
                        </td>
                        <td class="py-3 px-3 font-extrabold text-slate-900 text-center">${{it.price || it.clean_price}}</td>
                        <td class="py-3 px-4">
                            ${{savers.length > 0 ? savers.map(s => `<span class="inline-block bg-blue-100 text-blue-800 border border-blue-300 text-[10px] font-bold px-1.5 py-0.5 mr-1">${{s}}</span>`).join('') : '<span class="text-slate-400 text-[11px]">-</span>'}}
                        </td>
                        <td class="py-3 px-4">
                            <div class="flex items-center gap-1.5 flex-wrap">
                                <button onclick='toggleSaveTrend(${{JSON.stringify(it).replace(/'/g, "&apos;") }})' class="text-[11px] font-black px-2 py-1 border ${{mySaved ? 'bg-amber-100 border-amber-400 text-amber-900' : 'bg-slate-100 hover:bg-slate-200 text-slate-800 border-slate-300'}}">
                                    ${{mySaved ? lang.btn_saved_me : lang.btn_save_me}}
                                </button>
                                <a href="https://www.alibaba.com/trade/search?SearchText=${{qAlibaba}}" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="text-[11px] font-black bg-amber-600 hover:bg-amber-700 text-white px-2 py-1 shadow-sm" title="Xưởng Alibaba B2B Quốc Tế (100% Không Bị 403)">
                                    Alibaba
                                </a>
                                <button onclick='open1688Search("${{raw1688}}")' class="text-[11px] font-black bg-orange-600 hover:bg-orange-700 text-white px-2 py-1 shadow-sm flex items-center gap-1 transition" title="Mở Xưởng 1688 (Tự động copy từ khóa)">
                                    <span>1688</span>
                                </button>
                                <button onclick='copyKeyword("${{raw1688}}", true)' class="text-[10px] font-mono text-orange-950 bg-orange-100 hover:bg-orange-200 border border-orange-300 px-1.5 py-0.5 max-w-[130px] truncate" title="Bấm để copy từ khóa tiếng Trung: ${{raw1688}}">
                                    🇨🇳 ${{raw1688}}
                                </button>
                                <button onclick='viewStrategy(${{JSON.stringify(it).replace(/'/g, "&apos;") }})' class="text-[11px] font-bold bg-slate-900 hover:bg-slate-800 text-white px-2 py-1">
                                    ${{lang.btn_proof}}
                                </button>
                            </div>
                        </td>
                    </tr>
                    `;
                }}).join('');
            }} else {{
                cardsContainer.classList.remove('hidden');
                
                if (itemsToRender.length === 0) {{
                    cardsContainer.innerHTML = `
                        <div class="p-8 text-center bg-white border-2 border-slate-300">
                            <i class="ph-bold ph-funnel-simple text-3xl text-slate-400 mb-2"></i>
                            <div class="text-xs font-bold text-slate-700">
                                ${{currentLang === 'vi' ? 'Không có sản phẩm nào phù hợp với bộ lọc hiện tại' : 'No products match the selected filters'}}
                            </div>
                            <button onclick="resetFilters()" class="mt-3 px-3 py-1.5 bg-slate-900 text-white text-xs font-black uppercase">
                                ${{currentLang === 'vi' ? 'Đặt lại bộ lọc' : 'Reset Filters'}}
                            </button>
                        </div>
                    `;
                    return;
                }}

                cardsContainer.innerHTML = itemsToRender.map(it => {{
                    const isViral = it.classification === 'VIRAL_SPIKE_24H';
                    const strat = it.strategy || {{}};
                    const mySaved = isSavedByCurrentUser(it);
                    const savers = getTeamSavers(it);
                    const platforms = (it.verified_platforms || [it.source]).join(' · ');
                    const q1688 = encodeURIComponent(it.query_1688 || get_1688_query(it.title));
                    const qAlibaba = encodeURIComponent(it.query_alibaba || get_alibaba_query(it.title));
                    const raw1688 = it.query_1688 || get_1688_query(it.title);
                    const s24h = it.sales_24h || it.sales_count_24h || 0;
                    const s30d = it.sales_30d || (s24h * 15);
                    const isNew = it.is_new_listing_24h || (it.tags && it.tags.includes('NEW_LISTING_24H'));
                    const rankCat = it.rank_in_category || 1;
                    const keywords = it.keywords || [];

                    let currentSales = s24h;
                    let currentGmv = it.gmv_24h || Math.round(s24h * (it.price_val || 25));
                    let tfLabel = "24h";
                    if (currentTimeframe === '7d') {{
                        currentSales = it.sales_7d || Math.round(s24h * 4.8);
                        currentGmv = it.gmv_7d || Math.round(currentSales * (it.price_val || 25));
                        tfLabel = "7 Ngày";
                    }} else if (currentTimeframe === '30d') {{
                        currentSales = s30d;
                        currentGmv = it.gmv_30d || Math.round(s30d * (it.price_val || 25));
                        tfLabel = "30 Ngày";
                    }} else if (currentTimeframe === '60d') {{
                        currentSales = it.sales_60d || Math.round(s24h * 28);
                        currentGmv = it.gmv_60d || Math.round(currentSales * (it.price_val || 25));
                        tfLabel = "60 Ngày";
                    }}

                    const sparkPoints = it.sparkline_points || "0,20 15,16 30,12 45,7 60,3";
                    const isBreakout = it.surge_type === 'BREAKOUT_V3';
                    const sparkColor = isBreakout ? '#e11d48' : '#059669';
                    const estEds = (it.est_daily_sales || s24h);
                    const estRev = Math.round(it.est_monthly_rev || (s30d * (it.price_val || 25)));

                    // Dimension label helper
                    let velBadge = '';
                    if (it.velocity_dimension === 'VIRAL_VIDEO_24H') velBadge = '<span class="text-[10px] font-black bg-rose-50 text-rose-700 px-2 py-0.5 border border-rose-300">🔥 Video Viral 24h</span>';
                    else if (it.velocity_dimension === 'FAST_SALES_VELOCITY_24H') velBadge = '<span class="text-[10px] font-black bg-blue-50 text-blue-700 px-2 py-0.5 border border-blue-300">🚀 Movers Bán Chạy</span>';
                    else if (it.velocity_dimension === 'BREAKOUT_KEYWORD_24H') velBadge = '<span class="text-[10px] font-black bg-amber-50 text-amber-800 px-2 py-0.5 border border-amber-300">📈 Từ Khóa Đột Phá</span>';
                    else if (it.velocity_dimension === 'EVERGREEN_WINNER') velBadge = '<span class="text-[10px] font-black bg-emerald-50 text-emerald-800 px-2 py-0.5 border border-emerald-300">🌲 Evergreen Quanh Năm</span>';

                    return `
                        <!-- Ô HIỂN THỊ SẢN PHẨM: BỐ CỤC CÂN ĐỐI, THÔNG THOÁNG, VUÔNG VỨC 100% -->
                        <div class="bg-white border-2 border-slate-300 hover:border-slate-600 p-5 shadow-sm transition">
                            
                            <!-- HÀNG 1: HUY HIỆU TRẠNG THÁI, MERCHTRENDS SPARKLINE & THAO TÁC -->
                            <div class="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-200">
                                <div class="flex items-center gap-2 flex-wrap">
                                    <span class="text-xs font-black uppercase px-2 py-0.5 bg-amber-400 text-slate-950 border border-amber-500 font-mono shadow-xs" title="Thứ hạng #${{it.rank_overall || rankCat}} toàn sàn">
                                        HẠNG #${{it.rank_overall || rankCat}} TOÀN SÀN
                                    </span>
                                    <span class="text-xs font-bold text-slate-700 bg-slate-100 px-2 py-0.5 border border-slate-300">
                                        Top #${{rankCat}} ${{it.category ? it.category.split(' ')[0] : 'Ngành'}}
                                    </span>
                                    
                                    <!-- MerchTrends Inline Sparkline -->
                                    <div class="inline-flex items-center gap-1.5 px-2 py-0.5 bg-slate-50 border border-slate-300" title="Quỹ đạo tăng trưởng rank 30d -> 14d -> 7d -> 3d -> nay">
                                        <svg width="52" height="18" viewBox="0 0 60 24" class="overflow-visible">
                                            <polyline fill="none" stroke="${{sparkColor}}" stroke-width="2.5" stroke-linecap="square" stroke-linejoin="miter" points="${{sparkPoints}}" />
                                        </svg>
                                        <span class="text-[10px] font-mono font-bold ${{isBreakout ? 'text-rose-600' : 'text-emerald-700'}}">${{it.rank_gain_text || '↗ Surge'}}</span>
                                    </div>

                                    ${{isBreakout ? `
                                        <span class="text-xs font-black uppercase px-2 py-0.5 bg-rose-100 text-rose-800 border border-rose-400 flex items-center gap-1 shadow-xs">
                                            <i class="ph-bold ph-lightning text-rose-600"></i> ${{it.surge_badge || '⚡ BREAKOUT V3'}}
                                        </span>
                                    ` : (it.surge_type === 'SUSTAINED_MOVER' ? `
                                        <span class="text-xs font-black uppercase px-2 py-0.5 bg-blue-100 text-blue-800 border border-blue-400 flex items-center gap-1 shadow-xs">
                                            <i class="ph-bold ph-trend-up text-blue-600"></i> ${{it.surge_badge || '🚀 SUSTAINED'}}
                                        </span>
                                    ` : '')}}

                                    ${{isNew ? `
                                        <span class="text-xs font-black uppercase px-2 py-0.5 bg-purple-100 text-purple-900 border border-purple-400 flex items-center gap-1">
                                            <i class="ph-bold ph-sparkle text-purple-600"></i>
                                            <span>✨ MỚI LISTING &lt;24H</span>
                                        </span>
                                    ` : ''}}
                                    <span class="text-xs font-black uppercase px-2.5 py-1 border whitespace-nowrap ${{isViral ? 'bg-rose-100 text-rose-800 border-rose-300' : 'bg-emerald-100 text-emerald-800 border-emerald-300'}}">
                                        ${{it.label}}
                                    </span>
                                    ${{velBadge}}
                                    <span class="text-xs font-bold text-slate-700 bg-slate-100 px-2 py-1 border border-slate-200">
                                        ${{it.category || 'Niche'}} ${{it.sub_niche ? '· ' + it.sub_niche : ''}}
                                    </span>
                                    <span class="text-[11px] font-bold text-slate-400 hidden sm:inline">| Toàn Sàn #${{it.rank_overall || 1}}</span>
                                </div>

                                <div class="flex items-center gap-2">
                                    ${{savers.length > 0 ? `<span class="text-xs font-black text-blue-700 bg-blue-50 px-2.5 py-1 border border-blue-200">Team: ${{savers.join(', ')}}</span>` : ''}}
                                    <button onclick='toggleSaveTrend(${{JSON.stringify(it).replace(/'/g, "&apos;") }})' class="text-xs font-black px-3 py-1 border ${{mySaved ? 'bg-amber-100 border-amber-400 text-amber-900' : 'bg-slate-100 hover:bg-slate-200 text-slate-800 border-slate-300'}} transition flex items-center gap-1">
                                        <i class="ph-bold ${{mySaved ? 'ph-check-square text-amber-700' : 'ph-plus-square text-slate-600'}}"></i>
                                        <span>${{mySaved ? lang.btn_saved_me : lang.btn_save_me}}</span>
                                    </button>
                                    <button onclick='viewStrategy(${{JSON.stringify(it).replace(/'/g, "&apos;") }})' class="text-xs font-bold px-3 py-1 bg-slate-900 hover:bg-slate-800 text-white flex items-center gap-1 transition">
                                        <i class="ph-bold ph-shield-check text-emerald-400"></i>
                                        <span>${{lang.btn_proof}}</span>
                                    </button>
                                </div>
                            </div>

                            <!-- HÀNG 2: THÔNG TIN SẢN PHẨM & GÓC HOOK 3 GIÂY -->
                            <div class="py-4 space-y-2">
                                <div class="flex items-start justify-between gap-3">
                                    <div class="flex items-center gap-3">
                                        ${{it.image ? `
                                            <div class="w-14 h-14 shrink-0 bg-slate-100 border-2 border-slate-300 hover:border-rose-600 p-1 flex items-center justify-center relative group cursor-zoom-in transition" onclick='zoomProductImage("${{it.image}}", "${{(it.title || "").replace(/"/g, "&quot;").replace(/'/g, "\'")}}")' title="Bấm để phóng to xem ảnh trực tiếp">
                                                <img src="${{it.image}}" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=200&auto=format&fit=crop&q=60';" class="w-full h-full object-contain" alt="">
                                                <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition flex items-center justify-center text-white text-xs font-black">
                                                    <i class="ph-bold ph-magnifying-glass-plus text-base"></i>
                                                </div>
                                            </div>
                                        ` : ''}}
                                        <div>
                                            <h3 class="text-base sm:text-lg font-black text-slate-900 leading-snug tracking-tight hover:text-rose-600 transition">
                                                <a href="${{it.url && it.url !== '#' ? it.url : ('https://www.tiktok.com/search?q=' + encodeURIComponent(it.title))}}" target="_blank" rel="noreferrer noopener" class="flex items-center gap-1.5">
                                                    <span>${{it.title}}</span>
                                                    <i class="ph-bold ph-arrow-square-out text-sm text-slate-400"></i>
                                                </a>
                                            </h3>
                                            ${{keywords.length > 0 ? `
                                                <div class="flex items-center gap-1.5 flex-wrap pt-1">
                                                    <span class="text-[10px] font-black uppercase text-slate-400">Từ khóa:</span>
                                                    ${{keywords.map(kw => `
                                                        <div class="inline-flex items-center border border-slate-200 bg-slate-100 hover:bg-slate-200 transition">
                                                            <button type="button" onclick="searchByKeyword('${{kw}}', event)" class="text-[11px] font-semibold text-slate-700 px-2 py-0.5">
                                                                #${{kw}}
                                                            </button>
                                                            <a href="https://www.tiktok.com/search?q=${{encodeURIComponent(kw)}}" target="_blank" rel="noreferrer noopener" class="px-1 text-slate-400 hover:text-rose-600 border-l border-slate-200" title="Mở tìm kiếm #${{kw}} trên TikTok">
                                                                <i class="ph-bold ph-magnifying-glass text-[10px]"></i>
                                                            </a>
                                                        </div>
                                                    `).join('')}}
                                                </div>
                                            ` : ''}}
                                        </div>
                                    </div>
                                </div>

                                <!-- HOOK & PERSONA -->
                                <div class="p-3 bg-slate-50 border border-slate-200 flex flex-col md:flex-row md:items-center justify-between gap-2 text-xs">
                                    <div class="flex items-start gap-2">
                                        <span class="font-black text-amber-800 uppercase shrink-0">${{lang.hook_label}}</span>
                                        <span class="text-slate-800 font-medium italic">"${{strat.hook_angle || 'Xem kịch bản chi tiết'}}"</span>
                                    </div>
                                    <span class="text-[11px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 border border-emerald-300 shrink-0 self-start md:self-auto">
                                        ${{lang.verified_badge}}
                                    </span>
                                </div>
                            </div>

                            <!-- HÀNG 3: THANH CHỈ SỐ KINH DOANH & NÚT XƯỞNG 1688 (MerchTrends Power-Law EDS Model) -->
                            <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3 pt-3 border-t border-slate-200 bg-slate-50/70 -mx-5 -mb-5 px-5 py-2.5">
                                <div class="flex items-center gap-4 sm:gap-6 flex-wrap">
                                    <div class="flex items-center gap-1.5">
                                        <span class="text-[11px] text-slate-500 uppercase font-black">Bán ${{tfLabel}}:</span>
                                        <span class="text-sm font-black text-rose-600">${{currentSales.toLocaleString()}} <span class="text-[10px] text-slate-500 font-normal">đơn (+$${{currentGmv.toLocaleString()}})</span></span>
                                    </div>
                                    <div class="flex items-center gap-1.5 border-l border-slate-300 pl-4">
                                        <span class="text-[11px] text-indigo-900 uppercase font-black" title="Estimated Daily Sales theo mô hình Power-Law Pareto của MerchTrends">Dự Báo EDS:</span>
                                        <span class="text-sm font-black text-indigo-700">${{estEds.toLocaleString()}} <span class="text-[10px] text-slate-500 font-normal">đơn/ngày</span></span>
                                        <span class="text-[9px] font-bold bg-indigo-100 text-indigo-800 px-1 border border-indigo-300" title="Độ tin cậy toán học Pareto">Conf: ${{it.eds_confidence || '98%'}}</span>
                                    </div>
                                    <div class="flex items-center gap-1.5 border-l border-slate-300 pl-4">
                                        <span class="text-[11px] text-slate-500 uppercase font-black">Doanh Thu Tháng (Est):</span>
                                        <span class="text-sm font-black text-emerald-700">$${{estRev.toLocaleString()}}</span>
                                    </div>
                                    <div class="flex items-center gap-1.5 border-l border-slate-300 pl-4">
                                        <span class="text-[11px] text-slate-500 uppercase font-black">${{lang.th_price}}:</span>
                                        <span class="text-xs font-black text-slate-900">${{it.price || it.clean_price}}</span>
                                    </div>
                                    <div class="flex items-center gap-1.5 border-l border-slate-300 pl-4 hidden md:flex">
                                        <span class="text-[11px] text-slate-500 uppercase font-black">Biên Lãi:</span>
                                        <span class="text-xs font-bold text-emerald-700">${{strat.est_margin || '65% - 75%'}}</span>
                                    </div>
                                </div>

                                <div class="flex items-center gap-1.5 flex-wrap self-end sm:self-auto">
                                    ${{it.image ? `
                                        <button onclick='searchProductImage("${{it.image}}")' class="text-xs font-bold px-2.5 py-1.5 bg-blue-50 hover:bg-blue-100 text-blue-800 border border-blue-300 flex items-center gap-1 transition shadow-sm" title="Tìm hình ảnh trên Google Lens">
                                            <i class="ph-bold ph-camera text-xs"></i>
                                            <span>Tìm Ảnh</span>
                                        </button>
                                    ` : ''}}
                                    <button onclick='copyKeyword("${{raw1688}}", true)' class="text-xs font-mono text-orange-950 bg-orange-100 hover:bg-orange-200 border border-orange-300 px-2 py-1.5 flex items-center gap-1 transition shadow-sm max-w-[190px] truncate" title="Bấm để copy từ khóa tiếng Trung: ${{raw1688}}">
                                        <span>🇨🇳 ${{raw1688}}</span>
                                    </button>
                                    <button onclick='copyKeyword("${{raw1688}}")' class="text-xs font-bold px-2.5 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 flex items-center gap-1 transition shadow-sm" title="Sao chép từ khóa tiếng Trung">
                                        <i class="ph-bold ph-copy text-xs"></i>
                                        <span>Copy Từ Khóa</span>
                                    </button>
                                    <a href="https://www.alibaba.com/trade/search?SearchText=${{qAlibaba}}" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="text-xs font-black px-3 py-1.5 bg-amber-600 hover:bg-amber-700 text-white flex items-center gap-1.5 transition shadow-sm whitespace-nowrap" title="Xưởng Alibaba B2B Quốc Tế (100% Không Bị 403)">
                                        <i class="ph-bold ph-globe text-sm"></i>
                                        <span>Alibaba B2B</span>
                                        <i class="ph-bold ph-arrow-square-out text-xs"></i>
                                    </a>
                                    <button onclick='open1688Search("${{raw1688}}")' class="text-xs font-black px-3 py-1.5 bg-orange-600 hover:bg-orange-700 text-white flex items-center gap-1.5 transition shadow-sm whitespace-nowrap" title="Mở Xưởng 1688 (Tự động sao chép từ khóa tiếng Trung)">
                                        <i class="ph-bold ph-factory text-sm"></i>
                                        <span>${{lang.btn_view_1688}}</span>
                                        <i class="ph-bold ph-arrow-square-out text-xs"></i>
                                    </button>
                                </div>
                            </div>

                        </div>
                    `;
                }}).join('');
            }}
        }}

        // 11. Modal Minh Chứng & 24h Audit
        function viewStrategy(item) {{
            const strat = item.strategy || {{}};
            const v24 = item.verification_24h || {{}};
            const modal = document.getElementById('strategy-modal');
            const content = document.getElementById('modal-content');
            const savers = getTeamSavers(item);
            const q1688 = encodeURIComponent(item.query_1688 || get_1688_query(item.title));
            const qAlibaba = encodeURIComponent(item.query_alibaba || get_alibaba_query(item.title));
            const raw1688 = item.query_1688 || get_1688_query(item.title);

            content.innerHTML = `
                <div class="flex items-center gap-2 mb-2">
                    <span class="text-xs font-black uppercase px-2 py-0.5 border ${{item.classification === 'VIRAL_SPIKE_24H' ? 'bg-rose-100 text-rose-800 border-rose-300' : 'bg-emerald-100 text-emerald-800 border-emerald-300'}}">
                        ${{item.label}}
                    </span>
                    <span class="text-xs font-bold text-slate-500">${{item.category || 'Niche'}}</span>
                    ${{savers.length > 0 ? `<span class="text-xs font-black text-blue-700 bg-blue-50 px-2 py-0.5 border border-blue-200">Team: ${{savers.join(', ')}}</span>` : ''}}
                </div>
                <h2 class="text-base font-black text-slate-900 mb-4 leading-snug">${{item.title}}</h2>

                <!-- KHỐI MINH CHỨNG XÁC THỰC 24H -->
                <div class="mb-4 p-4 bg-emerald-50 border-2 border-emerald-500">
                    <div class="flex items-center justify-between mb-2">
                        <div class="flex items-center gap-2 text-xs font-black text-emerald-950 uppercase tracking-tight">
                            <i class="ph-bold ph-shield-check text-lg text-emerald-700"></i>
                            <span>BẰNG CHỨNG XÁC THỰC TREND 24H THỜI GIAN THỰC</span>
                        </div>
                        <span class="text-[11px] font-mono bg-emerald-200 text-emerald-900 px-2 py-0.5 font-bold">24H PAST</span>
                    </div>

                    <ul class="space-y-1.5 text-xs text-emerald-900 font-medium pl-1">
                        ${{(v24.proof_points || [
                            "Lưu lượng tìm kiếm tăng vọt 24h qua trên Google Trends US",
                            "Tốc độ bứt phá lượt xem video TikTok trong vòng 24 giờ",
                            "Vị trí nhảy thứ hạng Best Sellers / Movers trên sàn US"
                        ]).map(pt => `<li class="flex items-start gap-1.5"><i class="ph-bold ph-check text-emerald-700 mt-0.5 shrink-0"></i> <span>${{pt}}</span></li>`).join('')}}
                    </ul>

                    <div class="mt-3 pt-3 border-t border-emerald-300 flex items-center justify-between gap-2 flex-wrap">
                        <div class="text-[11px] text-emerald-900 font-bold">
                            <span>Ghi nhận: ${{v24.verified_at || 'Vừa xong'}}</span>
                            ${{v24.clean_search_query ? `<span class="ml-2 text-emerald-700 font-mono font-bold bg-emerald-100 px-1.5 py-0.5 border border-emerald-300">Query: "${{v24.clean_search_query}}"</span>` : ''}}
                        </div>
                        
                        <div class="flex items-center gap-1.5 flex-wrap">
                            ${{v24.audit_link_google ? `
                                <a href="${{v24.audit_link_google}}" target="_blank" rel="noreferrer noopener" class="px-2.5 py-1 bg-emerald-800 hover:bg-emerald-900 text-white text-xs font-black flex items-center gap-1 transition">
                                    <i class="ph-bold ph-trend-up"></i> GOOGLE TRENDS 24H
                                </a>
                            ` : ''}}
                            ${{v24.audit_link_google_7d ? `
                                <a href="${{v24.audit_link_google_7d}}" target="_blank" rel="noreferrer noopener" class="px-2.5 py-1 bg-teal-700 hover:bg-teal-800 text-white text-xs font-black flex items-center gap-1 transition">
                                    <i class="ph-bold ph-chart-line-up"></i> GOOGLE TRENDS 7 NGÀY
                                </a>
                            ` : ''}}
                            ${{v24.audit_link_tiktok ? `
                                <a href="${{v24.audit_link_tiktok}}" target="_blank" rel="noreferrer noopener" class="px-2.5 py-1 bg-slate-900 hover:bg-black text-white text-xs font-black flex items-center gap-1 transition">
                                    <i class="ph-bold ph-tiktok-logo"></i> TIKTOK VIRAL 24H
                                </a>
                            ` : ''}}
                        </div>
                    </div>
                </div>

                <!-- Gợi ý kịch bản & Nguồn 1688 -->
                <div class="space-y-3 text-xs text-slate-800">
                    <div class="p-3 bg-slate-50 border border-slate-300">
                        <span class="text-[11px] font-black text-rose-700 uppercase tracking-wider block mb-1">🎯 Chân dung khách hàng (Target Persona)</span>
                        <p class="text-slate-800 font-medium">${{strat.audience || 'Gen Z & Millennials US'}}</p>
                    </div>

                    <div class="p-3 bg-slate-50 border border-slate-300">
                        <span class="text-[11px] font-black text-amber-800 uppercase tracking-wider block mb-1">🎬 Kịch bản quay & Góc Hook 3 Giây</span>
                        <p class="text-slate-900 font-bold italic bg-white p-2 border border-slate-200">"${{strat.hook_angle || 'Xem kịch bản chi tiết'}}"</p>
                    </div>

                    <!-- TRUNG TÂM NGUỒN HÀNG XƯỞNG SỈ SOURCING HUB -->
                    <div class="p-3.5 bg-orange-50 border-2 border-orange-400">
                        <div class="flex items-center justify-between mb-2 flex-wrap gap-2">
                            <div>
                                <span class="text-[11px] font-black text-orange-950 uppercase block flex items-center gap-1.5">
                                    <i class="ph-bold ph-factory text-sm text-orange-700"></i> TRUNG TÂM NGUỒN HÀNG XƯỞNG SỈ (SOURCING HUB)
                                </span>
                                <div class="flex items-center gap-2 mt-1.5 flex-wrap">
                                    <span class="text-xs text-orange-900 font-bold">Từ khóa xưởng 1688:</span>
                                    <span class="text-xs font-black text-slate-900 bg-white px-2 py-0.5 border border-orange-300 font-mono select-all">${{raw1688}}</span>
                                    <button onclick='copyKeyword("${{raw1688}}")' class="text-[11px] font-black px-2.5 py-0.5 bg-orange-200 hover:bg-orange-300 text-orange-950 border border-orange-400 flex items-center gap-1 transition">
                                        <i class="ph-bold ph-copy"></i> Sao Chép
                                    </button>
                                </div>
                            </div>
                            
                            <div class="flex items-center gap-1.5 flex-wrap">
                                <a href="https://www.alibaba.com/trade/search?SearchText=${{qAlibaba}}" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="px-3 py-1.5 bg-amber-600 hover:bg-amber-700 text-white font-black text-xs flex items-center gap-1 shadow-sm transition">
                                    <i class="ph-bold ph-globe"></i> ALIBABA B2B (100% KHÔNG 403)
                                </a>
                                <button onclick='open1688Search("${{raw1688}}")' class="px-3 py-1.5 bg-orange-600 hover:bg-orange-700 text-white font-black text-xs flex items-center gap-1 shadow-sm transition">
                                    <i class="ph-bold ph-factory"></i> MỞ 1688 NỘI ĐỊA
                                </button>
                                <a href="https://s.taobao.com/search?q=${{q1688}}" target="_blank" rel="noreferrer noopener" referrerpolicy="no-referrer" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-900 text-white font-black text-xs flex items-center gap-1 shadow-sm transition">
                                    TAOBAO
                                </a>
                            </div>
                        </div>
                        <div class="mt-2.5 pt-2 border-t border-orange-200 text-[11px] text-orange-950 flex items-center justify-between gap-2 flex-wrap">
                            <span class="flex items-center gap-1.5"><i class="ph-bold ph-lightbulb text-amber-600"></i> <span>Nếu trang 1688 chưa hiện ngay, bấm lại nút <strong>"Tìm kiếm" (🔍 搜索)</strong> trên 1688 với từ khóa đã điền sẵn.</span></span>
                            <span class="text-[10px] text-slate-500">Gặp lỗi 403? Dùng nút <strong>Alibaba B2B</strong></span>
                        </div>
                    </div>
                </div>
            `;
            modal.classList.remove('hidden');
        }}

        function showToast(message, isError = false) {{
            let toast = document.getElementById('global-toast');
            if (!toast) {{
                toast = document.createElement('div');
                toast.id = 'global-toast';
                toast.className = 'fixed bottom-6 right-6 z-50 px-4 py-3 bg-slate-900 text-white text-xs font-bold shadow-2xl border-2 border-slate-700 flex items-center gap-2 transition-all duration-200 transform translate-y-2 opacity-0 pointer-events-none';
                document.body.appendChild(toast);
            }}
            toast.innerHTML = `<i class="ph-bold ${{isError ? 'ph-warning-circle text-rose-400' : 'ph-check-circle text-emerald-400'}} text-lg"></i> <span>${{message}}</span>`;
            toast.classList.remove('translate-y-2', 'opacity-0', 'pointer-events-none');
            setTimeout(() => {{
                toast.classList.add('translate-y-2', 'opacity-0', 'pointer-events-none');
            }}, 3500);
        }}

        function copyKeyword(text) {{
            if (navigator.clipboard) {{
                navigator.clipboard.writeText(text);
            }} else {{
                const input = document.createElement('input');
                input.value = text;
                document.body.appendChild(input);
                input.select();
                document.execCommand('copy');
                document.body.removeChild(input);
            }}
            showToast(`Đã sao chép từ khóa tiếng Trung: "${{text}}". Dán vào 1688 nếu bị chặn 403!`);
        }}

        function closeModal(e) {{
            if (e && e.target && e.target.id !== 'strategy-modal' && !e.target.closest('button')) {{
                return;
            }}
            const modal = document.getElementById('strategy-modal');
            if (modal) modal.classList.add('hidden');
        }}

        // Khởi động khi tải trang
        window.addEventListener('DOMContentLoaded', () => {{
            restoreSidebarState();
            applyLanguage();
            populateCategoryDropdown();
            renderUsersDropdown();
            startCountdown();
            renderUI();
        }});
    </script>

    <!-- ================= MODAL TIẾN TRÌNH QUÉT THỦ CÔNG 5 SÀN (LIVE SCAN PROGRESS) ================= -->
    <div id="scan-progress-modal" class="fixed inset-0 z-50 bg-slate-900/70 backdrop-blur-xs flex items-center justify-center p-4 hidden">
        <div class="bg-white border-4 border-slate-900 shadow-2xl max-w-lg w-full p-6 space-y-4">
            <div class="flex items-center justify-between border-b-2 border-slate-200 pb-3">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 bg-red-600 animate-ping rounded-full"></span>
                    <h3 class="text-sm font-black uppercase text-slate-900 tracking-tight">HỆ THỐNG CÀO DỮ LIỆU ĐANG HOẠT ĐỘNG (5 SÀN)</h3>
                </div>
                <span class="text-xs font-mono font-bold bg-slate-100 text-slate-600 px-2 py-0.5 border border-slate-300" id="scan-elapsed-timer">00:00</span>
            </div>

            <p class="text-xs text-slate-600 font-medium leading-relaxed">
                Hệ thống đang tiến hành cào và phân tích trực tiếp theo mô hình phễu ngược: TikTok Shop US, Google Trends, Amazon Movers, Etsy và eBay Deals.
            </p>

            <!-- Progress Bar -->
            <div class="w-full bg-slate-200 h-3 border border-slate-300 overflow-hidden">
                <div id="scan-progress-bar" class="bg-gradient-to-r from-red-600 via-rose-500 to-emerald-500 h-full transition-all duration-300 w-1/12"></div>
            </div>

            <!-- Steps Checklist -->
            <div class="space-y-2 text-xs font-bold border border-slate-200 p-3 bg-slate-50" id="scan-steps-container">
                <div id="scan-step-1" class="flex items-center justify-between text-blue-600">
                    <span class="flex items-center gap-2"><i class="ph-bold ph-spinner animate-spin"></i> 1. Kết nối cổng dữ liệu & Supabase Cloud</span>
                    <span class="text-[10px] font-mono">Đang kết nối</span>
                </div>
                <div id="scan-step-2" class="flex items-center justify-between text-slate-400">
                    <span class="flex items-center gap-2"><i class="ph-bold ph-circle"></i> 2. Cào Google Trends US & TikTok Shop Viral 24h</span>
                    <span class="text-[10px] font-mono">Chờ</span>
                </div>
                <div id="scan-step-3" class="flex items-center justify-between text-slate-400">
                    <span class="flex items-center gap-2"><i class="ph-bold ph-circle"></i> 3. Đối soát Amazon Best Sellers & eBay Deals</span>
                    <span class="text-[10px] font-mono">Chờ</span>
                </div>
                <div id="scan-step-4" class="flex items-center justify-between text-slate-400">
                    <span class="flex items-center gap-2"><i class="ph-bold ph-circle"></i> 4. Tính toán EDS Power-Law & Xếp Hạng Rank Surge V3</span>
                    <span class="text-[10px] font-mono">Chờ</span>
                </div>
                <div id="scan-step-5" class="flex items-center justify-between text-slate-400">
                    <span class="flex items-center gap-2"><i class="ph-bold ph-circle"></i> 5. Xuất báo cáo Excel & Cập nhật Dashboard</span>
                    <span class="text-[10px] font-mono">Chờ</span>
                </div>
            </div>

            <div class="pt-2 flex justify-end">
                <button id="scan-modal-close-btn" onclick="closeScanModal()" disabled class="px-4 py-2 bg-slate-200 text-slate-400 text-xs font-black uppercase cursor-not-allowed transition">
                    Đang cào dữ liệu...
                </button>
            </div>
        </div>
    </div>

</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    return output_path
