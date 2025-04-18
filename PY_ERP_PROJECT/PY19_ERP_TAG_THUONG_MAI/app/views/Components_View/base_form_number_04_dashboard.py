import tkinter as tk
from app.utils import *
from . import menu_top
from . import frame

class cls_base_form_number_04_dashboard(tk.Tk):
    def __init__(self, title_of_form="Default Title", name_of_slip="Default Name"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        # Set up window initial properties
        self.name_of_slip = name_of_slip
        self.title_of_form = title_of_form
        self.title(self.title_of_form)
        # Set up favicon and window configuration
        self.f_Thiet_lap_Kich_thuoc_Cua_So()
        # Set up reusable components
        self.f_Goi_Cac_Thanh_Phan_Tai_Su_Dung()
        self.f_setup_all_events()
    
    def f_setup_all_events(self):
        # Bind close event
        parent_window = self.winfo_toplevel()
        parent_window.protocol("WM_DELETE_WINDOW", self._close_window_Click)
        
    def f_Thiet_lap_Kich_thuoc_Cua_So(self):
        """Configures window size and position."""
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(self, maximize=True)
        f_utils_set_center_screen(self)
        try:
            f_utils_setup_fav_icon(self)
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
    
    def f_Goi_Cac_Thanh_Phan_Tai_Su_Dung(self):
        """Initializes reusable components."""
        try:
            # Add cls_menu_top
            menu_top.cls_menu_top(self)
            
            # Add cls_Frame_Main
            frame_main = frame.cls_Frame_Main(self)
            frame_main.grid(row=0, column=0, sticky="nsew")
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()
            # Add elements to frame_main
            Frame_Header = frame.cls_Frame_Header(frame_main, name_of_slip=self.name_of_slip)
            Frame_Header.grid(row=0, column=0, sticky="ew")

            self.Frame_Body = frame.cls_Frame_Body(frame_main)
            self.Frame_Body.grid(row=1, column=0, sticky="nsew")
            
            Frame_Footer = frame.cls_Frame_Footer(frame_main)
            Frame_Footer.grid(row=2, column=0, sticky="ew")
            
            # Add elements to frame_body
            self.f_add_elements_to_frame_body()
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
    
    def _configure_grid_weights_of_self(self):
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
        f_utils_open_dashboard_main()
    
    def f_add_elements_to_frame_body(self):
        print("f_add_elements_to_frame_body")