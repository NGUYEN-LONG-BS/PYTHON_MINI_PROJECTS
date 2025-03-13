import os
import shutil
from tkinter import Tk, filedialog, messagebox, Button
import glob

def select_folder(title):
    folder_selected = filedialog.askdirectory(title=title)
    return folder_selected

def find_and_copy_files(source_folder, destination_folder):
    if not source_folder or not destination_folder:
        messagebox.showerror("Error", "Vui lòng chọn đầy đủ thư mục nguồn và thư mục đích.")
        return

    # Duyệt qua các folder cấp 1 trong thư mục nguồn
    for folder1 in os.listdir(source_folder):
        folder1_path = os.path.join(source_folder, folder1)

        if os.path.isdir(folder1_path):  # Kiểm tra nếu là thư mục
            # Tạo thư mục cấp 1 trong thư mục đích
            destination_folder1 = os.path.join(destination_folder, folder1)
            if not os.path.exists(destination_folder1):
                os.makedirs(destination_folder1)

            # Tìm tất cả file Excel và PDF trong thư mục cấp 1 và các cấp dưới
            excel_files = glob.glob(os.path.join(folder1_path, '**', '*.xlsx'), recursive=True)
            pdf_files = glob.glob(os.path.join(folder1_path, '**', '*.pdf'), recursive=True)
            files_to_copy = excel_files + pdf_files

            # Sao chép các file vào thư mục đích
            for file in files_to_copy:
                if os.path.exists(file):  # Kiểm tra sự tồn tại của file trước khi sao chép
                    shutil.copy(file, destination_folder1)
                    print(f"Đã sao chép: {file} -> {destination_folder1}")
                else:
                    print(f"Lỗi: Không tìm thấy file {file}")

    messagebox.showinfo("Success", "Quá trình sao chép hoàn tất.")

def on_start():
    # Chọn thư mục nguồn
    source_folder = select_folder("Chọn thư mục nguồn")

    # Chọn thư mục đích
    destination_folder = select_folder("Chọn thư mục đích")

    # Thực hiện tìm và sao chép các file
    find_and_copy_files(source_folder, destination_folder)

# Tạo cửa sổ chính Tkinter
root = Tk()
root.title("Chương trình sao chép file Excel và PDF")

# Thêm nút để bắt đầu quá trình sao chép
start_button = Button(root, text="Bắt đầu", command=on_start)
start_button.pack(pady=20)

# Hiển thị cửa sổ
root.mainloop()
