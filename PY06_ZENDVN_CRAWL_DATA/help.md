# Cài đặt môi trường
1. Python 3.11.4 ->
2. Visual studio code: https://zendvn.com/bai-viet/huong-dan-su-dung-visual-studio-code-a-z-toan-tap-10
3. Extension Vscode: Python (Microsoft)
4. Trình duyệt chrome (bắt buộc)
5. Extension chrome: Toggle JavaScript (tắt hoặc mở js)

# Thu thập dữ liệu với Python
1. Phân tích website cần thu thập
- Web mẫu: http://demo-php-bookstore.zendvn.com/index.html
2. Cách thu thập dữ liệu cơ bản (nhanh, nhẹ)
- JS load "Học lập trình"
- Dùng requests để mình lấy dữ liệu thì mình sẽ nhận được source html (js không được chạy)
-> Source html không có "Học lập trình"
3. Kết nối và lưu dữ liệu vào MySQL
4. Thực hành thu thập toàn bộ dữ liệu sản phẩm
5. Xuất dữ liệu ra tệp tin excel
- 1 Sheet danh sách sản phẩm có chứa tên danh mục.
- 1 Sheet danh mục có chứa số lượng sản phẩm thuộc về nó.
6. Giả lập thao tác người dùng (các tình huống khó)
- Click
- Login, Submit Form
- Scroll

# Project tổng hợp: Xây dựng hệ thống crawler

1. Lấy toàn bộ data của web bao gồm: (chỉ cần chạy 1 file)
- Category: {name, link, special}
- Product: {name, link, image_link,... ,special}
- News: {name, link, image_link...,special}

2. Cập Nhật Tin Mới.

- Giải Pháp 1: 
+ Mỗi lần cập nhật sẽ vào web quét lấy toàn bộ dữ liệu.
+ Xoá toàn bộ dữ liệu cũ và lưu dữ liệu mới.

- Giải Pháp 2:
+ Lần đầu quét lưu toàn bộ dữ liệu và lưu thêm bảng history.

    type          time_get           time_sync
    category    datetime.now()     datetime.now()
    product     datetime.now()     datetime.now()
    News        datetime.now()     datetime.now()

+ Những lần sau chỉ quét lấy tin mới và chỉ lưu tin mới vào.

+ Lưu thêm source_id vào mỗi bảng, tìm latest_id từ source_id.

+ Từ latest_id so sánh các phần tử trong web, nếu source_id > latest_id thì mới lưu phần tử đó vào.

3. Đồng bộ tin.
- Quét qua toàn bộ link đã lưu của category, news, product hiện tại.
- Không tồn tại sẽ xoá đi.
- Tồn tại thì sẽ đối chiếu:
+ Nếu lần chỉnh sửa cuối != time_crawler thì lưu lại dữ liệu mới.
+ Nếu lần chỉnh sửa cuối = time_crawler thì không làm gì cả.

4. Cập nhật special (mở rộng)
+ Nếu product, news, category nào xuất hiện ở trang chủ, dựa vào source_id để update special cho nó.

# Video bổ trợ
- Học SQL cơ bản: https://www.youtube.com/playlist?list=PLv6GftO355AtXdxv1WLgxmorw3OMesoS7

# Các thư viện cần cài đặt
- pip install requests
- pip install beautifulsoup4
- pip install mysql-connector-python
- pip install openpyxl
- pip install pandas
- pip install pyppeteer
- pip install schedule