import tkinter as tk
from customtkinter import *

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
        # Create a Tkinter Menu bar
        menubar = tk.Menu(self)

        # Create a "Home" menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Home", command=self.show_about)

        # Create a "Quản lý gói thầu" menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Tạo mới gói thầu", command=self.open_file)
        file_menu.add_command(label="Các gói thầu đã lập", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Quản lý gói thầu", menu=file_menu)

        # Create a "Help" menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Đơn đặt hàng TALA", command=self.show_about)
        menubar.add_cascade(label="Đơn đặt hàng", menu=help_menu)
        
        # Create a "Help" menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Menu", menu=help_menu)

        # Set the menu bar for the root window
        self.config(menu=menubar)

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
