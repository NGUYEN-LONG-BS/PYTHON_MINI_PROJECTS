import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import PyPDF2
from docx import Document
# from utils import *

# Hàm chọn file PDF
def open_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        try:
            password = None  # Nếu không có mật khẩu, để None
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)

                # Kiểm tra xem file PDF có mã hóa hay không
                if pdf_reader.is_encrypted:
                    password = simpledialog.askstring("Mật khẩu", "Nhập mật khẩu để mở file PDF:")
                    if password:
                        pdf_reader.decrypt(password)
                    else:
                        messagebox.showerror("Lỗi", "Không có mật khẩu để mở file PDF!")
                        return

                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

            # Nếu có nội dung, lưu vào file Word
            if text:
                save_to_word(text)
            else:
                messagebox.showwarning("Lỗi", "Không thể đọc nội dung từ file PDF!")
        except Exception as e:
            print(f"Error: {e}")
            # print("Error at function: ", f_utils_get_current_function_name())
            messagebox.showerror("Lỗi", f"Đã có lỗi xảy ra: {str(e)}")
    else:
        messagebox.showwarning("Lỗi", "Không có file PDF nào được chọn.")

# Hàm lưu nội dung vào file Word
def save_to_word(text):
    doc = Document()
    doc.add_paragraph(text)
    save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Documents", "*.docx")])
    if save_path:
        doc.save(save_path)
        messagebox.showinfo("Thông báo", "File Word đã được lưu thành công!")

# Tạo giao diện với Tkinter
def create_gui():
    root = tk.Tk()
    root.title("PDF to Word Converter")

    # Cấu hình giao diện
    root.geometry("400x200")
    
    label = tk.Label(root, text="Chọn file PDF để chuyển thành file Word", font=("Arial", 12))
    label.pack(pady=20)

    btn_open = tk.Button(root, text="Chọn PDF", command=open_pdf_file, font=("Arial", 12))
    btn_open.pack(pady=10)

    root.mainloop()

# Gọi hàm để tạo giao diện
create_gui()
