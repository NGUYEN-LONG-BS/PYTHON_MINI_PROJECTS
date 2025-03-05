import os
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

def package_exe():
    file_path = entry_path.get()
    output_folder = entry_output.get()
    if not file_path:
        messagebox.showwarning("Cảnh báo", "Hãy chọn một file Python trước!")
        return
    if not output_folder:
        messagebox.showwarning("Cảnh báo", "Hãy chọn thư mục xuất file!")
        return
    
    # Xác định thư mục chứa file Python
    project_root = os.path.dirname(file_path)
    # assets_folder = os.path.join(project_root, "assets")
    config_folder = os.path.join(project_root, "config")

    # Kiểm tra thư mục assets
    if not os.path.exists(config_folder):
        messagebox.showerror("Lỗi", "Thư mục 'assets' không tồn tại! Hãy chắc chắn rằng nó nằm cùng cấp với file Python.")
        return

    try:
        messagebox.showinfo("Đang đóng gói", "Quá trình đóng gói đang diễn ra, vui lòng đợi!")

        # Thực thi lệnh PyInstaller với `--add-data` để đưa cả thư mục `assets` vào
        subprocess.run([
            "pyinstaller",
            "--onefile",
            # "--noconsole",
            # f"--add-data={assets_folder};assets",  # Đảm bảo thư mục được đóng gói
            f"--add-data={config_folder};config",  # Đảm bảo thư mục được đóng gói
            "--distpath", output_folder,
            file_path
        ], check=True)

        messagebox.showinfo("Thành công", f"Đóng gói thành công! File .exe nằm trong thư mục '{output_folder}'.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")

# Giao diện Tkinter
root = tk.Tk()
root.title("Đóng gói Python thành EXE")
root.geometry("400x250")

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

btn_package = tk.Button(root, text="Đóng gói", command=package_exe)
btn_package.pack(pady=10)

root.mainloop()
