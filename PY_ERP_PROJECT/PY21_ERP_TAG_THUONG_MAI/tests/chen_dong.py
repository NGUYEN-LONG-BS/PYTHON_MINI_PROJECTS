import tkinter as tk
from tkinter import filedialog
import openpyxl

def open_excel_file():
    # Tạo cửa sổ Tkinter (không hiển thị cửa sổ chính)
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ Tkinter chính

    # Mở hộp thoại để chọn file Excel
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xlsm")])
    
    if file_path:
        print(f"Đã chọn file: {file_path}")

        # Mở file Excel
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active  # Lấy sheet đầu tiên

        # Đổi giá trị của các ô trong vùng B4:F7 thành 123
        for row in range(4, 8):  # Dòng 4 đến 7
            for col in range(2, 7):  # Cột B đến F (B = 2, F = 6)
                cell = ws.cell(row=row, column=col)
                cell.value = 123  # Đặt giá trị của ô thành 123

        # Lưu lại file Excel sau khi thay đổi
        wb.save(file_path)

        # Mở file Excel bằng ứng dụng mặc định (Excel)
        import os
        os.startfile(file_path)  # Mở file trong Excel hoặc ứng dụng mặc định

        # Giữ cửa sổ Tkinter mở
        root.deiconify()  # Hiển thị cửa sổ Tkinter
        root.mainloop()  # Duy trì cửa sổ Tkinter mở

if __name__ == "__main__":
    open_excel_file()
