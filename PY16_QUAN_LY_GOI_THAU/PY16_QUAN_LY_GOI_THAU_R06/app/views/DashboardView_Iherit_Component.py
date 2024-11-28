# Project/Views/DashboardView_Iherit_Component.py
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
    create_menu_TK_02(root)
    left_menu_frame  = create_left_menu(root)
    right_banner_frame = create_right_banner(root)
    
    # # Call create_main_content to add content to the dashboard
    # create_main_content(root, content_type="statistics")  # You can change content type dynamically
    
     # Create the main content area
    main_content_frame = create_main_content(root, left_menu_frame, right_banner_frame, content_type="statistics")
    
    create_footer(root)
    
    # Start the Tkinter main loop
    root.mainloop()
