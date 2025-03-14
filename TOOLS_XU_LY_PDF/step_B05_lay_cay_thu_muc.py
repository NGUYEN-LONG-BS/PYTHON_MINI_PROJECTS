import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Hàm để chọn đường dẫn thư mục
def choose_directory():
    folder_path.set(filedialog.askdirectory())

# Hàm để lấy danh sách thư mục và file từ các cấp
def list_files():
    folder = folder_path.get()
    if not folder:
        return
    
    # Xóa dữ liệu hiện tại trong Treeview
    for item in treeview.get_children():
        treeview.delete(item)
    
    # Duyệt qua thư mục và các cấp con
    data = []  # Dữ liệu để lưu vào Excel
    for root, dirs, files in os.walk(folder):
        level = root.replace(folder, '').count(os.sep)
        
        # Cập nhật thông tin vào data cho từng cấp
        current_folder = os.path.basename(root)
        row = [current_folder] + [''] * (level + 1)  # Tạo dòng dữ liệu cho folder hiện tại
        
        # Thêm thư mục vào dữ liệu
        if level == 0:
            data.append(row)
        
        # Thêm các file vào dòng tương ứng
        for name in files:
            row_copy = row[:]
            row_copy[level + 1] = name  # Cập nhật tên file vào cột đúng
            data.append(row_copy)
        
        # Thêm các folder con vào dòng tương ứng
        for name in dirs:
            row_copy = row[:]
            row_copy[level + 1] = name  # Cập nhật tên folder vào cột đúng
            data.append(row_copy)

        # Cập nhật Treeview với tên các thư mục và file
        treeview.insert("", "end", text=current_folder, values=("Folder", os.path.join(root, "")))
        for name in files:
            treeview.insert("", "end", text=name, values=("File", os.path.join(root, name)))
        for name in dirs:
            treeview.insert("", "end", text=name, values=("Folder", os.path.join(root, name)))

    # Cập nhật treeview
    print(data)

# Hàm để xuất danh sách ra file Excel
def export_to_excel():
    folder = folder_path.get()
    if not folder:
        return
    
    # Cho người dùng chọn đường dẫn để lưu file Excel
    output_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
    if not output_path:
        return

    data = []
    # Duyệt qua các thư mục và file, lưu dữ liệu vào danh sách
    for root, dirs, files in os.walk(folder):
        level = root.replace(folder, '').count(os.sep)
        
        # Cập nhật thông tin vào data cho từng cấp
        current_folder = os.path.basename(root)
        row = [current_folder] + [''] * 4  # Tạo dòng dữ liệu cho folder hiện tại, tổng cộng 5 cột
        
        # Thêm thư mục vào dữ liệu
        if level == 0:
            data.append(row)
        
        # Thêm các file vào dòng tương ứng
        for name in files:
            row_copy = row[:]
            row_copy[level + 1] = name  # Cập nhật tên file vào cột đúng
            data.append(row_copy)
        
        # Thêm các folder con vào dòng tương ứng
        for name in dirs:
            row_copy = row[:]
            row_copy[level + 1] = name  # Cập nhật tên folder vào cột đúng
            data.append(row_copy)

    # Đảm bảo rằng mỗi dòng đều có đủ 5 cột (nếu thiếu cột, ta thêm giá trị rỗng vào)
    for i in range(len(data)):
        while len(data[i]) < 5:
            data[i].append('')
    
    # Xuất dữ liệu ra file Excel
    df = pd.DataFrame(data, columns=["Folder 0", "Folder 1", "Folder 2", "Folder 3", "Folder 4"])
    df.to_excel(output_path, index=False)
    print(f"Danh sách đã được xuất ra file {output_path}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Danh sách File và Folder")

# Biến chứa đường dẫn thư mục
folder_path = tk.StringVar()

# Khung nhập đường dẫn thư mục
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Chọn thư mục:")
label.grid(row=0, column=0)

entry = tk.Entry(frame, textvariable=folder_path, width=40)
entry.grid(row=0, column=1)

btn_choose = tk.Button(frame, text="Chọn thư mục", command=choose_directory)
btn_choose.grid(row=0, column=2)

# Treeview để hiển thị danh sách file và folder
treeview = ttk.Treeview(root, columns=("Type", "Path"), show="headings")
treeview.heading("Type", text="Type")
treeview.heading("Path", text="Path")
treeview.pack(padx=10, pady=10, fill="both", expand=True)

# Nút để lấy danh sách file và folder
btn_list_files = tk.Button(root, text="Lấy danh sách", command=list_files)
btn_list_files.pack(pady=5)

# Nút xuất danh sách ra file Excel
btn_export_excel = tk.Button(root, text="Xuất ra Excel", command=export_to_excel)
btn_export_excel.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
