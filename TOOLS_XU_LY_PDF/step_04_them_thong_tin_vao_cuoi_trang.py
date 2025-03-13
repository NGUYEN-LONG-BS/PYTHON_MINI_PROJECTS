import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter

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

def process_directory(selected_directory):
    # Duyệt qua các thư mục và file trong thư mục đã chọn
    for root, dirs, files in os.walk(selected_directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                # Lấy tên thư mục cấp 1
                directory_name = os.path.basename(root)
                
                # Lấy đường dẫn file PDF gốc và đường dẫn file PDF xuất ra
                pdf_path = os.path.join(root, file)
                output_pdf_path = os.path.join(root, f"modified_{file}")

                # Thêm tên thư mục vào file PDF
                add_directory_name_to_pdf(pdf_path, directory_name, output_pdf_path)
                print(f"Đã chỉnh sửa file: {output_pdf_path}")

def select_directory():
    # Khởi tạo giao diện để chọn thư mục
    root = Tk()
    root.withdraw()  # Ẩn cửa sổ chính
    selected_directory = filedialog.askdirectory(title="Chọn thư mục chứa file PDF")
    
    if selected_directory:
        process_directory(selected_directory)
    else:
        print("Không có thư mục nào được chọn.")

# Gọi hàm chọn thư mục
select_directory()
