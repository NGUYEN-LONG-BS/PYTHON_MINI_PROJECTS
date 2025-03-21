import os
import sys
import traceback
from tkinter import messagebox
import tkinter as tk
import time

class cls_App:
    def __init__(self):
        # Khởi tạo các cấu hình cần thiết, bao gồm thiết lập sys.path
        self.f_setup_sys_path()

    def f_setup_sys_path(self):
        """
        Thiết lập lại sys.path để Python có thể tìm thấy các module trong thư mục `app`.
        """
        try:
            # Lấy đường dẫn của file hiện tại
            base_dir = os.path.dirname(__file__)
            # Thêm đường dẫn tới thư mục app vào sys.path
            app_path = os.path.join(base_dir, 'app')
            if app_path not in sys.path:
                sys.path.append(app_path)
            
            # Thêm các thư mục con của app vào sys.path
            app_subdirectories = ['views', 'controllers', 'models', 'services', 'utils']
            for subdir in app_subdirectories:
                subdir_path = os.path.join(app_path, subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)
            
            # Thêm các thư mục con của viewsad,
            app_views_subdirectories = ['Components_View',
                                        'AD00_User_Management_View',
                                        'AD01_Dashboard_View',
                                        'AD02_SETTINGS_View',
                                        'KD01_QuanLyGoiThau_View', 'KD01_QuanLyGoiThau_TEST_01', 'KD01_QuanLyGoiThau_TEST_02',
                                        'KD02_QuanLyYeuCauDatHang_View','KD02_QuanLyYeuCauDatHang_TEST_01',
                                        'KD03_QuanLyKhachHang_View'
                                        ]
            for subdir in app_views_subdirectories:
                subdir_path = os.path.join(app_path, "views", subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)
                    
            # Thêm các thư mục con của controllers
            app_controllers_subdirectories = ['KD01_QuanLyGoiThau', 'KD0101_QuanLyGoiThau_Controller',
                                            'KD02_QuanLyYeuCauDatHang_Controller', 'KD02_QuanLyYeuCauDatHang',
                                            'KD03_QuanLyKhachHang_Controller'
                                            ]
            for subdir in app_controllers_subdirectories:
                subdir_path = os.path.join(app_path, "controllers", subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)
                    
            # Thêm các thư mục con của models
            app_models_subdirectories = ['KD01_QuanLyGoiThau','KD02_QuanLyYeuCauDatHang',
                                        'KD0101_QuanLyGoiThau_Model',
                                        'KD02_QuanLyYeuCauDatHang_Model',
                                        'KD03_QuanLyKhachHang_Model'
                                        ]
            for subdir in app_models_subdirectories:
                subdir_path = os.path.join(app_path, "models", subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)

            # Thêm đường dẫn tới thư mục assets vào sys.path (nếu cần thiết)
            assets_path = os.path.join(base_dir, 'assets')
            if assets_path not in sys.path:
                sys.path.append(assets_path)

            # Thêm các thư mục con của assets vào sys.path
            assets_subdirectories = ['icons', 'img', 'styles', 'templates']
            for subdir in assets_subdirectories:
                subdir_path = os.path.join(assets_path, subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)

            # # Hiển thị tất cả đường dẫn trong sys.path
            # print(sys.path)
        except Exception as e:
            self.handle_error(e)

    def run(self):
        """Chạy ứng dụng và render dashboard."""
        try:
            # Import đối tượng cls_LoginView
            from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View
            # Gọi cửa sổ LoginView
            login_window = cls_Login_View()
            login_window.mainloop()
        except Exception as e:
            self.handle_error(e)
        
    def handle_error(self, e):
        """Xử lý lỗi và hiển thị thông báo"""
        error_msg = traceback.format_exc()
        print("Lỗi ứng dụng:", error_msg)

        # Ghi lỗi vào file log
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_msg)

        # Hiển thị lỗi trong Tkinter nếu có giao diện GUI
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Lỗi Ứng Dụng", f"Đã xảy ra lỗi:\n\n{error_msg}")

        input("Nhấn Enter để thoát...")  # Giữ console mở

# Main function to run the program
if __name__ == "__main__":
    try:    
        # Khởi tạo đối tượng của class App và chạy ứng dụng
        app = cls_App()
        app.run()
    except Exception as e:
        error_msg = traceback.format_exc()
        print("Lỗi ngoài:", error_msg)
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_msg)
        input("Nhấn Enter để thoát...")


    