import tkinter as tk
from tkinter import ttk
import json
from Controller import Controller
from Model import Model

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Data from SQL Server")

        # File JSON chứa header
        self.json_file = "KD01_TABLE_ABC.JSON"
        
        # Tạo Model trong View
        self.model = Model(self.json_file)
        # Tạo Controller trong View
        self.controller = Controller(self.model)

        # Tạo Treeview widget
        self.tree = ttk.Treeview(self.root, show="headings")  # Khởi tạo mà không có columns

        # Cập nhật header từ JSON
        self.load_header()

        # Pack treeview
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Nút tải dữ liệu
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack()

        # Tải dữ liệu và header khi khởi động
        self.load_data()

    def load_data(self):
        """Tải dữ liệu từ SQL Server và hiển thị lên View"""
        query = "[BAN_KINH_DOANH].[dbo].[Proc_TB_QUAN_LY_GOI_THAU_SELECT_241129_09h07] '1'"  # Thay thế với câu lệnh SQL của bạn
        rows = self.controller.get_data(query)
        self.update_data(rows)

    def load_header(self):
        """Tải header từ JSON và cập nhật Treeview"""
        header_data = self.controller.get_header()
        self.update_header(header_data)

    def update_data(self, rows):
        """Cập nhật dữ liệu vào Treeview"""
        for row in rows:
            self.tree.insert("", "end", values=row)

    def update_header(self, header_data):
        """Cập nhật tiêu đề cột trong Treeview"""
        self.tree["columns"] = header_data  # Cập nhật danh sách cột trong treeview

        # Cập nhật các heading cho các cột
        for col in header_data:
            self.tree.heading(col, text=col)  # Thiết lập tiêu đề cột
