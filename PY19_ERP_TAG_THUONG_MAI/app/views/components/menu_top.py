# Project/views/components/menu.py
import tkinter as tk
from utils import *
import json
import sys
import os

class cls_menu_top:
    def __init__(self, parent, dashboard_window):
        """
        Initializes the Menu with the given parent and dashboard window.
        """
        self.parent = parent
        self.dashboard_window = dashboard_window
        self.top_menu = tk.Menu(self.parent)
        self.current_user = self.read_user_from_json()  # Read the logged-in user
        self.f_create_top_menu()
    #     self.f_check_credentials()
        
    # def f_check_credentials(self):
    #     print("check credentials")
    #     if self.current_user == "admin":
    #         self.KinhDoanh_menu.configure(bg="lightblue")
    #         print("Fucntion_QLGT_GoiThauDaLap selected")
    #     else:
    #         print("You must be an admin to access this.")

    def read_user_from_json(self):
        """ Reads the logged-in user's username from the JSON file. """
        # Sử dụng đường dẫn tuyệt đối
        json_file = os.path.join(os.path.dirname(__file__), '..', 'user_management', 'login_credentials.json')
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            return data.get("username", "")  # Return the username from the JSON file
        except Exception as e:
            print(f"Error reading credentials: {e}")
            return ""
        
    def f_create_top_menu(self):
    
        # Define the action fuctions for home menu
        def Function_Home_main_Click():
            print("Function_Home_main_Click selected")
            self.f_open_DashBoard()
        
        # Define the action fuctions for QLGT menu
        def Fucntion_QLGT_TaoMoi_Click():
            print("Fucntion_QLGT_TaoMoi_Click selected")
            self.f_open_KD01QuanLyGoiThauView()
        
        def Fucntion_QLGT_GoiThauDaLap():
            print("Fucntion_QLGT_GoiThauDaLap selected")
            self.f_open_KD01_01QuanLyGoiThauView()
        
        # Define the action fuctions for QLYCDT menu
        def Fuction_QLYCDH_TALA():
            print("Fuction_QLYCDH_TALA selected")
            self.f_open_KD02QuanLyYeuCauDatHangView()
            
        def Fuction_QLYCDH_TM():
            print("Fuction_QLYCDH_TM selected")
        
        def Fucntion_Help_About():
            print("Fucntion_Help_About selected")
        
        def Fucntion_Help_UserInfo():
            print("Fucntion_Help_UserInfo selected")
            self.f_open_UserInfo()
        
        def Fucntion_signout_click():
            print("Fucntion_signout_click selected")
            self.f_open_login_window()
        
        def Fucntion_exit_click():
            print("Fucntion_exit_click selected")
            self.f_destroy_current_window()
            
        def Fuction_do_nothing():
            f_show_fading_popup("coming soon")
        
        # Create a Tkinter Menu bar
        top_menu = tk.Menu(self.parent)

        # Create a "Home" menu
        HOME_menu = tk.Menu(top_menu, tearoff=0)
        HOME_menu.add_command(label="Home", command=Function_Home_main_Click)
        top_menu.add_cascade(label="Home", menu=HOME_menu)
        
        # menu của Kinh doanh
        khong_co_quyen_kinh_doanh = ["vt1", "tc1", "kt1"]
        if self.current_user in khong_co_quyen_kinh_doanh:
            KinhDoanh_menu = tk.Menu(top_menu, tearoff=0)
            # print("không khỏi tạo menu kinh doanh")
        else:
            KinhDoanh_menu = tk.Menu(top_menu, tearoff=0)
            KinhDoanh_menu.add_command(label="Tạo mới gói thầu", command=Fucntion_QLGT_TaoMoi_Click)
            KinhDoanh_menu.add_command(label="Các gói thầu đã lập", command=Fucntion_QLGT_GoiThauDaLap)
            KinhDoanh_menu.add_separator()
            KinhDoanh_menu.add_command(label="Yêu cầu đặt hàng TALA", command=Fuction_QLYCDH_TALA)
            KinhDoanh_menu.add_command(label="Yêu cầu đặt hàng TM", command=Fuction_QLYCDH_TM)
            top_menu.add_cascade(label="Kinh doanh", menu=KinhDoanh_menu)
            
        # menu của Vật Tư
        khong_co_quyen_vat_tu = ["kd1", "tc1", "kt1"]
        if self.current_user in khong_co_quyen_vat_tu:
            VatTu_menu = tk.Menu(top_menu, tearoff=0)
            # print("không khỏi tạo menu vật tư")
        else:
            VatTu_menu = tk.Menu(top_menu, tearoff=0)
            VatTu_menu.add_command(label="DS Yêu cầu đặt hàng", command=Fuction_do_nothing)
            VatTu_menu.add_command(label="QL Nhà Cung cấp", command=Fuction_do_nothing)
            top_menu.add_cascade(label="Vật Tư", menu=VatTu_menu)
    
        # menu của Kỹ thuật
        khong_co_quyen_ky_thuat = ["kd1", "tc1", "vt1"]
        if self.current_user in khong_co_quyen_ky_thuat:
            KyThuat_menu = tk.Menu(top_menu, tearoff=0)
            # print("không khỏi tạo menu kỹ thuật")
        else:
            KyThuat_menu = tk.Menu(top_menu, tearoff=0)
            KyThuat_menu.add_command(label="Yêu cầu KT 01", command=Fuction_do_nothing)
            KyThuat_menu.add_command(label="Yêu cầu KT 02", command=Fuction_do_nothing)
            top_menu.add_cascade(label="Kỹ thuật", menu=KyThuat_menu)
            
        # menu của Tài chính
        khong_co_quyen_tai_chinh = ["kd1", "kt1", "vt1"]
        if self.current_user in khong_co_quyen_tai_chinh:
            TaiChinh_menu = tk.Menu(top_menu, tearoff=0)
            # print("không khỏi tạo menu kỹ thuật")
        else:
            TaiChinh_menu = tk.Menu(top_menu, tearoff=0)
            TaiChinh_menu.add_command(label="Quỹ tiền mặt", command=Fuction_do_nothing)
            TaiChinh_menu.add_command(label="Quỹ tiền gửi", command=Fuction_do_nothing)
            top_menu.add_cascade(label="Tài chính", menu=TaiChinh_menu)
        
        # Create a "Help" menu
        HELP_menu = tk.Menu(top_menu, tearoff=0)
        HELP_menu.add_command(label="About", command=Fucntion_Help_About)
        HELP_menu.add_command(label="User Info", command=Fucntion_Help_UserInfo)
        HELP_menu.add_separator()
        HELP_menu.add_command(label="Sign out", command=Fucntion_signout_click)
        HELP_menu.add_command(label="Exit", command=Fucntion_exit_click)
        top_menu.add_cascade(label="Help", menu=HELP_menu)
        
        # Set font size to 15 for all menus
        f_set_menu_font(HOME_menu)
        f_set_menu_font(KinhDoanh_menu)
        f_set_menu_font(VatTu_menu)
        f_set_menu_font(KyThuat_menu)
        f_set_menu_font(TaiChinh_menu)
        f_set_menu_font(HELP_menu)

        # Set the menu bar for the root window
        self.parent.config(menu=top_menu)
            
    def f_open_login_window(self):
        from views.user_management.loginView import cls_LoginView   # lazy import to avoid circular import
        self.dashboard_window.destroy()
        kd01_view = cls_LoginView()                     # Create an instance of the class
        kd01_view.dashboard = self.dashboard_window     # Pass the reference of the dashboard to KD01 view
        kd01_view.mainloop()                            # Open the window by starting the Tkinter event loop for the new view
        
    def f_open_KD02QuanLyYeuCauDatHangView(self):
        from app.views.KD02_QuanLyYeuCauDatHang.KD02QuanLyYeuCauDatHangView import cls_CRUDTreeviewView
        self.dashboard_window.destroy()
        kd01_view = cls_CRUDTreeviewView()
        kd01_view.dashboard = self.dashboard_window
        kd01_view.mainloop()
    
    def f_open_KD01_01QuanLyGoiThauView(self):
        from views.KD01_QuanLyGoiThau_New.KD01_01QuanLyGoiThauView import cls_View
        self.dashboard_window.destroy()
        kd01_view = cls_View()
        kd01_view.dashboard = self.dashboard_window
        kd01_view.mainloop()
    
    def f_open_KD01QuanLyGoiThauView(self):
        from views.KD01_QuanLyGoiThau.KD01QuanLyGoiThauView import cls_KD01QuanLyGoiThauView
        self.dashboard_window.destroy()
        kd01_view = cls_KD01QuanLyGoiThauView()
        kd01_view.dashboard = self.dashboard_window
        kd01_view.mainloop()

    def f_open_UserInfo(self):
        from views.user_management.UserInfo import cls_user_info
        self.dashboard_window.destroy()
        kd01_view = cls_user_info()
        kd01_view.dashboard = self.dashboard_window
        kd01_view.mainloop()
    
    def f_open_DashBoard(self):
        self.dashboard_window.destroy()
        from app.views.dashboard.DashboardView import f_render_dashboard
        f_render_dashboard()
        
    def f_destroy_current_window(self):
        self.dashboard_window.destroy()
        
    