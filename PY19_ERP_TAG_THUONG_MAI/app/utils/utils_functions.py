import os
import sys
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox
import inspect
from define import *
import time

def f_utils_setup_logo(parent_frame):
    # Define function when click
    def on_logo_click(event):
        # Get the top-level window containing the parent_frame
        parent_window = parent_frame.winfo_toplevel()
        parent_window.destroy()  # Close the parent window
        # Open Dashboard
        from views.AD01_Dashboard_View.Dashboard_View import cls_Dashboard_View
        cls_Dashboard_View()
        
    try:
        # Try loading the light mode image first
        logo_image_light = Image.open(PATH_LOGO_LIGHT)
        logo_image_dark = Image.open(PATH_LOGO_DARK)
        
        # Convert the PIL image to a Tkinter-compatible photo image
        logo_image_light_tk = ImageTk.PhotoImage(logo_image_light)
        logo_image_dark_tk = ImageTk.PhotoImage(logo_image_dark)
        
        # Store the image as an attribute of the parent_frame (to prevent it from being garbage collected)
        parent_frame.logo_image_light = logo_image_light_tk
        parent_frame.logo_image_dark = logo_image_dark_tk
        
        # Create the tk.Label and display the image
        logo_label = tk.Label(parent_frame, image=logo_image_light_tk)
        logo_label.pack(fill="both", expand=True) # Using pack to add it to the parent_frame
        logo_label.bind("<Button-1>", on_logo_click)  # Button-1 is left mouse click
    except FileNotFoundError:
        print(f"Logo file not found at {logo_image_light} or {logo_image_dark}")
        error_label = tk.Label(parent_frame, text="Logo not found", font=("", 16))
        error_label.pack(fill="both", expand=True)
        error_label.bind("<Button-1>", on_logo_click)  # Button-1 is left mouse click

def f_utils_setup_fav_icon(window):
        # Get the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Going 2 levels up
        
        # Load the logo images
        fav_icon = os.path.join(project_root, "assets/icons/favicon.png")
        
        img = Image.open(fav_icon)  # Replace with the path to your image file
        logo = ImageTk.PhotoImage(img)
        # Set the window icon
        window.iconphoto(False, logo)

def f_utils_find_my_function_path(function_name):
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
    print(f"Position Right: {position_right}, Position Top: {position_top}")
    
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

def f_utils_set_window_size_is_4_per_5_screen(root, width=0, height=0):
    """Set the window size to 4/5 of the screen size."""
    if width == 0 or height == 0:
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calculate 4/5 of screen dimensions
        height = int(screen_height * 4 / 5)
        width = int(screen_width * 4 / 5)
    
    # Set the window size
    root.geometry(f"{width}x{height}")

def f_utils_set_center_screen(root):
    # Lấy kích thước của cửa sổ
    root.update_idletasks()  # Cập nhật các thay đổi về kích thước
    width = root.winfo_width()
    height = root.winfo_height()
    
    # lấy thông tin kích thước màn hình và tinh toán lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán vị trí để căn giữa cửa sổ
    position_top = int(screen_height / 2 - height / 2) - 50
    position_right = int(screen_width / 2 - width / 2)

    # Đặt lại vị trí của cửa sổ
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Reusable function to set font for menu items
def f_utils_set_menu_font(widget, size=14, font_is="Arial"):
    """Set the font for menu items to a specified size."""
    custom_font = font.Font(family=font_is, size=size)  # Create a new Font object with the desired size
    widget.config(font=custom_font)  # Apply the font to the menu

def f_utils_open_dashboard():
    from views.AD01_Dashboard_View.Dashboard_View import cls_Dashboard_View
    new_view = cls_Dashboard_View()
    f_utils_set_window_size_is_4_per_5_screen(new_view)
    f_utils_set_center_screen(new_view)
    new_view.focus_force()
    
def f_utils_show_fading_popup(message):
    # Tạo cửa sổ popup
    popup = tk.Toplevel()
    popup.title("Thông báo")
    # Set background color of popup window
    popup.config(bg=BG_COLOR_0_0)
    # Ẩn thanh tiêu đề (title bar)
    popup.overrideredirect(True)
    # Căn giữa màn hình
    f_utils_set_window_size_is_4_per_5_screen(popup, 150, 50)
    f_utils_set_center_screen(popup)
    
    # Add frame
    main_frame = tk.Frame(popup, width=popup.winfo_width(), height=popup.winfo_height(), bd=1, relief="solid")
    # main_frame.grid(row=0, column=0)
    main_frame.pack()

    # Tạo nhãn để hiển thị thông báo
    label = tk.Label(main_frame, text=message, font=("Helvetica", 12))
    label.pack(pady=10, padx=10)

    # Đặt thời gian để tự động đóng cửa sổ sau 3 giây (3000 milliseconds)
    popup.after(1000, popup.destroy)


def f_utils_tim_component_label_with_text(root=None, text_to_find=""):
    if root is None:  # Start from self if root is not provided
        # root = self
        return
    
    # Loop through all children of the current root
    for widget in root.winfo_children():
        # Check if widget is a Label and its text matches
        if isinstance(widget, tk.Label) and widget.cget("text") == text_to_find:
            return widget  # Found the Label, return it

        # If widget has children, recursively search in its children
        result = f_utils_tim_component_label_with_text(widget, text_to_find)
        if result:
            return result
    return None  # No matching Label found

def f_utils_open_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select a File")
    file_name = os.path.basename(file_path)
    if file_path:
        # Check if the file is an Excel file
        if file_path.endswith(('.xls', '.xlsx')):
            # messagebox.showinfo("File Selected", f"Valid Excel file selected:\n{file_path}")
            # return file_path[-50:]
            return file_name
        else:
            # print("Not valid")
            # messagebox.showerror("Invalid File", "The selected file is not a valid Excel file!")
            # return file_path[-50:]
            return file_name