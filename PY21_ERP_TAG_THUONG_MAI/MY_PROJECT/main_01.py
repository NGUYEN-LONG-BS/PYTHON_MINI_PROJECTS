import os
import sys
import traceback
import tkinter as tk
from tkinter import messagebox, ttk

class cls_SplashScreen(tk.Toplevel):
    def __init__(self, master=None, duration=3000):  # Thời gian hiển thị (3 giây)
        super().__init__(master)
        self.master = master
        self.duration = duration

        # Xóa viền cửa sổ
        self.overrideredirect(True)

        # Làm cửa sổ trong suốt
        self.attributes('-alpha', 0.0)

        # Căn giữa cửa sổ splash
        self.f_center_window(300, 50)

        # Thanh tiến trình quay
        self.progress = ttk.Progressbar(self, mode="indeterminate", length=250)
        self.progress.pack(expand=True)

        # Hiệu ứng mờ dần vào
        self.fade_in(0)

        # Đóng splash screen sau thời gian quy định
        self.after(self.duration, self.fade_out)

        # Bắt đầu vòng tròn quay
        self.progress.start(10)

    def f_center_window(self, width, height):
        """Căn giữa cửa sổ splash trên màn hình"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def fade_in(self, alpha):
        """Hiệu ứng xuất hiện dần"""
        if alpha < 1.0:
            self.attributes('-alpha', alpha)
            self.after(50, lambda: self.fade_in(alpha + 0.1))  

    def fade_out(self):
        """Hiệu ứng biến mất dần"""
        alpha = self.attributes('-alpha')
        if alpha > 0.0:
            self.attributes('-alpha', alpha - 0.1)
            self.after(50, self.fade_out)  
        else:
            self.destroy()  


class cls_App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Ẩn cửa sổ chính ban đầu
        self.image_cache = []  # Giữ hình ảnh trong bộ nhớ
        self.f_setup_sys_path()

    def f_setup_sys_path(self):
        """Thiết lập sys.path để Python có thể tìm thấy các module trong thư mục `app`."""
        try:
            base_dir = os.path.dirname(__file__)
            app_path = os.path.join(base_dir, 'app')
            if app_path not in sys.path:
                sys.path.append(app_path)

            # Thêm các thư mục con vào sys.path
            app_subdirectories = ['views', 'controllers', 'models', 'services', 'utils']
            for subdir in app_subdirectories:
                subdir_path = os.path.join(app_path, subdir)
                if subdir_path not in sys.path:
                    sys.path.append(subdir_path)

        except Exception as e:
            self.handle_error(e)

    def run(self):
        """Chạy ứng dụng với màn hình chờ trước khi hiển thị cửa sổ đăng nhập."""
        try:
            splash = cls_SplashScreen(self.root, duration=3000)  
            self.root.update()  

            # Chờ 3 giây rồi mở cửa sổ đăng nhập
            self.root.after(3000, self.f_show_login_window)

            self.root.mainloop()  
        except Exception as e:
            self.handle_error(e)

    def f_show_login_window(self):
        """Hiển thị cửa sổ đăng nhập sau màn hình chờ."""
        from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View
        login_window = cls_Login_View()
        login_window.image_cache = self.image_cache  # Giữ ảnh trong bộ nhớ
        login_window.mainloop()

    def handle_error(self, e):
        """Xử lý lỗi và hiển thị thông báo"""
        error_msg = traceback.format_exc()
        print("Lỗi ứng dụng:", error_msg)

        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_msg)

        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Lỗi Ứng Dụng", f"Đã xảy ra lỗi:\n\n{error_msg}")

        input("Nhấn Enter để thoát...")  


if __name__ == "__main__":
    try:
        app = cls_App()
        app.run()
    except Exception as e:
        error_msg = traceback.format_exc()
        print("Lỗi ngoài:", error_msg)
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_msg)
        input("Nhấn Enter để thoát...")
