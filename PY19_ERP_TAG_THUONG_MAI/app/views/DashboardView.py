# Project/Views/DashboardView.py
import tkinter as tk
from components import *
from utils import *
# import inspect

def render_dashboard():
    root = tk.Tk()
    # root = ctk.CTk()
    root.title("Dashboard")
    
    # Thiết lập kích thước cửa sổ
    set_window_size(root)

    # Debug
    # Kiểm tra đường dẫn của hàm set_window_size
    f_find_my_function_path(set_window_size)
    
    # Gọi các thành phần tái sử dụng
    create_header(root)
    create_top_menu(root, root)
    left_menu_frame  = create_left_menu(root)
    right_banner_frame = create_right_banner(root)
    
    create_footer(root)
    
    # Start the Tkinter main loop
    root.mainloop()
