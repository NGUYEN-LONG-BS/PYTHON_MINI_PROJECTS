import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import pyperclip  # Thư viện để copy vào clipboard
import textwrap  # Thư viện để wrap văn bản

# Danh sách các link thường dùng
PRESET_LINKS = {
    "VNExpress": "https://vnexpress.net/tin-tuc-24h",
    "Sài Gòn Đầu Tư": "https://dttc.sggp.org.vn/",
    "BBC": "https://www.bbc.com/news",
    "CNN": "https://edition.cnn.com/world",
}

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

def scrape_and_display_text():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Lỗi", "Vui lòng nhập một URL hợp lệ (bắt đầu bằng http hoặc https)")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        
        # Xóa dữ liệu cũ trong bảng
        for row in tree.get_children():
            tree.delete(row)

        # Cập nhật tiêu đề cột
        tree['columns'] = ('Content',)
        tree.heading('Content', text='Nội dung')
        tree.column('Content', width=700)  # Độ rộng cột Nội dung

        # Wrap văn bản dựa trên chiều rộng cột
        # Ước tính: 1 ký tự ~ 8 pixel (phụ thuộc vào font), cột rộng 700px ~ 80-90 ký tự
        wrap_width = 80  # Số ký tự tối đa mỗi dòng
        lines = text.split('\n')
        wrapped_lines = []
        for line in lines:
            if line.strip():  # Chỉ xử lý dòng không rỗng
                # Wrap dòng văn bản
                wrapped = textwrap.wrap(line, width=wrap_width, break_long_words=True)
                wrapped_lines.extend(wrapped if wrapped else [line])

        # Thêm các dòng đã wrap vào Treeview
        for line in wrapped_lines:
            tree.insert('', 'end', values=(line,))

        messagebox.showinfo("Thành công", "Đã hiển thị nội dung trong bảng")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lấy nội dung:\n{e}")

def scrape_and_preview_links():
    url = url_entry.get()
    if not url.startswith("http"):
        messagebox.showerror("Lỗi", "Vui lòng nhập một URL hợp lệ (bắt đầu bằng http hoặc https)")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        # Xóa dữ liệu cũ trong bảng
        for row in tree.get_children():
            tree.delete(row)

        # Cập nhật tiêu đề cột
        tree['columns'] = ('Link', 'Text')
        tree.heading('Link', text='Link')
        tree.heading('Text', text='Text')
        tree.column('Link', width=400)
        tree.column('Text', width=300)

        # Tạo danh sách để lưu trữ dữ liệu
        global link_data
        link_data = []
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if href or text:  # Chỉ lưu nếu có href hoặc text
                link_data.append({'Link': href, 'Text': text})
                tree.insert('', 'end', values=(href, text))

        if link_data:
            messagebox.showinfo("Thành công", "Đã hiển thị liên kết trong bảng")
        else:
            messagebox.showinfo("Thông báo", "Không tìm thấy liên kết nào")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lấy liên kết:\n{e}")

def save_links_to_excel():
    if not link_data:
        messagebox.showerror("Lỗi", "Không có dữ liệu liên kết để lưu. Vui lòng tải liên kết trước!")
        return

    try:
        df = pd.DataFrame(link_data)
        df.to_excel("links.xlsx", index=False, engine='openpyxl')
        messagebox.showinfo("Thành công", "Đã lưu liên kết vào links.xlsx")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể lưu liên kết:\n{e}")

def copy_link(event):
    # Lấy hàng được chọn
    selected_item = tree.selection()
    if selected_item:
        # Lấy giá trị cột đầu tiên của hàng được chọn (Link hoặc Content)
        value = tree.item(selected_item)['values'][0]
        if value:
            pyperclip.copy(value)
            messagebox.showinfo("Thành công", f"Đã sao chép: {value}")

def on_dropdown_select(event):
    # Điền URL từ dropdown vào ô nhập
    selected_name = dropdown.get()
    if selected_name in PRESET_LINKS:
        url_entry.delete(0, tk.END)
        url_entry.insert(0, PRESET_LINKS[selected_name])

# Giao diện người dùng
root = tk.Tk()
root.title("Web Text & Link Scraper - Anh Nè (Xài miễn phí)")
root.geometry("800x600")  # Tăng kích thước cửa sổ để chứa bảng

# Frame chứa các thành phần giao diện
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill='x')

# Dropdown menu cho các link thường dùng
tk.Label(frame, text="Chọn trang web:", font=("Arial", 12)).pack(pady=5)
dropdown = ttk.Combobox(frame, values=list(PRESET_LINKS.keys()), font=("Arial", 10), state="readonly")
dropdown.pack(pady=5)
dropdown.bind('<<ComboboxSelected>>', on_dropdown_select)

# Nhập URL
tk.Label(frame, text="Nhập URL:", font=("Arial", 12)).pack(pady=5)
url_entry = tk.Entry(frame, width=50, font=("Arial", 10))
url_entry.pack(pady=5)

# Frame chứa các nút
button_frame = tk.Frame(frame)
button_frame.pack(pady=10)

# Thêm nút "Tải và Hiển thị Nội dung" trước nút "Tải và Lưu Text"
tk.Button(button_frame, text="Tải và Hiển thị Nội dung", 
          command=scrape_and_display_text, width=25).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Tải và Lưu Text vào note.txt", 
          command=scrape_and_save_text, width=25).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Tải và Hiển thị Links", 
          command=scrape_and_preview_links, width=25).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Lưu Links vào Excel", 
          command=save_links_to_excel, width=25).pack(side=tk.LEFT, padx=5)

# Frame chứa bảng và thanh cuộn
table_frame = tk.Frame(root)
table_frame.pack(pady=10, padx=10, fill='both', expand=True)

table_note = tk.Label(table_frame, text="(Nhấp đúp vào dòng để copy nội dung hoặc link)", font=("Arial", 12))
table_note.pack(pady=5)

# Tạo bảng (Treeview)
tree = ttk.Treeview(table_frame, columns=('Content',), show='headings', height=13)  # Chiều cao ~300px
tree.heading('Content', text='Nội dung')
tree.column('Content', width=700)  # Độ rộng cột Nội dung

# Thanh cuộn dọc
scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Đặt bảng và thanh cuộn
tree.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Biến toàn cục để lưu dữ liệu liên kết
link_data = []

# Gắn sự kiện nhấp chuột vào hàng để sao chép link hoặc nội dung
tree.bind('<Double-1>', copy_link)  # Nhấp đúp để copy

root.mainloop()