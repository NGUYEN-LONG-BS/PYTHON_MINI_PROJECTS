import os
import tkinter as tk
from tkinter import filedialog

# Hàm để kiểm tra tệp và in ra kết quả
def check_files():
    # Lấy đường dẫn thư mục
    folder_path = filedialog.askdirectory()
    
    if folder_path:
        # Danh sách lưu các tệp không hợp lệ
        invalid_files = []
        
        # Duyệt qua tất cả các thư mục và tệp trong thư mục gốc và thư mục con
        print(f"Đang kiểm tra các tệp trong thư mục: {folder_path}")
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Kiểm tra tệp có đuôi .xlsx, .xls hoặc .pdf
                if file.endswith(('.xlsx', '.xls', '.pdf')):
                    if not file.startswith("NL"):
                        invalid_files.append(os.path.join(root, file))
                        print(f"Tệp không hợp lệ: {os.path.join(root, file)}")
                    else:
                        print(f"Tệp hợp lệ: {os.path.join(root, file)}")
        
        # In ra danh sách các tệp không hợp lệ sau khi hoàn thành kiểm tra
        if invalid_files:
            print("\nCác tệp không hợp lệ đã được tìm thấy:")
            for file in invalid_files:
                print(file)
        else:
            print("\nKhông có tệp không hợp lệ nào được tìm thấy.")

# Tạo giao diện Tkinter
root = tk.Tk()
root.title("Kiểm tra tệp Excel và PDF")

# Nút để chọn thư mục
btn_select_folder = tk.Button(root, text="Chọn thư mục", command=check_files)
btn_select_folder.pack(pady=20)

# Chạy giao diện
root.mainloop()
