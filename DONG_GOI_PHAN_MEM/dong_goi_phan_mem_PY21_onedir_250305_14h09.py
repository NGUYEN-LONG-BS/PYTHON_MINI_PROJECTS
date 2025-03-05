import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_output.delete(0, tk.END)
        entry_output.insert(0, folder_path)

def select_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
    if icon_path:
        entry_icon.delete(0, tk.END)
        entry_icon.insert(0, icon_path)

def package_exe():
    file_path = entry_path.get()
    output_folder = entry_output.get()
    icon_path = entry_icon.get()
    hide_console = var_noconsole.get()
    
    if not file_path:
        messagebox.showwarning("Cảnh báo", "Hãy chọn một file Python trước!")
        return
    if not output_folder:
        messagebox.showwarning("Cảnh báo", "Hãy chọn thư mục xuất file!")
        return
    
    project_root = os.path.dirname(file_path)
    assets_folder = os.path.join(project_root, "../", "assets")
    config_folder = os.path.join(project_root, "../", "config")
    
    try:
        messagebox.showinfo("Đang đóng gói", "Quá trình đóng gói đang diễn ra, vui lòng đợi!")

        # Tạo danh sách lệnh PyInstaller
        command = [
            "pyinstaller",
            "--onedir",  # Chế độ thư mục
            "--distpath", output_folder,  # Thư mục xuất file
        ]
        
        # Nếu chọn ẩn console, thêm --noconsole
        if hide_console:
            command.append("--noconsole")
        
        # Nếu có icon, thêm vào lệnh
        if icon_path:
            command.extend(["--icon", icon_path])
        
        command.append(file_path)  # Thêm file nguồn vào danh sách lệnh
        
        # Thực thi lệnh PyInstaller
        subprocess.run(command, check=True)

        # Xác định thư mục chứa main.exe
        exe_folder = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0])
        
        # Sao chép thư mục assets nếu tồn tại
        if os.path.exists(assets_folder):
            shutil.copytree(assets_folder, os.path.join(exe_folder, "assets"), dirs_exist_ok=True)
        
        # Sao chép thư mục config nếu tồn tại
        if os.path.exists(config_folder):
            shutil.copytree(config_folder, os.path.join(exe_folder, "config"), dirs_exist_ok=True)

        messagebox.showinfo("Thành công", f"Đóng gói thành công! Ứng dụng nằm trong thư mục '{exe_folder}'.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

# Giao diện Tkinter
root = tk.Tk()
root.title("Đóng gói Python thành EXE")
root.geometry("400x350")

tk.Label(root, text="Chọn file Python để đóng gói:").pack(pady=5)

entry_path = tk.Entry(root, width=50)
entry_path.pack(pady=5)

btn_select = tk.Button(root, text="Chọn tệp", command=select_file)
btn_select.pack(pady=5)

tk.Label(root, text="Chọn thư mục xuất file:").pack(pady=5)

entry_output = tk.Entry(root, width=50)
entry_output.pack(pady=5)

btn_output = tk.Button(root, text="Chọn thư mục", command=select_output_folder)
btn_output.pack(pady=5)

# Thêm chức năng chọn icon
entry_icon = tk.Entry(root, width=50)
entry_icon.pack(pady=5)

btn_icon = tk.Button(root, text="Chọn icon", command=select_icon)
btn_icon.pack(pady=5)

# Thêm checkbox để chọn có ẩn console hay không
var_noconsole = tk.BooleanVar()
chk_noconsole = tk.Checkbutton(root, text="Ẩn console (--noconsole)", variable=var_noconsole)
chk_noconsole.pack(pady=5)

btn_package = tk.Button(root, text="Đóng gói", command=package_exe)
btn_package.pack(pady=10)

root.mainloop()
