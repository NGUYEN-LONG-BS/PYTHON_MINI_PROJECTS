import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
import pandas as pd

def scrape_and_save_text():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Lỗi", "Vui lòng nhập một URL hợp lệ (bắt đầu bằng http hoặc https)")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)

        with open("note.txt", "w", encoding="utf-8") as f:
            f.write(text)

        messagebox.showinfo("Thành công", "Đã lưu nội dung vào note.txt")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lấy nội dung:\n{e}")

def scrape_and_save_links():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Lỗi", "Vui lòng nhập một URL hợp lệ (bắt đầu bằng http hoặc https)")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        # Tạo danh sách để lưu trữ dữ liệu
        data = []
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if href or text:  # Chỉ lưu nếu có href hoặc text
                data.append({'Link': href, 'Text': text})

        # Tạo DataFrame và lưu vào file Excel
        if data:
            df = pd.DataFrame(data)
            df.to_excel("links.xlsx", index=False, engine='openpyxl')
            messagebox.showinfo("Thành công", "Đã lưu liên kết vào links.xlsx")
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy liên kết nào để lưu")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lấy liên kết:\n{e}")

# Giao diện người dùng
root = tk.Tk()
root.title("Web Text & Link Scraper")
root.geometry("600x200")  # Kích thước cửa sổ

# Frame chứa các thành phần giao diện
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Nhập URL:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(frame, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Frame chứa các nút
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Tải và Lưu Text vào note.txt", 
          command=scrape_and_save_text, width=25).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Tải và Lưu Links vào Excel", 
          command=scrape_and_save_links, width=25).pack(side=tk.LEFT, padx=5)

root.mainloop()
