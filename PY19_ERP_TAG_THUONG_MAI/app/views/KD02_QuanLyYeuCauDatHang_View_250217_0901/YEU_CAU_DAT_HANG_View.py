import tkinter as tk
from tkinter import ttk
import time
import json
from Components_View import *
from Components_View.treeview import cls_Treeview_frame_number_01
from utils import *
from .YEU_CAU_DAT_HANG_Controller import cls_test_Controller
from .YEU_CAU_DAT_HANG_Controller import cls_test_Controller_02_treeview
from .YEU_CAU_DAT_HANG_Controller import cls_test_Controller_03_auto_update_number 

from .YEU_CAU_DAT_HANG_Controller import SQLController
from .YEU_CAU_DAT_HANG_Controller import Controller_SQL_to_excel
from .YEU_CAU_DAT_HANG_Controller import Controller_delete_row_in_SQL
from .YEU_CAU_DAT_HANG_Controller import Controller_handel_all_events

class cls_YEU_CAU_DAT_HANG_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD02 | QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        name = "QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        super().__init__(title_of_form=title, name_of_slip=name)
        # Add controller 01
        self.f_view_add_controller_01_basic()

        # call reuse components
        self._f_view_thay_doi_gia_tri_cua_base_form()
        self._f_view_create_all_container_frames_of_window()
        # set up formats
        self._f_view_set_up_formats_of_tab_01()
        self._f_view_set_up_formats_of_tab_02()
        Controller_handel_all_events.update_entry_id_when_initializing(self.table_of_tab_01, self.tab_01_entry_id)
        # Set up all global variants
        self._f_setup_all_binding()
        # Add controllers
        self.f_view_add_controller_02_all_logic_of_treeview()
        self.f_view_add_controller_03_auto_update_entries_amount_of_inventory()
        # Set up when initializing
        self.f_set_up_when_initializing()
        
    def f_set_up_when_initializing(self):
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(self.entry_so_phieu)
    
    def _f_setup_all_binding(self):
        # Find in tab_01
        tab_01_frame = self.tab_01
        self.entry_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "entry_sl_kha_dung")
        self.entry_sl_kha_dung.bind("<FocusOut>", self.f_view_clear_content_when_sl_kha_dung_change)
        
        self.entry_ma_hang_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_hang")
        self.entry_ten_hang_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_hang")
        self.entry_dvt = f_utils_tim_component_with_name(tab_01_frame, "entry_dvt")
        
        self.entry_so_phieu = f_utils_tim_component_with_name(tab_01_frame, "slips_entry")
        
        self.btn_refresh_number_of_slip = f_utils_tim_component_with_name(tab_01_frame, "refresh_number_of_slip_button")
        self.btn_refresh_number_of_slip.config(command=self.f_tab_01_button_get_number_of_slip_click)
        
        self.entry_ma_khach_hang_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_khach_hang")
        self.entry_ten_khach_hang_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_khach_hang")
        self.entry_mst_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_mst")
        self.entry_dia_chi_tab_01 = f_utils_tim_component_with_name(tab_01_frame, "entry_dia_chi")
        
        self.entry_so_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_so_hop_dong")
        self.entry_thong_tin_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_thong_tin_ngan_cua_hop_dong")
        
        # Find in tab_02
        tab_02_frame = self.tab_02
        self.entry_ma_khach_hang_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_khach_hang")
        self.entry_ten_khach_hang_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_khach_hang")
        self.entry_mst_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_mst")
        self.entry_mst_tab_02.pack_forget()
        self.entry_dia_chi_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_dia_chi")
        self.entry_dia_chi_tab_02.pack_forget()
        self.frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_02_frame, "frame_row_2_of_inventories_info")
        self.frame_row_2_of_inventories_info.pack_forget()
        
        self.entry_ma_hang_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_hang")
        self.entry_ten_hang_tab_02 = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_hang")
        
        self.ngay_filter_bat_dau = f_utils_tim_component_with_name(tab_02_frame, "start_date_entry")
        self.ngay_filter_ket_thuc = f_utils_tim_component_with_name(tab_02_frame, "end_date_entry")
        
        self.label_footer = f_utils_tim_component_label_with_text(self, "Notification")
        
    def f_view_clear_content_when_sl_kha_dung_change(self, event):
        f_utils_on_entry_change(self.entry_sl_kha_dung)
        self.tab_01_entry_nhu_cau.delete(0, tk.END)
        self.tab_01_entry_sl_giu_cho.delete(0, tk.END)
        self.tab_01_entry_sl_YCDH.delete(0, tk.END)
    
    def _f_view_thay_doi_gia_tri_cua_base_form(self):
        # Thay đổi thông tin các tab
        notebook = None
        def find_notebook(widget):
            nonlocal notebook
            for child in widget.winfo_children():
                if isinstance(child, ttk.Notebook):
                    notebook = child
                    return True
                if find_notebook(child):
                    return True
            return False

        find_notebook(self) 

        if not notebook:
            print("Error: notebook not found!")
            return

        # Change the text of the second tabs
        notebook.tab(0, text="TẠO MỚI YÊU CẦU ĐẶT HÀNG")
        notebook.tab(1, text="QUẢN LÝ YÊU CẦU ĐẶT HÀNG")
        
        # Delete the third tab
        notebook.forget(2)
        
        # Change the title of TieuDeTab_01
        for child in self.tab1.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-01":
                        grandchild.destroy()
                        break
        # Change the title of TieuDeTab_01
        for child in self.tab2.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-02":
                        grandchild.destroy()
                        break
        return notebook
        
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Adding controller
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def f_view_add_controller_01_basic(self):
        # Initialize controller_01
        self.controller_01 = cls_test_Controller()
        self.controller_01.view = self

    def f_view_add_controller_02_all_logic_of_treeview(self):
        # Initialize controller_02
        tree = self.table_of_tab_01
        entry_ma_hh = self.tab_01_entry_nhu_cau
        entry_ten_hh = self.tab_01_entry_nhu_cau
        entry_so_luong = self.tab_01_entry_nhu_cau
        entry_ghi_chu = self.tab_01_entry_nhu_cau
        self.controller_02_treeview = cls_test_Controller_02_treeview(tree, entry_ma_hh, entry_ten_hh, entry_so_luong, entry_ghi_chu)
        self.controller_02_treeview.view = self
    
    def f_view_add_controller_03_auto_update_entries_amount_of_inventory(self):
        # Initialize controller_03
        entry_sl_kha_dung = self.entry_sl_kha_dung
        entry_sl_nhu_cau = self.tab_01_entry_nhu_cau
        entry_sl_giu_cho = self.tab_01_entry_sl_giu_cho
        entry_sl_yeu_cau_dat_hang = self.tab_01_entry_sl_YCDH
        self.controller_03_auto_update_number = cls_test_Controller_03_auto_update_number(entry_sl_kha_dung, entry_sl_nhu_cau, entry_sl_giu_cho, entry_sl_yeu_cau_dat_hang)
        self.controller_03_auto_update_number.view = self
    
    def _f_view_create_all_container_frames_of_window(self):
        # Create tabs
        self.tab_01 = self.tab1
        self.tab_02 = self.tab2
        # Settings tab content
        self._f_view_create_widgets_all_container_frames_in_tab_01()
        self._f_view_create_all_container_frames_in_tab_02()

    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_01: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================

    def _f_view_create_widgets_all_container_frames_in_tab_01(self):
        parent_frame = self.tab_01

        # Frame H2
        self.tab_01_frame_H2 = tk.Frame(parent_frame)
        self.tab_01_frame_H2.grid(row=0, column=0, sticky="ew")

        self._f_view_create_widgets_in_tab_01_frame_H2()

        # Frame entries
        self.tab_01_frame_entries = tk.Frame(parent_frame)
        self.tab_01_frame_entries.grid(row=1, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_01_frame_entries()

        # Frame button
        self.tab_01_frame_button_of_treeview = tk.Frame(parent_frame)
        self.tab_01_frame_button_of_treeview.grid(row=2, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_01_frame_button_of_treeview()

        # Frame treeview
        self.tab_01_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_01_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self._f_view_create_widgets_in_tab_01_frame_treeview()
        
        # Frame button
        self.tab_01_frame_button_02 = tk.Frame(parent_frame)
        self.tab_01_frame_button_02.grid(row=4, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_01_frame_button_02()

        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)

    def _f_view_create_widgets_in_tab_01_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_01_frame_H2, text="PHIẾU YÊU CẦU ĐẶT HÀNG").pack(anchor="center")
     
    def _f_view_create_widgets_in_tab_01_frame_entries(self):
        self.tab_01_container_frame_entries = tk.Frame(self.tab_01_frame_entries)
        self.tab_01_container_frame_entries.pack(side="top", 
                                                 fill="x"
                                                 )
        self._f_view_create_widgets_in_tab_01_container_frame_entries()
    
    def _f_view_create_widgets_in_frame_date_and_number(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number)
        self.frame_date_and_number.pack(anchor="center")
    
    def _f_view_create_widgets_in_tab_01_container_frame_entries(self):
        # Create container for date and number of slip
        self.Frame_container_date_and_number = tk.Frame(self.tab_01_container_frame_entries)
        self.Frame_container_date_and_number.pack(side="top", 
                                                  fill="x"
                                                  )
        self._f_view_create_widgets_in_frame_date_and_number()

        # Create container for client and inventories
        self.Frame_clients_and_inventories_information = tk.Frame(self.tab_01_container_frame_entries)
        self.Frame_clients_and_inventories_information.pack(side="top",
                                                            fill="x",  
                                                            pady=(5,0)
                                                            )
        self._f_view_create_widgets_in_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(self.tab_01_container_frame_entries)
        self.frame_slip_informations.pack(side="top", 
                                          fill="x", 
                                          pady=(5,0)
                                          )
        self._f_view_create_widgets_in_frame_slip_informations()

    

    def _f_view_create_widgets_in_frame_clients_and_inventories(self):
        parent_frame = self.Frame_clients_and_inventories_information

        # Configure grid layout for parent frame
        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_rowconfigure(0, weight=1)

        # Create frame clients informations
        self.frame_clients_informations_tab_01 = cls_frame_client_information_view(parent_frame)
        self.frame_clients_informations_tab_01.config(bd=0, relief="flat")
        self.frame_clients_informations_tab_01.grid(row=0, column=0, sticky="nsew")
        self._f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01()
        
        # Create frame inventories informations
        self.frame_inventories_informations_tab_01 = cls_frame_inventories_information_view(parent_frame)
        self.frame_inventories_informations_tab_01.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_01.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self._f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01()
            
    def _f_view_create_widgets_in_frame_slip_informations(self):
        # Input fields
        tk.Label(self.frame_slip_informations, text="STT:").pack(side="left")
        self.tab_01_entry_id = tk.Entry(self.frame_slip_informations,
                                        width=10)
        self.tab_01_entry_id.pack(side="left")
        self.tab_01_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_01_note_for_slip = cls_my_text_entry_num_01(self.frame_slip_informations)
        self.tab_01_note_for_slip.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_note_for_slip.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_note_for_slip.pack(side="left", fill="x", expand=True, pady=10)
        
    def _f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = self.frame_inventories_informations_tab_01.frame_row_2
        
        self.label13_nhu_cau = tk.Label(parent_frame, text="nhu cầu:")
        # self.label13_nhu_cau.pack(side="left")
        self.label13_nhu_cau.grid(row=0, column=4, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_nhu_cau = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_nhu_cau.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_nhu_cau.f_on_not_selecting(color=COLOR_WHITE)
        # self.tab_01_entry_nhu_cau.pack(side="left")
        self.tab_01_entry_nhu_cau.grid(row=0, column=5, padx=(0, 10), pady=5, sticky="w")
        
        self.label_sl_giu_cho = tk.Label(parent_frame, text="SL giữ chỗ:")
        # self.label_sl_giu_cho.pack(side="left")
        self.label_sl_giu_cho.grid(row=0, column=6, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_giu_cho = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_giu_cho.config(state="readonly")
        # self.tab_01_entry_sl_giu_cho.pack(side="left")
        self.tab_01_entry_sl_giu_cho.grid(row=0, column=7, padx=(0, 10), pady=5, sticky="w")
        
        self.label_sl_YCDH = tk.Label(parent_frame, text="SL YCĐH:")
        # self.label_sl_YCDH.pack(side="left")
        self.label_sl_YCDH.grid(row=0, column=8, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_YCDH = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_YCDH.config(state="readonly")
        # self.tab_01_entry_sl_YCDH.pack(side="left")
        self.tab_01_entry_sl_YCDH.grid(row=0, column=9, padx=(0, 10), pady=5, sticky="w")

        # Configure column weights for proper resizing
        parent_frame.columnconfigure(5, weight=1)  # Allow tab_01_entry_nhu_cau to expand
        parent_frame.columnconfigure(7, weight=1)  # Allow tab_01_entry_sl_giu_cho to expand
        parent_frame.columnconfigure(9, weight=1)  # Allow tab_01_entry_sl_YCDH to expand
        
        self._f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01()
    
    def _f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = tk.Frame(self.frame_inventories_informations_tab_01)
        parent_frame.pack(side="bottom", fill="x", expand=True)

        tk.Label(parent_frame, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_01_entry_ghi_chu_mat_hang = cls_my_text_entry_num_01(parent_frame)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
    def _f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01(self):
        # create parent_frame
        parent_frame = cls_frame_contracts_management_view(self.frame_clients_informations_tab_01)
        parent_frame.pack(side="bottom", fill="x", expand=True)

    def _f_view_create_widgets_in_tab_01_frame_button_of_treeview(self):
        # Create a sub-frame to organize buttons in the center
        tab_01_button_container_01 = tk.Frame(self.tab_01_frame_button_of_treeview)
        tab_01_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_01_button_add = tk.Button(tab_01_button_container_01, text="Add Row", command=self.f_view_tab_01_button_add_click)
        self.tab_01_button_add.pack(side="left", padx=10)
        
        # Update button
        self.tab_01_button_update = tk.Button(tab_01_button_container_01, text="Update Row", command=self.f_view_tab_01_button_update_click)
        self.tab_01_button_update.pack(side="left", padx=10)
        
        # Delete button
        self.tab_01_button_delete = tk.Button(tab_01_button_container_01, text="Delete Row", command=self.f_view_tab_01_button_delete_click)
        self.tab_01_button_delete.pack(side="left", padx=10)
        
        # Clear button
        self.tab_01_button_clear = tk.Button(tab_01_button_container_01, text="Clear Rows", command=self.f_view_tab_01_button_clear_click)
        self.tab_01_button_clear.pack(side="left", padx=10)
    
    def _f_view_create_widgets_in_tab_01_frame_treeview(self):
        self.tab_01_frame_treeview = self.tab_01_frame_treeview
        self.table_of_tab_01 = self.tab_01_frame_treeview.treeview_normal
        self.treeview_test_of_tag_01 = self.tab_01_frame_treeview.treeview_normal
        self.treeview_test_of_tag_01.bind("<ButtonRelease-1>", self.f_view_table_of_tab_01_click)
        
    def f_view_table_of_tab_01_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_01_click(
            event, 
            self.table_of_tab_01,
            self.tab_01_entry_id,
            self.entry_ma_hang_tab_01,
            self.entry_ten_hang_tab_01,
            self.entry_dvt,
            self.entry_sl_kha_dung,
            self.tab_01_entry_nhu_cau,
            self.tab_01_entry_sl_giu_cho,
            self.tab_01_entry_sl_YCDH,
            self.tab_01_entry_ghi_chu_mat_hang)
        
        
    def _f_view_create_widgets_in_tab_02_frame_treeview(self):
        self.tab_02_frame_treeview = self.tab_02_frame_treeview
        self.table_of_tab_02 = self.tab_02_frame_treeview.treeview_normal
        self.treeview_test_of_tag_02 = self.tab_02_frame_treeview.treeview_normal
        self.treeview_test_of_tag_02.bind("<ButtonRelease-1>", self.f_view_table_of_tab_02_click)
    
    def _f_view_create_widgets_in_tab_01_frame_button_02(self):
        parent_frame = self.tab_01_frame_button_02
        # Create a sub-frame on the right
        tab_01_button_container_02_on_the_right = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_01_button_container_02_on_the_left = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # # BTN test
        # self.tab_01_button_save_02 = tk.Button(tab_01_button_container_02_on_the_right, 
        #                                        text="Test save 02", 
        #                                        background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
        #                                        command=self.f_tab_01_button_save_02_click)
        # self.tab_01_button_save_02.pack(side="right", padx=10)
        
        # # BTN test
        # self.tab_01_button_export = tk.Button(tab_01_button_container_02_on_the_right, 
        #                                       text="Test save 01", 
        #                                       background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
        #                                       command=self.f_tab_01_button_export_click)
        # self.tab_01_button_export.pack(side="right", padx=10)
        
        # # BTN test
        # self.tab_01_print_config = tk.Button(tab_01_button_container_02_on_the_right, 
        #                                      text="Test in cấu hình của bảng", 
        #                                      background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
        #                                      command=self.f_button_print_config_click)
        # self.tab_01_print_config.pack(side="right", padx=10)
        
        # # BTN test
        # self.tab_01_config_num_02 = tk.Button(tab_01_button_container_02_on_the_right, 
        #                                       text="Test print form print từ code", 
        #                                       background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
        #                                       command=self.f_tab_01_button_print_form_tu_tao_tu_code_click)
        # self.tab_01_config_num_02.pack(side="right", padx=10)
        
        # BTN save
        self.tab_01_button_save_03 = tk.Button(tab_01_button_container_02_on_the_right, 
                                               text="Save", 
                                               command=self.f_tab_01_button_save_03_click)
        self.tab_01_button_save_03.pack(side="right", padx=10)
        
        # BTN print
        self.tab_01_button_print_02 = tk.Button(tab_01_button_container_02_on_the_right, 
                                                text="Print", 
                                                command=self.f_tab_01_button_print_click)
        self.tab_01_button_print_02.pack(side="right", padx=10)
        
        # temp button
        self.tab_01_btn_template = tk.Button(tab_01_button_container_02_on_the_left, 
                                             text="Template", 
                                             command=self.f_tab_01_button_template_click)
        self.tab_01_btn_template.pack(side="left", padx=10)
        
        # get file button
        self.tab_01_btn_get_import_file = tk.Button(tab_01_button_container_02_on_the_left, 
                                                    text="Get file", 
                                                    command=self.f_tab_01_button_get_import_file_click)
        self.tab_01_btn_get_import_file.pack(side="left", padx=10)
        
        # import button
        self.tab_01_btn_import = tk.Button(tab_01_button_container_02_on_the_left, 
                                           text="Import excel", 
                                           command=self.f_tab_01_button_import_click)
        self.tab_01_btn_import.pack(side="left", padx=10)
        
        # star import button
        self.tab_01_btn_start_import_file = tk.Button(tab_01_button_container_02_on_the_left, 
                                                      text="Start import")
        self.tab_01_btn_start_import_file.pack(side="left", padx=10)

    def f_button_print_config_click(self):
        self.f_print_table_of_tab_01_config()
        
    def f_print_table_of_tab_01_config(self):
        # Get the Treeview configuration
        config = self.table_of_tab_01.config()

        # Convert Tcl objects to JSON-serializable Python objects
        json_serializable_config = {}
        for key, value in config.items():
            # Attempt to convert each value
            try:
                if isinstance(value, (list, tuple)):
                    # Recursively convert list or tuple
                    json_serializable_config[key] = [str(item) for item in value]
                else:
                    # Convert single value to string
                    json_serializable_config[key] = str(value)
            except Exception as e:
                # Handle unconvertible values (optional)
                json_serializable_config[key] = f"Error converting: {e}"

        # Save the configuration to a JSON file
        with open("treeview_config.json", "w" ,encoding='utf-8') as json_file:
            json.dump(json_serializable_config, json_file, indent=4, ensure_ascii=False)
    
    def f_view_tab_01_button_clear_click(self):
        notification_text = Controller_handel_all_events.f_handle_tab_01_button_clear_click(self.treeview_test_of_tag_01)
        self._f_config_notification(notification_text, fg="blue")

    def f_tab_01_button_print_form_tu_tao_tu_code_click(self):
        notification_text = Controller_handel_all_events.f_handle_btn_print_form_tu_tao_tu_code_click_()
        self._f_config_notification(notification_text, fg="blue")
        
    def f_tab_01_button_print_click(self):
        notification_text = Controller_handel_all_events.f_handle_btn_print_click()
        self._f_config_notification(notification_text, fg="blue")
        
    def f_tab_01_button_get_number_of_slip_click(self):        
        notification_text = Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(self.entry_so_phieu)
        self._f_config_notification(notification_text, fg="blue")
    
    def f_tab_01_button_import_click(self):
        print("Import config")
        
    def f_tab_01_button_template_click(self):
        self._f_config_notification(f_utils_create_template_excel_file(),"black")
        
    def f_tab_01_button_get_import_file_click(self):
        self._f_config_notification(f_utils_open_file(),"black")

    def f_view_tab_01_button_add_click(self):
        notification_text, text_color = Controller_handel_all_events.f_handle_event_tab_01_button_add_row_click(
            self.table_of_tab_01, 
            self.tab_01_entry_id, 
            self.entry_ma_hang_tab_01, 
            self.entry_ten_hang_tab_01, 
            self.entry_dvt, 
            self.entry_sl_kha_dung, 
            self.tab_01_entry_nhu_cau, 
            self.tab_01_entry_sl_giu_cho, 
            self.tab_01_entry_sl_YCDH, 
            self.tab_01_entry_ghi_chu_mat_hang
            )
        self._f_config_notification(notification_text, fg=text_color)
    
    def f_view_tab_01_button_delete_click(self):
        self.controller_02_treeview.f_controller_02_delete_selected(self.treeview_test_of_tag_01)
    
    def f_view_tab_01_button_update_click(self):
        # Khai báo các tham số
        tree = self.treeview_test_of_tag_01
        selected_item = tree.selection()
        param_00 = tree.item(selected_item, "values")[0] if tree.item(selected_item, "values") else None
        param_01 = self.entry_ma_hang_tab_01.get()
        param_02 = self.entry_ten_hang_tab_01.get()
        param_03 = self.entry_dvt.get()
        param_04 = float(self.entry_sl_kha_dung.get().replace(',', '') or 0)
        param_05 = float(self.tab_01_entry_nhu_cau.get().replace(',', '') or 0)
        param_06 = float(self.tab_01_entry_sl_giu_cho.get().replace(',', '') or 0)
        param_07 = float(self.tab_01_entry_sl_YCDH.get().replace(',', '') or 0)
        param_08 = self.tab_01_entry_ghi_chu_mat_hang.get()
        # Gọi hàm
        self.controller_02_treeview.update_selected_row(
            tree,
            param_00,
            param_01,
            param_02,
            param_03,
            param_04,
            param_05,
            param_06,
            param_07,
            param_08
        )
    
    def f_view_set_format_of_treeview_of_tab_01(self):
        my_treeview = self.treeview_test_of_tag_01
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_01(my_treeview)
    
    def _f_view_set_rows_count_of_treeview_01_when_add_new_row(self):
        row_count = 1 + self.controller_01.f_controller_get_row_count(self.table_of_tab_01)
        self.tab_01_entry_id.config(state="normal")
        self.tab_01_entry_id.delete(0, tk.END)
        self.tab_01_entry_id.insert(0, row_count)
        self.tab_01_entry_id.config(state="disabled")
    
    def _f_config_notification(self, text="", fg="black"):
        self.label_footer.config(text=text, fg=fg)
    
    def f_tab_01_button_export_click(self):
        text = self.controller_01.f_export_data_to_SQL(self.table_of_tab_01)
        self._f_config_notification(text=text, fg="blue")
        
    def f_tab_01_button_save_02_click(self):
        text = self.controller_01.f_controller_handle_btn_save_02_click_(self.table_of_tab_01)
        self._f_config_notification(text=text, fg="blue")
    
    def f_tab_01_button_save_03_click(self):        
        # Khai báo các tham số
        ID_nhan_vien = "NV01"
        Xoa_Sua = ""
        entry_so_phieu = self.entry_so_phieu
        entry_ma_kh = self.entry_ma_khach_hang_tab_01
        entry_ten_kh = self.entry_ten_khach_hang_tab_01
        entry_mst = self.entry_mst_tab_01
        entry_dia_chi = self.entry_dia_chi_tab_01
        entry_so_hop_dong = self.entry_so_hop_dong
        entry_thong_tin_hop_dong = self.entry_thong_tin_hop_dong
        entry_ghi_chu_cua_phieu = self.tab_01_note_for_slip
        tree = self.table_of_tab_01
        
        entry_ma_hang = self.entry_ma_hang_tab_01
        entry_ten_hang = self.entry_ten_hang_tab_01

        # Handel event click
        text = SQLController.f_controller_handle_btn_save_03_click_(ID_nhan_vien,
                                                                    Xoa_Sua,
                                                                    entry_so_phieu, 
                                                                    entry_ma_kh, 
                                                                    entry_ten_kh,
                                                                    entry_mst,
                                                                    entry_dia_chi,
                                                                    entry_so_hop_dong,
                                                                    entry_thong_tin_hop_dong,
                                                                    entry_ghi_chu_cua_phieu,
                                                                    entry_ma_hang,
                                                                    entry_ten_hang,
                                                                    tree
                                                                    )
        self._f_config_notification(text=text, fg="blue")
        
        # Phiên bản cũ, cần làm sạch rồi mới xoá
        # ====>
        # text, data = self.controller_02_treeview.print_data()
        # text = self.controller_02_treeview.f_controller_handle_btn_save_03_click_(self.table_of_tab_01)
        # self._f_config_notification(text=text, fg="blue")

    def _f_view_set_up_formats_of_tab_01(self):
        self.f_view_set_format_of_treeview_of_tab_01()
    
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_02: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def _f_view_create_all_container_frames_in_tab_02(self):
        parent_frame = self.tab_02

        # Frame H2
        self.tab_02_frame_H2 = tk.Frame(parent_frame)
        self.tab_02_frame_H2.grid(row=0, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_02_frame_H2()

        # Frame entries
        self.tab_02_frame_filter_entries = tk.Frame(parent_frame)
        self.tab_02_frame_filter_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_02_frame_filter_entries()

        # Frame button
        self.tab_02_frame_button_01 = tk.Frame(parent_frame)
        self.tab_02_frame_button_01.grid(row=2, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_02_frame_button_01()
        
        # Frame treeview
        self.tab_02_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_02_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self._f_view_create_widgets_in_tab_02_frame_treeview()
        
        # Frame button
        self.tab_02_frame_button_02 = tk.Frame(parent_frame)
        self.tab_02_frame_button_02.grid(row=4, column=0, sticky="ew")
        self._f_view_create_widgets_in_tab_02_frame_button_02()
        
        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)

    def _f_view_create_widgets_in_tab_02_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_02_frame_H2, text="NHẬT KÝ YÊU CẦU ĐẶT HÀNG").pack(anchor="center")
     
    def _f_view_create_widgets_in_tab_02_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_01 = tk.Frame(self.tab_02_frame_button_01)
        tab_02_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_02_button_add = tk.Button(tab_02_button_container_01, text="Filter")
        self.tab_02_button_add.config(command=self.f_tab_02_button_filter_click)
        self.tab_02_button_add.pack(side="left", padx=10)
        
        # Delete update
        self.tab_02_button_clear = tk.Button(tab_02_button_container_01, text="Clear")
        self.tab_02_button_clear.config(command=self.f_tab_02_button_clear_click)
        self.tab_02_button_clear.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_02_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        parent_frame_01 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        parent_frame_02 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_02.grid(row=0, column=2, sticky="nsew")
        
        # parent_frame_00.config(bd=1,relief="groove")
        # parent_frame_01.config(bd=1,relief="groove")
        # parent_frame_02.config(bd=1,relief="groove")
        
        # Create Number of slip and contract number
        tk.Label(parent_frame_00, text="Số phiếu").grid(row=0, column= 0, padx=(10, 0), pady=(10, 0), sticky="w")
        self.filter_entry_slip_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_slip_number.grid(row=0, column= 1, padx=(2, 10), pady=(10, 0), sticky="ew")
        tk.Label(parent_frame_00, text="Số hợp đồng").grid(row=1, column= 0, padx=(10, 0), pady=(15, 10), sticky="w")
        self.filter_entry_contract_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_contract_number.grid(row=1, column= 1, padx=(2, 10), pady=(15, 10), sticky="ew")
        
        # Create frame inventories informations
        self.frame_seclect_date_tab_02 = cls_frame_DateSelector_view(parent_frame_01)
        self.frame_seclect_date_tab_02.config(bd=0, relief="flat")
        self.frame_seclect_date_tab_02.grid(row=0, column=0, sticky="ew")
        
        # Create frame clients informations
        self.frame_clients_informations_tab_02 = cls_frame_client_information_view(parent_frame_02)
        self.frame_clients_informations_tab_02.config(bd=0, relief="flat")
        self.frame_clients_informations_tab_02.grid(row=0, column=0, sticky="ew")
        
        # Create frame inventories informations
        self.frame_inventories_informations_tab_02 = cls_frame_inventories_information_view(parent_frame_02)
        self.frame_inventories_informations_tab_02.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_02.grid(row=1, column=0, pady=(10, 0), sticky="ew")
    
        # Allow stretching
        self.tab_02_frame_filter_entries.columnconfigure(2, weight=1)   # Stretch the column to fill the width
        parent_frame_02.columnconfigure(0, weight=1)                    # Stretch parent_frame_02
    
    def _f_view_create_widgets_in_tab_02_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_02 = tk.Frame(self.tab_02_frame_button_02)
        tab_02_button_container_02.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_02_button_export_excel = tk.Button(tab_02_button_container_02, text="Export Excel")
        self.tab_02_button_export_excel.config(command=self.f_tab_02_button_export_excel_click)
        self.tab_02_button_export_excel.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_02_button_edit = tk.Button(tab_02_button_container_02, text="EDIT")
        self.tab_02_button_edit.config(command=self.f_tab_02_button_edit_click)
        self.tab_02_button_edit.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_02_button_DELETE = tk.Button(tab_02_button_container_02, text="DELETE")
        self.tab_02_button_DELETE.config(command=self.f_tab_02_button_delete_click)
        self.tab_02_button_DELETE.pack(side="left", padx=10)
    
    def f_tab_02_button_filter_click(self):
        so_phieu = self.filter_entry_slip_number.get()
        so_hop_dong = self.filter_entry_contract_number.get()
        ngay_bat_dau = self.ngay_filter_bat_dau.get()
        ngay_ket_thuc = self.ngay_filter_ket_thuc.get()
        ma_doi_tuong = self.entry_ma_khach_hang_tab_02.get()
        ma_hang = self.entry_ma_hang_tab_02.get()
        notification_text = Controller_handel_all_events.f_handle_event_tab_02_button_filter_slip(self.treeview_test_of_tag_02,
                                                                                                    so_phieu, 
                                                                                                    so_hop_dong,
                                                                                                    ngay_bat_dau,
                                                                                                    ngay_ket_thuc,
                                                                                                    ma_doi_tuong,
                                                                                                    ma_hang
                                                                                                    )
        self._f_config_notification(notification_text, fg="blue")
    
    def f_tab_02_button_clear_click(self):
        self.filter_entry_slip_number.delete(0, tk.END)
        self.filter_entry_contract_number.delete(0, tk.END)
        # self.ngay_filter_bat_dau.delete(0, tk.END)
        # self.ngay_filter_ket_thuc.delete(0, tk.END)
        self.entry_ma_khach_hang_tab_02.delete(0, tk.END)
        self.entry_ten_khach_hang_tab_02.delete(0, tk.END)
        self.entry_ma_hang_tab_02.delete(0, tk.END)
        self.entry_ten_hang_tab_02.delete(0, tk.END)
        notification_text = Controller_handel_all_events.f_handle_event_tab_02_button_clear_slip(self.treeview_test_of_tag_02)
        self._f_config_notification(notification_text, fg="blue")
        # SQLController.load_data(self.treeview_test_of_tag_02)
        
    def f_tab_02_button_export_excel_click(self):
        print("Export excel click")
        Controller_SQL_to_excel.export_log_to_excel(self.treeview_test_of_tag_02)
        
    def f_tab_02_button_edit_click(self):
        print("Edit click")
    
    def f_tab_02_button_delete_click(self):
        text = Controller_delete_row_in_SQL.handle_event_btn_delete_click(self.treeview_test_of_tag_02)
        self._f_config_notification(text=text, fg="blue")
        
    def _f_view_set_up_formats_of_tab_02(self):
        self.f_view_set_format_of_treeview_of_tab_02()

    def f_view_set_format_of_treeview_of_tab_02(self):
        my_treeview = self.treeview_test_of_tag_02
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_02(my_treeview)
    
    def f_view_table_of_tab_02_click(self, event):
        self.current_time = time.time()
    
    def f_tab_02_table_on_click(self, event):
        print("f_tab_02_table_on_click")    


    