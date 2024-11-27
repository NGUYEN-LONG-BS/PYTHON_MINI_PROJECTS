import tkinter as tk
import customtkinter as ctk

def create_right_banner(parent):
    right_banner_frame = tk.Frame(parent)
    right_banner_frame.pack(side=tk.RIGHT, fill=tk.Y)
    
    right_banner_label = tk.Label(right_banner_frame, text="Ad Banner Here", bg="lightgray")
    right_banner_label.pack(fill=tk.Y, padx=10)
    
    return right_banner_frame
