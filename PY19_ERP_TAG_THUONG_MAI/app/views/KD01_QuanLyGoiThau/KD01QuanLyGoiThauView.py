# Project/Views/KD01QuanLyGoiThauView.py
import tkinter as tk
from tkinter import ttk
from PIL import Image
from datetime import datetime
from app.controllers.KD01QuanLyGoiThauController import cls_KD01QuanLyGoiThauController
from app.controllers.KD01QuanLyGoiThauController import cls_Controller_config_treeview
from utils import *
from Components_View import *
from Components_View.user_Info import setup_employee_info_labels  # Import the function
from Components_View.logo import setup_logo  # Import the setup_logo function
from app.views.Components_View.menu import cls_Menu  # Import the menu creation function

class cls_KD01QuanLyGoiThauView(tk.Tk):
    
    def __init__(self):
        super().__init__()  # Gọi phương thức __init__ của lớp cha

        # Initialize controller
        self.controller = cls_KD01QuanLyGoiThauController()
        self.controller_02 = cls_Controller_config_treeview()

        # Setup window
        self.title("QUẢN LÝ GÓI THẦU - KD01QuanLyGoiThauView")
        
        # Thiết lập kích thước cửa sổ
        f_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_set_center_screen(self)

        # Gọi các thành phần tái sử dụng
        cls_menu_top(self, self)

        # Create a container frame to hold both the logo frame and user info frame
        frame_header_container = tk.Frame(self)
        frame_header_container.pack(side='top', fill='x', padx=10, pady=0)

        # Setup the logo in the Frame_logo using the imported function
        Frame_logo = tk.Frame(frame_header_container, width=100, height=100)
        Frame_logo.pack(side='left', padx=10)  # Pack the logo frame on the left side with some padding
        setup_logo(Frame_logo)  # Pass the frame as the parent for the logo
        
        
        # Wait for the window to render and then calculate the width of Frame_user_info
        def update_user_info_frame_width():
            window_width = self.winfo_width()  # Get the current window width
            logo_width = Frame_logo.winfo_width()  # Get the width of the Frame_logo
            user_info_width = window_width - logo_width - 20  # Subtract logo width and padding (10 + 10)
            
            # Update the width of Frame_user_info dynamically
            Frame_user_info.config(width=user_info_width)

        # Setup the logo in the Frame_logo using the imported function
        Frame_user_info = tk.Frame(frame_header_container, height=100)
        Frame_user_info.pack(side='left', padx=10)  # Pack the user info frame to the left with padding
        setup_employee_info_labels(Frame_user_info)  # Call the function to add employee info labels
        
        # Call the update function to adjust the width of Frame_user_info after the window has been rendered
        # 100 mili giây
        self.after(100, update_user_info_frame_width)
        
        self.setup_title_h1()
        self.setup_labels()
        self.setup_combobox_nam_goi_thau()
        self.setup_entries()
        self.setup_btn_tao_thu_muc_moi()
        self.setup_scrollable_frame()
        # self.setup_treeview_frame()
        self.setup_btn_show_dashboard()

        self.dashboard = None  # Placeholder for Dashboard window

        # Bind close event
        self.protocol("WM_DELETE_WINDOW", self.Function_close_KD01_Click)

    # Employee Info Labels
    def setup_employee_info_labels(self):
        tk.Label(self, text="ID: TBD001", font=("Arial", 13)).place(x=115, y=10)
        tk.Label(self, text="Họ tên: Nguyễn Văn B", font=("Arial", 13)).place(x=200, y=10)
        tk.Label(self, text="Bộ phận: Kinh doanh", font=("Arial", 13)).place(x=370, y=10)
        tk.Label(self, text="Cấp bậc: Nhân viên", font=("Arial", 13)).place(x=550, y=10)
        tk.Label(self, text="Cty: Thiết bị điện", font=("Arial", 13)).place(x=750, y=10)

    # Header Title
    def setup_title_h1(self):
        title_label = tk.Label(self, text="TẠO FOLDER QUẢN LÝ GÓI THẦU MỚI", font=("Arial", 25))
        title_label.place(relx=0.2, rely=0.1)

    # Static Labels
    def setup_labels(self):
        tk.Label(self, text="Số thông báo mời thầu", font=("Arial", 18)).place(x=50, y=200)
        tk.Label(self, text="Năm gói thầu", font=("Arial", 18)).place(x=50, y=130)
        tk.Label(self, text="Danh sách gói thầu", font=("Arial", 18)).place(x=50, y=300)

        self.folder_name_label = tk.Label(self, text="24_GOI_THAU_0000_0000", font=("Arial", 18))
        self.folder_name_label.place(x=390, y=230)

    # Combobox for Year
    def setup_combobox_nam_goi_thau(self):
        current_year = datetime.now().year
        year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

        self.year_combobox = ttk.Combobox(self, values=year_array)
        self.year_combobox.set(str(current_year))  # Default to current year
        self.year_combobox.place(x=50, y=160)
        self.year_combobox.bind("<<ComboboxSelected>>", self.on_combobox_nam_goi_thau_change)

    # Entry for notification number
    def setup_entries(self):
        self.notification_entry = tk.Entry(self, width=30)
        self.notification_entry.place(x=50, y=230)
        self.notification_entry.bind("<KeyRelease>", self.on_entry_change)

    # Button to create folder
    def setup_btn_tao_thu_muc_moi(self):
        def btn_tao_thu_muc_moi_click():
            folder_name = self.folder_name_label.cget("text")
            self.controller.create_folder(folder_name)

        create_folder_btn = tk.Button(self, text="Tạo thư mục mới", command=btn_tao_thu_muc_moi_click)
        # create_folder_btn.place(x=50, y=700)
        create_folder_btn.pack()

    # Button to show Dashboard
    def setup_btn_show_dashboard(self):
        def btn_show_dashboard_click():
            if self.dashboard:
                self.dashboard.deiconify()
                self.destroy()  # Close the current view
            else:
                print("Dashboard window not initialized yet.")

        show_dashboard_btn = tk.Button(self, text="Show Dashboard", command=btn_show_dashboard_click)
        # show_dashboard_btn.place(x=250, y=700)
        show_dashboard_btn.pack()

    # Scrollable frame for folder contents
    def setup_scrollable_frame(self):
        self.scrollable_frame = tk.Frame(self, width=800, height=200)
        self.scrollable_frame.place(x=50, y=330)

        canvas = tk.Canvas(self.scrollable_frame)
        scrollbar = tk.Scrollbar(self.scrollable_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def refresh_scrollable_frame():
            # Simulate directory contents
            directory_contents = [f"Folder {i}" for i in range(1, 21)]
            for widget in frame.winfo_children():
                widget.destroy()
            for item in directory_contents:
                label = tk.Label(frame, text=item, font=("Arial", 14))
                label.pack(anchor="w")

        refresh_scrollable_frame()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
        refresh_scrollable_frame()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
        
    # Treeview
    def setup_treeview_frame(self):
        # ==================================================================================================================================
        # Create a frame with a border
        frame_of_treeview = tk.Frame(self, bd=2, relief="solid")
        frame_of_treeview.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Treeview widget để hiển thị dữ liệu
        # self.tree = ttk.Treeview(self.root, show="headings")
        self.tree = ttk.Treeview(frame_of_treeview, show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load table configuration from JSON
        columns, scrollbars, general_settings = self.controller_02.get_table_config()

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
    

    # Combobox change handler
    def on_combobox_nam_goi_thau_change(self, event):
        self.update_folder_name()

    # Entry change handler
    def on_entry_change(self, event):
        self.update_folder_name()

    # Update folder name
    def update_folder_name(self):
        selected_year = self.year_combobox.get()
        year_suffix = selected_year[-2:]

        notification_number = self.notification_entry.get().zfill(4)

        folder_name = f"{year_suffix}_GOI_THAU_0000_{notification_number}"

        self.folder_name_label.configure(text=folder_name)

    # Close event handler
    def Function_close_KD01_Click(self):
        self.destroy()
        # Now import KD01QuanLyGoiThauView inside the function to avoid circular import
        from app.views.dashboard.DashboardView import f_render_dashboard
        f_render_dashboard()

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
        data = self.controller_02.get_data()
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
    
    
    # Run main event loop
    def main(self):
        self.mainloop()
        
    


# # To run the view
# if __name__ == "__main__":
#     view = cls_KD01QuanLyGoiThauView()
#     view.main()
    
    