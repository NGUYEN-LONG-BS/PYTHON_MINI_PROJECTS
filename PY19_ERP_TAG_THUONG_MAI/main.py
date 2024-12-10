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
    
    # Thêm các thư mục con của app vào sys.path
    app_views_subdirectories = ['components', 'dashboard', 'KD01_QuanLyGoiThau', 'KD01_QuanLyGoiThau_New', 'KD02_QuanLyYeuCauDatHang', 'settings', 'user_management']
    for subdir in app_views_subdirectories:
        subdir_path = os.path.join(app_path, "views", subdir)
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
    f_setup_sys_path()  # Thiết lập đường dẫn
    
    # Import hàm render_dashboard từ DashboardView_Iherit_Component trong views
    from app.views.dashboard.DashboardView import f_render_dashboard

    # Gọi hàm render_dashboard để hiển thị dashboard
    f_render_dashboard()

if __name__ == "__main__":
    f_main()