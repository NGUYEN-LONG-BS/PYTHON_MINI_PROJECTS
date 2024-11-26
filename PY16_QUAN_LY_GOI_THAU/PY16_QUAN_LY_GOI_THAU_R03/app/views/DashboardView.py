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
        self.title("TUẤN ÂN GROUP")
        
        # Initialize the customtkinter window (CTk is the root window here)
        super().__init__()  # Initialize the CTk window (this will call the __init__() of CTk)
        self.title("Dashboard")
        
        # Create a CTkButton (use CTkButton, not CTk.Button)
        self.button = CTkButton(self, text="Run KD01QuanLyGoiThauView", command=self.run_kd01_view)
        self.button.pack(pady=20)

    def run(self):
        print("Running the dashboard")
        # Run the tkinter main loop
        self.mainloop()

    def run_kd01_view(self):
        print("Button clicked: Running KD01QuanLyGoiThauView")
        # Initialize and run the KD01QuanLyGoiThauView
        kd01_view = KD01QuanLyGoiThauView()
        kd01_view.run()
