import tkinter as tk
from app.utils import *

def create_header(parent, title="TUẤN ÂN GROUP"):
    # Tạo một Frame container cho header
    header_frame_container = tk.Frame(parent)
    header_frame_container.pack(side='top', fill=tk.X)
    
    # Setup the logo in the Frame_logo using the imported function
    Frame_logo = tk.Frame(header_frame_container, width=100, height=100)
    Frame_logo.pack(side='left', pady=10)
    f_utils_setup_logo(Frame_logo)
    
    header_label = tk.Label(header_frame_container, text=title, font=("Arial", 20))
    header_label.pack(side='left', pady=10)
    
    return header_frame_container
