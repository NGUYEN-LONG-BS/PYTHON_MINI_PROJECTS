import tkinter as tk
from tkinter import messagebox

# View: The UI that the user interacts with
class cls_LoginView(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tkinter root window
        
        model = cls_UserModel()
        self.controller = cls_LoginController(model, self)
        
        self.title("Login System")
        self.geometry("300x200")  # Window size (300x200)

        # Add your widgets and layout here (e.g., Entry fields, buttons)
        self.create_widgets()

    def create_widgets(self):
        # Example of adding an entry field and button
        self.label_username = tk.Label(self, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(self, width=50)
        self.entry_username.pack(pady=5)

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
            self.destroy()
            self.open_dashboard()
        else:
            self.message_label.config(text="Invalid username or password.")
    
    def open_dashboard(self):
        # Import hàm render_dashboard từ DashboardView_Iherit_Component trong views
        from app.views.dashboard.DashboardView import f_render_dashboard
        # Gọi hàm render_dashboard để hiển thị dashboard
        f_render_dashboard()
        
    def toggle_password(self):
        # Toggle the password visibility
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
            self.toggle_password_button.config(text="Hide Password")
        else:
            self.entry_password.config(show='*')
            self.toggle_password_button.config(text="Show Password")
    
    def center_window(self, width, height):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position of the window to center it
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)

        # Set the dimensions of the window and its position
        self.geometry(f'{width}x{height}+{position_right}+{position_top}')

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