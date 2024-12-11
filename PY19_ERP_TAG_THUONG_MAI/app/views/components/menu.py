# Project/views/components/menu.py
import tkinter as tk
from components.font_size import set_menu_font

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
        
        def Fucntion_signout_click():
            print("Fucntion_signout_click selected")
            self.f_open_login_window()
        
        def Fucntion_exit_click():
            print("Fucntion_exit_click selected")
            self.f_destroy_current_window()
        
        # Create a Tkinter Menu bar
        menubar_BP_KD = tk.Menu(self.parent)

        # Create a "Home" menu
        HOME_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        HOME_menu.add_command(label="Home", command=Function_Home_main_Click)
        menubar_BP_KD.add_cascade(label="Home", menu=HOME_menu)

        # Create a "Quản lý gói thầu" menu
        QLGT_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        QLGT_menu.add_command(label="Tạo mới gói thầu", command=Fucntion_QLGT_TaoMoi_Click)
        QLGT_menu.add_command(label="Các gói thầu đã lập", command=Fucntion_QLGT_GoiThauDaLap)
        menubar_BP_KD.add_cascade(label="Quản lý gói thầu", menu=QLGT_menu)

        # Create a "Quản lý yêu cầu đặt hàng" menu
        QLYCDH_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        QLYCDH_menu.add_command(label="Yêu cầu đặt hàng TALA", command=Fuction_QLYCDH_TALA)
        QLYCDH_menu.add_command(label="Yêu cầu đặt hàng TM", command=Fuction_QLYCDH_TM)
        menubar_BP_KD.add_cascade(label="Quản lý yêu cầu đặt hàng", menu=QLYCDH_menu)
        
        # Create a "Help" menu
        HELP_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        HELP_menu.add_command(label="About", command=Fucntion_Help_About)
        HELP_menu.add_command(label="User-infor", command=Fucntion_Help_UserInfo)
        HELP_menu.add_separator()
        HELP_menu.add_command(label="Sign out", command=Fucntion_signout_click)
        HELP_menu.add_command(label="Exit", command=Fucntion_exit_click)
        menubar_BP_KD.add_cascade(label="Help", menu=HELP_menu)
        
        # Set font size to 15 for all menus
        font_size = 14
        set_menu_font(HOME_menu, font_size)
        set_menu_font(QLGT_menu, font_size)
        set_menu_font(QLYCDH_menu, font_size)
        set_menu_font(HELP_menu, font_size)

        # Set the menu bar for the root window
        self.parent.config(menu=menubar_BP_KD)
            
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

    def f_open_DashBoard(self):
        self.dashboard_window.destroy()
        from app.views.dashboard.DashboardView import f_render_dashboard
        f_render_dashboard()
        
    def f_destroy_current_window(self):
        self.dashboard_window.destroy()