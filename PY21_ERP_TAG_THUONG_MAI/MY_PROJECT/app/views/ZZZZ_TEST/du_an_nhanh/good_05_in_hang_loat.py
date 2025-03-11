import os
import tkinter as tk
from tkinter import filedialog
import win32print
import win32api

def print_pdf(pdf_path):
    try:
        win32api.ShellExecute(0, "print", pdf_path, None, ".", 0)
        print(f"Đang in: {pdf_path}")
    except Exception as e:
        print(f"Không thể in file {pdf_path}: {e}")

def print_pdfs_from_folder(folder_path):
    # Duyệt qua tất cả các thư mục và file trong folder, bao gồm các thư mục con
    for root_dir, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root_dir, file)
                print_pdf(file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        print_pdfs_from_folder(folder_path)

# Giao diện Tkinter
root = tk.Tk()
root.title("In các file PDF")
root.geometry("300x100")

# Nút để chọn folder và in các file PDF
btn_select_folder = tk.Button(root, text="Chọn thư mục để in PDF", command=select_folder)
btn_select_folder.pack(pady=20)

# Chạy giao diện
root.mainloop()
