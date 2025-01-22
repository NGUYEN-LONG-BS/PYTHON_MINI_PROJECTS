import tkinter as tk
from tkinter import ttk
from utils import *

class cls_Treeview_frame_number_01(tk.Frame):
    def __init__(self, parent, columns=["Col_01", "Col_02", "Col_03"], height=10, **kwargs):
        super().__init__(parent, **kwargs)
        # Setup Treeview
        self.treeview_normal = ttk.Treeview(self, columns=columns, show="headings", height=height)
        # Configure columns
        for col in columns:
            self.treeview_normal.heading(col, text=col)  # Set column headings
            self.treeview_normal.column(col, anchor="w")  # Align text to the left
        
        # Create scrollbars
        self.v_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview_normal.yview)
        self.h_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.treeview_normal.xview)
        
        self.treeview_normal.configure(yscrollcommand=self.v_scrollbar.set, xscrollcommand=self.h_scrollbar.set)
        
        # Place Treeview and Scrollbars
        self.treeview_normal.grid(row=0, column=0, sticky="nsew")
        self.v_scrollbar.grid(row=0, column=1, sticky="ns")
        self.h_scrollbar.grid(row=1, column=0, sticky="ew", columnspan=2)
        
        # Bind events (Example: clicking on a row)
        self.treeview_normal.bind("<ButtonRelease-1>", self.on_row_click)
        # Biến để theo dõi dòng đang được highlight
        self.current_highlighted = None
        self.treeview_normal.bind("<Motion>", self.highlight_row)
        
        # Configure grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)  # Vertical scrollbar column
    
    def on_row_click(self, event):
        """Event handler for row click"""
        selected_item = self.treeview_normal.selection()
        if selected_item:
            print(f"Item clicked: {self.treeview_normal.item(selected_item, 'values')}")
            
    def highlight_row(self, event):
        # Lấy ID của dòng dưới con trỏ chuột
        row_id = self.treeview_normal.identify_row(event.y)

        # Nếu có dòng mới dưới con trỏ, highlight nó
        if row_id and row_id != self.current_highlighted:
            # Bỏ highlight dòng trước đó
            if self.current_highlighted:
                self.treeview_normal.item(self.current_highlighted, tags=())
            
            # Gắn highlight cho dòng hiện tại
            self.treeview_normal.item(row_id, tags=("highlighted",))
            self.treeview_normal.tag_configure("highlighted", background=HIGHLIGHT_COLOR)
            # self.treeview_normal.tag_configure("highlighted", background="#f0c6a3")
            # "#f0c6a3"
            self.current_highlighted = row_id
        elif not row_id and self.current_highlighted:
            # Nếu không có dòng nào dưới con trỏ, bỏ highlight
            self.treeview_normal.item(self.current_highlighted, tags=())
            self.current_highlighted = None