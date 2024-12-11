import os
import tkinter as tk
from utils import *
from components.logo import setup_logo
from app.views.components.menu import cls_Menu
import json

class cls_user_info(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Setup window
        set_window_size(self)
        self.title("Thông tin người dùng - Userinfo")
        self.f_create_element()
        
    def f_create_element(self):
        # Create top menu (add the menu bar from menu.py)
        cls_Menu(self, self)
        
        # Setup the logo in the Frame_logo using the imported function
        Frame_logo = tk.Frame(self, width=100, height=100)
        Frame_logo.pack(side='left', padx=10)  # Pack the logo frame on the left side with some padding
        setup_logo(Frame_logo)  # Pass the frame as the parent for the logo
        
        ID_lable = tk.Label(text="Id:")
        ID_lable.pack()
        
        ID_value = tk.Label(text=self.get_username_from_json())
        ID_value.pack()
        
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