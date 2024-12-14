import tkinter as tk
from components import *
from utils import *

class cls_Dashboard_View(tk.Tk):
    def __init__(self):
        # Khởi tạo cửa sổ Tkinter
        super().__init__()

        # Thiết lập tiêu đề cửa sổ
        self.title("DashboardView_10h20")

        # Thiết lập kích thước cửa sổ và căn giữa
        self._initialize_window_size()

        # Render giao diện chính của Dashboard
        self.f_render_dashboard()

    def _initialize_window_size(self):
        """Thiết lập kích thước cửa sổ và căn giữa nó."""
        f_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_set_center_screen(self)

    def f_render_dashboard(self):
        """Render các thành phần giao diện chính của Dashboard."""
        self._create_menu_top()
        self._create_header()
        self._create_left_menu()
        self._create_right_banner()
        self._create_footer()

    def _create_menu_top(self):
        """Tạo menu trên cùng."""
        cls_menu_top(self, self)

    def _create_header(self):
        """Tạo phần tiêu đề (header)."""
        create_header(self)

    def _create_left_menu(self):
        """Tạo menu bên trái."""
        create_left_menu(self)

    def _create_right_banner(self):
        """Tạo banner bên phải."""
        create_right_banner(self)

    def _create_footer(self):
        """Tạo phần chân trang (footer)."""
        create_footer(self)
