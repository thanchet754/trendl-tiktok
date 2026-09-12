# TikTok Shop US - Trend & Evergreen Intelligence System (Bản Đa Người Dùng)

Hệ thống cào và phân tích ý tưởng sản phẩm hàng đầu cho **TikTok Shop US**, kết hợp dữ liệu đối soát thời gian thực từ 5 nguồn:
1. **Google Trends (US)**: Daily search trends & rising breakout queries.
2. **TikTok Viral 24h & Creative Center**: Video triệu view 24h, hook angles, tăng trưởng nóng, âm thanh & hashtag hot.
3. **Amazon US**: Best Sellers & Movers & Shakers qua các ngách trọng điểm.
4. **Etsy US**: Các ý tưởng sản phẩm Evergreen, handmade, POD cá nhân hóa có biên lợi nhuận cao.
5. **eBay US**: Trending deals & velocity sản phẩm bán chạy trong ngày.

---

## 🌟 Tính Năng Đa Người Dùng (Multi-User & Team Collaboration)

- **Thêm thành viên không giới hạn**: Nhấp nút **`+ THÊM USER`** trên thanh menu để thêm từng thành viên trong nhóm (VD: *Ngọc - Quản trị, Hoàng - Sourcing, Linh - Content...*).
- **Lưu trend riêng biệt theo từng người**: Mỗi thành viên khi đăng nhập/chọn tên mình có thể bấm **`+ Lưu Cho Tôi`** để lưu các sản phẩm ưng ý vào bộ sưu tập riêng.
- **Tránh trùng lặp ý tưởng (Team Synergy)**: Nếu một thành viên trong nhóm đã lưu sản phẩm đó, trên dòng sản phẩm sẽ tự động hiện nhãn: `👥 Đã lưu: [Tên thành viên]` để cả nhóm nắm được ai đang phụ trách sản phẩm nào.
- **Xem danh sách linh hoạt**:
  - Tab **`📌 Đã Lưu Của Tôi`**: Chỉ xem danh sách sản phẩm của riêng bạn.
  - Tab **`👥 Cả Nhóm Đã Lưu`**: Xem tổng hợp toàn bộ các ý tưởng mà tất cả thành viên trong nhóm đã lưu lại.

---

## 📐 Giao Diện Nền Sáng - Dòng Ngang - Vuông Vức 100%

- **Định dạng Dòng Ngang (Horizontal Rows)**: Mỗi sản phẩm là một dòng ngang trải rộng toàn màn hình, hiển thị đầy đủ tiêu đề, nhãn xác thực 24h, góc quay Hook 3s, điểm số, giá bán và nút thao tác.
- **Nền Sáng (Light Mode)**: Màu trắng `#ffffff` và xám nhạt `#f8fafc`, viền xám đậm `#cbd5e1`, chữ đen tương phản cao.
- **Vuông Vức Hoàn Toàn (`rounded-none`)**: Không có bất kỳ góc bo tròn nào.

---

## 🔍 Minh Chứng Xác Thực Trend 24h Thời Gian Thực

- Mỗi sản phẩm Viral đều có:
  - Huy hiệu xanh: `✔ ĐÃ XÁC THỰC TREND 24H (HỢP LỆ)`.
  - Khối minh chứng đo lường thực tế trong 24 giờ (Lưu lượng tìm kiếm Google Trends, tốc độ view TikTok, vị trí nhảy thứ hạng Amazon Movers & Shakers).
  - **Nút "ĐỐI SOÁT GOOGLE TRENDS 24H TRỰC TIẾP"**: Bấm vào mở thẳng biểu đồ Google Trends tại Mỹ lọc đúng `date=now 1-d` (24 giờ gần nhất).

---

## ⏰ Hẹn Giờ Tự Động Quét 6 Tiếng / Lần

- Tự động chạy nền cào lại dữ liệu 5 sàn mỗi 6 tiếng một lần.
- Hiển thị đồng hồ đếm ngược trực tiếp trên trang: `Tự động quét 6h: 05:48:12`.

---

## 🚀 Hướng Dẫn Sử Dụng Nhanh

1. **Xem Bảng Điều Khiển Trên Trình Duyệt**:
   - Nhấp đúp chuột vào file **[`dashboard.html`](dashboard.html)**.
2. **Cào Dữ Liệu Mới Nhất & Kích Hoạt Hẹn Giờ 6 Tiếng**:
   - Nhấp đúp chuột vào file **`run.bat`** (hoặc gõ `python main.py`).
