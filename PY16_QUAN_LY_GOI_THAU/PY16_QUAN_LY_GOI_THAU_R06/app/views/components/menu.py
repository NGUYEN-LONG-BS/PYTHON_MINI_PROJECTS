# Project/views/components/menu.py
import tkinter as tk
from views.KD01QuanLyGoiThauView import KD01QuanLyGoiThauView

def create_menu_TK_02(parent, dashboard_window):
    
        # Define the action fuctions for home menu
        def Fucntion_Home_main():
            print("Fucntion_Home_main selected")
        
        # Define the action fuctions for QLGT menu
        def Fucntion_QLGT_TaoMoi():
            print("Fucntion_QLGT_TaoMoi selected")
            dashboard_window.withdraw()
            kd01_view = KD01QuanLyGoiThauView()  # Create an instance of the KD01QuanLyGoiThauView
            kd01_view.dashboard = dashboard_window  # Pass the reference of the dashboard to KD01 view
            kd01_view.mainloop()  # Open the window by starting the Tkinter event loop for the new view
        def Fucntion_QLGT_GoiThauDaLap():
            print("Fucntion_QLGT_GoiThauDaLap selected")
        
        # Define the action fuctions for QLYCDT menu
        def Fuction_QLYCDH_TALA():
            print("Fuction_QLYCDH_TALA selected")
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
        help_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        menubar_BP_KD.add_cascade(label="Home", command=Fucntion_Home_main)

        # Create a "Quản lý gói thầu" menu
        file_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        file_menu.add_command(label="Tạo mới gói thầu", command=Fucntion_QLGT_TaoMoi)
        file_menu.add_command(label="Các gói thầu đã lập", command=Fucntion_QLGT_GoiThauDaLap)
        menubar_BP_KD.add_cascade(label="Quản lý gói thầu", menu=file_menu)

        # Create a "Quản lý yêu cầu đặt hàng" menu
        help_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        help_menu.add_command(label="Yêu cầu đặt hàng TALA", command=Fuction_QLYCDH_TALA)
        help_menu.add_command(label="Yêu cầu đặt hàng TM", command=Fuction_QLYCDH_TM)
        menubar_BP_KD.add_cascade(label="Quản lý yêu cầu đặt hàng", menu=help_menu)
        
        # Create a "Help" menu
        help_menu = tk.Menu(menubar_BP_KD, tearoff=0)
        help_menu.add_command(label="About", command=Fucntion_Help_About)
        help_menu.add_command(label="User-infor", command=Fucntion_Help_UserInfo)
        help_menu.add_separator()
        help_menu.add_command(label="Exit", command=parent.quit)
        menubar_BP_KD.add_cascade(label="Help", menu=help_menu)

        # Set the menu bar for the root window
        parent.config(menu=menubar_BP_KD)
        
        