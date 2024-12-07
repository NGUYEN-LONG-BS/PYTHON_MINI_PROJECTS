import tkinter as tk

class Header:
    def __init__(self, master):
        self.master = master
        self.header_frame = tk.Frame(self.master, bg="lightblue", height=50)
        self.header_frame.pack(fill=tk.X)

        self.create_header()

    def create_header(self):
        # Example header with a title and placeholder buttons
        title = tk.Label(self.header_frame, text="My Application", font=("Arial", 18), bg="lightblue")
        title.pack(side=tk.LEFT, padx=10)

        logout_button = tk.Button(self.header_frame, text="Logout", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10)

    def logout(self):
        print("Logging out...")
