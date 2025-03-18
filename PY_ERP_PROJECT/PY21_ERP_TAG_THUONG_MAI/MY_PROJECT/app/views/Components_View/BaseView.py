# Project/Views/BaseView.py
import tkinter as tk
from customtkinter import *
from components import *

class BaseView(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800")
        self.title("TUẤN ÂN GROUP")
        self.center_window()
        self.create_menu()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Get the window's width and height
        window_width = 900  # Window width you set
        window_height = 800  # Window height you set

        # Calculate the position to center the window
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Set the window's geometry with the calculated position
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def create_menu(self):
        # create_menu_TK_02(self, self)
        cls_Menu(self, self)

    def open_file(self):
        print("Open file selected")

    def save_file(self):
        print("Save file selected")

    def show_about(self):
        print("About selected")
        
    def show_home(self):
        print("Home selected")
    
    def run(self):
        self.mainloop()
