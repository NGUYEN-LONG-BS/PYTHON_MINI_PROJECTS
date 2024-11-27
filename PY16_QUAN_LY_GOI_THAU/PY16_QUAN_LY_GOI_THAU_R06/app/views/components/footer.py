import tkinter as tk
import customtkinter as ctk

def create_footer(parent):
    footer_frame = tk.Frame(parent)
    footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    footer_label = tk.Label(footer_frame, text="© 2024 Company Name. All Rights Reserved.")
    footer_label.pack()
    
    return footer_frame
