import tkinter as tk
from tkinter import messagebox

# Model: Handles data
class UserModel:
    def __init__(self):
        # Example credentials, can be replaced with a database or file storage
        self.credentials = {
            "user1": "password123",
            "user2": "mypassword"
        }

    def validate_user(self, username, password):
        # Validate the user's credentials
        return self.credentials.get(username) == password


# View: The UI that the user interacts with
class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.center_window(300, 200)  # Center window with specified width and height

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(root, width=50)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=5)

        # Frame to contain the password entry and the toggle button side by side
        self.password_frame = tk.Frame(root)
        self.password_frame.pack(pady=5)

        self.entry_password = tk.Entry(self.password_frame, show="*", width=30)
        self.entry_password.pack(side="left", pady=5)

        # Button to toggle password visibility
        self.toggle_password_button = tk.Button(self.password_frame, text="Show Password", command=self.toggle_password)
        self.toggle_password_button.pack(side="left", pady=5)
        
        self.login_button = tk.Button(root, text="Login", command=self.on_login)
        self.login_button.pack(pady=10)

        self.message_label = tk.Label(root, text="", fg="red")
        self.message_label.pack(pady=5)

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.controller.handle_login(username, password)

    def set_controller(self, controller):
        self.controller = controller

    def show_message(self, message):
        self.message_label.config(text=message)
        
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
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position of the window to center it
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)

        # Set the dimensions of the window and its position
        self.root.geometry(f'{width}x{height}+{position_right}+{position_top}')


# Controller: The logic and interaction between the model and view
class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def handle_login(self, username, password):
        if self.model.validate_user(username, password):
            self.view.show_message("Login successful!")
        else:
            self.view.show_message("Invalid username or password.")


# Main function to run the program
if __name__ == "__main__":
    root = tk.Tk()
    model = UserModel()
    view = LoginView(root)
    controller = LoginController(model, view)
    root.mainloop()
