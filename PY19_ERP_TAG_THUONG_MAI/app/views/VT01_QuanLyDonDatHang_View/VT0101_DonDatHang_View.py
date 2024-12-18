import tkinter as tk
from Components_View import *
from utils import *
from utils.define import *

class cls_VT0101_DonDatHang_View(tk.Tk):
    def __init__(self):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        self.title("VT0101 | ĐƠN ĐẶT HÀNG")
        f_utils_setup_fav_icon(self)
        
        self.f_Thiet_lap_Kich_thuoc_Cua_So()
        self.f_Goi_Cac_Thanh_Phan_Tai_Su_Dung()
        
    def f_Thiet_lap_Kich_thuoc_Cua_So(self):
        # Thiết lập kích thước cửa sổ
        f_utils_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_utils_set_center_screen(self)
        f_utils_setup_fav_icon(self)
    
    def f_Goi_Cac_Thanh_Phan_Tai_Su_Dung(self):
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self, self)
        
        frame_main = cls_Frame_Main(self)
        frame_main.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights for resizing
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Configure rows and columns inside frame_main
        frame_main.rowconfigure(0, weight=0)  # Header
        frame_main.rowconfigure(1, weight=1)  # Body
        frame_main.rowconfigure(2, weight=0)  # Footer
        frame_main.columnconfigure(0, weight=1)

        Frame_Header = cls_Frame_Header(frame_main)
        Frame_Header.grid(row=0, column=0, sticky="ew")
        
        Frame_Footer = cls_Frame_Footer(frame_main)
        Frame_Footer.grid(row=2, column=0, sticky="ew")
        
        Frame_Body = cls_Frame_Body(frame_main)
        Frame_Body.grid(row=1, column=0, sticky="nsew")
        