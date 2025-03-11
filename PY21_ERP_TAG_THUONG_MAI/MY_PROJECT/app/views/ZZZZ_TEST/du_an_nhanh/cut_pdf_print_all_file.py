import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import subprocess

# Hàm để in một file PDF
def print_pdf(file_path):
    try:
        # Sử dụng lệnh để in file PDF (Windows)
        subprocess.run(["lp", file_path], check=True)
        print(f"Đang in file: {file_path}")
    except Exception as e:
        print(f"Không thể in file {file_path}. Lỗi: {e}")

# Hàm chính để chọn thư mục và in tất cả các file PDF trong thư mục đó
def print_all_pdfs_in_directory():
    # Tạo cửa sổ chọn thư mục
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính
    folder_path = filedialog.askdirectory(title="Chọn thư mục chứa file PDF")

    if folder_path:
        # Duyệt qua tất cả các tệp trong thư mục đã chọn
        for filename in os.listdir(folder_path):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(folder_path, filename)
                print_pdf(pdf_path)
    else:
        print("Không có thư mục nào được chọn.")

if __name__ == "__main__":
    print_all_pdfs_in_directory()
