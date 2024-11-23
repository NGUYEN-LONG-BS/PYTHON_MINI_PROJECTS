
# ======================================================================================
# Mở bằng trình duyệt mặt định trong máy tính
# ======================================================================================
import webbrowser
import time
webbrowser.open("https://vnexpress.net/")
# Giữ script chạy trong 5 giây (hoặc bất kỳ khoảng thời gian nào bạn muốn)
print("Keeping browser open for 30 seconds...")
time.sleep(5)
print("Script finished.")

# ======================================================================================
# Mở bằng trình duyệt tự chọn: Chrome
# ======================================================================================
import webbrowser
import time
url = "https://vnexpress.net/"
webbrowser.register('chrome',None,\
        webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)
# Giữ script chạy trong 5 giây (hoặc bất kỳ khoảng thời gian nào bạn muốn)
print("Keeping browser open for 30 seconds...")
time.sleep(5)
print("Script finished.")

# ======================================================================================
# Mở bằng trình duyệt tự chọn: Edge
# ======================================================================================
import webbrowser
import time
url = "https://vnexpress.net/"
webbrowser.register('chrome',None,\
        webbrowser.BackgroundBrowser(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
webbrowser.get('chrome').open(url)
# Giữ script chạy trong 5 giây (hoặc bất kỳ khoảng thời gian nào bạn muốn)
print("Keeping browser open for 30 seconds...")
time.sleep(5)
print("Script finished.")

# ======================================================================================
# Mở trình duyệt vô thời hạn
# ======================================================================================
import webbrowser
import time

# Mở URL trong trình duyệt mặc định
webbrowser.open("https://vnexpress.net/")

# Giữ script chạy vô hạn
print("Browser will remain open until you stop the script.")
try:
    while True:
        time.sleep(1)  # Đợi 1 giây và lặp lại
except KeyboardInterrupt:
    print("\nScript stopped by user.")
