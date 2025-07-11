import tkinter as tk
from tkinter import filedialog, messagebox
import os
from PyPDF2 import PdfMerger

def choose_file(label):
    filepath = filedialog.askopenfilename(title="Chọn file PDF", filetypes=[("PDF files", "*.pdf")])
    if filepath:
        label.config(text=filepath)
    return filepath

def merge_pdfs():
    file1 = file1_label.cget("text")
    file2 = file2_label.cget("text")

    if not file1 or not file2 or file1 == "Chưa chọn file" or file2 == "Chưa chọn file":
        messagebox.showerror("Thiếu file", "Bạn cần chọn đủ hai file PDF.")
        return

    output_dir = filedialog.askdirectory(title="Chọn thư mục lưu file đã nối")
    if not output_dir:
        return

    output_name = name_entry.get().strip()
    if not output_name:
        output_name = "output.pdf"
    if not output_name.lower().endswith(".pdf"):
        output_name += ".pdf"

    output_path = os.path.join(output_dir, output_name)
    base_name = output_name[:-4]
    counter = 1
    while os.path.exists(output_path):
        output_name = f"{base_name}_{counter}.pdf"
        output_path = os.path.join(output_dir, output_name)
        counter += 1

    try:
        merger = PdfMerger()
        merger.append(file1)
        merger.append(file2)
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Thành công", f"Đã nối file PDF thành công:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra:\n{e}")

# Tạo giao diện
root = tk.Tk()
root.title("PDF - Anh Nè (xài miễn phí)")
root.geometry("500x400")

frame = tk.Frame(root, padx=15, pady=15)
frame.pack()

# Nút chọn file 1 và hiển thị path
tk.Label(frame, text="Chọn file PDF thứ nhất:").pack(anchor="w")
file1_label = tk.Label(frame, text="Chưa chọn file", fg="blue")
file1_label.pack()
tk.Button(frame, text="Chọn file 1", command=lambda: choose_file(file1_label)).pack(pady=(0, 10))

# Nút chọn file 2 và hiển thị path
tk.Label(frame, text="Chọn file PDF thứ hai:").pack(anchor="w")
file2_label = tk.Label(frame, text="Chưa chọn file", fg="blue")
file2_label.pack()
tk.Button(frame, text="Chọn file 2", command=lambda: choose_file(file2_label)).pack(pady=(0, 20))

# Nhập tên file output
tk.Label(frame, text="Nhập tên file output (mặc định: output.pdf):").pack(anchor="w")
name_entry = tk.Entry(frame, width=40)
name_entry.pack(pady=(0, 15))

# Nút thực hiện nối
tk.Button(frame, text="Chọn nơi lưu và bắt đầu nối PDF", command=merge_pdfs, bg="green", fg="white").pack()

root.mainloop()
