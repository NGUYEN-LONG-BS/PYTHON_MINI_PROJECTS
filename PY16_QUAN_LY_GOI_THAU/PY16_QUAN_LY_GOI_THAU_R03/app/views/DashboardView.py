# DashboardView.py
# import tkinter as tk
from customtkinter import *  # Ensure all necessary components are imported
from app.controllers.DashboardController import DashboardController
from app.views.KD01QuanLyGoiThauView import KD01QuanLyGoiThauView

class Dashboard(CTk):
    def __init__(self):
        print("Dashboard initialized")
        super().__init__()
        # Initialize controller
        self.controller = DashboardController()  # Assign the controller to an instance variable
        
        # Setup the main window
        self.geometry("900x800")
        self.title("TUẤN ÂN GROUP - DASHBOARD")
        
        # Center the window on the screen
        self.center_window()
        
        # Setup the components
        # self.setup_logo()
        self.setup_BTN_KD01QuanLyGoiThauView()
        
    # ==================================================================================================
    # center_window
    # ==================================================================================================
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

    # ==================================================================================================
    # setup_BTN_TaoThuMucMoi
    # ==================================================================================================
    def setup_BTN_KD01QuanLyGoiThauView(self):
        # Button to create folder
        def BTN_TaoThuMucMoi_Click():
            folder_name = self.LABEL_TenThuMucSeKhoiTao.cget("text")  # Get the current folder name
            self.controller.create_folder(folder_name)  # Pass folder name to controller

        BTN_KD01QuanLyGoiThauView = CTkButton(self, text="Quản lý gói thầu", command=self.run_kd01_view)
        BTN_KD01QuanLyGoiThauView.pack(pady=20)

    def run(self):
        print("Running the dashboard")
        # Run the tkinter main loop
        self.mainloop()

    def run_kd01_view(self):
        print("Button clicked: Running KD01QuanLyGoiThauView")
        
        # Destroy the current Dashboard window
        self.withdraw()  # Hide the Dashboard window
        
        # Initialize and run the KD01QuanLyGoiThauView
        kd01_view = KD01QuanLyGoiThauView()
        
        # Pass the current Dashboard instance to the KD01 view so it can be shown later
        kd01_view.dashboard = self
        
        # Start the KD01 window's mainloop
        kd01_view.main()
