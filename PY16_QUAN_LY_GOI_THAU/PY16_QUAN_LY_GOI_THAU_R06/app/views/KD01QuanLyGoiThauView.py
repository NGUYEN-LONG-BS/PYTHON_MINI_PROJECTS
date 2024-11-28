# Project/Views/KD01QuanLyGoiThauView.py
import tkinter as tk
from tkinter import ttk
from PIL import Image
from datetime import datetime
from app.controllers.KD01QuanLyGoiThauController import KD01QuanLyGoiThauController
from utils import *
from components.user_Info import setup_employee_info_labels  # Import the function
from components.logo import setup_logo  # Import the setup_logo function

class KD01QuanLyGoiThauView(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize controller
        self.controller = KD01QuanLyGoiThauController()

        # Setup window
        set_window_size(self)
        self.title("QUẢN LÝ GÓI THẦU")

        # Create a container frame to hold both the logo frame and user info frame
        frame_container = tk.Frame(self)
        frame_container.pack(side='top', padx=10, pady=10)

        # Setup the logo in the Frame_logo using the imported function
        Frame_logo = tk.Frame(frame_container, width=100, height=100)
        Frame_logo.pack(side='left', padx=10)  # Pack the logo frame on the left side with some padding
        setup_logo(Frame_logo)  # Pass the frame as the parent for the logo

        # Setup the logo in the Frame_logo using the imported function
        Frame_user_info = tk.Frame(frame_container, width=900, height=100)
        Frame_user_info.pack(side='left', padx=10)  # Pack the user info frame to the left with padding
        setup_employee_info_labels(Frame_user_info)  # Call the function to add employee info labels
        
        self.setup_title_h1()
        self.setup_labels()
        self.setup_combobox_nam_goi_thau()
        self.setup_entries()
        self.setup_btn_tao_thu_muc_moi()
        self.setup_scrollable_frame()
        self.setup_btn_show_dashboard()

        self.dashboard = None  # Placeholder for Dashboard window

        # Bind close event
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    # Employee Info Labels
    def setup_employee_info_labels(self):
        tk.Label(self, text="ID: TBD001", font=("Arial", 13)).place(x=115, y=10)
        tk.Label(self, text="Họ tên: Nguyễn Văn B", font=("Arial", 13)).place(x=200, y=10)
        tk.Label(self, text="Bộ phận: Kinh doanh", font=("Arial", 13)).place(x=370, y=10)
        tk.Label(self, text="Cấp bậc: Nhân viên", font=("Arial", 13)).place(x=550, y=10)
        tk.Label(self, text="Cty: Thiết bị điện", font=("Arial", 13)).place(x=750, y=10)

    # Header Title
    def setup_title_h1(self):
        title_label = tk.Label(self, text="TẠO FOLDER QUẢN LÝ GÓI THẦU MỚI", font=("Arial", 25))
        title_label.place(relx=0.2, rely=0.1)

    # Static Labels
    def setup_labels(self):
        tk.Label(self, text="Số thông báo mời thầu", font=("Arial", 18)).place(x=50, y=200)
        tk.Label(self, text="Năm gói thầu", font=("Arial", 18)).place(x=50, y=130)
        tk.Label(self, text="Danh sách gói thầu", font=("Arial", 18)).place(x=50, y=300)

        self.folder_name_label = tk.Label(self, text="24_GOI_THAU_0000_0000", font=("Arial", 18))
        self.folder_name_label.place(x=390, y=230)

    # Combobox for Year
    def setup_combobox_nam_goi_thau(self):
        current_year = datetime.now().year
        year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

        self.year_combobox = ttk.Combobox(self, values=year_array)
        self.year_combobox.set(str(current_year))  # Default to current year
        self.year_combobox.place(x=50, y=160)
        self.year_combobox.bind("<<ComboboxSelected>>", self.on_combobox_nam_goi_thau_change)

    # Entry for notification number
    def setup_entries(self):
        self.notification_entry = tk.Entry(self, width=30)
        self.notification_entry.place(x=50, y=230)
        self.notification_entry.bind("<KeyRelease>", self.on_entry_change)

    # Button to create folder
    def setup_btn_tao_thu_muc_moi(self):
        def btn_tao_thu_muc_moi_click():
            folder_name = self.folder_name_label.cget("text")
            self.controller.create_folder(folder_name)

        create_folder_btn = tk.Button(self, text="Tạo thư mục mới", command=btn_tao_thu_muc_moi_click)
        create_folder_btn.place(x=50, y=700)

    # Button to show Dashboard
    def setup_btn_show_dashboard(self):
        def btn_show_dashboard_click():
            if self.dashboard:
                self.dashboard.deiconify()
                self.destroy()  # Close the current view
            else:
                print("Dashboard window not initialized yet.")

        show_dashboard_btn = tk.Button(self, text="Show Dashboard", command=btn_show_dashboard_click)
        show_dashboard_btn.place(x=250, y=700)

    # Scrollable frame for folder contents
    def setup_scrollable_frame(self):
        self.scrollable_frame = tk.Frame(self, width=800, height=200)
        self.scrollable_frame.place(x=50, y=330)

        canvas = tk.Canvas(self.scrollable_frame)
        scrollbar = tk.Scrollbar(self.scrollable_frame, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def refresh_scrollable_frame():
            # Simulate directory contents
            directory_contents = [f"Folder {i}" for i in range(1, 21)]
            for widget in frame.winfo_children():
                widget.destroy()
            for item in directory_contents:
                label = tk.Label(frame, text=item, font=("Arial", 14))
                label.pack(anchor="w")

        refresh_scrollable_frame()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # Combobox change handler
    def on_combobox_nam_goi_thau_change(self, event):
        self.update_folder_name()

    # Entry change handler
    def on_entry_change(self, event):
        self.update_folder_name()

    # Update folder name
    def update_folder_name(self):
        selected_year = self.year_combobox.get()
        year_suffix = selected_year[-2:]

        notification_number = self.notification_entry.get().zfill(4)

        folder_name = f"{year_suffix}_GOI_THAU_0000_{notification_number}"

        self.folder_name_label.configure(text=folder_name)

    # Close event handler
    def on_close(self):
        if self.dashboard:
            self.dashboard.deiconify()
        self.destroy()  # Close the current view

    # Run main event loop
    def main(self):
        self.mainloop()


# To run the view
if __name__ == "__main__":
    view = KD01QuanLyGoiThauView()
    view.main()