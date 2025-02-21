import tkinter as tk
from Components_View import *
from Components_View.menu_top import cls_menu_top
from utils import *
from utils.define import *
import datetime

class cls_base_form_number_01_EntryForm(tk.Tk):
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
            cls_menu_top(self)

            frame_main = cls_Frame_Main(self)
            frame_main.grid(row=0, column=0, sticky="nsew")
            
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()

            Frame_Header = cls_Frame_Header(frame_main, name_of_slip=self.name_of_slip)
            Frame_Header.grid(row=0, column=0, sticky="ew")
            
            Frame_Footer = cls_Frame_Footer(frame_main)
            Frame_Footer.grid(row=2, column=0, sticky="ew")
            
            self.Frame_Body = cls_Frame_Body(frame_main)
            self.Frame_Body.grid(row=1, column=0, sticky="nsew")
            
            # Add elements to frame_info_of_slip
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
        # Add Frame_Info_of_Slip at the top
        self.frame_info_of_slip = tk.Frame(self.Frame_Body, bg="lightblue")
        self.frame_info_of_slip.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Add Frame_Treeview
        self.frame_treeview = tk.Frame(self.Frame_Body, bg="white")
        self.frame_treeview.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        # Add Frame_Button
        self.frame_button = tk.Frame(self.Frame_Body, bg="gray")
        self.frame_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        
        # Configure internal rows and columns in Frame_Body
        self.Frame_Body.rowconfigure(0, weight=0)  # Info of Slip
        self.Frame_Body.rowconfigure(1, weight=1)  # Treeview (expandable)
        self.Frame_Body.rowconfigure(2, weight=0)  # Button
        self.Frame_Body.columnconfigure(0, weight=1)
        
        # Add elements to frame_info_of_slip
        self.f_add_elements_to_frame_info_of_slip()
        # Add elements to frame_button
        self.f_add_elements_to_frame_button()
    
    def f_add_elements_to_frame_info_of_slip(self):
        from Components_View import cls_my_text_entry_num_01
        
        # Get today's date in the format dd/mm/yyyy
        today = datetime.datetime.today().strftime('%d/%m/%Y')
        
        # Row 0: Date
        label_date_on_slip = tk.Label(self.frame_info_of_slip, text=f"Ngày:")
        label_date_on_slip.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        entry_date_on_slip = cls_my_text_entry_num_01(self.frame_info_of_slip)
        entry_date_on_slip.insert(0, today)  # Set the default value
        entry_date_on_slip.grid(row=0, column=1, padx=10, pady=5)
        
        # Row 0: Slip Number
        label_number_of_slip = tk.Label(self.frame_info_of_slip, text=f"Số phiếu:")
        label_number_of_slip.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        entry_number_of_slip = cls_my_text_entry_num_01(self.frame_info_of_slip)
        entry_number_of_slip.insert(0, "")  # Set the default value
        entry_number_of_slip.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Row 1: Customer ID
        label_ma_doi_tuong = tk.Label(self.frame_info_of_slip, text=f"Mã KH:")
        label_ma_doi_tuong.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        entry_ma_doi_tuong = cls_my_text_entry_num_01(self.frame_info_of_slip)
        entry_ma_doi_tuong.insert(0, "")  # Set the default value
        entry_ma_doi_tuong.grid(row=1, column=1, padx=10, pady=5)
        
        # Row 1: Customer Name - Span to the end of the frame
        label_ten_doi_tuong = tk.Label(self.frame_info_of_slip, text=f"Tên KH:")
        label_ten_doi_tuong.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        entry_ten_doi_tuong = cls_my_text_entry_num_01(self.frame_info_of_slip)
        entry_ten_doi_tuong.insert(0, "")  # Set the default value
        entry_ten_doi_tuong.grid(row=1, column=3, columnspan=2, padx=10, pady=5, sticky="ew")
        
        # Configure grid to stretch properly
        self.frame_info_of_slip.grid_columnconfigure(3, weight=2)  # Allow column 3 to expand to fill the space
        
    def f_add_elements_to_frame_button(self):
        from Components_View import cls_my_button_num_01
        
        Button_01 = cls_my_button_num_01(self.frame_button, text="BTN 01", command=self.f_do_nothing)
        Button_01.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        
        Button_02 = cls_my_button_num_01(self.frame_button, text="BTN 02", command=self.f_do_nothing)
        Button_02.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        Button_03 = cls_my_button_num_01(self.frame_button, text="BTN 03", command=self.f_do_nothing)
        Button_03.grid(row=0, column=2, padx=10, pady=5, sticky="ew")
        
        # Configure grid columns to expand equally
        self.frame_button.grid_columnconfigure(0, weight=1)
        self.frame_button.grid_columnconfigure(1, weight=1)
        self.frame_button.grid_columnconfigure(2, weight=1)
        
    def f_do_nothing(self):
        print("Button click")