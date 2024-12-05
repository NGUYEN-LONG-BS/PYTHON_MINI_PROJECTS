# View.py
import tkinter as tk
from tkinter import ttk
from Controller import Controller
from datetime import datetime

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
        
        # Create a frame with a border
        frame_of_treeview = tk.Frame(root, bd=2, relief="solid")
        frame_of_treeview.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview widget để hiển thị dữ liệu
        # self.tree = ttk.Treeview(self.root, show="headings")
        self.tree = ttk.Treeview(frame_of_treeview, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Create and configure horizontal scrollbar
        self.h_scrollbar = tk.Scrollbar(frame_of_treeview, orient="horizontal", command=self.tree.xview)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=self.h_scrollbar.set)

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
        
        # # Set specific width for each column
        # if col == "STT":
        #     self.tree.column(col, width=20, anchor="center")  # Set width for the first column
        # elif col == "GHI_CHU":
        #     self.tree.column(col, width=300, anchor="w")  # Set width for the second column
        # elif col == "MA_NHAN_VIEN":
        #     self.tree.column(col, width=150, anchor="center")  # Set width for the third column
        # elif col == "TEN_NHAN_VIEN":
        #     self.tree.column(col, width=200, anchor="w")  # Set width for the fourth column
        # elif col == "ID_NHAN_VIEN":
        #     self.tree.column(col, width=100, anchor="center")  # Set width for the fifth column
        # elif col == "NGAY_TAO":
        #     self.tree.column(col, width=150, anchor="e")  # Set width for the sixth column
        # elif col == "XOA_SUA":
        #     self.tree.column(col, width=100, anchor="center")  # Set width for the seventh column

        # Hiển thị dữ liệu
        for row in rows:
            # Handle datetime and None values before inserting into Treeview
            formatted_row = self.format_row(row)
            self.tree.insert("", "end", values=formatted_row)
            
    def clear(self):
        """Xóa tất cả dữ liệu trong Treeview"""
        for item in self.tree.get_children():  # Lấy tất cả các item con trong Treeview
            self.tree.delete(item)  # Xóa từng item
            
    def format_row(self, row):
        """Format a row to handle datetime and None values"""
        formatted_row = []
        
        for item in row:
            if isinstance(item, datetime):
                # Format datetime to string (e.g., YYYY-MM-DD)
                formatted_row.append(item.strftime('%Y-%m-%d'))
            elif item is None:
                # Replace None with an empty string or a placeholder
                formatted_row.append('--')
            elif isinstance(item, (int, float)):
                # Format numbers with commas and 2 decimal places (e.g., 1,123,156.23)
                formatted_row.append(f"{item:,.2f}")
            elif isinstance(item, float) and 0 <= item <= 1:
                # If the item is a percentage (between 0 and 1), format as percentage with 2 decimal places
                formatted_row.append(f"{item * 100:.2f}%")
            else:
                # Keep other items as they are
                formatted_row.append(item)
        
        return tuple(formatted_row)
