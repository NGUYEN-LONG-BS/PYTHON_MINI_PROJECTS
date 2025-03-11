import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import shutil
import subprocess

# Hàm để tạo một file PDF mới chứa tên thư mục
def create_pdf_with_directory_name(directory_name, output_pdf_path):
    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    c.drawString(100, 750, f"Ten thu muc me: {directory_name}")
    c.save()

# Hàm để kết hợp nội dung PDF ban đầu và tên thư mục
def add_directory_name_to_pdf(pdf_path, directory_name, output_pdf_path):
    # Tạo file PDF chứa tên thư mục
    temp_pdf_path = "temp_directory_name.pdf"
    create_pdf_with_directory_name(directory_name, temp_pdf_path)
    
    # Mở file PDF ban đầu
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Mở file PDF chứa tên thư mục
    temp_reader = PdfReader(temp_pdf_path)
    
    # Thêm tên thư mục vào trang đầu của file PDF
    writer.add_page(temp_reader.pages[0])  # Thêm trang chứa tên thư mục
    for page in reader.pages:
        writer.add_page(page)  # Thêm các trang còn lại của file PDF

    # Ghi kết quả vào file PDF mới
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)
    
    # Xóa file tạm thời
    os.remove(temp_pdf_path)

# Hàm để in file PDF
def print_pdf(file_path):
    try:
        subprocess.run(["lp", file_path], check=True)
        print(f"Đang in file: {file_path}")
    except Exception as e:
        print(f"Không thể in file {file_path}. Lỗi: {e}")

# Hàm để sao chép file PDF vào thư mục đích
def copy_pdf_to_destination(file_path, destination_folder):
    try:
        shutil.copy(file_path, destination_folder)
        print(f"Đã sao chép file {file_path} đến {destination_folder}")
    except Exception as e:
        print(f"Không thể sao chép file {file_path}. Lỗi: {e}")

# Hàm chính để chọn thư mục nguồn, thư mục đích và in các file PDF
def process_pdfs():
    # Tạo cửa sổ chọn thư mục nguồn
    folder_path = filedialog.askdirectory(title="Chọn thư mục chứa các thư mục mẹ")

    if folder_path:
        # Tạo cửa sổ chọn thư mục đích
        destination_folder = filedialog.askdirectory(title="Chọn thư mục đích để sao chép PDF")

        if destination_folder:
            # Duyệt qua các thư mục con trong thư mục đã chọn
            for subdir, _, files in os.walk(folder_path):
                for filename in files:
                    if filename.endswith(".pdf"):
                        pdf_path = os.path.join(subdir, filename)
                        output_pdf_path = os.path.join(subdir, f"modified_{filename}")
                        
                        # Thêm tên thư mục vào PDF
                        add_directory_name_to_pdf(pdf_path, os.path.basename(subdir), output_pdf_path)
                        
                        # Sao chép file PDF đã chỉnh sửa vào thư mục đích
                        copy_pdf_to_destination(output_pdf_path, destination_folder)
                        
                        # In file PDF đã được chỉnh sửa
                        print_pdf(output_pdf_path)
                        
                        # Xóa file đã in sau khi hoàn tất
                        os.remove(output_pdf_path)
            messagebox.showinfo("Hoàn thành", "Tất cả các file PDF đã được sao chép và in thành công!")
        else:
            messagebox.showwarning("Cảnh báo", "Không có thư mục đích nào được chọn.")
    else:
        messagebox.showwarning("Cảnh báo", "Không có thư mục nguồn nào được chọn.")

# Giao diện Tkinter
def create_gui():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Ứng Dụng In và Sao Chép PDF với Tên Thư Mục")

    # Thêm nút để chọn thư mục và in PDF
    print_button = tk.Button(root, text="Chọn thư mục nguồn và thư mục đích", command=process_pdfs)
    print_button.pack(pady=20)

    # Chạy giao diện Tkinter
    root.mainloop()

if __name__ == "__main__":
    create_gui()
