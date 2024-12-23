import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Form")
        self.geometry("400x500")
        self.configure(bg="#f0f0f5")
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        # Logo Section
        self.logo_frame = tk.Frame(self, bg="#f0f0f5")
        self.logo_frame.pack(pady=20)

        try:
            logo_image = Image.open(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__))), "assets/img/logo-Light.jpg"))  # Replace with your logo path
            logo_image = logo_image.resize((100, 42), Image.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(self.logo_frame, image=self.logo, bg="#f0f0f5")
            logo_label.pack()
        except FileNotFoundError:
            tk.Label(self.logo_frame, text="[Logo Here]", font=("Arial", 16), bg="#f0f0f5", fg="#666").pack()

        # Title Label
        self.title_label = tk.Label(self, text="Welcome Back!", font=("Helvetica", 20, "bold"), bg="#f0f0f5", fg="#333")
        self.title_label.pack(pady=10)

        # Username Section
        self.username_frame = tk.Frame(self, bg="#f0f0f5")
        self.username_frame.pack(pady=10, padx=30, fill="x")

        self.username_label = tk.Label(self.username_frame, text="Username", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.username_label.pack(fill="x")

        self.username_entry = tk.Entry(self.username_frame, font=("Arial", 12), bg="#ffffff", relief="solid", bd=1)
        self.username_entry.pack(fill="x", pady=5)

        # Password Section
        self.password_frame = tk.Frame(self, bg="#f0f0f5")
        self.password_frame.pack(pady=10, padx=30, fill="x")

        self.password_label = tk.Label(self.password_frame, text="Password", font=("Arial", 12), bg="#f0f0f5", anchor="w")
        self.password_label.pack(fill="x")

        self.password_entry = tk.Entry(self.password_frame, font=("Arial", 12), bg="#ffffff", relief="solid", bd=1, show="*")
        self.password_entry.pack(fill="x", pady=5)

        # Toggle Password Visibility
        self.toggle_password_button = tk.Button(self.password_frame, text="Show", font=("Arial", 10), command=self.toggle_password, relief="flat", bg="#f0f0f5", fg="#007bff", cursor="hand2")
        self.toggle_password_button.pack(anchor="ne", pady=5)

        # Login Button
        self.login_button = tk.Button(self, text="Login", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", relief="flat", command=self.handle_login, cursor="hand2")
        self.login_button.pack(pady=20, padx=30, fill="x")

        # Register Link
        self.register_label = tk.Label(self, text="Don't have an account? Register", font=("Arial", 10), bg="#f0f0f5", fg="#007bff", cursor="hand2")
        self.register_label.pack(pady=10)
        self.register_label.bind("<Button-1>", lambda e: self.open_register())

    def toggle_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
            self.toggle_password_button.config(text="Hide")
        else:
            self.password_entry.config(show='*')
            self.toggle_password_button.config(text="Show")

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "123":  # Replace with actual validation logic
            messagebox.showinfo("Success", "Login Successful!")
            self.open_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def open_dashboard(self):
        print("Opening Dashboard...")

    def open_register(self):
        print("Opening Registration Form...")

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
