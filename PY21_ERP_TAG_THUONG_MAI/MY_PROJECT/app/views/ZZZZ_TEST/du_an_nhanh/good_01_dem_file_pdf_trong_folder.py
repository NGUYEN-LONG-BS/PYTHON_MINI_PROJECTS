import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_pdf_files(folder_path):
    # Biến đếm số lượng file PDF
    pdf_count = 0
    
    # Duyệt qua tất cả các file và thư mục trong thư mục
    for root_dir, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Kiểm tra nếu file có đuôi là .pdf (không phân biệt chữ hoa/thường)
            if file_name.lower().endswith(".pdf"):
                pdf_count += 1
    
    return pdf_count

def on_select_folder():
    # Mở hộp thoại chọn thư mục
    folder_path = filedialog.askdirectory(title="Chọn thư mục")
    if folder_path:
        # Đếm số lượng file PDF trong thư mục
        pdf_count = count_pdf_files(folder_path)
        
        # Hiển thị kết quả trong cửa sổ thông báo
        messagebox.showinfo("Kết quả", f"Số lượng file PDF trong thư mục {folder_path}: {pdf_count}")

# Tạo cửa sổ chính của Tkinter
root = tk.Tk()
root.title("Đếm file PDF trong thư mục")

# Tạo nút để người dùng chọn thư mục
btn_select_folder = tk.Button(root, text="Chọn thư mục", command=on_select_folder)
btn_select_folder.pack(pady=20)

# Chạy giao diện Tkinter
root.mainloop()
