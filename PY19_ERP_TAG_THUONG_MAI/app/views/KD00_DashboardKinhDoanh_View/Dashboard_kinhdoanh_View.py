import tkinter as tk
from Components_View import *
from utils import *

from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class cls_Dashboard_kinhdoanh_View(cls_base_form_number_04_dashboard):
    def __init__(self):
        title = "KD00 - DashboardKinhDoanhView"
        name_of_slip = "KINH DOANH"
        super().__init__(title_of_form=title, name_of_slip=name_of_slip)
        self.create_dashboard()
        
    def create_dashboard(self):
        self.Frame_Body.configure(bg=BG_COLOR_0_0)

        # Create a frame to hold the chart
        chart_frame_01 = ttk.Frame(self.Frame_Body, padding="10", borderwidth=2, relief="solid")
        chart_frame_01.pack(side="top", fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a Matplotlib figure and plot
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Line")
        ax.set_title("Sample Chart")
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")
        ax.legend()

        # Embed the Matplotlib figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame_01)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        # Create a frame to hold the chart
        chart_frame_02 = ttk.Frame(self.Frame_Body, padding="10", borderwidth=2, relief="solid")
        chart_frame_02.pack(side="top", fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create a Matplotlib figure and plot
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Line")
        ax.set_title("Sample Chart")
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")
        ax.legend()

        # Embed the Matplotlib figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame_02)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        
        