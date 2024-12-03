import tkinter as tk
from View import View

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()

# Tạo View (View sẽ tự động xử lý việc load JSON và dữ liệu)
view = View(root)

# Bắt đầu chạy ứng dụng Tkinter
root.mainloop()
