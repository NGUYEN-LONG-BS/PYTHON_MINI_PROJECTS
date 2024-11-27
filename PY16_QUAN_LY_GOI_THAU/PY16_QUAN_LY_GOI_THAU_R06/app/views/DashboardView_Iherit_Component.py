import tkinter as tk
import customtkinter as ctk
from components.menu import create_menu
from components.footer import create_footer
from components.header import create_header
from components.left_menu import create_left_menu
from components.right_banner import create_right_banner
from ..utils.utils import set_window_size

def render_dashboard():
    root = tk.Tk()
    root.title("Dashboard")
    
    # Thiết lập kích thước cửa sổ
    set_window_size(root)
    
    # Gọi các thành phần tái sử dụng
    create_header(root)
    create_menu(root)
    create_left_menu(root)
    create_right_banner(root)
    create_footer(root)
    
    # Start the Tkinter main loop
    root.mainloop()
