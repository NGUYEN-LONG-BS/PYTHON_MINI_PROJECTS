"""
Giải thích từng phần của code
Thay đổi User-Agent: Dùng chuỗi User-Agent thông thường để giả lập trình duyệt thật.
Ẩn thuộc tính webdriver:
Xóa navigator.webdriver để ngăn trang web kiểm tra xem trình duyệt có được tự động hóa hay không.
Chế độ stealth:
Tinh chỉnh một số thuộc tính như languages, vendor, platform, webgl_vendor, v.v., để trông giống một trình duyệt thông thường.
Tắt thông báo trình duyệt: Tắt các thông báo như "Show Notifications?" thông qua ChromeOptions.
Thêm độ trễ tự nhiên: Tạo khoảng thời gian chờ giữa các hành động để mô phỏng hành vi của con người.
Sử dụng Selenium-Stealth: Công cụ tự động ngụy trang Selenium.
Lưu ý
Nếu bạn chạy code này trên các trang web có bảo mật cao, hãy kết hợp với proxy hoặc VPN để tránh bị phát hiện do gửi nhiều yêu cầu từ cùng một IP.
Kiểm tra kỹ chính sách sử dụng của trang web để đảm bảo rằng bạn không vi phạm các điều khoản.
    
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from webdriver_manager.chrome import ChromeDriverManager

# Thiết lập ChromeOptions
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")  # User-Agent thông thường
options.add_argument("--disable-blink-features=AutomationControlled")  # Ẩn chế độ tự động hóa
options.add_argument("--start-maximized")  # Mở trình duyệt ở chế độ tối đa
options.add_argument("--disable-infobars")  # Tắt thông báo "Chrome is being controlled by automated test software"
options.add_argument("--disable-notifications")  # Tắt thông báo trình duyệt

# Khởi tạo trình điều khiển Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Kích hoạt chế độ stealth
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# Xóa thuộc tính `navigator.webdriver`
driver.execute_script("""
Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
});
""")

# Truy cập vào trang web và thực hiện hành động
driver.get("https://www.google.com")
time.sleep(3)  # Đợi trang tải hoàn toàn

# Tìm kiếm một từ khóa trên Google (mô phỏng hành vi người dùng)
try:
    search_box = driver.find_element(By.NAME, "q")  # Tìm hộp tìm kiếm
    time.sleep(2)  # Thêm độ trễ tự nhiên
    search_box.send_keys("Python Selenium stealth mode")  # Nhập từ khóa tìm kiếm
    time.sleep(1)
    search_box.submit()  # Nhấn Enter để tìm kiếm
    print("Search completed successfully.")
except Exception as e:
    print("Error:", e)

# Đợi một lát và đóng trình duyệt
time.sleep(20)
driver.quit()
