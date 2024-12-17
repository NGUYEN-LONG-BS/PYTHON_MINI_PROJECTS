import os
import tkinter as tk
from utils import *
from Components_View.logo import setup_logo
from Components_View import *
import json
from utils import *

class cls_user_info(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Setup window
        self.title("Thông tin người dùng - Userinfo")
        # Thiết lập kích thước cửa sổ
        f_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_set_center_screen(self)
        
        self.f_create_element()
        
    def f_create_element(self):
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self, self)
        
        # Setup the logo in the Frame_logo using the imported function
        Frame_logo = tk.Frame(self, width=100, height=100)
        Frame_logo.pack(side='top', pady=10)  # Pack the logo frame on the left side with some padding
        setup_logo(Frame_logo)  # Pass the frame as the parent for the logo
        
        # Setup frame info
        frame_info = tk.Frame(self, width=100, height=100)
        frame_info.pack(side="top", pady=10)
        ID_lable = tk.Label(frame_info, text="Id:")
        ID_lable.pack(side="left")
        
        ID_value = tk.Label(frame_info, text=self.get_username_from_json())
        ID_value.pack(side="left")
        
        # Set font size to 15 for all menus
        
        # set_menu_font(ID_lable, font_size)
        # set_menu_font(ID_value, font_size)
        
        for widget in frame_info.winfo_children():
            font_size = 20
            f_set_menu_font(widget, font_size)
            # for widget in widget.winfo_children():
            #     if widget.winfo_children():
            #         set_menu_font(widget)
        
        
    def get_username_from_json(self):
        # Xác định đường dẫn file json
        base_dir = os.path.dirname(__file__)
        json_file = os.path.join(base_dir, 'login_credentials.json')
        try:
            # Open and load the JSON file
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            # Extract and return the 'username' value
            return data.get("username", None)  # Returns None if 'username' is not found

        except FileNotFoundError:
            print(f"Error: The file {json_file} does not exist.")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON.")
            return None