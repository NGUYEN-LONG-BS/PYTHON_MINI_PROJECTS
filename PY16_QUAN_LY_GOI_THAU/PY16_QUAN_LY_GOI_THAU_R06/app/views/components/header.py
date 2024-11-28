import tkinter as tk
import customtkinter as ctk

def create_header(parent, title="TUẤN ÂN GROUP"):
    header_frame = tk.Frame(parent)
    header_frame.pack(side=tk.TOP, fill=tk.X)
    
    header_label = tk.Label(header_frame, text=title, font=("Arial", 20))
    header_label.pack()
    
    return header_frame
