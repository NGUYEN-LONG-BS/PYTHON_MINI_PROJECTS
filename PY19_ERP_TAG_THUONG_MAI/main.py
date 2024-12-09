# Project/main.py
import os
import sys

def f_setup_sys_path():
    """
    Thiết lập lại sys.path để Python có thể tìm thấy các module trong thư mục `app`.
    """
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
    
    # Thêm các thư mục con của views
    app_views_subdirectories = ['components', 'dashboard', 'KD0101_QuanLyGoiThau_View', 'KD01_QuanLyGoiThau', 
                                'KD01_QuanLyGoiThau_New', 'KD02_QuanLyYeuCauDatHang', 
                                'settings', 'user_management']
    for subdir in app_views_subdirectories:
        subdir_path = os.path.join(app_path, "views", subdir)
        if subdir_path not in sys.path:
            sys.path.append(subdir_path)
            
    # Thêm các thư mục con của controllers
    app_controllers_subdirectories = ['KD0101_QuanLyGoiThau_View']
    for subdir in app_controllers_subdirectories:
        subdir_path = os.path.join(app_path, "controllers", subdir)
        if subdir_path not in sys.path:
            sys.path.append(subdir_path)
            
    # Thêm các thư mục con của models
    app_models_subdirectories = ['KD0101_QuanLyGoiThau_Model']
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

    # print(sys.path)

def f_main():
    """
    Chạy ứng dụng và render dashboard.
    """
    # Thiết lập các đường dẫn
    f_setup_sys_path()
    
    # Import đối tượng cls_LoginView
    from app.views.user_management.loginView import cls_LoginView

    # Gọi cửa sổ LoginView
    login_window = cls_LoginView()
    # Start the Tkinter event loop
    login_window.mainloop()

# Main function to run the program
if __name__ == "__main__":
    f_main()