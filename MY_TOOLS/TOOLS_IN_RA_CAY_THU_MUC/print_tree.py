import tkinter as tk
from tkinter import filedialog
import os

# Hàm để in cây thư mục
def print_tree(path, indent=""):
    # Lấy danh sách các tệp và thư mục trong thư mục hiện tại
    try:
        entries = os.listdir(path)
    except PermissionError:
        return
    for entry in entries:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            print(f"{indent}[D] {entry}")  # In thư mục
            print_tree(full_path, indent + "  ")  # Đệ quy để in cây thư mục con
        else:
            print(f"{indent}[F] {entry}")  # In tệp

# Hàm mở hộp thoại để chọn thư mục
def select_folder():
    folder_path = filedialog.askdirectory()  # Mở hộp thoại để chọn thư mục
    if folder_path:
        print(f"\nCây thư mục của {folder_path}:")
        print_tree(folder_path)

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Directory Tree Viewer")

# Tạo nút để chọn thư mục
select_button = tk.Button(root, text="Chọn Thư Mục", command=select_folder)
select_button.pack(pady=20)

# Khởi chạy giao diện
root.mainloop()
