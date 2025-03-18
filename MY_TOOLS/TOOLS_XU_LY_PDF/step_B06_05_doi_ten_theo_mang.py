import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# To store the rename rules and data files
rename_rules = {}

# Hàm xử lý đổi tên với quy tắc từ Excel
def load_rename_rules(file_path):
    try:
        # Đọc dữ liệu từ sheet đầu tiên trong file Excel
        df = pd.read_excel(file_path, sheet_name=0, header=None)  # header=None để lấy dữ liệu từ dòng đầu tiên

        # Xây dựng quy tắc đổi tên từ các cột Excel
        rename_rules.clear()  # Clear any previous data
        for index, row in df.iterrows():
            prefix = str(row[0])  # Giả sử prefix nằm trong cột đầu tiên
            old_code = str(row[1])  # Mã cũ trong cột thứ hai
            new_code = str(row[2])  # Mã mới trong cột thứ ba
            
            # Tạo dictionary cho từng prefix nếu chưa có
            if prefix not in rename_rules:
                rename_rules[prefix] = {}
            
            # Lưu quy tắc đổi tên
            rename_rules[prefix][old_code] = new_code

        # In ra quy tắc đổi tên trong terminal
        print("Rename Rules Loaded:")
        print(rename_rules)
        messagebox.showinfo("Rename Rules", "Rules loaded successfully. Check terminal for details.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading rules: {str(e)}")

# Hàm xử lý mảng dữ liệu và áp dụng quy tắc đổi tên
def apply_rename_rules_to_data(data_df):
    # Duyệt qua từng dòng dữ liệu
    renamed_data = []
    for index, row in data_df.iterrows():
        prefix = str(row[0])  # Cột prefix nằm ở cột đầu tiên (22, NL17,...)
        
        # Kiểm tra xem prefix trong ô đầu tiên có trùng với prefix trong quy tắc không
        if prefix in rename_rules:
            # Duyệt qua tất cả các cột trong dòng để tìm giá trị bắt đầu bằng "NL"
            for col_index in range(len(row)):
                cell_value = str(row[col_index])
                
                # Nếu ô có giá trị bắt đầu bằng "NL"
                if cell_value.startswith('NL'):
                    old_code = cell_value  # Lấy giá trị của ô bắt đầu bằng "NL"
                    
                    # Kiểm tra xem có quy tắc đổi tên hay không
                    if old_code in rename_rules[prefix]:
                        new_code = rename_rules[prefix][old_code]
                        # Thay thế giá trị ô với mã mới
                        new_row = row.copy()
                        new_row[col_index] = new_code
                        renamed_data.append(new_row)
                        break  # Chỉ đổi tên một lần trong mỗi dòng
            else:
                renamed_data.append(row)
        else:
            renamed_data.append(row)
    
    # Trả về dữ liệu đã đổi tên
    return pd.DataFrame(renamed_data)

# Hàm xuất kết quả
def save_renamed_data():
    global rename_rules
    if not rename_rules:
        messagebox.showerror("Error", "No rename rules loaded.")
        return

    # Chọn file dữ liệu cần đổi tên
    data_file = filedialog.askopenfilename(title="Chọn file dữ liệu", filetypes=[("Excel files", "*.xlsx;*.xls")])
    if not data_file:
        return  # Nếu người dùng không chọn file, dừng chương trình

    # Đọc dữ liệu từ file dữ liệu
    try:
        data_df = pd.read_excel(data_file, header=None)  # Đọc dữ liệu mà không có header
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data file: {str(e)}")
        return

    # Áp dụng quy tắc đổi tên vào dữ liệu
    renamed_df = apply_rename_rules_to_data(data_df)

    # Mở hộp thoại chọn thư mục xuất kết quả
    output_folder = filedialog.askdirectory(title="Chọn thư mục để lưu kết quả")
    if not output_folder:
        return  # Nếu người dùng không chọn thư mục, dừng chương trình

    # Tạo tên file kết quả
    output_file = os.path.join(output_folder, "renamed_data.xlsx")
    
    # Kiểm tra nếu file đã tồn tại, đổi tên
    if os.path.exists(output_file):
        base, ext = os.path.splitext(output_file)
        i = 1
        while os.path.exists(output_file):
            output_file = f"{base}_{i}{ext}"
            i += 1

    # Lưu kết quả vào file Excel mới
    try:
        renamed_df.to_excel(output_file, index=False, header=False)  # Không ghi tiêu đề cột
        messagebox.showinfo("Rename Files", f"File has been saved to {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save renamed data: {str(e)}")

# Tạo giao diện người dùng với tkinter
root = tk.Tk()
root.title("Rename Files from Excel")
root.geometry("400x400")

# Nút để chọn file quy tắc đổi tên
choose_rules_button = tk.Button(root, text="Choose Rename Rules File", command=lambda: load_rename_rules(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])))
choose_rules_button.pack(pady=20)

# Nút để chọn và đổi tên các file
rename_button = tk.Button(root, text="Choose Data File and Apply Rename", command=save_renamed_data)
rename_button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
