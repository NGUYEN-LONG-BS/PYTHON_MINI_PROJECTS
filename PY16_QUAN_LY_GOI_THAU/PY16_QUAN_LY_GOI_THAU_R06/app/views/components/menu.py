import tkinter as tk
import customtkinter as ctk

# Tkinter Menu
def create_menu(parent):
    menu_frame = tk.Frame(parent)
    menu_frame.pack(side=tk.TOP, fill=tk.X)
    
    menu_button1 = tk.Button(menu_frame, text="Home", command=lambda: print("Home clicked"))
    menu_button1.pack(side=tk.LEFT, padx=10)
    
    menu_button2 = tk.Button(menu_frame, text="About", command=lambda: print("About clicked"))
    menu_button2.pack(side=tk.LEFT, padx=10)
    
    menu_button3 = tk.Button(menu_frame, text="Services", command=lambda: print("Services clicked"))
    menu_button3.pack(side=tk.LEFT, padx=10)

    return menu_frame

# CustomTkinter Menu
def create_custom_menu(parent):
    menu_frame = ctk.CTkFrame(parent)
    menu_frame.pack(side=tk.TOP, fill=tk.X)
    
    menu_button1 = ctk.CTkButton(menu_frame, text="Home", command=lambda: print("Home clicked"))
    menu_button1.pack(side=tk.LEFT, padx=10)
    
    menu_button2 = ctk.CTkButton(menu_frame, text="About", command=lambda: print("About clicked"))
    menu_button2.pack(side=tk.LEFT, padx=10)
    
    menu_button3 = ctk.CTkButton(menu_frame, text="Services", command=lambda: print("Services clicked"))
    menu_button3.pack(side=tk.LEFT, padx=10)

    return menu_frame
