import os
import tkinter as tk
from utils import *
from PIL import Image, ImageTk

class cls_Register_View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AD0002 - Register")
        f_utils_set_window_size_is_4_per_5_screen(self, 400, 300)
        f_utils_set_center_screen(self)
        self.f_create_faricon()

        # Add your widgets and layout here (e.g., Entry fields, buttons)
        self.create_widgets()
        
        # Bind Enter key to on_enter method
        self.bind('<Return>', self.f_button_register_click)

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
        
        username_label = tk.Label(self, text="Username")
        username_label.pack()
        username_entry = tk.Entry(self)
        username_entry.pack()

        email_label = tk.Label(self, text="Email")
        email_label.pack()
        email_entry = tk.Entry(self)
        email_entry.pack()

        password_label = tk.Label(self, text="Password")
        password_label.pack()
        password_entry = tk.Entry(self, show="*")
        password_entry.pack()

        register_button = tk.Button(self, text="Register", command=self.f_button_register_click)
        register_button.pack()
        
        login_button = tk.Button(self, text="login", command=self.f_button_login_click)
        login_button.pack()
        
    def f_button_register_click(self):
        print("Đã đăng ký")
        
    def f_button_login_click(self):
        self.destroy()
        from AD0001_login_View import cls_Login_View
        cls_Login_View()
