import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def scrape_and_save():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Lỗi", "Vui lòng nhập một URL hợp lệ (bắt đầu bằng http hoặc https)")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # Lấy tất cả nội dung text
        text = soup.get_text()

        # Ghi vào file note.txt
        with open("note.txt", "w", encoding="utf-8") as f:
            f.write(text)

        messagebox.showinfo("Thành công", "Đã lưu nội dung vào note.txt")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lấy nội dung:\n{e}")

# Giao diện người dùng
root = tk.Tk()
root.title("Web Text Scraper")

tk.Label(root, text="Nhập URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(padx=10)

tk.Button(root, text="Tải và Lưu vào note.txt", command=scrape_and_save).pack(pady=10)

root.mainloop()
