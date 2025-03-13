import os
import shutil
import zipfile
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import pandas as pd

def choose_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)  # Hiển thị đường dẫn thư mục đã chọn
        extract_zip_files(folder_selected)  # Giải nén tất cả các tệp zip trong thư mục gốc
    else:
        messagebox.showwarning("Chọn thư mục", "Vui lòng chọn thư mục gốc.")

def choose_destination_directory():
    destination_folder = filedialog.askdirectory()
    if destination_folder:
        dest_path_var.set(destination_folder)  # Hiển thị đường dẫn thư mục đích
    else:
        messagebox.showwarning("Chọn thư mục đích", "Vui lòng chọn thư mục đích.")

def list_pdf_files(folder_path, output_excel_path):
    # Danh sách chứa đường dẫn đến các tệp PDF
    pdf_files = []
    
    # Duyệt qua tất cả các thư mục và tệp con trong thư mục gốc
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                # Thêm đường dẫn đầy đủ đến tệp PDF
                pdf_files.append(os.path.join(root, file))
    
    # Nếu không có tệp PDF nào, hiển thị thông báo
    if not pdf_files:
        print("Không tìm thấy tệp PDF trong thư mục.")
        return

    # Tạo DataFrame từ danh sách các đường dẫn
    pdf_df = pd.DataFrame(pdf_files, columns=["PDF File Path"])

    # Xuất DataFrame ra file Excel
    pdf_df.to_excel(output_excel_path, index=False, engine='openpyxl')

    print(f"Đã xuất {len(pdf_files)} tệp PDF vào file Excel: {output_excel_path}")
            
def extract_zip_files(folder_path):
    # Duyệt qua tất cả các thư mục và tệp con trong thư mục gốc
    zip_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.zip'):
                zip_files.append(os.path.join(root, file))
    
    if not zip_files:
        messagebox.showinfo("Không có tệp zip", "Không tìm thấy tệp zip trong thư mục và các thư mục con.")
        return

    for zip_file in zip_files:
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                # Giải nén vào thư mục hiện tại (Extract here)
                zip_ref.extractall(os.path.dirname(zip_file))  # Giải nén vào thư mục chứa tệp zip
            # messagebox.showinfo("Giải nén thành công", f"Đã giải nén {zip_file} thành công.")
        except zipfile.BadZipFile:
            messagebox.showerror("Lỗi giải nén", f"Tệp {zip_file} không phải là tệp zip hợp lệ.")

# def copy_pdf_files():
#     folder_path = path_var.get()
#     dest_folder_path = dest_path_var.get()
#     subfolder_name = entry_subfolder.get()

#     if not folder_path or not dest_folder_path or not subfolder_name:
#         messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn thư mục gốc, thư mục đích và nhập tên thư mục con.")
#         return

#     subfolder_path = os.path.join(folder_path, subfolder_name)
    
#     if not os.path.isdir(subfolder_path):
#         messagebox.showerror("Lỗi", f"Thư mục con '{subfolder_name}' không tồn tại.")
#         return

#     copied_files = 0
#     # Duyệt qua tất cả các thư mục con
#     for root, dirs, files in os.walk(subfolder_path):
#         for dir_name in dirs:
#             if dir_name.startswith('NL'):  # Kiểm tra tên thư mục bắt đầu bằng 'NL'
#                 nl_folder_path = os.path.join(root, dir_name)
#                 # Duyệt các tệp trong thư mục NL
#                 for file_name in os.listdir(nl_folder_path):
#                     if file_name.lower().endswith('.pdf'):
#                         source_file = os.path.join(nl_folder_path, file_name)
#                         dest_file = os.path.join(dest_folder_path, file_name)
#                         shutil.copy(source_file, dest_file)  # Sao chép tệp PDF
#                         copied_files += 1

#     if copied_files > 0:
#         messagebox.showinfo("Hoàn thành", f"Đã sao chép {copied_files} tệp PDF.")
#     else:
#         messagebox.showinfo("Không tìm thấy", "Không tìm thấy tệp PDF trong các thư mục NL.")

def copy_pdf_files():
    folder_path = path_var.get()  # Đường dẫn thư mục gốc
    dest_folder_path = dest_path_var.get()  # Đường dẫn thư mục đích

    if not folder_path or not dest_folder_path:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn thư mục gốc và thư mục đích.")
        return

    if not os.path.isdir(folder_path):
        messagebox.showerror("Lỗi", "Thư mục gốc không tồn tại.")
        return

    if not os.path.isdir(dest_folder_path):
        messagebox.showerror("Lỗi", "Thư mục đích không tồn tại.")
        return

    copied_files = 0
    
    # Duyệt qua tất cả các thư mục con cấp 1 trong thư mục gốc
    for subfolder_name in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder_name)
        
        if os.path.isdir(subfolder_path):
            # Tạo thư mục con mới trong thư mục đích
            new_dest_folder = os.path.join(dest_folder_path, subfolder_name)
            if not os.path.exists(new_dest_folder):
                os.makedirs(new_dest_folder)
            
            # Duyệt qua các tệp trong thư mục con cấp 1
            for file_name in os.listdir(subfolder_path):
                if file_name.lower().endswith('.pdf'):
                    source_file = os.path.join(subfolder_path, file_name)
                    dest_file = os.path.join(new_dest_folder, file_name)
                    shutil.copy(source_file, dest_file)  # Sao chép tệp PDF
                    copied_files += 1

    if copied_files > 0:
        messagebox.showinfo("Hoàn thành", f"Đã sao chép {copied_files} tệp PDF.")
    else:
        messagebox.showinfo("Không tìm thấy", "Không tìm thấy tệp PDF trong các thư mục con.")

# Giao diện chính
root = tk.Tk()
root.title("Sao chép tệp PDF và Giải nén ZIP")

# Biến lưu trữ đường dẫn thư mục
path_var = tk.StringVar()
dest_path_var = tk.StringVar()

# Đặt kích thước cửa sổ
root.geometry("400x650")

# Tạo các widget
label_path = tk.Label(root, text="Chọn thư mục gốc:")
label_path.pack(pady=10)

button_browse = tk.Button(root, text="Chọn thư mục gốc và giải nén tất cả các tệp zip", command=choose_directory)
button_browse.pack()

label_selected_path = tk.Label(root, textvariable=path_var, wraplength=350)
label_selected_path.pack(pady=10)

label_subfolder = tk.Label(root, text="Nhập tên thư mục con:")
label_subfolder.pack(pady=5)

entry_subfolder = tk.Entry(root, width=30)
entry_subfolder.pack(pady=5)

label_dest_path = tk.Label(root, text="Chọn thư mục đích để sao chép PDF:")
label_dest_path.pack(pady=10)

button_dest_browse = tk.Button(root, text="Chọn thư mục đích", command=choose_destination_directory)
button_dest_browse.pack()

label_selected_dest_path = tk.Label(root, textvariable=dest_path_var, wraplength=350)
label_selected_dest_path.pack(pady=10)

button_copy = tk.Button(root, text="Sao chép tệp PDF", command=copy_pdf_files)
button_copy.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
