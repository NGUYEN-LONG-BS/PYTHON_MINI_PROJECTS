import os
import sys
import traceback
from tkinter import messagebox
import tkinter as tk
import time

class cls_App:
    
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


    