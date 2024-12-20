import tkinter as tk
from utils import *
from utils.define import *
import json
import sys
import os

class cls_menu_top:
    def __init__(self, parent):
        """
        Initializes the Menu with the given parent and dashboard window.
        """
        self.parent = parent
        self.parent = parent
        self.top_menu = tk.Menu(self.parent)
        self.current_user = self.read_user_from_json()  # Read the logged-in user
        self.f_create_top_menu()

    def f_create_top_menu(self):
        # Create a Tkinter Menu bar
        top_menu = tk.Menu(self.parent)
        
        # Khởi tạo các menu level 0
        self.f_create_menu_Home(top_menu)
        self.f_create_menu_kinhdoanh(top_menu)
        self.f_create_menu_vattu(top_menu)
        self.f_create_menu_kythuat(top_menu)
        self.f_create_menu_taichinh(top_menu)
        self.f_create_menu_Help(top_menu)
        self.f_create_menu_Test(top_menu)
        self.f_create_menu_Exit(top_menu)
        
        # Set the menu bar for the root window
        self.parent.config(menu=top_menu)
    
    def read_user_from_json(self):
        """ Reads the logged-in user's username from the JSON file. """
        # Sử dụng đường dẫn tuyệt đối
        json_file = os.path.join(PATH_ROOT, 'app', 'views','AD00_User_Management_View', 'login_credentials.json')
        # print(json_file)
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            return data.get("username", "")  # Return the username from the JSON file
        except Exception as e:
            print(f"Error reading credentials: {e}")
            return ""
    
    def f_check_permission(self, menu_name):
        permissions = {
                        "kinhdoanh": ["vt1", "tc1", "kt1"],
                        "vattu": ["kd1", "tc1", "kt1"],
                        "kythuat": ["kd1", "tc1", "vt1"],
                        "taichinh": ["kd1", "kt1", "vt1"]
                    }
        return self.current_user not in permissions.get(menu_name, [])
    
    def f_create_menu_Exit(self, top_menu):
        # Create a "Exit" menu
        top_menu.add_command(label="Exit", command=self.f_destroy_current_window)

    def f_create_menu_Home(self, top_menu):
        # Create a "Home" menu
        top_menu.add_command(label="Home", command=self.f_Home_main_click)
    
    def f_create_menu_kinhdoanh(self, top_menu):
        if self.f_check_permission("kinhdoanh") == False:
            menu_KinhDoanh = tk.Menu(top_menu, tearoff=0)
        else:
            # menu_KinhDoanh level 0
            menu_KinhDoanh = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Kinh doanh", menu=menu_KinhDoanh)
            
            # menu_KinhDoanh level 1
            menu_KinhDoanh_QuanLyGoiThau = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Quản lý gói thầu", menu=menu_KinhDoanh_QuanLyGoiThau)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_QuanLyYeuCauDatHang = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Quản lý yêu cầu đặt hàng", menu=menu_KinhDoanh_QuanLyYeuCauDatHang)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_QuanLyKhachHang = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Quản lý khách hàng", menu=menu_KinhDoanh_QuanLyKhachHang)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_QuanLyTonKho = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Quản lý tồn kho", menu=menu_KinhDoanh_QuanLyTonKho)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyGoiThau
            menu_KinhDoanh_QuanLyGoiThau.add_command(label="KD0101 |Quản lý gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
            menu_KinhDoanh_QuanLyGoiThau.add_command(label="KD0102 |Tạo mới gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyYeuCauDatHang
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_command(label="KD0201 |Tạo mới YCĐH", command=self.f_QLYCDH_TALA_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_command(label="KD0202 |Nhật ký YCĐH", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_separator()
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH = tk.Menu(menu_KinhDoanh_QuanLyYeuCauDatHang, tearoff=0)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_cascade(label="Báo cáo YCDH", menu=menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyKhachHang
            menu_KinhDoanh_QuanLyKhachHang.add_command(label="KD0301 |Quản lý khách hàng", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyKhachHang.add_command(label="KD0301 |Tạo mới khách hàng", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyKhachHang.add_separator()
            menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH = tk.Menu(menu_KinhDoanh_QuanLyKhachHang, tearoff=0)
            menu_KinhDoanh_QuanLyKhachHang.add_cascade(label="Báo cáo khách hàng", menu=menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyTonKho
            menu_KinhDoanh_QuanLyTonKho.add_command(label="KD0401 |Yêu cầu tạo mã hàng mới", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyTonKho.add_separator()
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho = tk.Menu(menu_KinhDoanh_QuanLyTonKho, tearoff=0)
            menu_KinhDoanh_QuanLyTonKho.add_cascade(label="Báo cáo tồn kho", menu=menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho)
            
            # menu_KinhDoanh level 3: menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH
            menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH.add_command(label="Báo cáo 01", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH.add_command(label="Báo cáo 02", command=self.f_do_nothing_click)
            
            # menu_KinhDoanh level 3: menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH.add_command(label="Báo cáo YCDH 01", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH.add_command(label="Báo cáo YCDH 02", command=self.f_do_nothing_click)
            
            # menu_KinhDoanh level 3: menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho.add_command(label="Báo cáo tồn kho 01", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho.add_command(label="Báo cáo tồn kho 02", command=self.f_do_nothing_click)
        
        # Set font-size
        f_utils_set_menu_font(menu_KinhDoanh)
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyGoiThau)
        
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyYeuCauDatHang)
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH)
        
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyKhachHang)
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyKhachHang_BaoCaoKH)
        
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyTonKho)
        f_utils_set_menu_font(menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho)
    
    def f_create_menu_vattu(self, top_menu):
        if self.f_check_permission("vattu") == False:
            menu_VatTu = tk.Menu(top_menu, tearoff=0)
        else:
            menu_VatTu = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Vật Tư", menu=menu_VatTu)
            
            # menu_KinhDoanh level 1
            menu_VatTu_QuanLyDonDatHang = tk.Menu(menu_VatTu, tearoff=0)
            menu_VatTu.add_cascade(label="Quản lý đơn đặt hàng", menu=menu_VatTu_QuanLyDonDatHang)
            menu_VatTu.add_separator()
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyGoiThau
            menu_VatTu_QuanLyDonDatHang.add_command(label="Đơn đặt hàng TALA", command=self.f_open_cls_VT0101_DonDatHang_View)
            menu_VatTu_QuanLyDonDatHang.add_command(label="Đơn đặt hàng TM", command=self.f_open_cls_VT0102_DonDatHang_TM_View)
            menu_VatTu_QuanLyDonDatHang.add_command(label="Nhật ký đơn đặt hàng", command=self.f_do_nothing_click)
            
            menu_VatTu.add_separator()
            menu_VatTu.add_command(label="DS Yêu cầu đặt hàng", command=self.f_do_nothing_click)
            menu_VatTu.add_command(label="QL Nhà Cung cấp", command=self.f_do_nothing_click)
            
        # Set font-size
        f_utils_set_menu_font(menu_VatTu)
        f_utils_set_menu_font(menu_VatTu_QuanLyDonDatHang)
            
    def f_create_menu_kythuat(self, top_menu):
        if self.f_check_permission("kythuat") == False:
            menu_KyThuat = tk.Menu(top_menu, tearoff=0)
        else:
            menu_KyThuat = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Kỹ thuật", menu=menu_KyThuat)
            
            menu_KyThuat.add_command(label="Yêu cầu KT 01", command=self.f_do_nothing_click)
            menu_KyThuat.add_command(label="Yêu cầu KT 02", command=self.f_do_nothing_click)
        
        # Set font-size
        f_utils_set_menu_font(menu_KyThuat)
            
    def f_create_menu_taichinh(self, top_menu):
        if self.f_check_permission("taichinh") == False:
            menu_TaiChinh = tk.Menu(top_menu, tearoff=0)
        else:
            menu_TaiChinh = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Tài chính", menu=menu_TaiChinh)
            
            # Sub-menu level 1
            TaiChinh_menu_Level_1 = tk.Menu(menu_TaiChinh, tearoff=0)
            menu_TaiChinh.add_cascade(label="Quản lý thu chi", menu=TaiChinh_menu_Level_1)
            TaiChinh_menu_Level_1.add_command(label="TC0101 |Quỹ tiền mặt", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0102 |Quỹ tiền gửi", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0103 |Thu chi tiền mặt", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0104 |Thu chi tiền gửi", command=self.f_do_nothing_click)
            
            # Sub-menu level 1
            menu_TaiChinh.add_cascade(label="Quản lý thu chi", menu=TaiChinh_menu_Level_1)
            TaiChinh_menu_Level_1.add_command(label="TC0101 |Quỹ tiền mặt", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0102 |Quỹ tiền gửi", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0103 |Thu chi tiền mặt", command=self.f_do_nothing_click)
            TaiChinh_menu_Level_1.add_command(label="TC0104 |Thu chi tiền gửi", command=self.f_do_nothing_click)
            
        # Set font-size
        f_utils_set_menu_font(menu_TaiChinh)
    
    def f_create_menu_Help(self, top_menu):
        # Create a "Help" menu
        menu_HELP = tk.Menu(top_menu, tearoff=0)
        top_menu.add_cascade(label="Help", menu=menu_HELP)
        
        menu_HELP.add_command(label="About", command=self.f_Help_About_click)
        menu_HELP.add_command(label="User Info", command=self.f_Help_UserInfo_click)
        menu_HELP.add_separator()
        menu_HELP.add_command(label="Sign out", command=self.f_menu_Help_Signout_click)
        menu_HELP.add_command(label="Exit", command=self.f_Help_Exit_click)
        
        # Set font-size
        f_utils_set_menu_font(menu_HELP)
    
    def f_create_menu_Test(self, top_menu):
        # Create a "Test" menu
        menu_TEST = tk.Menu(top_menu, tearoff=0)
        top_menu.add_cascade(label="TEST", menu=menu_TEST)
        
        menu_TEST.add_command(label="Các gói thầu đã lập", command=self.f_QLGT_GoiThauDaLap_click)
        menu_TEST.add_command(label="Tạo mới gói thầu", command=self.f_QLGT_TaoMoi_click)
        menu_TEST.add_command(label="Các gói thầu đã lập", command=self.f_QLGT_GoiThauDaLap_click)
    
        menu_TEST.add_command(label="KD0201 |Phiếu Yêu cầu đặt hàng", command=self.f_QLYCDH_TALA_click)
        menu_TEST.add_command(label="KD0202 |Nhật ký yêu cầu đặt hàng", command=self.f_QLYCDH_TM_click)
        
        menu_TEST.add_separator()
        menu_TEST.add_command(label="KD0101 |Quản lý gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
        menu_TEST.add_command(label="KD0102 |Tạo mới gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
        
        # Set font-size
        f_utils_set_menu_font(menu_TEST)
    
    # Define the action fuctions for home menu
    def f_Home_main_click(self):
        print("f_Home_main_click selected")
        self.f_open_DashBoard()
    
    # Define the action fuctions for QLGT menu
    def f_QLGT_TaoMoi_click(self):
        print("f_QLGT_TaoMoi_click selected")
        self.f_open_KD01QuanLyGoiThauView()
        
    def f_KD0101_QuanLyGoiThau_click(self):
        print("f_QLGT_TaoMoi_click selected")
        self.f_open_KD0101_QuanLyGoiThau_View()
    
    def f_QLGT_GoiThauDaLap_click(self):
        print("f_QLGT_GoiThauDaLap_click selected")
        self.f_open_KD01_01QuanLyGoiThauView()
    
    # Define the action fuctions for QLYCDT menu
    def f_QLYCDH_TALA_click(self):
        print("f_QLYCDH_TALA_click selected")
        self.f_open_KD02QuanLyYeuCauDatHangView()
        
    def f_QLYCDH_TM_click(self):
        print("f_QLYCDH_TM_click selected")
    
    def f_Help_About_click(self):
        print("f_Help_About_click selected")
    
    def f_Help_UserInfo_click(self):
        print("f_Help_UserInfo_click selected")
        self.f_open_UserInfo()
    
    def f_menu_Help_Signout_click(self):
        print("f_menu_Help_Signout_click selected")
        self.f_open_login_window()
    
    def f_Help_Exit_click(self):
        print("f_Help_Exit_click selected")
        self.f_destroy_current_window()
        
    def f_do_nothing_click(self):
        f_utils_show_fading_popup("coming soon")
    
    def f_open_login_window(self):
        from views.AD00_User_Management_View.AD0001_login_View import cls_Login_View   # lazy import to avoid circular import
        self.parent.destroy()
        new_view = cls_Login_View()                             # Create an instance of the class
        new_view.dashboard = self.parent                        # Pass the reference of the dashboard to KD01 view
        f_utils_set_center_screen(new_view)                     # Center the new window on the screen
        new_view.focus_force()                                  # Ensure the new window is in focus
        
    def f_open_KD02QuanLyYeuCauDatHangView(self):
        from views.KD02_QuanLyYeuCauDatHang_View.KD0201_PhieuYeuCauDatHang_View import cls_KD0201_PhieuYeuCauDatHang_View
        self.parent.destroy()
        new_view = cls_KD0201_PhieuYeuCauDatHang_View()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    
    def f_open_KD01_01QuanLyGoiThauView(self):
        from views.KD01_QuanLyGoiThau_TEST_02.KD01_01QuanLyGoiThauView import cls_View
        self.parent.destroy()
        new_view = cls_View()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    
    def f_open_KD01QuanLyGoiThauView(self):
        from views.KD01_QuanLyGoiThau_TEST_01.KD01QuanLyGoiThauView import cls_KD01QuanLyGoiThauView
        self.parent.destroy()
        new_view = cls_KD01QuanLyGoiThauView()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
        
    def f_open_KD0101_QuanLyGoiThau_View(self):
        from views.KD01_QuanLyGoiThau_View.KD0101_QuanLyGoiThau_View import cls_KD0101_QuanLyGoiThau_View
        self.parent.destroy()
        new_view = cls_KD0101_QuanLyGoiThau_View()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
        
    def f_open_cls_VT0101_DonDatHang_View(self):
        from views.VT01_QuanLyDonDatHang_View.VT0101_DonDatHang_View import cls_VT0101_DonDatHang_View
        self.parent.destroy()
        new_view = cls_VT0101_DonDatHang_View()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
        
    def f_open_cls_VT0102_DonDatHang_TM_View(self):
        from views.VT01_QuanLyDonDatHang_View.VT0102_DonDatHang_TM_View import cls_VT0102_DonDatHang_TM_View
        self.parent.destroy()
        new_view = cls_VT0102_DonDatHang_TM_View()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        

    def f_open_UserInfo(self):
        from AD00_User_Management_View.AD0003_UserInfo_View import cls_user_info
        self.parent.destroy()
        new_view = cls_user_info()
        new_view.dashboard = self.parent
        f_utils_set_window_size_is_4_per_5_screen(new_view)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    
    def f_open_DashBoard(self):
        self.parent.destroy()
        f_utils_open_dashboard()
        
    def f_destroy_current_window(self):
        self.parent.destroy()
        