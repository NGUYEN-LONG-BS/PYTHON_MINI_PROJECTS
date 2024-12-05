import tkinter as tk

def set_window_size(root, width=1600, height=900):
    # Thiết lập kích thước cửa sổ
    root.geometry(f"{width}x{height}")
    
    # Đảm bảo cửa sổ không thể thay đổi kích thước
    # root.resizable(False, False)
    root.resizable(True, True)
    
    # Nếu bạn muốn căn giữa cửa sổ, bạn có thể tính toán vị trí và đặt lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')
