import os
from utils import *
import tkinter as tk
from tkinter import messagebox
import json
from AD0101_Dashboard_View import *
# from Components_View.logo import setup_logo  # Import the setup_logo function
from PIL import Image, ImageTk

# View: The UI that the user interacts with
class cls_LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        
        model = cls_UserModel()
        self.controller = cls_LoginController(model, self)
        
        self.title("AD0001 - Login")
        f_set_window_size_is_4_per_5_screen(self, 400, 300)
        f_set_center_screen(self)
        
        self.f_create_faricon()

        # Add your widgets and layout here (e.g., Entry fields, buttons)
        self.create_widgets()

        # Bind Enter key to on_enter method
        self.bind('<Return>', self.on_enter)

    def f_create_faricon(self):
        # Get the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))  # Going 3 levels up
        
        # Load the logo images
        Far_icon = os.path.join(project_root, "assets/icons/far_icon.png")
        
        img = Image.open(Far_icon)  # Replace with the path to your image file
        logo = ImageTk.PhotoImage(img)
        # Set the window icon
        self.iconphoto(False, logo)
    
    def create_widgets(self):
        # Setup the logo in the Frame_logo using the imported function
        Frame_logo = tk.Frame(self, width=100, height=100)
        Frame_logo.pack(pady=5)  # Pack the logo frame on the left side with some padding
        f_utils_setup_logo(Frame_logo)  # Pass the frame as the parent for the logo
        
        # Example of adding an entry field and button
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(self, width=50)
        self.entry_username.pack(pady=5)
        # Set focus on the username entry field when the form initializes
        self.entry_username.focus_set()

        self.label_password = tk.Label(self, text="Password:")
        self.label_password.pack(pady=5)

        # Frame to contain the password entry and the toggle button side by side
        self.password_frame = tk.Frame(self)
        self.password_frame.pack(pady=5)

        self.entry_password = tk.Entry(self.password_frame, show="*", width=30)
        self.entry_password.pack(side="left", pady=5)

        # Button to toggle password visibility
        self.toggle_password_button = tk.Button(self.password_frame, text="Show Password", command=self.toggle_password)
        self.toggle_password_button.pack(side="left", pady=5)
        
        self.login_button = tk.Button(self, text="Login", command=self.on_login)
        self.login_button.pack(pady=10)

        self.message_label = tk.Label(self, text="", fg="red")
        self.message_label.pack(pady=5)
        
        # self.f_main_loop()

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.handle_login(username, password)

    def set_controller(self, controller):
        self.controller = controller
        # print(f"Controller được set: {self.controller}")

    def show_message(self, login_sucess):
        if login_sucess == True:
            self.write_credentials_to_json(self.entry_username.get(), self.entry_password.get())
            self.destroy()
            self.open_dashboard()
        else:
            self.message_label.config(text="Invalid username or password.")
    
    def open_dashboard(self):
        cls_Dashboard_View()
        
    def toggle_password(self):
        # Toggle the password visibility
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
            self.toggle_password_button.config(text="Hide Password")
        else:
            self.entry_password.config(show='*')
            self.toggle_password_button.config(text="Show Password")
        
    # Function to write credentials to a JSON file
    def write_credentials_to_json(self, username, password):
        # Xác định đường dẫn file json
        base_dir = os.path.dirname(__file__)
        json_file = os.path.join(base_dir, 'login_credentials.json')
        
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
class cls_LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def handle_login(self, username, password):
        # Xử lý đăng nhập
        # print(f"Username: {username}, Password: {password}")
        if self.model.validate_user(username, password):
            self.view.show_message(True)
        else:
            self.view.show_message(False)

# Model: Handles data
class cls_UserModel:
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