import tkinter as tk

class LoginView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Login")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self.master, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.on_login)
        self.login_button.pack()

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)
