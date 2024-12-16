# Project/views/components/menu.py
import tkinter as tk
from utils import *

class cls_Menu:
    def __init__(self, parent, dashboard_window):
        """
        Initializes the Menu with the given parent and dashboard window.
        """
        self.parent = parent
        self.dashboard_window = dashboard_window
        self.top_menu = tk.Menu(self.parent)
        self.f_create_top_menu()
        
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
        
        # Create a Tkinter Menu bar
        top_menu = tk.Menu(self.parent)

        # Create a "Home" menu
        HOME_menu = tk.Menu(top_menu, tearoff=0)
        HOME_menu.add_command(label="Home", command=Function_Home_main_Click)
        top_menu.add_cascade(label="Home", menu=HOME_menu)

        # Create a "Quản lý gói thầu" menu
        QLGT_menu = tk.Menu(top_menu, tearoff=0)
        QLGT_menu.add_command(label="Tạo mới gói thầu", command=Fucntion_QLGT_TaoMoi_Click)
        QLGT_menu.add_command(label="Các gói thầu đã lập", command=Fucntion_QLGT_GoiThauDaLap)
        top_menu.add_cascade(label="Quản lý gói thầu", menu=QLGT_menu)

        # Create a "Quản lý yêu cầu đặt hàng" menu
        QLYCDH_menu = tk.Menu(top_menu, tearoff=0)
        QLYCDH_menu.add_command(label="Yêu cầu đặt hàng TALA", command=Fuction_QLYCDH_TALA)
        QLYCDH_menu.add_command(label="Yêu cầu đặt hàng TM", command=Fuction_QLYCDH_TM)
        top_menu.add_cascade(label="Quản lý yêu cầu đặt hàng", menu=QLYCDH_menu)
        
        # menu của Vật Tư
        VatTu_menu = tk.Menu(top_menu, tearoff=0)
        VatTu_menu.add_command(label="DS Yêu cầu đặt hàng", command=Fuction_QLYCDH_TALA)
        VatTu_menu.add_command(label="QL Nhà Cung cấp", command=Fuction_QLYCDH_TM)
        top_menu.add_cascade(label="Vật Tư", menu=VatTu_menu)
    
        # menu của Kỹ thuật
        KyThuat_menu = tk.Menu(top_menu, tearoff=0)
        KyThuat_menu.add_command(label="Yêu cầu KT 01", command=Fuction_QLYCDH_TALA)
        KyThuat_menu.add_command(label="Yêu cầu KT 02", command=Fuction_QLYCDH_TM)
        top_menu.add_cascade(label="Kỹ thuật", menu=KyThuat_menu)
        
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
        f_set_menu_font(QLGT_menu)
        f_set_menu_font(QLYCDH_menu)
        f_set_menu_font(VatTu_menu)
        f_set_menu_font(KyThuat_menu)
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
        
    