import tkinter as tk

class LeftMenu:
    def __init__(self, master):
        self.master = master
        self.left_frame = tk.Frame(self.master, bg="white", width=200)
        self.left_frame.pack(fill=tk.Y, side=tk.LEFT)

        self.create_menu()

    def create_menu(self):
        # Example navigation menu
        nav_button1 = tk.Button(self.left_frame, text="Dashboard", command=self.go_to_dashboard, width=20)
        nav_button1.pack(pady=5)

        nav_button2 = tk.Button(self.left_frame, text="Settings", command=self.go_to_settings, width=20)
        nav_button2.pack(pady=5)

    def go_to_dashboard(self):
        print("Navigating to Dashboard...")

    def go_to_settings(self):
        print("Navigating to Settings...")
