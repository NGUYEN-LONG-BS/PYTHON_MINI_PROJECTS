import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

# To store the rename rules and data files
rename_rules = {}
data_files = []
output_file = None  # To store the path of the output file

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



# Tạo giao diện người dùng với tkinter
root = tk.Tk()
root.title("Rename Files from Excel")
root.geometry("400x350")

# Nút để chọn file quy tắc đổi tên
choose_rules_button = tk.Button(root, text="Choose Rename Rules File", command=lambda: load_rename_rules(filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])))
choose_rules_button.pack(pady=20)



# Chạy ứng dụng
root.mainloop()
