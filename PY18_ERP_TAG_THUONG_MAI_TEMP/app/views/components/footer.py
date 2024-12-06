import tkinter as tk

class Footer:
    def __init__(self, master):
        self.master = master
        self.footer_frame = tk.Frame(self.master, bg="lightgray", height=30)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.create_footer()

    def create_footer(self):
        # Example footer with static text
        footer_label = tk.Label(self.footer_frame, text="© 2024 My Application. All rights reserved.", font=("Arial", 10), bg="lightgray")
        footer_label.pack(side=tk.LEFT, padx=10)
