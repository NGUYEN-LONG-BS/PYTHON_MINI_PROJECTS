import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    source_folder.set(folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory()
    destination_folder.set(folder_selected)

def copy_and_rename_pdfs():
    source = source_folder.get()
    destination = destination_folder.get()

    if not source or not destination:
        messagebox.showerror("Lỗi", "Vui lòng chọn cả folder gốc và folder đích")
        return

    pdf_files = []
    for root, dirs, files in os.walk(source):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append((root, file))

    if not pdf_files:
        messagebox.showinfo("Thông báo", "Không tìm thấy file PDF nào trong folder gốc và các folder con")
        return

    for i, (dir_path, file_name) in enumerate(pdf_files):
        # Lấy tên folder cha (cấp 1) của file PDF
        relative_path = os.path.relpath(dir_path, source)
        folder_name = os.path.basename(dir_path)
        new_name = f"{folder_name[:3]}_{i+1:02d}.pdf"
        source_file = os.path.join(dir_path, file_name)
        destination_file = os.path.join(destination, new_name)
        shutil.copy(source_file, destination_file)

    messagebox.showinfo("Thông báo", f"Đã copy và đổi tên {len(pdf_files)} file PDF thành công")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Copy và Đổi tên PDF")

# Tạo các biến để lưu đường dẫn
source_folder = tk.StringVar()
destination_folder = tk.StringVar()

# Tạo các nút và label
tk.Label(root, text="Folder gốc:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_folder, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Chọn Folder gốc", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Folder đích:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Chọn Folder đích", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Copy và Đổi tên PDF", command=copy_and_rename_pdfs).grid(row=2, column=1, padx=10, pady=20)

# Chạy chương trình
root.mainloop()