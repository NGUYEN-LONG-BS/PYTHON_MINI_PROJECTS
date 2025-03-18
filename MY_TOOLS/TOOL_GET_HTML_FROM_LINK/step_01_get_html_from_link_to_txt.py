import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import os

# Hàm lấy mã HTML từ URL và lưu vào file
def get_html():
    url = entry_url.get()  # Lấy đường link từ ô nhập liệu
    if not url:
        messagebox.showerror("Lỗi", "Vui lòng nhập URL.")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra xem yêu cầu có thành công không
        
        # Mở hộp thoại cho phép người dùng chọn đường dẫn và tên file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="html_from_link.txt", title="Chọn nơi lưu file")
        
        if not file_path:
            return  # Nếu người dùng hủy thao tác chọn file
        
        # Kiểm tra xem file có tồn tại không, nếu có thì thêm số thứ tự vào tên file
        if os.path.exists(file_path):
            base, ext = os.path.splitext(file_path)
            i = 1
            new_file_path = f"{base}_{i}{ext}"
            while os.path.exists(new_file_path):
                i += 1
                new_file_path = f"{base}_{i}{ext}"
            file_path = new_file_path
        
        # Lưu mã HTML vào file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        
        messagebox.showinfo("Thành công", f"Đã lưu mã HTML vào file: {file_path}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Lỗi", f"Không thể tải trang web: {e}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lấy Mã HTML Từ URL")

# Tạo nhãn hướng dẫn
label = tk.Label(root, text="Nhập URL:")
label.pack(pady=5)

# Tạo ô nhập URL
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Tạo nút lấy mã HTML và lưu vào file
button = tk.Button(root, text="Lấy Mã HTML và Lưu", command=get_html)
button.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
