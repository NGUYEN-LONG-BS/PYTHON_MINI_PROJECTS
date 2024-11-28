# Views/DashboardView_Iherit_Component.py
import tkinter as tk
import customtkinter as ctk
from components import *
from utils import *

def render_dashboard():
    root = tk.Tk()
    # root = ctk.CTk()
    root.title("Dashboard")
    
    # Thiết lập kích thước cửa sổ
    set_window_size(root)
    
    # Gọi các thành phần tái sử dụng
    create_header(root)
    # create_menu(root)
    create_menu_TK_02(root)
    create_left_menu(root)
    create_right_banner(root)
    create_footer(root)
    
    # Start the Tkinter main loop
    root.mainloop()
