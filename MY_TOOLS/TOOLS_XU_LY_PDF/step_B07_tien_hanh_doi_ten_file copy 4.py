import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Hàm để chọn thư mục cấp 0
def select_folder():
    folder_selected = filedialog.askdirectory(title="Chọn thư mục cấp 0")
    if folder_selected:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_selected)

# Hàm để chọn file Excel
def select_excel():
    file_selected = filedialog.askopenfilename(title="Chọn file Excel", filetypes=[("Excel files", "*.xlsx")])
    if file_selected:
        entry_excel.delete(0, tk.END)
        entry_excel.insert(0, file_selected)

# Hàm để đổi tên các file
def rename_files():
    folder_path = entry_folder.get()
    excel_path = entry_excel.get()

    if not folder_path or not excel_path:
        status_label.config(text="Vui lòng chọn thư mục và file Excel", fg="red")
        return

    try:
        # Đọc file Excel
        df = pd.read_excel(excel_path, header=None)

        # Kiểm tra dữ liệu trong file Excel
        if df.shape[1] != 2:
            status_label.config(text="File Excel không hợp lệ. Cần 2 cột.", fg="red")
            return

        # Loại bỏ các dòng có dữ liệu không hợp lệ
        df = df.dropna()  # Loại bỏ các giá trị NaN
        df = df[df[0].apply(lambda x: isinstance(x, str))]  # Giữ lại chỉ các giá trị chuỗi

        # Duyệt qua từng dòng trong Excel và đổi tên file
        for _, row in df.iterrows():
            old_file_path = os.path.join(folder_path, row[0])
            new_file_path = os.path.join(folder_path, row[1])

            if os.path.exists(old_file_path):
                # Đổi tên file
                os.rename(old_file_path, new_file_path)
        
        status_label.config(text="Đổi tên thành công!", fg="green")
    except Exception as e:
        status_label.config(text=f"Lỗi: {str(e)}", fg="red")

# Giao diện người dùng
root = tk.Tk()
root.title("Đổi tên file tự động")

# Entry cho thư mục
label_folder = tk.Label(root, text="Chọn thư mục cấp 0:")
label_folder.pack(padx=10, pady=5)
entry_folder = tk.Entry(root, width=50)
entry_folder.pack(padx=10, pady=5)
button_folder = tk.Button(root, text="Chọn thư mục", command=select_folder)
button_folder.pack(padx=10, pady=5)

# Entry cho file Excel
label_excel = tk.Label(root, text="Chọn file Excel:")
label_excel.pack(padx=10, pady=5)
entry_excel = tk.Entry(root, width=50)
entry_excel.pack(padx=10, pady=5)
button_excel = tk.Button(root, text="Chọn file Excel", command=select_excel)
button_excel.pack(padx=10, pady=5)

# Nút đổi tên
button_rename = tk.Button(root, text="Tiến hành đổi tên", command=rename_files)
button_rename.pack(padx=10, pady=10)

# Label hiển thị trạng thái
status_label = tk.Label(root, text="", fg="black")
status_label.pack(padx=10, pady=10)

# Chạy ứng dụng
root.mainloop()
