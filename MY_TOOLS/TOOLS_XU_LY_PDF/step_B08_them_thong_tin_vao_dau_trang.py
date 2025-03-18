import os
from tkinter import Tk, filedialog
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter

def add_directory_name_to_pdf(pdf_path, directory_name, filename):
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

        # Tính toán vị trí vẽ thông tin (x, y) cho đầu trang bên phải
        page_width, page_height = letter
        text_x = page_width - 150  # Vị trí x (bên phải, cách từ lề phải ...px)
        text_y = page_height - 5  # Vị trí y (cách đầu trang ...px)

        # Chèn tên thư mục vào đầu trang bên phải
        c.drawString(text_x, text_y, f"{directory_name}")

        # Tính toán vị trí để chèn tên file dưới tên thư mục
        text_y -= 12  # Giảm 12px để tên file nằm dưới thư mục

        # Chèn tên file dưới tên thư mục
        c.drawString(text_x, text_y, f"File: {filename}")

        c.save()

        # Di chuyển đến vị trí của trang PDF gốc và thêm nội dung
        packet.seek(0)
        new_pdf = PdfReader(packet)
        page.merge_page(new_pdf.pages[0])

        # Thêm trang đã chỉnh sửa vào writer
        writer.add_page(page)

    # Ghi trực tiếp lên file PDF gốc
    with open(pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

def process_directory(selected_directory):
    # Duyệt qua các thư mục và file trong thư mục đã chọn
    for root, dirs, files in os.walk(selected_directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                # Lấy tên thư mục cấp 1
                directory_name = os.path.basename(root)
                
                # Lấy đường dẫn file PDF gốc
                pdf_path = os.path.join(root, file)

                # Thêm tên thư mục và tên file vào file PDF
                add_directory_name_to_pdf(pdf_path, directory_name, file)
                print(f"Đã chỉnh sửa file: {pdf_path}")

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
