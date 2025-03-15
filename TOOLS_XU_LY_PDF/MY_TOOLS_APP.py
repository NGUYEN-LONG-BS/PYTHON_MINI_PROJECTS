import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import os
from PyPDF2 import PdfMerger
from PIL import Image
from fpdf import FPDF

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Anh Nè 27 - Ver_01.01_250315")
root.geometry("800x600")

# Tạo widget Notebook để chứa các tab
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Tạo các khung nội dung cho từng tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# ================================================================================================================================================
# Tạo Canvas và Scrollbar
tab_pdf_canvas = tk.Canvas(tab2)
tab_pdf_scrollbar = ttk.Scrollbar(tab2, orient="vertical", command=tab_pdf_canvas.yview)
tab_pdf_canvas.config(yscrollcommand=tab_pdf_scrollbar.set)

# Tạo frame con trong Canvas để chứa các widget
tab_pdf_scrollable_frame = ttk.Frame(tab_pdf_canvas)
# tab_pdf_scrollable_frame.pack(side="left", fill="both", expand=True)

# Đặt scrollable_frame vào canvas
tab_pdf_canvas.create_window((0, 0), window=tab_pdf_scrollable_frame, anchor="nw")

# Kết nối Scrollbar với Canvas
tab_pdf_scrollbar.pack(side="right", fill="y")
tab_pdf_canvas.pack(side="left", fill="both", expand=True)

# Cập nhật vùng cuộn khi kích thước thay đổi
tab_pdf_scrollable_frame.update_idletasks()
tab_pdf_canvas.config(scrollregion=tab_pdf_canvas.bbox("all"))

# Sự kiện cuộn chuột
def on_mouse_wheel(event):
    tab_pdf_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Liên kết sự kiện cuộn chuột với Canvas
tab_pdf_canvas.bind_all("<MouseWheel>", on_mouse_wheel)
# ================================================================================================================================================

# Thêm nội dung vào tab1
label1 = tk.Label(tab1, text="CÁC TÁC VỤ VỚI FOLDER")
label1.pack(padx=10, pady=10)

# Thêm nội dung vào tab2
label2 = tk.Label(tab_pdf_scrollable_frame, text="CÁC TÁC VỤ VỚI FILE PDF")
label2.pack(padx=10, pady=10)

# Thêm nội dung vào tab thông tin thêm
tab_cuoi_label_header = tk.Label(tab3, text="CÁC THÔNG TIN KHÁC")
tab_cuoi_label_header.pack(padx=10, pady=10)

tab_cuoi_label_01 = tk.Label(tab3, text="Link tải version mới nhất")
tab_cuoi_label_01.pack(padx=10, pady=10)

tab_cuoi_label_02 = tk.Label(tab3, text="Link github source code")
tab_cuoi_label_02.pack(padx=10, pady=10)

tab_cuoi_label_03 = tk.Label(tab3, text="Link donate")
tab_cuoi_label_03.pack(padx=10, pady=10)

tab_cuoi_label_04 = tk.Label(tab3, text="Link các sản phẩm mình bán")
tab_cuoi_label_04.pack(padx=10, pady=10)

# Thêm các tab vào notebook
notebook.add(tab1, text="FOLDER")
notebook.add(tab2, text="PDF")
notebook.add(tab3, text="INFO")

# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# Tab folder

# ================================================================================================================================================
# Tác vụ với folder - số 01
def count_pdf_files(folder_path, string_extension):
    # Biến đếm số lượng file PDF
    pdf_count = 0
    
    # Duyệt qua tất cả các file và thư mục trong thư mục
    for root_dir, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Kiểm tra nếu file có đuôi là .pdf (không phân biệt chữ hoa/thường)
            if file_name.lower().endswith(f".{string_extension}"):
                pdf_count += 1
    
    return pdf_count

def on_select_folder(label_path, label_result, entry_extension):
    var_extension = entry_extension.get()
    if not var_extension:
        messagebox.showerror("Lỗi", "Vui lòng nhập extension")
        return
    # Mở hộp thoại chọn thư mục
    folder_path = filedialog.askdirectory(title="Chọn thư mục")
    if folder_path:
        # Đếm số lượng file PDF trong thư mục
        pdf_count = count_pdf_files(folder_path, var_extension)
        
        label_path.config(text=f"Thư mục kiểm tra {folder_path}")
        label_result.config(text=f"Số lượng file có đuôi .{var_extension} là: {pdf_count}")

def tab1_frame_01_btn_01_on_click():
    on_select_folder(tab_folder_frame_01_lable_path, tab_folder_frame_01_lable_result, tab_folder_frame_01_entry_extension)

