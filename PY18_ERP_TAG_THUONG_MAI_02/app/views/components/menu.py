# Project/views/components/menu.py
import tkinter as tk
from components.font_size import set_menu_font

class cls_Menu:
    def __init__(self, master):
        self.master = master
        self.create_top_menu()
    
    def create_top_menu(self):
        # Create the menu bar
        menubar = tk.Menu(self.master)
        
        # Define Home menu
        home_menu = tk.Menu(menubar, tearoff=0)
        home_menu.add_command(label="Home Main", command=self.Function_Home_main_Click)
        menubar.add_cascade(label="Home", menu=home_menu)

        # Define QLGT (Quan Ly Goi Thau) menu
        qlgt_menu = tk.Menu(menubar, tearoff=0)
        qlgt_menu.add_command(label="Tao Moi", command=self.Fucntion_QLGT_TaoMoi_Click)
        qlgt_menu.add_command(label="Goi Thau Da Lap", command=self.Fucntion_QLGT_GoiThauDaLap)
        menubar.add_cascade(label="QLGT", menu=qlgt_menu)

        # Define QLYCDT (Quan Ly Yeu Cau Dat Hang) menu
        qlycdt_menu = tk.Menu(menubar, tearoff=0)
        qlycdt_menu.add_command(label="TALA", command=self.Fuction_QLYCDH_TALA)
        qlycdt_menu.add_command(label="TM", command=self.Fuction_QLYCDH_TM)
        menubar.add_cascade(label="QLYCDT", menu=qlycdt_menu)

        # Define Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.Fucntion_Help_About)
        help_menu.add_command(label="User Info", command=self.Fucntion_Help_UserInfo)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Attach the menu bar to the main window
        self.master.config(menu=menubar)

    # Define the action functions for the menus
    def Function_Home_main_Click(self):
        print("Function_Home_main_Click selected")
        self.master.destroy()  # Assuming 'self.master' is the dashboard window
        from PY18_ERP_TAG_THUONG_MAI_02.app.views.dashboard.DashboardView import render_dashboard
        render_dashboard()

    def Fucntion_QLGT_TaoMoi_Click(self):
        print("Fucntion_QLGT_TaoMoi_Click selected")
        self.master.destroy()
        from views.KD01QuanLyGoiThauView import KD01QuanLyGoiThauView
        kd01_view = KD01QuanLyGoiThauView()
        kd01_view.dashboard = self.master
        kd01_view.mainloop()

    def Fucntion_QLGT_GoiThauDaLap(self):
        print("Fucntion_QLGT_GoiThauDaLap selected")
        self.master.destroy()
        from views.KD01_01QuanLyGoiThauView import View
        kd01_view = View()
        kd01_view.dashboard = self.master
        kd01_view.mainloop()

    def Fuction_QLYCDH_TALA(self):
        print("Fuction_QLYCDH_TALA selected")
        self.master.destroy()
        from views.KD02QuanLyYeuCauDatHangView import cls_CRUDTreeviewView
        kd01_view = cls_CRUDTreeviewView()
        kd01_view.dashboard = self.master
        kd01_view.mainloop()

    def Fuction_QLYCDH_TM(self):
        print("Fuction_QLYCDH_TM selected")

    def Fucntion_Help_About(self):
        print("Fucntion_Help_About selected")

    def Fucntion_Help_UserInfo(self):
        print("Fucntion_Help_UserInfo selected")
