import tkinter as tk
from tkinter import font

def set_window_size(root, width=1600, height=900):
    # Thiết lập kích thước cửa sổ
    root.geometry(f"{width}x{height}")
    
    # Đảm bảo cửa sổ không thể thay đổi kích thước
    root.resizable(False, False)
    
    # Nếu bạn muốn căn giữa cửa sổ, bạn có thể tính toán vị trí và đặt lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Reusable function to set font for menu items
def f_set_menu_font(widget, size=14, font_is="Arial"):
    """Set the font for menu items to a specified size."""
    custom_font = font.Font(family=font_is, size=size)  # Create a new Font object with the desired size
    widget.config(font=custom_font)  # Apply the font to the menu