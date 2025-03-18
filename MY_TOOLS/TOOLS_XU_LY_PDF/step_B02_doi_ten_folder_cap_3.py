import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Hàm đổi tên thư mục cấp 3 và file PDF
def rename_folders_and_pdf():
    # Mở cửa sổ chọn thư mục gốc (cấp 0)
    root_folder = filedialog.askdirectory(title="Chọn thư mục gốc")
    if not root_folder:
        print("Không có thư mục gốc được chọn!")
        return

    print(f"Đang xử lý thư mục gốc: {root_folder}")

    result_message = []  # Danh sách chứa các thông báo kết quả

    # Duyệt qua các thư mục cấp 1
    for folder_name_1 in os.listdir(root_folder):
        folder_path_1 = os.path.join(root_folder, folder_name_1)
        if os.path.isdir(folder_path_1):  # Kiểm tra nếu là thư mục cấp 1
            print(f"Đang xử lý thư mục cấp 1: {folder_path_1}")
            # Duyệt qua các thư mục cấp 2
            for folder_name_2 in os.listdir(folder_path_1):
                folder_path_2 = os.path.join(folder_path_1, folder_name_2)
                if os.path.isdir(folder_path_2):  # Kiểm tra nếu là thư mục cấp 2
                    print(f"Đang xử lý thư mục cấp 2: {folder_path_2}")
                    # Duyệt qua các thư mục cấp 3 trong thư mục cấp 2
                    for subfolder_name in os.listdir(folder_path_2):
                        subfolder_path = os.path.join(folder_path_2, subfolder_name)
                        if os.path.isdir(subfolder_path):  # Kiểm tra nếu là thư mục cấp 3
                            print(f"Đang xử lý thư mục cấp 3: {subfolder_path}")
                            # Đổi tên thư mục cấp 3 theo tên của thư mục cấp 2
                            new_subfolder_name = folder_name_2  # Đặt tên thư mục cấp 3 giống tên thư mục cấp 2
                            new_subfolder_path = os.path.join(folder_path_2, new_subfolder_name)
                            
                            # Kiểm tra xem tên mới có trùng với tên thư mục cấp 3 không
                            if subfolder_path != new_subfolder_path:
                                # Kiểm tra nếu thư mục với tên mới đã tồn tại
                                if os.path.exists(new_subfolder_path):
                                    # Nếu tồn tại, tạo một tên mới với hậu tố (ví dụ: "_1")
                                    i = 1
                                    while os.path.exists(f"{new_subfolder_path}_{i}"):
                                        i += 1
                                    new_subfolder_path = f"{new_subfolder_path}_{i}"
                                
                                # Thực hiện đổi tên thư mục
                                os.rename(subfolder_path, new_subfolder_path)
                                result_message.append(f"Đổi tên thư mục: {subfolder_path} -> {new_subfolder_path}")
                                print(f"Đổi tên thư mục: {subfolder_path} -> {new_subfolder_path}")
                                
                                # Kiểm tra và đổi tên file PDF trong thư mục cấp 3
                                for file_name in os.listdir(new_subfolder_path):
                                    file_path = os.path.join(new_subfolder_path, file_name)
                                    if os.path.isfile(file_path) and file_name.lower().endswith(".pdf"):
                                        new_pdf_name = f"{new_subfolder_name}.pdf"  # Đổi tên file PDF giống thư mục
                                        new_pdf_path = os.path.join(new_subfolder_path, new_pdf_name)
                                        
                                        # Đổi tên file PDF nếu cần thiết
                                        if file_path != new_pdf_path:
                                            os.rename(file_path, new_pdf_path)
                                            result_message.append(f"Đổi tên file PDF: {file_path} -> {new_pdf_path}")
                                            print(f"Đổi tên file PDF: {file_path} -> {new_pdf_path}")

    # Hiển thị thông báo kết quả sau khi hoàn thành
    if result_message:
        messagebox.showinfo("Hoàn thành", "\n".join(result_message))
        print("Hoàn thành việc đổi tên các thư mục và file PDF!")
    else:
        messagebox.showinfo("Thông báo", "Không có thư mục cấp 3 hoặc file PDF để đổi tên.")
        print("Không có thư mục cấp 3 hoặc file PDF để đổi tên.")

# Tạo cửa sổ tkinter
window = tk.Tk()
window.title("Đổi tên thư mục cấp 3 và file PDF")

# Tạo nhãn hướng dẫn
label = tk.Label(window, text="Chọn thư mục gốc để đổi tên thư mục cấp 3 và file PDF")
label.pack(pady=10)

# Tạo nút bấm để người dùng chọn thư mục và thực hiện công việc
rename_button = tk.Button(window, text="Chọn thư mục và đổi tên", command=rename_folders_and_pdf)
rename_button.pack(pady=20)

# Tạo cửa sổ chính
window.geometry("400x200")
window.mainloop()
