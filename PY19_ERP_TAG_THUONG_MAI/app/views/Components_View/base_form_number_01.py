import tkinter as tk
from Components_View import *
from utils import *
from utils.define import *

class cls_base_form_number_01(tk.Tk):
    def __init__(self, title_of_form="Default Title", name_of_slip="Default Name"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        self.name_of_slip = name_of_slip
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
            # cls_menu_top(self, self)
            
            frame_main = cls_Frame_Main(self)
            frame_main.grid(row=0, column=0, sticky="nsew")
            
            # Configure grid weights for resizing
            self._configure_grid_weights()

            Frame_Header = cls_Frame_Header(frame_main, name_of_slip=self.name_of_slip)
            Frame_Header.grid(row=0, column=0, sticky="ew")
            
            Frame_Footer = cls_Frame_Footer(frame_main)
            Frame_Footer.grid(row=2, column=0, sticky="ew")
            
            Frame_Body = cls_Frame_Body(frame_main)
            Frame_Body.grid(row=1, column=0, sticky="nsew")
        except Exception as e:
            print(f"Error initializing components: {e}")
    
    def _configure_grid_weights(self):
        """Configures grid weights for resizing."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Ensure proper layout for the main frame
        frame_main = self.children.get('!cls_frame_main', None)
        if frame_main:
            frame_main.rowconfigure(0, weight=0)  # Header
            frame_main.rowconfigure(1, weight=1)  # Body
            frame_main.rowconfigure(2, weight=0)  # Footer
            frame_main.columnconfigure(0, weight=1)
            
    def _close_window_Click(self):
        self.destroy()
        from views.AD01_Dashboard_View.Dashboard_View import cls_Dashboard_View
        cls_Dashboard_View()