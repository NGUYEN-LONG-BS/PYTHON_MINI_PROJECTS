# main.py
import tkinter as tk
from KD01_01QuanLyGoiThauView import View

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()

# Tạo View và gắn file JSON vào View
view = View(root)

# Bắt đầu chạy ứng dụng Tkinter
root.mainloop()
