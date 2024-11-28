import os
import sys

def setup_sys_path():
    """
    Thiết lập lại sys.path để Python có thể tìm thấy các module trong thư mục `app`.
    """
    base_dir = os.path.dirname(__file__)
    # Thêm đường dẫn tới thư mục app vào sys.path
    app_path = os.path.join(base_dir, 'app')
    if app_path not in sys.path:
        sys.path.append(app_path)
    # Thêm đường dẫn tới thư mục views trong app
    views_path = os.path.join(app_path, 'views')
    if views_path not in sys.path:
        sys.path.append(views_path)

def main():
    """
    Chạy ứng dụng và render dashboard.
    """
    setup_sys_path()  # Thiết lập đường dẫn
    # Import hàm render_dashboard từ DashboardView_Iherit_Component trong views
    from app.views.DashboardView_Iherit_Component import render_dashboard
    # Gọi hàm render_dashboard để hiển thị dashboard
    render_dashboard()

if __name__ == "__main__":
    main()