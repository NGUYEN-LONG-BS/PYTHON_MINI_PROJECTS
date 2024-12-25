import tkinter as tk
from tkinter import ttk
from Components_View import *
from Components_View.menu_top import cls_menu_top
from utils import *
from utils.define import *
import datetime

class cls_base_form_number_03_DashBoard(tk.Tk):
    def __init__(self, title_of_form="Default Title"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        self.title_of_form = title_of_form
        self.title(self.title_of_form)
        
        f_utils_setup_fav_icon(self)
        
        # Set up favicon and window configuration
        self.f_Thiet_lap_Kich_thuoc_Cua_So()
        
        # Set up reusable components
        self.f_Goi_Cac_Thanh_Phan_Tai_Su_Dung()
        
        # Bind close event
        parent_window = self.winfo_toplevel()
        parent_window.protocol("WM_DELETE_WINDOW", self._close_window_Click)
        
        
    def f_Thiet_lap_Kich_thuoc_Cua_So(self):
        """Configures window size and position."""
        f_utils_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_utils_set_center_screen(self)
        try:
            f_utils_setup_fav_icon(self)
        except Exception as e:
            print(f"Error setting up favicon: {e}")
    
    def f_Goi_Cac_Thanh_Phan_Tai_Su_Dung(self):
        """Initializes reusable components."""
        try:
            # Add cls_menu_top
            cls_menu_top(self)

            self.frame_main = cls_Frame_Main(self)
            self.frame_main.grid(row=0, column=0, sticky="nsew")
            
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()
            
            # Add elements to frame_info_of_slip
            self.f_add_elements_to_frame_main()
            
        except Exception as e:
            print(f"Error initializing components: {e}")
    
    def _configure_grid_weights_of_self(self):
        """Configures grid weights for resizing."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Ensure proper layout for the main frame
        frame_main = self.children.get('!cls_frame_main', None)
        if frame_main:
            frame_main.rowconfigure(0, weight=1)
            frame_main.columnconfigure(0, weight=1)
            
    def _close_window_Click(self):
        self.destroy()
        from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View
        # Gọi cửa sổ LoginView
        login_window = cls_Login_View()
        login_window.mainloop()
    
    def f_add_elements_to_frame_main(self):
        # Create 3 Frame
        self.frame_left_body = tk.Frame(self.frame_main, bg="yellow")
        self.frame_middle_body = tk.Frame(self.frame_main, bg="white")
        self.frame_right_body = tk.Frame(self.frame_main, bg="green")
        # Pack frames
        self.frame_left_body.pack(side="left", fill="both", expand=True)
        self.frame_middle_body.pack(side="left", fill="both", expand=True)
        self.frame_right_body.pack(side="left", fill="both", expand=True)
        # Bind hover events
        self.frame_left_body.bind("<Enter>", lambda event: self._frame_left_body_Hover())
        self.frame_middle_body.bind("<Enter>", lambda event: self._frame_middle_body_Hover())
        self.frame_right_body.bind("<Enter>", lambda event: self._frame_right_body_Hover())
        
    def _frame_left_body_Hover(self):
        total_width = self.frame_main.winfo_width()
        left_width = 200
        right_width = 10
        middle_width = total_width - left_width - right_width
        self._animate_frame_width(self.frame_left_body, left_width)
        self._animate_frame_width(self.frame_middle_body, middle_width)
        self._animate_frame_width(self.frame_right_body, right_width)

    def _frame_middle_body_Hover(self):
        total_width = self.frame_main.winfo_width()
        left_width = 10
        right_width = 10
        middle_width = total_width - left_width - right_width
        self._animate_frame_width(self.frame_left_body, left_width)
        self._animate_frame_width(self.frame_middle_body, middle_width)
        self._animate_frame_width(self.frame_right_body, right_width)

    def _frame_right_body_Hover(self):
        total_width = self.frame_main.winfo_width()
        left_width = 10
        right_width = 200
        middle_width = total_width - left_width - right_width
        self._animate_frame_width(self.frame_left_body, left_width)
        self._animate_frame_width(self.frame_middle_body, middle_width)
        self._animate_frame_width(self.frame_right_body, right_width)

    def _animate_frame_width(self, frame, target_width, step=2):
        current_width = frame.winfo_width()
        if current_width < target_width:
            new_width = min(current_width + step, target_width)
        elif current_width > target_width:
            new_width = max(current_width - step, target_width)
        else:
            return  # Animation complete

        frame.config(width=new_width)
        self.after(2, self._animate_frame_width, frame, target_width, step)