import tkinter as tk

class RegisterView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Register")
        self.master.geometry("400x350")

        self.create_widgets()

    def create_widgets(self):
        self.username_label = tk.Label(self.master, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.email_label = tk.Label(self.master, text="Email")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        self.password_label = tk.Label(self.master, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self.master, text="Register", command=self.on_register)
        self.register_button.pack()

    def on_register(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.register(username, email, password)
