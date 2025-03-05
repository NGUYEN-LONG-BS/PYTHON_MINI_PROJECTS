import tkinter as tk
from tkinter import ttk
from app.views.Components_View import *
from app.utils import *
from utils.define import *

class cls_VT0101_DonDatHang_View(cls_base_form_number_01_EntryForm):
    def __init__(self):
        title = "VT0101 | ĐƠN ĐẶT HÀNG"
        name = "ĐƠN ĐẶT HÀNG TALA"
        super().__init__(title_of_form=title, name_of_slip=name)
        
        # Add Treeview to the main frame
        self.f_add_tree_view()
        
    def f_add_tree_view(self):
        # Locate the frame_main component
        frame_main = self.children.get('!cls_frame_main')
        if not frame_main:
            print("Error: frame_main not found!")
            return
        
        # Add treeview_frame inside frame_main
        self.treeview_frame = tk.Frame(frame_main, bd=BORDER_SIZE_0, relief="solid", bg=COLOR_PINK)
        self.treeview_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Configure grid weights for frame_main
        frame_main.rowconfigure(1, weight=1)  # Ensure treeview_frame row expands
        frame_main.columnconfigure(0, weight=1)  # Ensure treeview_frame column expands

        # Configure the Treeview and Scrollbar here
        tree_scrollbar = tk.Scrollbar(self.treeview_frame, orient="vertical")
        tree_scrollbar.pack(side="right", fill="y")

        self.treeview = ttk.Treeview(self.treeview_frame, yscrollcommand=tree_scrollbar.set)
        self.treeview.pack(side="left", fill="both", expand=True)

        tree_scrollbar.config(command=self.treeview.yview)

        # Example columns
        self.treeview["columns"] = ("Column1", "Column2", "Column3")
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("Column1", text="Name")
        self.treeview.heading("Column2", text="Date")
        self.treeview.heading("Column3", text="Amount")
        
        # Add dummy data
        for i in range(10):
            self.treeview.insert(
                "", "end", text=f"ID {i+1}", values=(f"Name {i+1}", "2024-12-19", f"${i+10}.00")
            )
