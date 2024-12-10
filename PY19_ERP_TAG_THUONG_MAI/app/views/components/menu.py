# Project/views/components/menu.py
import tkinter as tk
from components.font_size import set_menu_font

def create_top_menu(parent, dashboard_window):
    # Create the menu
    top_menu = tk.Menu(parent)
    
    # Set the background color for the entire menu
    # top_menu.config(bg="lightblue")
    top_menu.config(bg="white")
    
    
    # Define the action fuctions for home menu
    def Function_Home_main_Click():
        print("Function_Home_main_Click selected")
        dashboard_window.destroy()
        # Now import KD01QuanLyGoiThauView inside the function to avoid circular import
        from app.views.dashboard.DashboardView import f_render_dashboard
        f_render_dashboard()
    
    # Define the action fuctions for QLGT menu
    def Fucntion_QLGT_TaoMoi_Click():
        # Now import KD01QuanLyGoiThauView inside the function to avoid circular import
        from views.KD01_QuanLyGoiThau.KD01QuanLyGoiThauView import cls_KD01QuanLyGoiThauView
        print("Fucntion_QLGT_TaoMoi_Click selected")
        # dashboard_window.withdraw()
        dashboard_window.destroy()
        kd01_view = cls_KD01QuanLyGoiThauView()  # Create an instance of the KD01QuanLyGoiThauView
        kd01_view.dashboard = dashboard_window  # Pass the reference of the dashboard to KD01 view
        kd01_view.mainloop()  # Open the window by starting the Tkinter event loop for the new view
    
    def Fucntion_QLGT_GoiThauDaLap():
        # Now import KD01QuanLyGoiThauView inside the function to avoid circular import
        from views.KD01_QuanLyGoiThau_New.KD01_01QuanLyGoiThauView import cls_View
        print("Fucntion_QLGT_GoiThauDaLap selected")
        dashboard_window.destroy()
        kd01_view = cls_View()  # Create an instance of the KD01QuanLyGoiThauView
        kd01_view.dashboard = dashboard_window  # Pass the reference of the dashboard to KD01 view
        kd01_view.mainloop()  # Open the window by starting the Tkinter event loop for the new view
    
    # =====================================================================================================================
    # Define the action fuctions for QLYCDT menu
    def Fuction_QLYCDH_TALA():
        # Now import KD01QuanLyGoiThauView inside the function to avoid circular import
        from app.views.KD02_QuanLyYeuCauDatHang.KD02QuanLyYeuCauDatHangView import cls_CRUDTreeviewView
        print("Fuction_QLYCDH_TALA selected")
        dashboard_window.destroy()
        kd01_view = cls_CRUDTreeviewView()  # Create an instance of the KD01QuanLyGoiThauView
        kd01_view.dashboard = dashboard_window  # Pass the reference of the dashboard to KD01 view
        kd01_view.mainloop()  # Open the window by starting the Tkinter event loop for the new view
        
    def Fuction_QLYCDH_TM():
        print("Fuction_QLYCDH_TM selected")
    
    # Define the action fuctions for Help menu
    def Fucntion_Help_About():
        print("Fucntion_Help_About selected")
    def Fucntion_Help_UserInfo():
        print("Fucntion_Help_UserInfo selected")
    
    # Create a Tkinter Menu bar
    menubar_BP_KD = tk.Menu(parent)

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
    HELP_menu.add_command(label="Exit", command=parent.quit)
    menubar_BP_KD.add_cascade(label="Help", menu=HELP_menu)
    
    # Set font size to 15 for all menus
    font_size = 14
    set_menu_font(HOME_menu, font_size)
    set_menu_font(QLGT_menu, font_size)
    set_menu_font(QLYCDH_menu, font_size)
    set_menu_font(HELP_menu, font_size)

    # Set the menu bar for the root window
    parent.config(menu=menubar_BP_KD)
        