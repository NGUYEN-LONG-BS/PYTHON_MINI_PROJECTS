# main.py
import tkinter as tk
from view import CRUDTreeviewView

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()

# Tạo View
view = CRUDTreeviewView(root)

# Bắt đầu chạy ứng dụng Tkinter
root.mainloop()
