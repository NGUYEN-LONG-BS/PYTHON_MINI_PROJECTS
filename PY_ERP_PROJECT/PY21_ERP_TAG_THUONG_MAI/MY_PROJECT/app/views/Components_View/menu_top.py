import tkinter as tk
from app.utils import *
import json
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
        self.f_create_menu_nhansu(top_menu)
        self.f_create_menu_admin(top_menu)
        self.f_create_menu_Help(top_menu)
        self.f_create_menue_AI_chatbot(top_menu)
        self.f_create_menu_Test(top_menu)
        self.f_create_menu_Exit(top_menu)
        self.f_create_menu_Signout(top_menu)
        
        # Set the menu bar for the root window
        self.parent.config(menu=top_menu)
    
    def read_user_from_json(self):
        """ Reads the logged-in user's username from the JSON file. """
        # Sử dụng đường dẫn tuyệt đối
        # json_file = os.path.join(PATH_ROOT, 'app', 'views','AD00_User_Management_View', 'login_credentials.json')
        json_file = define.PATH_JSON_LOGIN_CREDENTIALS
        # print(json_file)
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
            return data.get("username", "")  # Return the username from the JSON file
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return ""
    
    def f_check_permission(self, menu_name):
        permissions = {
                        "kinhdoanh": ["vt1", "tc1", "kt1", "ns1"],
                        "vattu": ["kd1", "tc1", "kt1", "ns1"],
                        "kythuat": ["kd1", "tc1", "vt1", "ns1"],
                        "admin": ["kd1", "tc1", "vt1", "kt1", "ns1"],
                        "taichinh": ["kd1", "kt1", "vt1", "ns1"],
                        "nhansu": ["kd1", "kt1", "vt1", "tc1"]
                    }
        return self.current_user not in permissions.get(menu_name, [])
    
    def f_create_menu_Exit(self, top_menu):
        # Create a "Exit" menu
        top_menu.add_command(label="Exit", command=self.f_destroy_current_window)
        
    def f_create_menu_Signout(self, top_menu):
        # Create a "Exit" menu
        top_menu.add_command(label="Sign out", command=self.f_menu_Help_Signout_click)

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
            menu_KinhDoanh.add_command(label="BP kinh doanh", command=self.f_Kinh_Doanh_Home_main_click)
            menu_KinhDoanh.add_separator()
            
            # menu_KinhDoanh level 1
            menu_KinhDoanh_KeHoachDatHang = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Kế hoạch đặt hàng", menu=menu_KinhDoanh_KeHoachDatHang)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_QuanLyYeuCauDatHang = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Quản lý yêu cầu đặt hàng", menu=menu_KinhDoanh_QuanLyYeuCauDatHang)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_DeNghiXuatKho = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Đề nghị xuất kho", menu=menu_KinhDoanh_DeNghiXuatKho)
            menu_KinhDoanh.add_separator()
            menu_KinhDoanh_QuanLyTonKho = tk.Menu(menu_KinhDoanh, tearoff=0)
            menu_KinhDoanh.add_cascade(label="Tồn kho", menu=menu_KinhDoanh_QuanLyTonKho)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_KeHoachDatHang
            menu_KinhDoanh_KeHoachDatHang.add_command(label="KD0201 |Tạo mới kế hoạch đặt hàng", command=self.f_tao_moi_KeHoachDatHang_click)
            menu_KinhDoanh_KeHoachDatHang.add_command(label="KD0201 |Nhật ký kế hoạch đặt hàng", command=self.f_nhat_ky_KeHoachDatHang_click)
            menu_KinhDoanh_KeHoachDatHang.add_separator()
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyYeuCauDatHang
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_command(label="KD0202 |Tạo mới yêu cầu đặt hàng", command=self.f_tao_moi_YCDH_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_command(label="KD0202 |Nhật ký yêu cầu đặt hàng", command=self.f_nhat_ky_YCDH_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_separator()
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH = tk.Menu(menu_KinhDoanh_QuanLyYeuCauDatHang, tearoff=0)
            menu_KinhDoanh_QuanLyYeuCauDatHang.add_cascade(label="Báo cáo YCDH", menu=menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH)
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_DeNghiXuatKho
            menu_KinhDoanh_DeNghiXuatKho.add_command(label="KD0301 |Tạo mới đề nghị xuất kho", command=self.f_tao_moi_DeNghiXuatKho_click)
            menu_KinhDoanh_DeNghiXuatKho.add_command(label="KD0301 |Nhật ký đề nghị xuất kho", command=self.f_nhat_ky_DeNghiXuatKho_click)
            menu_KinhDoanh_DeNghiXuatKho.add_separator()
            
            # menu_KinhDoanh level 2: menu_KinhDoanh_QuanLyTonKho
            menu_KinhDoanh_QuanLyTonKho.add_command(label="KD0401 |Yêu cầu tạo mã hàng mới", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyTonKho.add_separator()
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho = tk.Menu(menu_KinhDoanh_QuanLyTonKho, tearoff=0)
            menu_KinhDoanh_QuanLyTonKho.add_cascade(label="Báo cáo tồn kho", menu=menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho)
            
            # menu_KinhDoanh level 3: menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH.add_command(label="Báo cáo YCDH 01", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH.add_command(label="Báo cáo YCDH 02", command=self.f_do_nothing_click)
            
            # menu_KinhDoanh level 3: menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho.add_command(label="Báo cáo tồn kho 01", command=self.f_do_nothing_click)
            menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho.add_command(label="Báo cáo tồn kho 02", command=self.f_do_nothing_click)
        
            # Set font-size
            f_utils_set_menu_font(menu_KinhDoanh)
            f_utils_set_menu_font(menu_KinhDoanh_KeHoachDatHang)
            
            f_utils_set_menu_font(menu_KinhDoanh_QuanLyYeuCauDatHang)
            f_utils_set_menu_font(menu_KinhDoanh_QuanLyYeuCauDatHang_BaoCaoYCDH)
            
            f_utils_set_menu_font(menu_KinhDoanh_DeNghiXuatKho)
            
            f_utils_set_menu_font(menu_KinhDoanh_QuanLyTonKho)
            f_utils_set_menu_font(menu_KinhDoanh_QuanLyTonKho_BaoCaoTonKho)
        
    def f_create_menu_vattu(self, top_menu):
        if self.f_check_permission("vattu") == False:
            menu_VatTu = tk.Menu(top_menu, tearoff=0)
        else:
            menu_VatTu = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Vật Tư", menu=menu_VatTu)
            menu_VatTu.add_command(label="BP vật tư", command=self.f_Vat_Tu_Home_main_click)
            menu_VatTu.add_separator()
            
            # menu_KinhDoanh level 1
            menu_VatTu_QuanLyDonDatHang = tk.Menu(menu_VatTu, tearoff=0)
            menu_VatTu.add_cascade(label="Quản lý đơn đặt hàng", menu=menu_VatTu_QuanLyDonDatHang)
            menu_VatTu.add_separator()
            
            # menu_KinhDoanh level 2:
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
            menu_TaiChinh_QuanLyThuChi = tk.Menu(menu_TaiChinh, tearoff=0)
            menu_TaiChinh.add_cascade(label="Quản lý thu chi", menu=menu_TaiChinh_QuanLyThuChi)
            menu_TaiChinh.add_separator()
            menu_TaiChinh_QuanLyKyQuy = tk.Menu(menu_TaiChinh, tearoff=0)
            menu_TaiChinh.add_cascade(label="Quản lý ký quỹ", menu=menu_TaiChinh_QuanLyKyQuy)
            
            # Sub-menu level 2
            menu_TaiChinh_QuanLyThuChi.add_command(label="TC0101 |Quỹ tiền mặt", command=self.f_do_nothing_click)
            menu_TaiChinh_QuanLyThuChi.add_command(label="TC0102 |Quỹ tiền gửi", command=self.f_do_nothing_click)
            
            # Sub-menu level 2
            menu_TaiChinh_QuanLyKyQuy.add_command(label="TC0201 |Ký quỹ tiền mặt", command=self.f_do_nothing_click)
            menu_TaiChinh_QuanLyKyQuy.add_command(label="TC0202 |Ký quỹ bằng tài sản", command=self.f_do_nothing_click)
            
            # Set font-size
            f_utils_set_menu_font(menu_TaiChinh)
            
            f_utils_set_menu_font(menu_TaiChinh_QuanLyThuChi)
            f_utils_set_menu_font(menu_TaiChinh_QuanLyKyQuy)

    def f_create_menu_nhansu(self, top_menu):
        if self.f_check_permission("nhansu") == False:
            menu_NhanSu = tk.Menu(top_menu, tearoff=0)
        else:
            menu_NhanSu = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Nhân sự", menu=menu_NhanSu)
            
            # Sub-menu level 1
            menu_NhanSu_QuanLyNhanVien = tk.Menu(menu_NhanSu, tearoff=0)
            menu_NhanSu.add_cascade(label="Quản lý nhân viên", menu=menu_NhanSu_QuanLyNhanVien)
            menu_NhanSu.add_separator()
            menu_NhanSu_QuanLyCongPhep = tk.Menu(menu_NhanSu, tearoff=0)
            menu_NhanSu.add_cascade(label="Quản lý công - phép", menu=menu_NhanSu_QuanLyCongPhep)
            menu_NhanSu.add_separator()
            menu_NhanSu_QuanLyThongBao = tk.Menu(menu_NhanSu, tearoff=0)
            menu_NhanSu.add_cascade(label="Quản lý thông báo", menu=menu_NhanSu_QuanLyThongBao)
            menu_NhanSu.add_separator()
            menu_NhanSu.add_command(label="Form mẫu", command=self.f_HR01_click)

            # Sub-menu level 2
            menu_NhanSu_QuanLyNhanVien.add_command(label="NS0101 |Danh sách nhân viên", command=self.f_do_nothing_click)
            menu_NhanSu_QuanLyNhanVien.add_command(label="NS0102 |Tạo mới nhân viên", command=self.f_do_nothing_click)

            # Sub-menu level 2
            menu_NhanSu_QuanLyCongPhep.add_command(label="NS0101 |Danh sách nghỉ phép", command=self.f_do_nothing_click)
            menu_NhanSu_QuanLyCongPhep.add_command(label="NS0102 |Điều chỉnh công - phép", command=self.f_do_nothing_click)
            
            # Sub-menu level 2
            menu_NhanSu_QuanLyThongBao.add_command(label="NS0101 |Danh sách thông báo", command=self.f_do_nothing_click)
            menu_NhanSu_QuanLyThongBao.add_command(label="NS0102 |Tạo mới thông báo", command=self.f_do_nothing_click)
            
            # Set font-size
            f_utils_set_menu_font(menu_NhanSu)
            
            f_utils_set_menu_font(menu_NhanSu_QuanLyCongPhep)
            f_utils_set_menu_font(menu_NhanSu_QuanLyNhanVien)
            f_utils_set_menu_font(menu_NhanSu_QuanLyThongBao)

    def f_create_menu_admin(self, top_menu):
        if self.f_check_permission("admin") == False:
            menu_Admin = tk.Menu(top_menu, tearoff=0)
        else:
            menu_Admin = tk.Menu(top_menu, tearoff=0)
            top_menu.add_cascade(label="Admin", menu=menu_Admin)
            menu_Admin.add_command(label="Dashboard Admin", command=self.f_Admin_Home_main_click)
            menu_Admin.add_separator()
            
            # Sub-menu level 1
            Admin_menu_Level_1 = tk.Menu(menu_Admin, tearoff=0)
            menu_Admin.add_cascade(label="Quản lý danh sách chi nhánh", menu=Admin_menu_Level_1)
            Admin_menu_Level_1.add_command(label="AD0101 |Tạo mới chi nhánh", command=self.f_do_nothing_click)
            Admin_menu_Level_1.add_command(label="AD0102 |Danh sách chi nhánh", command=self.f_do_nothing_click)
            
            # Sub-menu level 1
            menu_Admin.add_cascade(label="Quản lý danh sách người dùng", menu=Admin_menu_Level_1)
            Admin_menu_Level_1.add_command(label="AD0101 |Tạo mới người dùng", command=self.f_do_nothing_click)
            Admin_menu_Level_1.add_command(label="AD0102 |Danh sách người dùng", command=self.f_do_nothing_click)
            menu_Admin.add_separator()
            
            # Set font-size
            f_utils_set_menu_font(menu_Admin)
    
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
    
    def f_create_menue_AI_chatbot(self, top_menu):
        # Create a "AI-Chatbot" menu
        top_menu.add_command(label="AI-Chatbot", command=self.f_AI_Chatbot_click)
    
    def f_create_menu_Test(self, top_menu):
        # Create a "Test" menu
        menu_TEST = tk.Menu(top_menu, tearoff=0)
        top_menu.add_cascade(label="TEST", menu=menu_TEST)
        
    #     menu_TEST.add_command(label="Các gói thầu đã lập", command=self.f_QLGT_GoiThauDaLap_click)
    #     menu_TEST.add_command(label="Tạo mới gói thầu", command=self.f_QLGT_TaoMoi_click)
    #     menu_TEST.add_command(label="Các gói thầu đã lập", command=self.f_QLGT_GoiThauDaLap_click)

    #     menu_TEST.add_separator()
    #     menu_TEST.add_command(label="Test |Phiếu Yêu cầu đặt hàng", command=self.f_test_tao_moi_YCDH_TALA_click)
    #     menu_TEST.add_command(label="Test |Nhật ký yêu cầu đặt hàng", command=self.f_test_nhat_ky_YCDH_TALA_click)
        
    #     menu_TEST.add_separator()
        menu_TEST.add_command(label="KD0101 |Quản lý gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
        menu_TEST.add_command(label="KD0102 |Tạo mới gói thầu", command=self.f_KD0101_QuanLyGoiThau_click)
        menu_TEST.add_separator()
    #     menu_TEST.add_command(label="Test tốt import, Export", command=self.f_test_tot_click)
    #     menu_TEST.add_command(label="CRUPP Khách hàng", command=self.f_KD_CRUDP_KhachHang_click)
        
        
        
        # Set font-size
        f_utils_set_menu_font(menu_TEST)
    
    # Define the action fuctions for home menu
    def f_Home_main_click(self):
        print("f_Home_main_click selected")
        self.f_open_DashBoard()
    
    # Define the action fuctions for AI-chatbot menu
    def f_AI_Chatbot_click(self):
        self.f_open_AI_chatbot()
        
    # Define the action fuctions for Kinh doanh home menu
    def f_Kinh_Doanh_Home_main_click(self):
        self.f_open_Kinh_Doanh_DashBoard()
        
    # Define the action fuctions for Vat tu home menu
    def f_Vat_Tu_Home_main_click(self):
        self.f_open_Vat_Tu_DashBoard()
        
    def f_Admin_Home_main_click(self):
        self.f_open_Admin_DashBoard()
    
    # Define the action fuctions for QLGT menu
    def f_QLGT_TaoMoi_click(self):
        print("f_QLGT_TaoMoi_click selected")
        self.f_open_KD01QuanLyGoiThauView()
        
    def f_KD0101_QuanLyGoiThau_click(self):
        print("f_QLGT_TaoMoi_click selected")
        self.f_open_KD0101_QuanLyGoiThau_View()
    
    # def f_test_tot_click(self):
    #     print("f_test_tot_click selected")
    #     self.f_open_f_test_tot_click_View()
    
    # def f_QLGT_GoiThauDaLap_click(self):
    #     print("f_QLGT_GoiThauDaLap_click selected")
    #     self.f_open_KD01_01QuanLyGoiThauView()
    
    # Define the action fuctions for QLYCDT menu
    def f_tao_moi_YCDH_click(self):
        self.f_open_tao_moi_YEU_CAU_DAT_HANG_View()
    
    def f_tao_moi_DeNghiXuatKho_click(self):
        self.f_open_tao_moi_DE_NGHI_XUAT_KHO_View()
    
    def f_tao_moi_KeHoachDatHang_click(self):
        self.f_open_tao_moi_KE_HOACH_DAT_HANG_View()
        
    
    def f_nhat_ky_YCDH_click(self):
        self.f_open_nhat_ky_YEU_CAU_DAT_HANG_View()
    
    def f_nhat_ky_DeNghiXuatKho_click(self):
        self.f_open_nhat_ky_DE_NGHI_XUAT_KHO_View()
    
    def f_nhat_ky_KeHoachDatHang_click(self):
        self.f_open_nhat_ky_KE_HOACH_DAT_HANG_View()
        
    def f_test_tao_moi_YCDH_TALA_click(self):
        self.f_open_testview()
        
    def f_HR01_click(self):
        print("f_HR01_click selected")
        self.f_open_HR01()
        
    def f_KD_CRUDP_KhachHang_click(self):
        print("f_KD_QuanLyKhachHang_click selected")
        self.f_open_KD0301_CRUDP_KhachHang_View()
        
    def f_test_nhat_ky_YCDH_TALA_click(self):
        self.f_open_tab_02_of_testview()
    
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
        from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View   # lazy import to avoid circular import
        self.parent.destroy()
        new_view = cls_Login_View()                             # Create an instance of the class
        new_view.dashboard = self.parent                        # Pass the reference of the dashboard to KD01 view
        f_utils_set_center_screen(new_view)                     # Center the new window on the screen
        new_view.focus_force()                                  # Ensure the new window is in focus
        
    # def f_open_KD02QuanLyYeuCauDatHangView(self):
    #     from app.views.KD02_QuanLyYeuCauDatHang_View.KD0201_PhieuYeuCauDatHang_View import cls_KD0201_PhieuYeuCauDatHang_View
    #     self.parent.destroy()
    #     new_view = cls_KD0201_PhieuYeuCauDatHang_View()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()

    def f_open_tao_moi_YEU_CAU_DAT_HANG_View(self):
        from app.views.KD0202_QuanLyYeuCauDatHang_View_250217_09h01.YEU_CAU_DAT_HANG_View import cls_YEU_CAU_DAT_HANG_View
        self.parent.destroy()
        new_view = cls_YEU_CAU_DAT_HANG_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
    
    def f_open_tao_moi_DE_NGHI_XUAT_KHO_View(self):
        from app.views.KD0301_QuanLyDeNghiXuatKho_View_250225_10h00.DE_NGHI_XUAT_KHO_View import cls_DE_NGHI_XUAT_KHO_View
        self.parent.destroy()
        new_view = cls_DE_NGHI_XUAT_KHO_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
    
    def f_open_tao_moi_KE_HOACH_DAT_HANG_View(self):
        from app.views.KD0201_QuanLyKeHoachDatHang_View_250225_11h40.KE_HOACH_DAT_HANG_View import cls_KE_HOACH_DAT_HANG_View
        self.parent.destroy()
        new_view = cls_KE_HOACH_DAT_HANG_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
    
    def f_open_nhat_ky_YEU_CAU_DAT_HANG_View(self):
        from app.views.KD0202_QuanLyYeuCauDatHang_View_250217_09h01.YEU_CAU_DAT_HANG_View import cls_YEU_CAU_DAT_HANG_View
        self.parent.destroy()
        new_view = cls_YEU_CAU_DAT_HANG_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        # Activate tab02
        try:
            tab_02 = f_utils_tim_component_with_name(new_view, "tab_02")
            new_view.notebook.select(tab_02)  # Ensure `notebook` exists in `new_view`
        except AttributeError:
            my_current_function = f_utils_get_current_function_name()
            print(f"Error at function: {my_current_function}")
    
    def f_open_nhat_ky_DE_NGHI_XUAT_KHO_View(self):
        from app.views.KD0301_QuanLyDeNghiXuatKho_View_250225_10h00.DE_NGHI_XUAT_KHO_View import cls_DE_NGHI_XUAT_KHO_View
        self.parent.destroy()
        new_view = cls_DE_NGHI_XUAT_KHO_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        # Activate tab02
        try:
            tab_02 = f_utils_tim_component_with_name(new_view, "tab_02")
            new_view.notebook.select(tab_02)  # Ensure `notebook` exists in `new_view`
        except AttributeError:
            my_current_function = f_utils_get_current_function_name()
            print(f"Error at function: {my_current_function}")
    
    def f_open_nhat_ky_KE_HOACH_DAT_HANG_View(self):
        from app.views.KD0201_QuanLyKeHoachDatHang_View_250225_11h40.KE_HOACH_DAT_HANG_View import cls_KE_HOACH_DAT_HANG_View
        self.parent.destroy()
        new_view = cls_KE_HOACH_DAT_HANG_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        # Activate tab02
        try:
            tab_02 = f_utils_tim_component_with_name(new_view, "tab_02")
            new_view.notebook.select(tab_02)  # Ensure `notebook` exists in `new_view`
        except AttributeError:
            my_current_function = f_utils_get_current_function_name()
            print(f"Error at function: {my_current_function}")
    
    # def f_open_testview(self):
    #     from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
    #     self.parent.destroy()
    #     new_view = cls_test_View()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
    
    # def f_open_tab_02_of_testview(self):
    #     from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
    #     self.parent.destroy()
    #     new_view = cls_test_View()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
    #     # Activate tab02
    #     try:
    #         tab_02 = f_utils_tim_component_with_name(new_view, "tab_02")
    #         new_view.notebook.select(tab_02)  # Ensure `notebook` exists in `new_view`
    #     except AttributeError:
    #         my_current_function = f_utils_get_current_function_name()
    #         print(f"Error at function: {my_current_function}")
            
    def f_open_HR01(self):
        from app.views.HR01_FORM_VIEW.set_margins import cls_hr01_view
        self.parent.destroy()
        new_view = cls_hr01_view()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
    
    # def f_open_KD0301_CRUDP_KhachHang_View(self):
    #     from app.views.KD03_QuanLyKhachHang_View.KD0301_CRUDP_KhachHang_View import cls_KD0301_CRUDP_KhachHang_View
    #     self.parent.destroy()
    #     new_view = cls_KD0301_CRUDP_KhachHang_View()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
    
    # def f_open_KD01_01QuanLyGoiThauView(self):
    #     from app.views.KD01_QuanLyGoiThau_TEST_02.KD01_01QuanLyGoiThauView import cls_View
    #     self.parent.destroy()
    #     new_view = cls_View()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
        
    
    # def f_open_KD01QuanLyGoiThauView(self):
    #     from app.views.KD01_QuanLyGoiThau_TEST_01.KD01QuanLyGoiThauView import cls_KD01QuanLyGoiThauView
    #     self.parent.destroy()
    #     new_view = cls_KD01QuanLyGoiThauView()
    #     new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
        
        
    def f_open_KD0101_QuanLyGoiThau_View(self):
        from app.views.KD01_QuanLyGoiThau_View.KD0101_QuanLyGoiThau_View import cls_KD0101_QuanLyGoiThau_View
        self.parent.destroy()
        new_view = cls_KD0101_QuanLyGoiThau_View()
        new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    # def f_open_f_test_tot_click_View(self):
    #     from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
    #     self.parent.destroy()
    #     new_view = cls_test_View()
    #     # new_view.dashboard = self.parent
    #     utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
    #     f_utils_set_center_screen(new_view)
    #     new_view.focus_force()
        
    def f_open_cls_VT0101_DonDatHang_View(self):
        from app.views.VT01_QuanLyDonDatHang_View.VT0101_DonDatHang_View import cls_VT0101_DonDatHang_View
        self.parent.destroy()
        new_view = cls_VT0101_DonDatHang_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
        
    def f_open_cls_VT0102_DonDatHang_TM_View(self):
        from app.views.VT01_QuanLyDonDatHang_View.VT0102_DonDatHang_TM_View import cls_VT0102_DonDatHang_TM_View
        self.parent.destroy()
        new_view = cls_VT0102_DonDatHang_TM_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        

    def f_open_UserInfo(self):
        from AD00_User_Management_View.AD0003_UserInfo_View import cls_user_info
        self.parent.destroy()
        new_view = cls_user_info()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    
    def f_open_DashBoard(self):
        self.parent.destroy()
        f_utils_open_dashboard_main()
        
    def f_open_AI_chatbot(self):
        f_utils_open_AI_chatbot()
        
    def f_open_Kinh_Doanh_DashBoard(self):
        self.parent.destroy()
        f_utils_open_dashboard_kinh_doanh()
        
    def f_open_Vat_Tu_DashBoard(self):
        self.parent.destroy()
        f_utils_open_dashboard_vat_tu()
    
    def f_open_Admin_DashBoard(self):
        self.parent.destroy()
        f_utils_open_dashboard_admin()
        
    def f_destroy_current_window(self):
        self.parent.destroy()
        