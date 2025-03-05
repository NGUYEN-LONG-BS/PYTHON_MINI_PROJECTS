import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from PIL import Image, ImageTk
from app.views.Components_View import *
from app.utils import *

# View: The UI that the user interacts with
class cls_Login_View(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Initialize controller
        model = cls_User_Model()
        self.controller = cls_Login_Controller(model, self)
        
        self.title("AD0001 - Login Form")
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(self, 400, 550, maximize=False)
        f_utils_set_center_screen(self)
        f_utils_setup_fav_icon(self)
        self.resizable(False, False)

        # Add your widgets and layout here (e.g., Entry fields, buttons)
        self.f_create_widgets()

        # Bind Enter key to f_on_enter method
        self.bind('<Return>', self.f_on_enter)

    def f_on_enter(self, event):
        self.f_on_login()

    def f_create_widgets(self):
        # Logo Section
        self.logo_frame = tk.Frame(self, bg="#f0f0f5")
        self.logo_frame.pack(pady=20)

        try:
            logo_image = Image.open(PATH_LOGO_LIGHT)
            logo_image = logo_image.resize((100, 42), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.logo_frame, image=self.logo, bg="#f0f0f5")
            logo_label.pack()
        except FileNotFoundError:
            tk.Label(self.logo_frame, text="[Logo Here]", font=("Arial", 16), bg="#f0f0f5", fg="#666").pack()
            # print(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__))), "....", "assets/img/logo-Light.jpg"))

        # Title Label
        self.title_label = tk.Label(self, text="Welcome Back!", font=("Helvetica", 20, "bold"), bg="#f0f0f5", fg="#333")
        self.title_label.pack(pady=10)

        # Username Section
        self.username_frame = tk.Frame(self, bg="#f0f0f5")
        self.username_frame.pack(pady=10, padx=30, fill="x")

        self.username_label = tk.Label(self.username_frame, text="Username", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.username_label.pack(fill="x")

        # self.entry_username = tk.Entry(self.username_frame, font=("Arial", 12), bg="#ffffff", relief="solid", bd=1)
        self.entry_username = cls_my_text_entry_num_01(self.username_frame, font=("Arial", 12), bg="#ffffff", relief="solid", bd=1)
        self.entry_username.pack(fill="x", pady=5)
        self.entry_username.focus_set()

        # Password Section
        self.password_frame = tk.Frame(self, bg="#f0f0f5")
        self.password_frame.pack(pady=10, padx=30, fill="x")

        self.password_label = tk.Label(self.password_frame, text="Password", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.password_label.pack(fill="x")

        self.entry_password = cls_my_text_entry_num_01(self.password_frame, font=("Arial", 12), bg="#ffffff", relief="solid", bd=1, show="*")
        self.entry_password.pack(fill="x", pady=5)

        # Toggle Password Visibility
        self.button_toggle_password = tk.Button(self.password_frame, text="Show", font=FONT_DEFAULT_NUM_01, command=self.f_toggle_password, relief="flat", bg="#f0f0f5", fg="#007bff", cursor="hand2")
        self.button_toggle_password.pack(anchor="ne", pady=5)

        # Subsidiary Selection
        self.subsidiary_frame = tk.Frame(self, bg="#f0f0f5")
        self.subsidiary_frame.pack(pady=10, padx=30, fill="x")

        self.subsidiary_label = tk.Label(self.subsidiary_frame, text="Subsidiary", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.subsidiary_label.pack(fill="x")
        
        self.subsidiary_combobox = ttk.Combobox(self.subsidiary_frame, font=("Arial", 12), state="readonly")
        self.subsidiary_combobox['values'] = ["TA Thiết bị điện", "TA Hà Nội", "TA Việt An", "TA Nam An", "TA Long An"]
        self.subsidiary_combobox.current(0)  # Set default value
        # Load subsidiary from JSON if exists
        self.f_load_subsidiary_from_json()
        self.subsidiary_combobox.pack(fill="x", pady=5)
        
        # Login Button
        self.login_button = tk.Button(self, text="Login", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", relief="flat", command=self.f_on_login, cursor="hand2")
        self.login_button.pack(pady=20, padx=30, fill="x")

        # Register Link
        self.register_label = tk.Label(self, text="Don't have an account? Register", font=FONT_DEFAULT_NUM_01, bg="#f0f0f5", fg="#007bff", cursor="hand2")
        self.register_label.pack(pady=10)
        self.register_label.bind("<Button-1>", lambda e: self.f_open_register())

    def f_on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.f_handle_login(username, password)
        
    def f_on_register(self):
        self.destroy()
        self.f_open_register()

    def f_set_controller(self, controller):
        self.controller = controller
        # print(f"Controller được set: {self.controller}")

    def f_show_message(self, login_sucess):
        if login_sucess == True:
            self.f_write_credentials_to_json(self.entry_username.get(), self.subsidiary_combobox.get())
            self.f_open_dashboard()
        else:
            # self.message_label.config(text="Invalid username or password.")
            messagebox.showerror("Error", "Invalid username or password")
    
    def f_open_dashboard(self):
        self.destroy()
        f_utils_open_dashboard_main()
        
    def f_open_register(self):
        self.destroy()
        from AD0002_register_View import cls_Register_View
        cls_Register_View()
    
    def f_toggle_password(self):
        # Toggle the password visibility
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
            self.button_toggle_password.config(text="Hide")
        else:
            self.entry_password.config(show='*')
            self.button_toggle_password.config(text="Show")
        
    def f_write_credentials_to_json(self, username, subsidiary):    # Function to write credentials to a JSON file
        # Xác định đường dẫn file json
        json_file = PATH_JSON_LOGIN_CREDENTIALS
        
        # Create a dictionary with the credentials
        data = {
            "username": username,
            "Subsidiary": subsidiary
            }
        
        # Write to JSON file
        try:
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            # print(f"Credentials saved to {json_file}")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            
    def f_load_subsidiary_from_json(self):
        # Xác định đường dẫn file json
        json_file = PATH_JSON_LOGIN_CREDENTIALS  
        
        if os.path.exists(json_file):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    subsidiary = data.get("Subsidiary", None)
                    if subsidiary:
                        # Set the combobox value to the saved subsidiary
                        try:
                            self.subsidiary_combobox.set(subsidiary)
                        except Exception as e:
                            print(f"Error: {e}")
                            print("Error at function: ", f_utils_get_current_function_name())
            except Exception as e:
                print(f"Error: {e}")
                print("Error at function: ", f_utils_get_current_function_name())

# Controller: The logic and interaction between the model and view
class cls_Login_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.f_set_controller(self)

    def f_handle_login(self, username, password):
        # Xử lý đăng nhập
        if self.model.f_validate_user(username, password):
            self.view.f_show_message(True)
        else:
            self.view.f_show_message(False)

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

    def f_validate_user(self, username, password):
        # Validate the user's credentials
        return self.credentials.get(username) == password
    