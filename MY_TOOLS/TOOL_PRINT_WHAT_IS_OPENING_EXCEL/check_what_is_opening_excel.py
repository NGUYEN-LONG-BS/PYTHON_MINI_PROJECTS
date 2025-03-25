import tkinter as tk
from tkinter import filedialog
import psutil
import os

# Hàm tìm tiến trình đang mở tệp Excel
def find_process_opening_file(file_name):
    # Duyệt qua tất cả các tiến trình đang chạy
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            # Kiểm tra tiến trình có đang mở tệp không
            for file in proc.info['open_files'] or []:
                if file_name in file.path:
                    print(f"Tiến trình {proc.info['name']} (PID: {proc.info['pid']}) đang mở tệp {file_name}")
                    return proc.info['name']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return None

# Hàm mở tệp Excel và kiểm tra tiến trình mở tệp
def open_excel_file():
    try:
        # Mở hộp thoại chọn file
        file_path = filedialog.askopenfilename(title="Select an Excel File", filetypes=[("Excel Files", "*.xlsx;*.xls")])
        if file_path:
            file_name = os.path.basename(file_path)
            # Kiểm tra xem tệp Excel có đang mở không
            process_name = find_process_opening_file(file_name)
            
            if process_name:
                result_label.config(text=f"Tệp {file_name} đang được mở bởi tiến trình: {process_name}")
            else:
                result_label.config(text=f"Tệp {file_name} không được mở bởi bất kỳ tiến trình nào.")
        else:
            result_label.config(text="Không có tệp nào được chọn.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Kiểm Tra Tệp Excel")

# Tạo nút để mở file
open_button = tk.Button(root, text="Chọn File Excel", command=open_excel_file)
open_button.pack(pady=20)

# Tạo nhãn để hiển thị kết quả
result_label = tk.Label(root, text="", wraplength=400)
result_label.pack(pady=10)

# Chạy giao diện Tkinter
root.mainloop()
