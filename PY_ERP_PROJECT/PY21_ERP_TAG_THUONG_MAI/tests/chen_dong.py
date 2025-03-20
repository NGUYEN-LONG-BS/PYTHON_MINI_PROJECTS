import tkinter as tk
from tkinter import filedialog
import xlwings as xw

def open_excel_file():
    # Mở hộp thoại để chọn file Excel
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xlsm")])
    
    if file_path:
        print(f"Đã chọn file: {file_path}")

        # Mở Excel và workbook
        wb = xw.Book(file_path)
        ws = wb.sheets['Sheet1']  # Đảm bảo bạn chọn đúng sheet nếu cần, ở đây là Sheet1
        range_to_insert = ws.range('B5:F7')
        
        # Chèn một dòng mới vào vị trí hiện tại của selection
        range_to_insert.api.Rows.Insert(Shift=-4121) # Trong Excel, -4121 là giá trị đại diện cho hành động "ShiftDown", di chuyển các dòng xuống khi chèn dòng mới.

        # Xác định vùng cần sao chép và dán
        RANGE_COPY = 'B4:F4'
        RANGE_PASTE = 'B5:F7'

        # Sao chép và dán dữ liệu
        ws.range(RANGE_COPY).copy(ws.range(RANGE_PASTE))

if __name__ == "__main__":
    open_excel_file()
