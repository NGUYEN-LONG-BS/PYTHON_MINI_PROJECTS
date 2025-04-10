import tkinter as tk
from tkinter import filedialog
import os

# Hàm để in cây thư mục vào file
def print_tree_to_file(path, file_path, indent=""):
    try:
        entries = os.listdir(path)
    except PermissionError:
        return
    with open(file_path, "a") as f:  # Mở file với chế độ 'append' để thêm nội dung
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                f.write(f"{indent}[D] {entry}\n")  # In thư mục
                print_tree_to_file(full_path, file_path, indent + "  ")  # Đệ quy để in thư mục con
            else:
                f.write(f"{indent}[F] {entry}\n")  # In tệp

# Hàm mở hộp thoại để chọn thư mục và lưu tệp
def select_folder():
    folder_path = filedialog.askdirectory()  # Mở hộp thoại để chọn thư mục
    if folder_path:
        # Mở hộp thoại để chọn nơi lưu tệp
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        
        if save_path:
            # Kiểm tra và tự động thay đổi tên file nếu đã tồn tại
            base_name, ext = os.path.splitext(save_path)
            counter = 1
            while os.path.exists(save_path):
                save_path = f"{base_name}_{counter}{ext}"
                counter += 1

            # Xóa nội dung cũ nếu tệp đã tồn tại trước đó
            with open(save_path, "w"): pass

            # In cây thư mục vào file
            print_tree_to_file(folder_path, save_path)
            print(f"\nCây thư mục đã được lưu tại: {save_path}")

# Tạo giao diện tkinter
root = tk.Tk()
root.title("Directory Tree Viewer")

# Tạo nút để chọn thư mục
select_button = tk.Button(root, text="Chọn Thư Mục", command=select_folder)
select_button.pack(pady=20)

# Khởi chạy giao diện
root.mainloop()
