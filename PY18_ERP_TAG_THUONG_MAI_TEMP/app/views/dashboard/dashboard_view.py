import tkinter as tk
# from app.views.dashboard_widgets import DashboardWidgets
from dashboard_widgets import DashboardWidgets

class DashboardView:
    def __init__(self, master):
        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("800x600")
        
        # Use the dashboard widgets
        self.widgets = DashboardWidgets(self.master)
        self.widgets.create_widgets()
