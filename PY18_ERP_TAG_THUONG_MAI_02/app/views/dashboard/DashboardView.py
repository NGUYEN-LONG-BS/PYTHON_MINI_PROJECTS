# Project/Views/DashboardView.py
import tkinter as tk
from components import *
from utils import *

class cls_Dashboard:
    def __init__(self, master=None):
        # Nếu master không được truyền vào, thì tự tạo root
        if master is None:
            self.master = tk.Tk()  # Nếu không có master, tự khởi tạo root
        else:
            self.master = master
        
        self.master.title("Dashboard")
        set_window_size(self.master)
        
        # Create frames for header, footer, and main content
        self.header_frame = tk.Frame(self.master, 
                                     bg="lightgrey"
                                     ,bd=2
                                     ,relief="solid"
                                     )
        self.footer_frame = tk.Frame(self.master
                                     ,bg="lightgrey"
                                     ,bd=2
                                     ,relief="solid"
                                     )
        self.main_container_frame = tk.Frame(self.master
                                             ,bg="white"
                                             ,bd=2
                                             ,relief="solid"
                                             )
        
        # Place frames for layout management
        self.header_frame.pack(side=tk.TOP, fill=tk.X)
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.main_container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def render(self):
        # Khởi tạo các thành phần
        self.top_menu = cls_Menu(self.master)
        self.header = cls_Header(self.header_frame)  # Pass header_frame as parent
        self.footer = cls_Footer(self.footer_frame)  # Pass footer_frame as parent
        self.container = cls_MainContainer(self.main_container_frame)  # Pass footer_frame as parent
        
        self.master.mainloop()
        
    def render_dashboard(self):
        # Gọi phương thức render để hiển thị giao diện
        self.render()