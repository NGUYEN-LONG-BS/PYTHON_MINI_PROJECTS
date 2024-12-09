# View.py
import tkinter as tk
from tkinter import ttk
from Controller import Controller

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("Data from SQL Server")
        
        # Thiết lập kích thước cửa sổ với tỷ lệ 16:9 và chiều rộng = 900
        width = 900
        height = int((width / 16) * 9)  # Tính toán chiều cao theo tỷ lệ 16:9
        self.root.geometry(f"{width}x{height}")

        # Tạo Controller trong View
        self.controller = Controller()  # Không cần biết về file JSON

        # Treeview widget để hiển thị dữ liệu
        self.tree = ttk.Treeview(self.root, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Nút tải dữ liệu
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack()
        
        # Gọi load_data khi khởi tạo cửa sổ
        self.load_data()  # Tải dữ liệu ngay khi cửa sổ được khởi tạo

    def load_data(self):
        """Tải dữ liệu từ Controller và hiển thị lên View"""
        self.clear()
        header = self.controller.get_header()  # Lấy header từ Model (JSON)
        rows = self.controller.get_data()  # Lấy dữ liệu từ DB
        self.update_data(header, rows)
        
        # Debug
        thong_so = len(self.tree["columns"])
        print(f"Thông số cần kiểm tra là: {thong_so}")

    def update_data(self, header, rows):
        """Cập nhật dữ liệu vào Treeview"""
        # Thêm header vào Treeview
        self.tree["columns"] = header
        for col in header:
            self.tree.heading(col, text=col)

        # Hiển thị dữ liệu
        for row in rows:
            self.tree.insert("", "end", values=row)
            
    def clear(self):
        """Xóa tất cả dữ liệu trong Treeview"""
        for item in self.tree.get_children():  # Lấy tất cả các item con trong Treeview
            self.tree.delete(item)  # Xóa từng item
