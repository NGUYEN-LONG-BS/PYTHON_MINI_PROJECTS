import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Hàm lấy danh sách thư mục và file con cấp 1
def get_files_and_folders(path):
    data = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            # Thêm thư mục cấp 0 vào danh sách
            sub_items = []
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                if os.path.isfile(sub_item_path):
                    sub_items.append(sub_item)
            # Thêm thư mục cấp 0 và danh sách file con
            data.append((item, ', '.join(sub_items)))
        elif os.path.isfile(item_path):
            data.append((item, ''))
    return data

# Hàm kiểm tra tên file đã tồn tại chưa và tự động tăng số thứ tự
def get_unique_filename(file_path):
    base, ext = os.path.splitext(file_path)
    counter = 1
    while os.path.exists(file_path):
        file_path = f"{base}_{counter}{ext}"
        counter += 1
    return file_path

# Hàm xuất dữ liệu ra Excel
def export_to_excel(data, save_path):
    df = pd.DataFrame(data, columns=["Cấp 0", "Cấp 1"])
    save_path = get_unique_filename(save_path)
    df.to_excel(save_path, index=False)
    print(f"Đã xuất dữ liệu ra Excel: {save_path}")

# Hàm để mở cửa sổ chọn thư mục
def choose_folder():
    global folder_path
    folder_path = filedialog.askdirectory(title="Chọn thư mục cấp 0")
    if folder_path:
        print(f"Đang xử lý thư mục: {folder_path}")
        save_file()

# Hàm để mở cửa sổ chọn nơi lưu file Excel
def save_file():
    save_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel Files", "*.xlsx")],
                                             title="Chọn nơi lưu file Excel")
    if save_path:
        print(f"Đang lưu file tại: {save_path}")
        data = get_files_and_folders(folder_path)
        export_to_excel(data, save_path)

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Chọn thư mục và xuất dữ liệu")
root.geometry("300x150")

# Thêm nút để chọn thư mục
button_choose_folder = tk.Button(root, text="Chọn thư mục", command=choose_folder)
button_choose_folder.pack(pady=20)

# Thêm nút để chọn nơi lưu file Excel
button_save_file = tk.Button(root, text="Chọn nơi lưu file Excel", command=save_file)
button_save_file.pack(pady=20)

# Chạy giao diện Tkinter
root.mainloop()