tab_folder_frame_01 = ttk.Frame(tab1)
tab_folder_frame_01.pack(padx=10, pady=10, fill="x", expand=True)
tab_folder_frame_01.config(border=1, relief=tk.RAISED)
# Tạo nút để người dùng chọn thư mục
tk.Label(tab_folder_frame_01, text="TASK 01 - Đếm số lượng file trong thư mục theo phần extension").grid(row=0, column=0, padx=10, pady=10)
tab_folder_frame_01_btn_01 = tk.Button(tab_folder_frame_01, text="Chọn thư mục", command=tab1_frame_01_btn_01_on_click)
tab_folder_frame_01_btn_01.grid(row=1, column=0, padx=10, pady=10)

tab_folder_frame_01_entry_extension = tk.Entry(tab_folder_frame_01, width=10)
tab_folder_frame_01_entry_extension.grid(row=1, column=1, padx=10, pady=10)

tab_folder_frame_01_lable_path = tk.Label(tab_folder_frame_01, wraplength=600) # 600px
tab_folder_frame_01_lable_path.grid(row=2, column=0, padx=10, pady=10)

tab_folder_frame_01_lable_result = tk.Label(tab_folder_frame_01)
tab_folder_frame_01_lable_result.grid(row=3, column=0, padx=10, pady=10)

# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# Tác vụ với pdf - số 01

def select_pdf_files():
    global tab_pdf_frame_01_pdf_files  # Chỉ rõ là sử dụng biến toàn cục
    # Mở hộp thoại chọn file và cho phép chọn nhiều file PDF
    selected_files = filedialog.askopenfilenames(
        title="Chọn các file PDF",
        filetypes=[("PDF files", "*.pdf")]
    )

    if selected_files:
        for file in selected_files:
            # Thêm từng file vào listbox và danh sách pdf_files
            tab_pdf_frame_01_pdf_files.append(file)
            tab_pdf_frame_01_file_listbox.insert(tk.END, file)

        tab_pdf_frame_01_status_label.config(text=f"Đã chọn {len(tab_pdf_frame_01_pdf_files)} file PDF.")
        tab_pdf_frame_01_merge_button.config(state=tk.NORMAL)  # Kích hoạt nút "Nối file PDF"
    else:
        tab_pdf_frame_01_status_label.config(text="Không có file PDF nào được chọn.")
        tab_pdf_frame_01_merge_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút "Nối file PDF"

