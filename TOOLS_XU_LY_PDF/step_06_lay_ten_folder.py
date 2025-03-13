import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Hàm chọn thư mục và lấy danh sách các thư mục con và file
def select_folder_and_generate_excel():
    folder_path = filedialog.askdirectory()  # Mở hộp thoại chọn thư mục
    if not folder_path:
        return  # Nếu người dùng không chọn thư mục, thoát

    data = []  # Danh sách lưu các dòng dữ liệu để ghi vào Excel

    # Lấy danh sách các thư mục cấp 1 trong thư mục đã chọn
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        
        if os.path.isdir(folder_full_path):  # Kiểm tra nếu là thư mục cấp 1
            sub_files_folders = os.listdir(folder_full_path)  # Lấy danh sách file và thư mục con
            for item in sub_files_folders:
                data.append([folder, item])  # Thêm vào dữ liệu

    # Tạo DataFrame từ dữ liệu đã thu thập
    df = pd.DataFrame(data, columns=["Folder Level 1", "Sub-file/Folder"])

    # Lưu DataFrame vào file Excel
    output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if output_file:
        df.to_excel(output_file, index=False, engine="openpyxl")
        print(f"File Excel đã được lưu tại: {output_file}")

# Tạo cửa sổ giao diện với Tkinter
root = tk.Tk()
root.title("Chọn thư mục và xuất Excel")

# Thêm nút để chọn thư mục và xuất file Excel
button = tk.Button(root, text="Chọn thư mục và xuất Excel", command=select_folder_and_generate_excel)
button.pack(pady=20)

root.mainloop()
