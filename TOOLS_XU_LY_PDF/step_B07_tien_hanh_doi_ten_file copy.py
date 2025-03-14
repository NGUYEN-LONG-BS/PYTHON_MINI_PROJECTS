import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Hàm chọn thư mục
def select_folder():
    folder_path = filedialog.askdirectory()  # Chọn thư mục
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)  # Hiển thị đường dẫn vào Entry

# Hàm chọn file Excel
def select_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])  # Chọn file Excel
    excel_entry.delete(0, tk.END)
    excel_entry.insert(0, file_path)  # Hiển thị đường dẫn vào Entry

# Hàm xử lý đổi tên file và cập nhật kết quả
def process_files():
    folder_path = folder_entry.get()  # Lấy thư mục đã chọn
    excel_file = excel_entry.get()  # Lấy file Excel đã chọn

    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(excel_file, sheet_name='Sheet1', usecols=[0, 1])  # Đọc 2 cột đầu tiên

    updated_files = []  # Lưu kết quả đã đổi tên

    for index, row in df.iterrows():
        # Truy xuất theo vị trí cột
        file_name = row.iloc[0]  # Tên file gốc từ cột đầu
        updated_name = row.iloc[1]  # Tên file mới từ cột 2

        # Kết hợp thư mục đã chọn với tên file
        original_file_path = os.path.join(folder_path, file_name)
        updated_file_path = os.path.join(folder_path, updated_name)

        # Đổi tên file
        if os.path.exists(original_file_path):
            os.rename(original_file_path, updated_file_path)  # Đổi tên file thực tế
            updated_files.append(f"{original_file_path} --> {updated_file_path}")
        else:
            updated_files.append(f"{original_file_path} không tồn tại!")

    # Hiển thị kết quả
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n".join(updated_files))

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Đổi Tên File Từ Excel")

# Tạo giao diện
tk.Label(root, text="Chọn thư mục:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1, padx=10, pady=5)
folder_button = tk.Button(root, text="Chọn thư mục", command=select_folder)
folder_button.grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Chọn file Excel:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
excel_entry = tk.Entry(root, width=50)
excel_entry.grid(row=1, column=1, padx=10, pady=5)
excel_button = tk.Button(root, text="Chọn Excel", command=select_excel_file)
excel_button.grid(row=1, column=2, padx=10, pady=5)

process_button = tk.Button(root, text="Xử Lý", command=process_files)
process_button.grid(row=2, column=0, columnspan=3, pady=10)

# Khu vực hiển thị kết quả
tk.Label(root, text="Kết quả:").grid(row=3, column=0, sticky="w", padx=10, pady=5)
result_text = tk.Text(root, height=10, width=70)
result_text.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Chạy chương trình
root.mainloop()
