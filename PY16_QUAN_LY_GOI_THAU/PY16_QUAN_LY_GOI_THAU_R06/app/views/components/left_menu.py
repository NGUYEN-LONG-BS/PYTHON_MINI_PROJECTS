import tkinter as tk
import customtkinter as ctk

def create_left_menu(parent):
    left_menu_frame = tk.Frame(parent)
    left_menu_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    left_menu_button1 = tk.Button(left_menu_frame, text="Profile", command=lambda: print("Profile clicked"))
    left_menu_button1.pack(fill=tk.X, padx=10, pady=5)
    
    left_menu_button2 = tk.Button(left_menu_frame, text="Settings", command=lambda: print("Settings clicked"))
    left_menu_button2.pack(fill=tk.X, padx=10, pady=5)
    
    return left_menu_frame
