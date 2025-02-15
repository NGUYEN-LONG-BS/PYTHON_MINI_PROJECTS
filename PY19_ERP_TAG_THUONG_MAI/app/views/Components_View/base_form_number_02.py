import tkinter as tk
from tkinter import ttk
from Components_View import *
from Components_View.menu_top import cls_menu_top
from utils import *
from utils.define import *

class cls_base_form_number_02_ManyTabs(tk.Tk):
    def __init__(self, title_of_form="Default Title", name_of_slip="Default Name"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        # Set up window initial properties
        self.name_of_slip = name_of_slip
        self.title_of_form = title_of_form
        self.title(self.title_of_form)
        # Set up favicon and window configuration
        self.f_Thiet_lap_Kich_thuoc_Cua_So()
        # Set up reusable components
        f_utils_set_style(self)
        self.f_Goi_Cac_Thanh_Phan_Tai_Su_Dung()
        self.f_setup_all_events()
    
    def f_setup_all_events(self):
        # Bind close event
        parent_window = self.winfo_toplevel()
        parent_window.protocol("WM_DELETE_WINDOW", self._close_window_Click)
        
    def f_Thiet_lap_Kich_thuoc_Cua_So(self):
        """Configures window size and position."""
        f_utils_set_window_size_of_new_view(self, maximize=True)
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
            # Add cls_Frame_Main
            frame_main = cls_Frame_Main(self)
            frame_main.grid(row=0, column=0, sticky="nsew")
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()
            # Add elements to frame_main
            Frame_Header = cls_Frame_Header(frame_main, name_of_slip=self.name_of_slip)
            Frame_Header.grid(row=0, column=0, sticky="ew")
            
            Frame_Footer = cls_Frame_Footer(frame_main)
            Frame_Footer.grid(row=2, column=0, sticky="ew")
            
            self.Frame_Body = cls_Frame_Body(frame_main)
            self.Frame_Body.grid(row=1, column=0, sticky="nsew")
            
            # Add elements to frame_body
            self.f_add_elements_to_frame_body()
            
        except Exception as e:
            print(f"Error initializing components: {e}")
    
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
        parent_frame = self.Frame_Body
        # Create a notebook (tabs)
        self.notebook = ttk.Notebook(parent_frame)
        self.notebook.pack(fill="both", expand=True)
        # self.notebook.pack(fill="x", expand=True)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.tab1, text="Tab-00")
        self.notebook.add(self.tab2, text="Tab-01")
        self.notebook.add(self.tab3, text="Tab-02")