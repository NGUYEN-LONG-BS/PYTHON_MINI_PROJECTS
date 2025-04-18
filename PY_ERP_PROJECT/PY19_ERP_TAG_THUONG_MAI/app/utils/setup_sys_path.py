import os
import sys

def f_utils_setup_sys_path():
    """
    Thiết lập lại sys.path để Python có thể tìm thấy các module trong thư mục `app`.
    """
    # Lấy đường dẫn của file hiện tại
    base_dir = os.path.dirname(__file__)
    # Thêm đường dẫn tới thư mục app vào sys.path
    app_path = os.path.join(base_dir, 'app')
    if app_path not in sys.path:
        sys.path.append(app_path)
    # Thêm đường dẫn tới thư mục views trong app
    views_path = os.path.join(app_path, 'views')
    if views_path not in sys.path:
        sys.path.append(views_path)
        
    # Thêm đường dẫn tới thư mục controllers trong app
    controllers_path = os.path.join(app_path, 'controllers')
    if controllers_path not in sys.path:
        sys.path.append(controllers_path)
        
    # Thêm đường dẫn tới thư mục models trong app
    models_path = os.path.join(app_path, 'models')
    if models_path not in sys.path:
        sys.path.append(models_path)
        
    # Thêm đường dẫn tới thư mục services trong app
    services_path = os.path.join(app_path, 'services')
    if services_path not in sys.path:
        sys.path.append(services_path)
        
    # Thêm đường dẫn tới thư mục utils trong app
    utils_path = os.path.join(app_path, 'utils')
    if utils_path not in sys.path:
        sys.path.append(utils_path)
    
    # Thêm đường dẫn tới thư mục assets vào sys.path
    assets_path = os.path.join(base_dir, 'assets')
    if assets_path not in sys.path:
        sys.path.append(assets_path)
        
    # Thêm đường dẫn tới thư mục icons trong app
    icons_path = os.path.join(assets_path, 'icons')
    if icons_path not in sys.path:
        sys.path.append(icons_path)
        
    # Thêm đường dẫn tới thư mục img trong app
    img_path = os.path.join(assets_path, 'img')
    if img_path not in sys.path:
        sys.path.append(img_path)