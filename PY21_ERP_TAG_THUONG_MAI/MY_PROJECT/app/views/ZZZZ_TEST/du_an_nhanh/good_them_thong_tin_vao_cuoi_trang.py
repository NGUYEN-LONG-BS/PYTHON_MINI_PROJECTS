import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import shutil
import subprocess

# Hàm để chèn tên thư mục vào trang hiện tại của file PDF
def add_directory_name_to_pdf(pdf_path, directory_name, output_pdf_path):
    # Đọc file PDF gốc
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Duyệt qua tất cả các trang của file PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        # Sử dụng BytesIO để tạo trang PDF mới mà không tạo thêm trang
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=letter)
        c.setFont("Helvetica", 10)
        
        # Chèn tên thư mục vào vị trí mong muốn trên trang
        c.drawString(10, 10, f"{directory_name}")
        c.save()

        # Di chuyển đến vị trí của trang PDF gốc và thêm nội dung
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])

        # Thêm trang đã chỉnh sửa vào writer
        writer.add_page(page)

    # Ghi lại file PDF đã được chỉnh sửa
    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

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
                        
                        # Thêm tên thư mục vào PDF mà không tạo trang mới
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
