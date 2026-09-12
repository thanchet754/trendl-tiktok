"""
Strategy Generator: Generates actionable TikTok Shop Selling Playbooks, Hooks, and Demographics.
"""

from typing import Dict, Any

def generate_tiktok_strategy(item: Dict[str, Any], score_data: Dict[str, Any]) -> Dict[str, Any]:
    title = item.get("title", "")
    t_lower = title.lower()
    cat = item.get("category", "").lower()
    c_type = score_data.get("classification", "VIRAL_SPIKE_24H")
    
    # Check if item already has a verified authentic hook from TikTok or Etsy collector
    existing_hook = item.get("hook_style") or item.get("hook_angle")
    existing_margin = item.get("margin") or item.get("est_margin")
    
    # 1. Beauty & Skincare (Including Face Towels, Toner Pads, Pimple Patches, Lip Masks)
    if (any(k in t_lower for k in ["towel", "cleanskin", "clean skin", "facetowel", "biobased", "cotton tissue"]) and any(k in t_lower or k in cat for k in ["skin", "beauty", "face", "towel"])) or \
       any(k in t_lower for k in ["makeup", "toner", "skincare", "lotion", "pore", "lip", "acne", "patch", "serum", "mucin", "cleanser", "collagen", "sunscreen"]) or \
       "beauty" in cat or "skin" in cat:
        audience = "Gen Z & Millennials (18-34 tuổi), Chăm sóc da mụn, tín đồ Skincare & 'Clean Girl' aesthetic US."
        if any(k in t_lower for k in ["towel", "clean skin", "biobased"]):
            hook_angle = existing_hook or "Microscope Gross-Out Angle: 'Dừng ngay việc dùng khăn tắm vi khuẩn lau mặt nếu không muốn mụn viêm tái phát!'"
            format_type = "Problem - Agitate - Solution (So sánh vi khuẩn kính hiển vi)"
            est_margin = "70% - 82% (Source $3.5 - $5.0 -> Bán $15.95 - $17.95)"
        else:
            hook_angle = existing_hook or "Before & After cận cảnh lỗ chân lông: 'Dừng ngay nếu bạn vẫn đang nặn mụn hoặc dùng tẩy tế bào chết hạt to!'"
            format_type = "Before/After Macro Skin Texture Zoom (Cận cảnh bề mặt da)"
            est_margin = "70% - 85% (Source $3.5 - $6.0 -> Bán $18.99 - $24.99)"
        call_to_action = "Bấm vào giỏ hàng màu vàng góc dưới nhận voucher freeship hôm nay!"

    # 2. Pets & Animals (Must check before general cleaning keywords)
    elif any(k in t_lower for k in ["pet", "dog", "cat", "puppy", "kitten", "fur", "deshedding", "slicker", "grooming"]) or "pet" in cat:
        audience = "Hội những người 'nghiện' chó mèo (Dog/Cat Parents) tại US, chi tiêu mạnh tay cho thú cưng."
        hook_angle = existing_hook or "Âm thanh bấm nút nhả cả búi lông chó rụng chỉ trong 1 giây: 'Mùa rụng lông không còn là ác mộng!'"
        format_type = "Emotional Reaction & Satisfying Fur Release ASMR"
        est_margin = "75% - 85% (Source $2.0 - $4.0 -> Bán $11.99 - $16.99)"
        call_to_action = "Bảo vệ đường hô hấp cho cả nhà, sắm ngay chiếc lược tự nhả lông này!"

    # 3. Drinkware / Tumbler / Bottles
    elif any(k in t_lower for k in ["tumbler", "bottle", "cup", "owala", "stanley", "mug", "flask"]):
        audience = "Học sinh/Sinh viên US, Dân văn phòng, Người đi tập Gym & Pilates yêu thích đồ cute, thẩm mỹ."
        hook_angle = existing_hook or "Thử nghiệm dốc ngược bình lắc mạnh: 'Review bình chống tràn 100% đánh bại hoàn toàn cốc Stanley!'"
        format_type = "Drop Test & Leak-proof Challenge (Thử thách va đập & chống đổ nước)"
        est_margin = "60% - 75% (Source $6.0 - $9.0 -> Bán $24.99 - $37.99)"
        call_to_action = "Màu hot này liên tục cháy hàng, click giỏ hàng đặt ngay kẻo hết size!"

    # 4. Bathroom & Home Deep Cleaning Gadgets (Only true cleaning appliances)
    elif any(k in t_lower for k in ["scrubber", "spin scrubber", "shower clean", "vacuum", "mop", "stain remover", "electric brush"]):
        audience = "Các mẹ bỉm sữa, Người độc thân yêu nhà cửa gọn gàng, Hội nghiện dọn dẹp CleanTok US."
        hook_angle = existing_hook or "Góc quay cận cảnh vết bẩn lâu năm trong nhà tắm bay sạch sau 30 giây bấm nút."
        format_type = "Satisfying Deep Clean ASMR (Âm thanh chà sạch cực đã tai)"
        est_margin = "65% - 75% (Source $8.0 - $14.0 -> Bán $29.99 - $49.99)"
        call_to_action = "Cứu rỗi cái lưng và đầu gối khi cọ nhà tắm, số lượng ưu đãi có hạn trong giỏ hàng!"

    # 5. Tech Gadgets & Creator Gear
    elif any(k in t_lower for k in ["printer", "mic", "microphone", "charger", "gadget", "bluetooth", "watch", "lavalier", "earbuds", "thermal"]):
        audience = "Học sinh, Gen Z làm bullet journal, Content Creator quay video TikTok / Vlog tại US."
        hook_angle = existing_hook or "So sánh âm thanh: 'Bật lọc tạp âm và nói chuyện giữa chợ ồn ào xem micro này xịn cỡ nào!'"
        format_type = "Side-by-side Live Demo & Unboxing ASMR"
        est_margin = "68% - 78% (Source $4.0 - $7.5 -> Bán $19.99 - $29.99)"
        call_to_action = "Phụ kiện bắt buộc cho dân làm video TikTok, bấm góc trái đặt hàng liền tay!"

    # 6. Personalized POD & Custom Gifts
    elif any(k in t_lower for k in ["custom", "personalized", "necklace", "gift", "board", "calendar", "engraved", "charcuterie"]) or "handmade" in cat or "pod" in cat:
        audience = "Người tìm quà tặng sinh nhật, kỷ niệm, Mother's Day, quà tân gia ý nghĩa quanh năm."
        hook_angle = existing_hook or "Quá trình máy khắc laser tên khách hàng lên gỗ/kim loại: 'Làm món quà độc nhất vô nhị tặng mẹ...'"
        format_type = "Behind The Scenes Crafting & Emotional Gift Unboxing"
        est_margin = existing_margin or "75% - 88% (Source $4.0 - $8.0 -> Bán $24.00 - $48.00)"
        call_to_action = "Gõ tên người bạn muốn khắc vào ghi chú đơn hàng ngay dưới video!"

    # 7. General TikTok Impulse Buy Fallback
    else:
        audience = "Khách hàng mua sắm ngẫu hứng (Impulse Buyers) trên TikTok Shop US độ tuổi 18 - 45."
        hook_angle = existing_hook or "Đặt câu hỏi trúng nỗi đau thường ngày: 'Tại sao không ai nói cho tôi biết món đồ này sớm hơn?!'"
        format_type = "TikTok Made Me Buy It / Honest Review"
        est_margin = existing_margin or "65% - 75% (Ước tính giá bán $15 - $29)"
        call_to_action = "Xem ngay giá ưu đãi độc quyền hôm nay trên TikTok Shop!"

    # Strategy Summary
    strategy_type = "Chiến dịch Bắt Trend Nhanh (Flash Trend Surge)" if c_type == "VIRAL_SPIKE_24H" else "Xây Kênh Bền Vững & Chạy Quảng Cáo Quanh Năm (Evergreen Flywheel)"

    return {
        "audience": audience,
        "hook_angle": hook_angle,
        "format_type": format_type,
        "est_margin": est_margin,
        "call_to_action": call_to_action,
        "strategy_type": strategy_type
    }
