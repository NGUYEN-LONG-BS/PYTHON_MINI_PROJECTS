# Project/Views/DashboardView.py
import tkinter as tk
from components import *
from utils import *

class cls_Dashboard_View(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tkinter root window
        
        self.title("DashboardView_10h20")
        f_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_set_center_screen(self)
        
        # # Kiểm tra đường dẫn của hàm set_window_size
        # f_find_my_function_path(set_window_size)

        self.f_render_dashboard()
        
    def f_render_dashboard(self):
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self, self)
        
        create_header(self)
        create_left_menu(self)
        create_right_banner(self)
        create_footer(self)
        