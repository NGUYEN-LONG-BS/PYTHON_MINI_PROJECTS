import tkinter as tk
from tkinter import filedialog, messagebox
import os
import zipfile
import shutil
import pandas as pd

def select_root_folder():
    folder_path.set(filedialog.askdirectory())

def unzip_all_files():
    root_folder = folder_path.get()
    if not root_folder:
        messagebox.showerror("Error", "Please select a root folder")
        return

    # Duyệt qua tất cả các thư mục con và giải nén file zip
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                folder_name = os.path.splitext(file)[0]  # Lấy tên file zip không có đuôi .zip
                final_folder_path = os.path.join(root, folder_name)

                # Tạo thư mục tạm để giải nén
                temp_folder_path = os.path.join(root, "temp")
                os.makedirs(temp_folder_path, exist_ok=True)
                
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_folder_path)

                    # Kiểm tra nếu thư mục đích đã tồn tại
                    if os.path.exists(final_folder_path):
                        shutil.rmtree(final_folder_path)  # Xóa thư mục nếu đã tồn tại
                    os.rename(temp_folder_path, final_folder_path)
                    print(f"Unzipped: {zip_path}")
                except Exception as e:
                    print(f"Error unzipping {zip_path}: {e}")
    
    messagebox.showinfo("Success", "All zip files have been extracted")

def delete_all_zips():
    root_folder = folder_path.get()
    if not root_folder:
        messagebox.showerror("Error", "Please select a root folder")
        return

    # Duyệt qua tất cả các thư mục con và xoá file zip
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".zip"):
                zip_path = os.path.join(root, file)
                try:
                    os.remove(zip_path)
                    print(f"Deleted: {zip_path}")
                except Exception as e:
                    print(f"Error deleting {zip_path}: {e}")
    messagebox.showinfo("Success", "All zip files have been deleted")


def export_to_excel():
    root_folder = folder_path.get()
    if not root_folder:
        messagebox.showerror("Error", "Please select a root folder")
        return

    data = []
    
    # Duyệt qua tất cả các thư mục con và tìm các file PDF
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".pdf"):
                level_1_folder = os.path.basename(root_folder)
                level_2_folder = os.path.basename(root)
                data.append([f"{file} - {level_1_folder}", f"{file} - {level_2_folder}"])

    if data:
        df = pd.DataFrame(data, columns=["Level 1", "Level 2"])
        excel_path = os.path.join(root_folder, "output.xlsx")
        df.to_excel(excel_path, index=False)
        messagebox.showinfo("Success", f"Excel file has been saved at {excel_path}")
    else:
        messagebox.showinfo("No PDFs", "No PDFs found to export.")


# Create main window
root = tk.Tk()
root.title("File Management Tool")

folder_path = tk.StringVar()

# Create buttons and labels
tk.Button(root, text="Select Root Folder", command=select_root_folder).pack(pady=10)
tk.Label(root, textvariable=folder_path).pack(pady=10)

tk.Button(root, text="Unzip All Files and rename", command=unzip_all_files).pack(pady=10)

tk.Button(root, text="Delete All Zips", command=delete_all_zips).pack(pady=10)

tk.Button(root, text="Export to Excel", command=export_to_excel).pack(pady=10)


root.mainloop()
