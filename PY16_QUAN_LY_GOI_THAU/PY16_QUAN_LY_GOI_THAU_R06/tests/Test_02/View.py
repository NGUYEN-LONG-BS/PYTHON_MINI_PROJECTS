import tkinter as tk
from tkinter import ttk
import json
from db_connection import create_connection  # Import hàm kết nối từ db_connection.py

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Data from SQL Server")

        # File JSON chứa header (có thể thay đổi tên file JSON tại đây)
        self.json_file = "KD01_TABLE_ABC.JSON"
        
        # Tạo Model trong View
        self.model = self.Model(self.json_file)
        # Tạo Controller trong View
        self.controller = self.Controller(self.model)

        # Treeview widget để hiển thị dữ liệu
        self.tree = ttk.Treeview(self.root, columns=("STT", "Mã hàng", "Tên hàng", "Đvt", "Số lượng"), show="headings")
        self.tree.heading("STT", text="STT")
        self.tree.heading("Mã hàng", text="Mã hàng")
        self.tree.heading("Tên hàng", text="Tên hàng")
        self.tree.heading("Đvt", text="Đvt")
        self.tree.heading("Số lượng", text="Số lượng")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Nút tải dữ liệu
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack()

        # Nút tải header từ JSON
        self.load_header_button = tk.Button(self.root, text="Load Header", command=self.load_header)
        self.load_header_button.pack()

        # Tải dữ liệu và header khi khởi động
        self.load_header()
        self.load_data()

    class Model:
        def __init__(self, json_file):
            self.json_file = json_file

        def load_header_from_json(self):
            """Đọc header từ file JSON"""
            try:
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data.get("header", [])
            except FileNotFoundError:
                return []

        def fetch_data_from_db(self, query):
            """Truy vấn dữ liệu từ SQL Server"""
            conn = create_connection()  # Gọi hàm kết nối từ db_connection.py
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            return rows

    class Controller:
        def __init__(self, model):
            self.model = model

        def get_header(self):
            """Lấy header từ JSON"""
            return self.model.load_header_from_json()

        def get_data(self, query):
            """Lấy dữ liệu từ SQL Server"""
            return self.model.fetch_data_from_db(query)

    def load_data(self):
        """Tải dữ liệu từ SQL Server và hiển thị lên View"""
        
        query_01 = "SELECT TOP 100 [MA_THANH_PHAM]\
                                ,[TEN_THANH_PHAM]\
                                ,[DVT]\
                                ,[ID_NHAN_VIEN]\
                                ,[NGAY_TAO_PHIEU]\
                                ,[XOA_SUA]\
        FROM [LA_2024].[dbo].[TB_FINISHED_PRODUCT_CATEGORIES]"  # Thay thế với câu lệnh SQL của bạn
        
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
        for i, col in enumerate(header_data):
            self.tree.heading(self.tree["columns"][i], text=col)
