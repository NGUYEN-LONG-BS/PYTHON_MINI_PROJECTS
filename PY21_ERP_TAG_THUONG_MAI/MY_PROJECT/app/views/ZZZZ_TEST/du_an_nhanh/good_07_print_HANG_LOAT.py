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
    # Lấy danh sách các file trong folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # In từng file PDF
    for file in files:
        file_path = os.path.join(folder_path, file)
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
