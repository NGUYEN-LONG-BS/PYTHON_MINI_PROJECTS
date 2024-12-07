# Project/Views/DashboardView.py
import tkinter as tk
from components import *
from utils import *

def render_dashboard():
    root = tk.Tk()
    # root = ctk.CTk()
    root.title("Dashboard")
    
    # Thiết lập kích thước cửa sổ
    set_window_size(root)
    
    # Gọi các thành phần tái sử dụng
    cls_Header.create_header(root)
    create_top_menu(root, root)
    left_menu_frame  = create_left_menu(root)
    right_banner_frame = create_right_banner(root)
    
    cls_Footer.create_footer(root)
    
    # Start the Tkinter main loop
    root.mainloop()
