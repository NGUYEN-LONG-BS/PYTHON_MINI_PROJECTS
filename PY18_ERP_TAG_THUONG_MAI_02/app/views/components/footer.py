# Project/views/components/footer.py
import tkinter as tk

class cls_Footer:
    def __init__(self, master):
        self.master = master
        self.footer_frame = tk.Frame(self.master, bg="lightgray", height=30)
        self.footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.create_footer()

    def create_footer(self):
        # Use self.master as the parent instead of self
        footer_frame = tk.Frame(self.master)
        footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        footer_label = tk.Label(footer_frame, text="© 2025 Tuan An Group. All Rights Reserved.")
        footer_label.pack()
        
        return footer_frame
