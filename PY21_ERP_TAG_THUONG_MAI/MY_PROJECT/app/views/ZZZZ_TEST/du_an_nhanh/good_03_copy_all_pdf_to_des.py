import os
import shutil
from tkinter import filedialog, Tk, messagebox
import time

def copy_pdf_files():
    # Tạo cửa sổ chính Tkinter
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ chính của Tkinter

    # Chọn thư mục nguồn
    source_folder = filedialog.askdirectory(title="Chọn thư mục nguồn")
    if not source_folder:
        messagebox.showwarning("Cảnh báo", "Không chọn thư mục nguồn!")
        return

    # Chọn thư mục đích
    destination_folder = filedialog.askdirectory(title="Chọn thư mục đích")
    if not destination_folder:
        messagebox.showwarning("Cảnh báo", "Không chọn thư mục đích!")
        return

    # Duyệt qua tất cả các thư mục cấp 1 trong thư mục nguồn
    for folder_name in os.listdir(source_folder):
        source_subfolder = os.path.join(source_folder, folder_name)
        if os.path.isdir(source_subfolder):  # Chỉ xử lý thư mục cấp 1
            # Tạo thư mục cấp 1 trong thư mục đích
            destination_subfolder = os.path.join(destination_folder, folder_name)
            if not os.path.exists(destination_subfolder):
                os.makedirs(destination_subfolder)

            # Gọi hàm đệ quy để tìm tất cả các file PDF trong thư mục cấp 1 và thư mục con
            find_and_copy_pdfs(source_subfolder, destination_subfolder)
    
    messagebox.showinfo("Thông báo", "Hoàn thành việc sao chép!")

def find_and_copy_pdfs(source_folder, destination_folder):
    # Duyệt qua tất cả các file và thư mục trong thư mục nguồn
    for root_dir, dirs, files in os.walk(source_folder):
        for file_name in files:
            if file_name.lower().endswith(".pdf"):  # Kiểm tra file PDF
                source_file = os.path.join(root_dir, file_name)
                destination_file = os.path.join(destination_folder, file_name)
                
                # Nếu file đã tồn tại trong thư mục đích, thay đổi tên file
                if os.path.exists(destination_file):
                    base, ext = os.path.splitext(file_name)
                    timestamp = time.strftime("_%Y%m%d_%H%M%S")
                    destination_file = os.path.join(destination_folder, base + timestamp + ext)

                try:
                    # Sao chép file PDF vào thư mục đích
                    shutil.copy(source_file, destination_file)
                    # Dòng này đã được comment lại
                    # print(f"Đã sao chép {file_name} vào {destination_file}")
                except Exception as e:
                    # In ra thông báo lỗi kèm theo đường dẫn file không sao chép được
                    print(f"Không thể sao chép file: {source_file} vì lỗi: {e}")

# Gọi hàm
copy_pdf_files()
