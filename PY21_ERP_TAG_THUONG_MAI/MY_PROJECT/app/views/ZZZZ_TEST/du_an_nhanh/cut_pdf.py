import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def choose_directory():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        path_var.set(folder_selected)  # Hiển thị đường dẫn thư mục đã chọn
    else:
        messagebox.showwarning("Chọn thư mục", "Vui lòng chọn thư mục gốc.")

def choose_destination_directory():
    destination_folder = filedialog.askdirectory()
    if destination_folder:
        dest_path_var.set(destination_folder)  # Hiển thị đường dẫn thư mục đích
    else:
        messagebox.showwarning("Chọn thư mục đích", "Vui lòng chọn thư mục đích.")

def copy_pdf_files():
    folder_path = path_var.get()
    dest_folder_path = dest_path_var.get()
    subfolder_name = entry_subfolder.get()

    if not folder_path or not dest_folder_path or not subfolder_name:
        messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn thư mục gốc, thư mục đích và nhập tên thư mục con.")
        return

    subfolder_path = os.path.join(folder_path, subfolder_name)
    
    if not os.path.isdir(subfolder_path):
        messagebox.showerror("Lỗi", f"Thư mục con '{subfolder_name}' không tồn tại.")
        return

    copied_files = 0
    # Duyệt qua tất cả các thư mục con
    for root, dirs, files in os.walk(subfolder_path):
        for dir_name in dirs:
            if dir_name.startswith('NL'):  # Kiểm tra tên thư mục bắt đầu bằng 'NL'
                nl_folder_path = os.path.join(root, dir_name)
                # Duyệt các tệp trong thư mục NL
                for file_name in os.listdir(nl_folder_path):
                    if file_name.lower().endswith('.pdf'):
                        source_file = os.path.join(nl_folder_path, file_name)
                        dest_file = os.path.join(dest_folder_path, file_name)
                        shutil.copy(source_file, dest_file)  # Sao chép tệp PDF
                        copied_files += 1

    if copied_files > 0:
        messagebox.showinfo("Hoàn thành", f"Đã sao chép {copied_files} tệp PDF.")
    else:
        messagebox.showinfo("Không tìm thấy", "Không tìm thấy tệp PDF trong các thư mục NL.")

# Giao diện chính
root = tk.Tk()
root.title("Sao chép tệp PDF")

# Biến lưu trữ đường dẫn thư mục
path_var = tk.StringVar()
dest_path_var = tk.StringVar()

# Đặt kích thước cửa sổ
root.geometry("400x300")

# Tạo các widget
label_path = tk.Label(root, text="Chọn thư mục gốc:")
label_path.pack(pady=10)

button_browse = tk.Button(root, text="Chọn thư mục", command=choose_directory)
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
