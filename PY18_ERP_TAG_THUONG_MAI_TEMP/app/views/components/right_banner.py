import tkinter as tk

class RightBanner:
    def __init__(self, master):
        self.master = master
        self.right_frame = tk.Frame(self.master, bg="white", width=200)
        self.right_frame.pack(fill=tk.Y, side=tk.RIGHT)

        self.create_banner()

    def create_banner(self):
        # Example banner with static content
        banner_label = tk.Label(self.right_frame, text="Advertisement", font=("Arial", 12), bg="white")
        banner_label.pack(pady=10)

        banner_content = tk.Label(self.right_frame, text="This is a placeholder for ads or notifications.", wraplength=180, bg="white")
        banner_content.pack(pady=5)
