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
        
        # Khởi tạo các thành phần
        self.header = cls_Header(self.master)
        self.top_menu = cls_Menu(self.master)
        self.footer = cls_Footer(self.master)
        self.left_menu = cls_LeftMenu(self.master)
        self.right_banner = cls_RightBanner(self.master)
        self.mainContent = cls_MainContent(self.master)

    def render(self):
        # Gọi các phương thức để render các phần tử giao diện
        self.header.create_header()
        self.top_menu.create_top_menu()
        self.footer.create_footer()
        self.left_menu.create_left_menu()
        self.right_banner.create_right_banner()
        self.mainContent.create_content()

        # Bắt đầu vòng lặp Tkinter
        self.master.mainloop()

    # @classmethod                # Khi một phương thức là classmethod, bạn phải gọi nó thông qua class chứ không phải qua đối tượng.
    # def render_dashboard(cls):
    #     # Không cần truyền root từ bên ngoài nữa, sẽ tự tạo
    #     dashboard = cls()  # Khởi tạo cls_Dashboard, Tk sẽ tự tạo ở constructor
    #     dashboard.render()  # Gọi phương thức render để hiển thị giao diện
        
    def render_dashboard(self):
        # Gọi phương thức render để hiển thị giao diện
        self.render()