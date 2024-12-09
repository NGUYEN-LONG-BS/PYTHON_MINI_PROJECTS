# Project/Views/DashboardView.py
import tkinter as tk
from components import *
from utils import *

def f_render_dashboard():
    root = tk.Tk()
    # root = ctk.CTk()
    root.title("DashboardView")
    
    # Thiết lập kích thước cửa sổ
    f_set_window_size_is_4_per_5_screen(root, 0, 0)
    f_set_center_screen(root)
    
    # # Kiểm tra đường dẫn của hàm set_window_size
    # f_find_my_function_path(set_window_size)
    
    # Gọi các thành phần tái sử dụng
    cls_menu_top(root, root)
    
    create_header(root)
    create_left_menu(root)
    create_right_banner(root)
    create_footer(root)
    
    
    # Start the Tkinter main loop
    root.mainloop()
