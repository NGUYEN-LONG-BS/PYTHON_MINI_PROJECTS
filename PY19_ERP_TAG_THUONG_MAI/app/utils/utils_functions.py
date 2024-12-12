import tkinter as tk
from tkinter import font
import inspect

def f_find_my_function_path(function_name):
    source_file = inspect.getfile(function_name)
    print(f"Function is defined in: {source_file}")

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

def f_set_window_size_is_4_per_5_screen(root, width=0, height=0):
    if width == 0 or height == 0:
        # lấy thông tin kích thước màn hình và tinh toán lại
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        height = int(screen_height * 4 / 5)
        width = int(screen_width * 4 / 5)
        
        # Đặt lại kích thước cửa sổ
        root.geometry(f"{width}x{height}")
    else:
        root.geometry(f"{width}x{height}")

def f_set_center_screen(root):
    # Lấy kích thước của cửa sổ
    root.update_idletasks()  # Cập nhật các thay đổi về kích thước
    width = root.winfo_width()
    height = root.winfo_height()
    
    # lấy thông tin kích thước màn hình và tinh toán lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    print(screen_width)
    print(screen_height)
    # position_top = int(screen_height / 2 - height / 2)
    # position_right = int(screen_width / 2 - width / 2)
    position_top = int(screen_height * 0.1)
    position_right = int(screen_width * 0.1)
    
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Reusable function to set font for menu items
def f_set_menu_font(widget, size=14, font_is="Arial"):
    """Set the font for menu items to a specified size."""
    custom_font = font.Font(family=font_is, size=size)  # Create a new Font object with the desired size
    widget.config(font=custom_font)  # Apply the font to the menu
    
def f_show_fading_popup(message):
    # Tạo cửa sổ popup
    popup = tk.Toplevel()
    popup.title("Thông báo")
    
    # Căn giữa màn hình
    f_set_center_screen(popup)

    # Tạo nhãn để hiển thị thông báo
    label = tk.Label(popup, text=message, font=("Helvetica", 12))
    label.pack(pady=10, padx=10)

    # Đặt thời gian để tự động đóng cửa sổ sau 3 giây (3000 milliseconds)
    popup.after(3000, popup.destroy)
