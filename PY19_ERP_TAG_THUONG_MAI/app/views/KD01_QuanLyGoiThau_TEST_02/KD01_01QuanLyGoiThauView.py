import tkinter as tk
from tkinter import ttk
from KD01_01QuanLyGoiThauController import cls_Controller
from datetime import datetime
from Components_View import *
from utils import *

class cls_View(tk.Tk):
    def __init__(self):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        # self.root = root
        self.title("KD01_01QuanLyGoiThauView")
        # Thiết lập kích thước cửa sổ
        f_utils_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_utils_set_center_screen(self)

        
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self, self)
        
        # # Thiết lập kích thước cửa sổ với tỷ lệ 16:9 và chiều rộng = 900
        # width = 900
        # height = int((width / 16) * 9)  # Tính toán chiều cao theo tỷ lệ 16:9
        # self.geometry(f"{width}x{height}")

        # Tạo Controller trong View
        self.controller = cls_Controller()  # Không cần biết về file JSON
        
        # ==================================================================================================================================
        # Create a frame with a border
        frame_of_treeview = tk.Frame(self, bd=2, relief="solid")
        frame_of_treeview.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview widget để hiển thị dữ liệu
        # self.tree = ttk.Treeview(self.root, show="headings")
        self.tree = ttk.Treeview(frame_of_treeview, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load table configuration from JSON
        columns, scrollbars, general_settings = self.controller.get_table_config()

        # Configure the general appearance of the Treeview
        self.tree.configure(
            height=20,
            selectmode="browse"
        )
        
        # Add the scrollbars if enabled
        if scrollbars.get("vertical", {}).get("enabled", False):
            vsb = tk.Scrollbar(frame_of_treeview, orient="vertical", command=self.tree.yview)
            vsb.pack(side="right", fill="y")
            self.tree.configure(yscrollcommand=vsb.set)

        if scrollbars.get("horizontal", {}).get("enabled", False):
            hsb = tk.Scrollbar(frame_of_treeview, orient="horizontal", command=self.tree.xview)
            hsb.pack(side="bottom", fill="x")
            self.tree.configure(xscrollcommand=hsb.set)

        # Set column properties
        self.tree["columns"] = [col["name"] for col in columns]
        for col in columns:
            self.tree.heading(col["name"], text=col["name"], anchor=col["anchor"])
            self.tree.column(
                col["name"], 
                width=col["width"], 
                # Keep minwidth if it's defined
                minwidth=col["min_width"],
                # Use stretch if it's defined
                stretch=col["stretch"], 
                anchor=col["anchor"]
            )
            self.tree.tag_configure(col["name"], font=(col["font"]["family"], col["font"]["size"], col["font"]["weight"]))

        # Nút tải dữ liệu
        self.load_button = tk.Button(self, text="Load Data", command=self.load_data)
        self.load_button.pack()
        
        # Gọi load_data khi khởi tạo cửa sổ
        self.load_data()  # Tải dữ liệu ngay khi cửa sổ được khởi tạo

    # =======================================================================================================================
    # Fnction of treeview
    def load_data(self):
        """Tải dữ liệu từ Controller và hiển thị lên View"""
        self.clear()
        """Load and display data (mockup for now)"""
        data = self.controller.get_data()
        for row in data:
            self.tree.insert("", "end", values=row)
        
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
            # Handle datetime and None values before inserting into Treeview
            formatted_row = self.format_row(row)
            self.tree.insert("", "end", values=formatted_row)
            
    def clear(self):
        """Xóa tất cả dữ liệu trong Treeview"""
        for item in self.tree.get_children():  # Lấy tất cả các item con trong Treeview
            self.tree.delete(item)  # Xóa từng item
            
    def format_row(self, row):
        """Format a row to handle:
             - datetime
             - None values
             - number
             - percentage
        """
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
