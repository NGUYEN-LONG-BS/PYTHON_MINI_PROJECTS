import tkinter as tk
from tkinter import ttk
# from app.utils import *

class cls_Register_View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AD0002 - Register")
        
        # Configure a grid layout
        self.configure(bg="#f9f9f9")
        self.create_widgets()
        
        # Bind Enter key to on_enter method
        self.bind('<Return>', self.f_button_register_click)
        self.protocol("WM_DELETE_WINDOW", self.f_button_login_click)

    def create_widgets(self):
        # Header Section
        Frame_logo = tk.Frame(self, bg="#f9f9f9", width=400, height=100)
        Frame_logo.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")
        # f_utils_setup_logo(Frame_logo)

        header_label = tk.Label(self, text="Create Your Account", font=("Arial", 16, "bold"), bg="#f9f9f9", fg="#333")
        header_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Username
        username_label = tk.Label(self, text="Username", font=("Arial", 12), bg="#f9f9f9", fg="#333")
        username_label.grid(row=2, column=0, padx=20, pady=5, sticky="w")
        self.username_entry = ttk.Entry(self, width=30)
        self.username_entry.grid(row=2, column=1, padx=20, pady=5)

        # Email
        email_label = tk.Label(self, text="Email", font=("Arial", 12), bg="#f9f9f9", fg="#333")
        email_label.grid(row=3, column=0, padx=20, pady=5, sticky="w")
        self.email_entry = ttk.Entry(self, width=30)
        self.email_entry.grid(row=3, column=1, padx=20, pady=5)

        # Password
        password_label = tk.Label(self, text="Password", font=("Arial", 12), bg="#f9f9f9", fg="#333")
        password_label.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.password_entry = ttk.Entry(self, show="*", width=30)
        self.password_entry.grid(row=4, column=1, padx=20, pady=5)

        # Register Button
        register_button = ttk.Button(self, text="Register", command=self.f_button_register_click)
        register_button.grid(row=5, column=0, columnspan=2, pady=20)

        # Login Button
        login_button = ttk.Button(self, text="Already have an account? Login", command=self.f_button_login_click)
        login_button.grid(row=6, column=0, columnspan=2, pady=10)

    def f_button_register_click(self, event=None):
        print(f"Registered with Username: {self.username_entry.get()}, Email: {self.email_entry.get()}")
        
    def f_button_login_click(self):
        self.destroy()
        from AD0001_login_View import cls_Login_View
        cls_Login_View()

if __name__ == "__main__":
    app = cls_Register_View()
    app.mainloop()