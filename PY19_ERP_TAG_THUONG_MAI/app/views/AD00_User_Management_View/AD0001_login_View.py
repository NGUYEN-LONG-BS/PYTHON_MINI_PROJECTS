import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import json
from PIL import Image, ImageTk

from Components_View import cls_my_button_num_01, cls_my_label_num_01, cls_my_entry_num_01
from utils import *
from utils.define import *
from AD01_Dashboard_View import *

# View: The UI that the user interacts with
class cls_Login_View(tk.Tk):
    def __init__(self):
        super().__init__()
        
        model = cls_User_Model()
        self.controller = cls_Login_Controller(model, self)
        
        self.title("AD0001 - Login")
        f_utils_set_window_size_is_4_per_5_screen(self, 400, 300)
        f_utils_set_center_screen(self)
        f_utils_setup_fav_icon(self)
        self.resizable(False, False)

        # Add your widgets and layout here (e.g., Entry fields, buttons)
        self.create_widgets_all_frames()

        # Bind Enter key to on_enter method
        self.bind('<Return>', self.on_enter)
    
    def create_widgets_all_frames(self):
        self.Frame_main = tk.Frame(self, bd=1, relief="solid")
        self.Frame_main.pack(fill="both", expand=True)
        
        # Setup the logo in the Frame_logo using the imported function
        self.Frame_logo = tk.Frame(self.Frame_main, width=100, height=100, bd=1, relief="solid")
        self.Frame_logo.pack(pady=5)  # Pack the logo frame on the left side with some padding
        self.create_widgets_in_frame_logo()
        
        self.Frame_content = tk.Frame(self.Frame_main, bd=1, relief="solid")
        self.Frame_content.pack(fill="both", expand=True)
        self.create_widgets_in_frame_content()
        
        # Frame to contain the password entry and the toggle button side by side
        self.button_frame = tk.Frame(self.Frame_main, bd=1, relief="solid")
        self.button_frame.pack(fill="both", expand=True)
        self.create_widgets_in_frame_buttons()
        
    def create_widgets_in_frame_logo(self):
        # Load the logo image
        parent_frame = self.Frame_logo
        try:
            # Try loading the light mode image first
            logo_image_light = Image.open(PATH_LOGO_LIGHT)
            
            # Convert the PIL image to a Tkinter-compatible photo image
            logo_image_light_tk = ImageTk.PhotoImage(logo_image_light)
            
            # Store the image as an attribute of the Frame_logo (to prevent it from being garbage collected)
            parent_frame.logo_image_light = logo_image_light_tk
            
            # Create the tk.Label and display the image
            logo_label = tk.Label(parent_frame, image=logo_image_light_tk)
            logo_label.pack(fill="both", expand=True) # Using pack to add it to the Frame_logo
        except FileNotFoundError:
            print(f"Logo file not found at {PATH_LOGO_LIGHT}")
            error_label = tk.Label(parent_frame, text="Logo not found", font=("", 16))
            error_label.pack(fill="both", expand=True)
    
    def create_widgets_in_frame_content(self):
        parent_frame = self.Frame_content
        
        # Frame to contain the password entry and the toggle button side by side
        self.user_frame = tk.Frame(parent_frame)
        self.user_frame.pack(pady=5)
        self.create_widgets_in_frame_user()
        
        # Frame to contain the password entry and the toggle button side by side
        self.password_frame = tk.Frame(parent_frame)
        self.password_frame.pack(pady=5)
        self.create_widgets_in_frame_password()
        
    def create_widgets_in_frame_user(self):
        parent_frame = self.user_frame
        self.label_username = cls_my_label_num_01(parent_frame)
        self.label_username.configure(text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = cls_my_entry_num_01(parent_frame)
        self.entry_username.configure(width=50)
        self.entry_username.pack(pady=5)
        self.entry_username.focus_set()

    
    def create_widgets_in_frame_password(self):
        parent_frame = self.password_frame
        
        self.label_password_frame = tk.Frame(parent_frame)
        self.label_password_frame.pack(side="top", pady=5)
        
        self.entry_password_frame = tk.Frame(parent_frame)
        self.entry_password_frame.pack(side="top", pady=5)
        
        self.label_password = cls_my_label_num_01(self.label_password_frame)
        self.label_password.configure(text="Password:")
        self.label_password.pack(side="left", pady=5)

        self.message_label = tk.Label(self.label_password_frame, text="", fg="red")
        self.message_label.pack(side="left", padx=5)
        
        self.entry_password = cls_my_entry_num_01(self.entry_password_frame)
        self.entry_password.configure(show="*", width=30)
        self.entry_password.pack(side="left")

        
        
        # Button to toggle password visibility
        self.create_icons()
        self.toggle_password_button = cls_my_button_num_01(self.entry_password_frame)
        self.toggle_password_button.pack(side="left", padx=5)
        self.toggle_password_button.configure(command=self.toggle_password, font=("Arial", 10),
                                            image=self.icon_image_hide,
                                            compound="center"
                                            )
        
        
    def create_icons(self):
        # Load the icon image
        icon_path_hide = os.path.join(PATH_ASSETS_ICONS, "icon-closed-eye-50.png")
        icon_image_hide = Image.open(icon_path_hide)
        icon_image_hide = icon_image_hide.resize((20, 20), Image.LANCZOS)  # Resize the image to fit the button
        
        icon_path_unhide = os.path.join(PATH_ASSETS_ICONS, "icon-opening-eye-26.png")
        icon_image_unhide = Image.open(icon_path_unhide)
        icon_image_unhide = icon_image_unhide.resize((20, 20), Image.LANCZOS)  # Resize the image to fit the button
        
        self.icon_image_hide = ImageTk.PhotoImage(icon_image_hide)
        self.icon_image_unhide = ImageTk.PhotoImage(icon_image_unhide)
        
    def create_widgets_in_frame_buttons(self):
        parent_frame = self.button_frame
        
        # Configure the grid layout to center the buttons
        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_columnconfigure(2, weight=1)
        parent_frame.grid_columnconfigure(3, weight=1)
        parent_frame.grid_columnconfigure(4, weight=1)
        
        self.login_button = cls_my_button_num_01(parent_frame)
        self.login_button.configure(text="Login", width=10, command=self.on_login, font=("Arial", 10))
        # self.login_button.pack(side="left", padx=10, anchor="center")
        self.login_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        self.register_button = cls_my_button_num_01(parent_frame)
        self.register_button.configure(text="Register", width=10, command=self.on_register, font=("Arial", 10))
        # self.register_button.pack(side="left", padx=10, anchor="center")
        self.register_button.grid(row=0, column=3, padx=10, pady=5, sticky="ew")

    def on_logo_click(self, event):
        # Define the action to be taken when the logo is clicked
        print("Logo clicked")

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.handle_login(username, password)
        
    def on_register(self):
        self.destroy()
        self.open_register()

    def set_controller(self, controller):
        self.controller = controller
        # print(f"Controller được set: {self.controller}")

    def show_message(self, login_sucess):
        if login_sucess == True:
            self.write_credentials_to_json(self.entry_username.get(), self.entry_password.get())
            self.open_dashboard()
        else:
            self.message_label.config(text="Invalid username or password.")
    
    def open_dashboard(self):
        self.destroy()
        f_utils_open_dashboard()
        
    def open_register(self):
        from AD0002_register_View import cls_Register_View
        cls_Register_View()
    
    def toggle_password(self):
        # Toggle the password visibility
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
            self.toggle_password_button.config(image=self.icon_image_unhide)
        else:
            self.entry_password.config(show='*')
            self.toggle_password_button.config(image=self.icon_image_hide)
        
    def write_credentials_to_json(self, username, password):    # Function to write credentials to a JSON file
        # Xác định đường dẫn file json
        base_dir = os.path.dirname(__file__)
        json_file = os.path.join(base_dir, 'login_credentials.json')
        # print(json_file)
        
        # Create a dictionary with the credentials
        data = {
            "username": username
        }
        
        # Write to JSON file
        try:
            with open(json_file, 'w') as f:
                json.dump(data, f, indent=4)
            # print(f"Credentials saved to {json_file}")
        except Exception as e:
            print(f"Error saving credentials: {e}")

    def on_enter(self, event):
        self.on_login()


# Controller: The logic and interaction between the model and view
class cls_Login_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def handle_login(self, username, password):
        # Xử lý đăng nhập
        if self.model.validate_user(username, password):
            self.view.show_message(True)
        else:
            self.view.show_message(False)

# Model: Handles data
class cls_User_Model:
    def __init__(self):
        # Example credentials, can be replaced with a database or file storage
        self.credentials = {
            "admin": "123",     # admin
            "kd1": "123",       # kinh doanh
            "vt1": "123",       # vật tư
            "tc1": "123",       # tài chính
            "kt1": "123"        # kỹ thuật
        }

    def validate_user(self, username, password):
        # Validate the user's credentials
        return self.credentials.get(username) == password