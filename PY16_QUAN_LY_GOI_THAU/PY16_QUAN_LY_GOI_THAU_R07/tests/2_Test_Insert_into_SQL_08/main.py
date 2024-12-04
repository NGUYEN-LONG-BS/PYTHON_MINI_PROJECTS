# main.py
import tkinter as tk
from KD02QuanLyYeuCauDatHangView import cls_CRUDTreeviewView

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()

# Tạo View
view = cls_CRUDTreeviewView(root)

# Bắt đầu chạy ứng dụng Tkinter
root.mainloop()
