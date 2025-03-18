import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

# Hàm để chọn file PDF và chuyển đổi sang Word
def convert_pdf_to_word():
    # Mở cửa sổ chọn file
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        # Đổi file PDF thành file Word
        word_path = file_path.replace(".pdf", ".docx")
        converter = Converter(file_path)
        converter.convert(word_path, start=0, end=None)
        converter.close()
        result_label.config(text=f"Đã chuyển đổi thành công sang: {word_path}")

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Chuyển PDF sang Word")

# Tạo nút chuyển đổi
convert_button = tk.Button(root, text="Chọn file PDF để chuyển đổi", command=convert_pdf_to_word)
convert_button.pack(pady=20)

# Label hiển thị kết quả
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Chạy giao diện
root.mainloop()
