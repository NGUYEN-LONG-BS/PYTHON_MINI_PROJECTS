import tkinter as tk
from Components_View import *
from utils import *

from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        
        # content_frame = tk.Frame(self.Frame_Body, bg="#ffffff")
        content_frame = tk.Frame(self.Frame_Body, bg=BG_COLOR_0_0)
        content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        sidebar_frame = tk.Frame(content_frame, bg=BG_COLOR_0_0, width=200)        
        sidebar_frame.pack(side="left", fill="y")

        main_frame = tk.Frame(content_frame, bg=BG_COLOR_0_0)
        main_frame.pack(side="right", fill="both", expand=True)

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Sidebar menu
        for i, item in enumerate(["Home", "Reports", "Settings", "Help"]):
            btn = ttk.Button(sidebar_frame, text=item)
            btn.pack(pady=10, padx=10, fill="x")

        # Chart 1: Line Chart
        fig1, ax1 = plt.subplots(figsize=(5, 3))
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax1.plot(x, y, label="Sine Wave", color="blue")
        ax1.set_title("Line Chart")
        ax1.set_xlabel("X Axis")
        ax1.set_ylabel("Y Axis")
        ax1.legend()

        chart1 = FigureCanvasTkAgg(fig1, scrollable_frame)
        chart1.get_tk_widget().pack(fill="both", expand=True, pady=10)

        # Chart 2: Column Chart
        fig2, ax2 = plt.subplots(figsize=(5, 3))
        categories = ['A', 'B', 'C', 'D']
        values = [23, 45, 56, 78]
        ax2.bar(categories, values, color="skyblue")
        ax2.set_title("Column Chart")
        ax2.set_ylabel("Values")

        chart2 = FigureCanvasTkAgg(fig2, scrollable_frame)
        chart2.get_tk_widget().pack(fill="both", expand=True, pady=10)

        # Chart 3: Pie Chart
        fig3, ax3 = plt.subplots(figsize=(5, 3))
        labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']
        sizes = [15, 30, 45, 10]
        ax3.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["gold", "lightcoral", "lightskyblue", "yellowgreen"])
        ax3.set_title("Pie Chart")

        chart3 = FigureCanvasTkAgg(fig3, scrollable_frame)
        chart3.get_tk_widget().pack(fill="both", expand=True, pady=10)

        # Chart 4: Waterfall Chart
        fig4, ax4 = plt.subplots(figsize=(5, 3))
        steps = [10, 15, -5, 20, -10]
        cumulative = np.cumsum([0] + steps)
        ax4.bar(range(len(steps)), steps, color=["green" if x > 0 else "red" for x in steps])
        ax4.step(range(len(cumulative)), cumulative, where="mid", color="blue")
        ax4.set_title("Waterfall Chart")
        ax4.set_xlabel("Steps")
        ax4.set_ylabel("Cumulative Value")

        chart4 = FigureCanvasTkAgg(fig4, scrollable_frame)
        chart4.get_tk_widget().pack(fill="both", expand=True, pady=10)