def merge_pdfs():
    global tab_pdf_frame_01_pdf_files  # Chỉ rõ là sử dụng biến toàn cục
    if not tab_pdf_frame_01_pdf_files:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một file PDF!")
        return

    # Chọn nơi lưu file PDF đã nối
    output_file = filedialog.asksaveasfilename(
        title="Lưu file PDF đã nối",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if output_file:
        try:
            merger = PdfMerger()

            # Đang nối theo thứ tự tên file
            # Thêm từng file PDF vào merger
            for pdf in tab_pdf_frame_01_pdf_files:
                merger.append(pdf)
                
            # Lưu file PDF đã nối
            merger.write(output_file)
            merger.close()

            messagebox.showinfo("Thành công", f"Đã nối và lưu file PDF tại:\n{output_file}")
            tab_pdf_frame_01_status_label.config(text="Hoàn thành!")
            tab_pdf_frame_01_pdf_files = []  # Reset danh sách file
            tab_pdf_frame_01_file_listbox.delete(0, tk.END)  # Xóa tất cả các file trong listbox
            tab_pdf_frame_01_merge_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút sau khi hoàn thành
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi nối file PDF:\n{str(e)}")
    else:
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn nơi lưu file PDF!")

tab_pdf_frame_01 = ttk.Frame(tab_pdf_scrollable_frame)
tab_pdf_frame_01.pack(padx=10, pady=10, fill="x", expand=True)
tab_pdf_frame_01.config(border=1, relief=tk.RAISED)

# Biến lưu trữ đường dẫn các file PDF
tab_pdf_frame_01_pdf_files = []

# Tạo giao diện
tab_pdf_frame_01_label_01 = tk.Label(tab_pdf_frame_01, text="TASK 01 - Chọn các file PDF để nối:", font=("Arial", 12))
tab_pdf_frame_01_label_01.pack(pady=10)

tab_pdf_frame_01_label_02 = tk.Label(tab_pdf_frame_01, text="Lưu ý: nối theo thứ tự abc tên file", font=("Arial", 9))
tab_pdf_frame_01_label_02.pack(pady=10)

tab_pdf_frame_01_select_button = tk.Button(tab_pdf_frame_01, text="Chọn file PDF", command=select_pdf_files)
tab_pdf_frame_01_select_button.pack(pady=5)

tab_pdf_frame_01_merge_button = tk.Button(tab_pdf_frame_01, text="Nối file PDF", command=merge_pdfs, state=tk.DISABLED)
tab_pdf_frame_01_merge_button.pack(pady=5)

tab_pdf_frame_01_status_label = tk.Label(tab_pdf_frame_01, text="", fg="blue")
tab_pdf_frame_01_status_label.pack(pady=10)

# Listbox để hiển thị các file đã chọn
tab_pdf_frame_01_file_listbox = tk.Listbox(tab_pdf_frame_01, width=50, height=10)
tab_pdf_frame_01_file_listbox.pack(pady=10)

# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# Tác vụ với pdf - số 02

def select_images():
    global tab_pdf_frame_02_image_files
    # Mở hộp thoại chọn file và cho phép chọn nhiều file ảnh
    tab_pdf_frame_02_image_files = filedialog.askopenfilenames(
        title="Chọn file ảnh",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if tab_pdf_frame_02_image_files:
        tab_pdf_frame_02_status_label.config(text=f"Đã chọn {len(tab_pdf_frame_02_image_files)} file ảnh.")
        tab_pdf_frame_02_convert_button.config(state=tk.NORMAL)  # Kích hoạt nút "Chuyển sang PDF"
    else:
        tab_pdf_frame_02_status_label.config(text="Không có file ảnh nào được chọn.")
        tab_pdf_frame_02_convert_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút "Chuyển sang PDF"

def convert_to_pdf():
    global tab_pdf_frame_02_image_files
    if not tab_pdf_frame_02_image_files:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một file ảnh!")
        return

    # Chọn nơi lưu file PDF
    output_file = filedialog.asksaveasfilename(
        title="Lưu file PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )

    if output_file:
        try:
            # Tạo một đối tượng PDF
            pdf = FPDF()

            # Thêm từng ảnh vào PDF
            for image_file in tab_pdf_frame_02_image_files:
                # Mở ảnh bằng Pillow
                img = Image.open(image_file)

                # Chuyển đổi ảnh sang PDF
                pdf.add_page()
                pdf.image(image_file, x=10, y=10, w=190)  # Điều chỉnh kích thước và vị trí

            # Lưu file PDF
            pdf.output(output_file)

            messagebox.showinfo("Thành công", f"Đã chuyển đổi và lưu file PDF tại:\n{output_file}")
            tab_pdf_frame_02_status_label.config(text="Hoàn thành!")
            tab_pdf_frame_02_image_files = []  # Reset danh sách file
            tab_pdf_frame_02_convert_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút sau khi hoàn thành
        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chuyển đổi:\n{str(e)}")
    else:
        messagebox.showwarning("Cảnh báo", "Bạn chưa chọn nơi lưu file PDF!")
        
        
tab_pdf_frame_02 = ttk.Frame(tab_pdf_scrollable_frame)
tab_pdf_frame_02.pack(padx=10, pady=10, fill="x", expand=True)
tab_pdf_frame_02.config(border=1, relief=tk.RAISED)

# Tạo giao diện
tab_pdf_frame_02_label_01 = tk.Label(tab_pdf_frame_02, text="TASK 02 - Chuyển hình jpg sang pdf:", font=("Arial", 12))
tab_pdf_frame_02_label_01.pack(pady=10)

# Biến lưu trữ đường dẫn file ảnh
tab_pdf_frame_02_image_files = []

# Tạo giao diện
tab_pdf_frame_02_label = tk.Label(tab_pdf_frame_02, text="Chọn file ảnh để chuyển sang PDF:", font=("Arial", 12))
tab_pdf_frame_02_label.pack(pady=10)

tab_pdf_frame_02_select_button = tk.Button(tab_pdf_frame_02, text="Chọn ảnh", command=select_images)
tab_pdf_frame_02_select_button.pack(pady=5)

tab_pdf_frame_02_convert_button = tk.Button(tab_pdf_frame_02, text="Chuyển sang PDF", command=convert_to_pdf, state=tk.DISABLED)
tab_pdf_frame_02_convert_button.pack(pady=5)

tab_pdf_frame_02_status_label = tk.Label(tab_pdf_frame_02, text="", fg="blue")
tab_pdf_frame_02_status_label.pack(pady=10)

# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# ================================================================================================================================================
# Chạy ứng dụng
root.mainloop()
