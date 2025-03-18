import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import re

def select_source_folder():
    folder_selected = filedialog.askdirectory(title="Chọn thư mục chứa các file PDF")
    source_folder_var.set(folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory(title="Chọn thư mục đích")
    destination_folder_var.set(folder_selected)

def copy_files():
    source_folder = source_folder_var.get()
    destination_folder = destination_folder_var.get()

    if not source_folder or not destination_folder:
        messagebox.showerror("Lỗi", "Vui lòng chọn cả hai thư mục nguồn và đích.")
        return

    # Lọc các file PDF trong thư mục nguồn
    pdf_files = [f for f in os.listdir(source_folder) if f.endswith('.pdf') and f.startswith('CT phiếu')]
    
    if not pdf_files:
        messagebox.showinfo("Thông báo", "Không tìm thấy file PDF nào trong thư mục nguồn.")
        return
    
    # Tiến hành sao chép các file
    for file in pdf_files:
        # Sử dụng regex để tách số từ tên file và bỏ số 0 đầu tiên
        match = re.match(r"CT phiếu (\d+)\.pdf", file)  # Sử dụng \d+ để khớp với bất kỳ số nào (bao gồm cả số bắt đầu với 0)
        
        if match:
            file_prefix = match.group(1)  # Lấy số từ tên file, bao gồm cả số không có 0 đầu
            
            # Xóa số 0 đầu nếu có
            file_prefix = str(int(file_prefix))  # Chuyển số thành kiểu int rồi lại về kiểu string để loại bỏ 0 đầu
            
            # Tạo tiền tố thư mục đích với số từ tên file (ví dụ: 32 từ "CT phiếu 032.pdf")
            destination_subfolder_prefix = f"{file_prefix}"  
            
            # Kiểm tra xem thư mục có tên bắt đầu bằng tiền tố này không
            valid_folders = [folder for folder in os.listdir(destination_folder) if folder.startswith(destination_subfolder_prefix)]
            
            if not valid_folders:
                print(f"Không tìm thấy thư mục nào bắt đầu bằng {destination_subfolder_prefix}. Bỏ qua file {file}.")
                continue  # Bỏ qua file nếu không có thư mục tương ứng
            
            # Đường dẫn đầy đủ của file nguồn
            source_file = os.path.join(source_folder, file)

            # Sao chép vào tất cả thư mục có tiền tố trùng
            for valid_folder in valid_folders:
                destination_file = os.path.join(destination_folder, valid_folder, file)
                
                # Kiểm tra nếu file đích đã tồn tại, nếu có, thay thế nó
                try:
                    shutil.copy(source_file, destination_file)  # Sẽ tự động thay thế nếu file đã tồn tại
                    print(f"Đã sao chép (thay thế): {file} vào {os.path.join(destination_folder, valid_folder)}")
                except Exception as e:
                    messagebox.showerror("Lỗi sao chép", f"Lỗi khi sao chép {file}: {e}")
                    return

    messagebox.showinfo("Thông báo", "Quá trình sao chép hoàn tất!")

# Giao diện Tkinter
root = tk.Tk()
root.title("Chương trình sao chép file PDF")

# Biến để lưu thư mục nguồn và đích
source_folder_var = tk.StringVar()
destination_folder_var = tk.StringVar()

# Cấu hình giao diện
tk.Label(root, text="Thư mục chứa file PDF:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Chọn thư mục", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Thư mục đích để sao chép:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Chọn thư mục", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Tiến hành sao chép", command=copy_files).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
