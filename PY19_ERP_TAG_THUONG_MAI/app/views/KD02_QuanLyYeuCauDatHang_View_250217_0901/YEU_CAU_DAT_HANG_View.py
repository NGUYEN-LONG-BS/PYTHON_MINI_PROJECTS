import tkinter as tk
from tkinter import ttk
from Components_View import *
from Components_View.treeview import cls_Treeview_frame_number_01
from utils import *
from .YEU_CAU_DAT_HANG_Controller import Controller_auto_update_sl_giu_cho_va_sl_ycdh
from .YEU_CAU_DAT_HANG_Controller import Controller_handel_all_events

class cls_YEU_CAU_DAT_HANG_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD02 | QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        name = "QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        super().__init__(title_of_form=title, name_of_slip=name)
        # call reuse components
        self.f_view_thay_doi_gia_tri_cua_base_form()
        self.f_view_create_all_container_frames_of_window()
        self.f_set_up_format_of_tree_view()
        # Set up all global variants
        self.f_define_all_elements()
        # Add controllers
        self.f_create_controller_auto_update_3_entries_sl_nhu_cau_sl_giu_cho_sl_ycdh()
        # Set up when initializing
        self.f_set_up_when_initializing()
        self.f_set_command_for_elements()
    
    def f_view_create_all_container_frames_of_window(self):
        # Settings tab content
        self.f_view_create_widgets_all_container_frames_in_tab_01()
        self._f_view_create_all_container_frames_in_tab_02()
    
    def f_set_up_format_of_tree_view(self):
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_01(self.tab_01_treeview_YCDH)
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_02(self.tab_02_treeview_log_of_YCDH)
        
    def f_set_up_when_initializing(self):
        # Update entry id
        Controller_handel_all_events.update_entry_id_when_initializing(self.tab_01_treeview_YCDH, self.tab_01_entry_id)
        # Update entry slip number
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(self.tab_01_entry_so_phieu)
        # Load data to tab 2: treeview YCDH log
        self.event_tab_02_button_filter_click()
    
    def f_set_command_for_elements(self):
        # config command for elements
        self.tab_01_btn_refresh_number_of_slip.config(command=self.event_tab_01_button_get_number_of_slip_click)
        
        self.tab_01_button_add.config(command=self.event_tab_01_button_add_row_click)
        self.tab_01_button_update_row_in_treeview.config(command=self.event_tab_01_button_update_row_click)
        self.tab_01_button_delete.config(command=self.event_tab_01_button_delete_click)
        self.tab_01_button_clear.config(command=self.event_tab_01_button_clear_click)
        
        self.tab_01_button_update_slip.config(command=self.event_tab_01_button_update_slip_click)
        self.tab_01_button_save.config(command=self.event_tab_01_button_save_click)
        self.tab_01_button_print.config(command=self.event_tab_01_button_print_click)
        
        self.tab_01_btn_template.config(command=self.event_tab_01_button_template_click)
        self.tab_01_btn_get_import_file.config(command=self.event_tab_01_button_get_import_file_click)
        # self.tab_01_btn_import.config(command=self.event_tab_01_button_import_click)
        # self.tab_01_btn_start_import_file.config(command=self.event_tab_01_button_start_import_file_click)
        
        self.tab_02_button_filter.config(command=self.event_tab_02_button_filter_click)
        self.tab_02_button_clear_filter.config(command=self.event_tab_02_button_clear_filter_click)
        self.tab_02_button_export_excel.config(command=self.event_tab_02_button_export_excel_click)
        self.tab_02_button_export_all_data.config(command=self.event_tab_02_button_export_all_data_click)
        
        self.tab_02_button_edit_slip.config(command=self.event_tab_02_button_edit_slip_click)
        self.tab_02_button_delete_slip.config(command=self.event_tab_02_button_delete_slip_click)
        
        # Gán sự kiện
        self.tab_01_treeview_YCDH.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_01_single_click)  # Single click
        self.tab_01_treeview_YCDH.bind("<Double-1>", self.f_view_treeview_of_tab_01_double_click)  # Double click
        
        self.tab_02_treeview_log_of_YCDH.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_02_single_click)  # Single click
        self.tab_02_treeview_log_of_YCDH.bind("<Double-1>", self.f_view_treeview_of_tab_02_double_click)  # Double click
        
    def f_define_all_elements(self):
        # Find in tab_01
        tab_01_frame = self.tab1
        self.tab_01_entry_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "entry_sl_kha_dung")
        self.tab_01_entry_ma_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_hang")
        self.tab_01_entry_ten_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_hang")
        self.tab_01_entry_dvt = f_utils_tim_component_with_name(tab_01_frame, "entry_dvt")
        self.tab_01_entry_ngay_tren_phieu = f_utils_tim_component_with_name(tab_01_frame, "date_entry")
        self.tab_01_entry_so_phieu = f_utils_tim_component_with_name(tab_01_frame, "slips_entry")
        self.tab_01_btn_refresh_number_of_slip = f_utils_tim_component_with_name(tab_01_frame, "refresh_number_of_slip_button")
        self.tab_01_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_khach_hang")
        self.tab_01_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_khach_hang")
        self.tab_01_entry_mst = f_utils_tim_component_with_name(tab_01_frame, "entry_mst")
        self.tab_01_entry_dia_chi = f_utils_tim_component_with_name(tab_01_frame, "entry_dia_chi")
        self._tab_01_entry_so_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_so_hop_dong")
        self.tab_01_entry_thong_tin_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_thong_tin_ngan_cua_hop_dong")
        self.tab_01_label_footer_notification = f_utils_tim_component_label_with_text(self, "Notification")
        
        # Find in tab_02
        tab_02_frame = self.tab2
        self.tab_02_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_khach_hang")
        self.tab_02_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_khach_hang")
        self.tab_02_entry_mst = f_utils_tim_component_with_name(tab_02_frame, "entry_mst")
        self.tab_02_entry_mst.pack_forget()
        self.tab_02_entry_dia_chi = f_utils_tim_component_with_name(tab_02_frame, "entry_dia_chi")
        self.tab_02_entry_dia_chi.pack_forget()
        self._tab_02_frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_02_frame, "frame_row_2_of_inventories_info")
        self._tab_02_frame_row_2_of_inventories_info.pack_forget()
        self.tab_02_entry_ma_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_hang")
        self.tab_02_entry_ten_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_hang")
        self.tab_02_ngay_filter_bat_dau = f_utils_tim_component_with_name(tab_02_frame, "start_date_entry")
        self.tab_02_ngay_filter_ket_thuc = f_utils_tim_component_with_name(tab_02_frame, "end_date_entry")
    
    def f_view_thay_doi_gia_tri_cua_base_form(self):
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
    
    def f_create_controller_auto_update_3_entries_sl_nhu_cau_sl_giu_cho_sl_ycdh(self):
        # Initialize controller
        self.controller_03_auto_update_number = Controller_auto_update_sl_giu_cho_va_sl_ycdh(
            self.tab_01_entry_sl_kha_dung, 
            self.tab_01_entry_nhu_cau, 
            self.tab_01_entry_sl_giu_cho, 
            self.tab_01_entry_sl_YCDH)
        self.controller_03_auto_update_number.view = self

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
        
    def f_view_create_widgets_all_container_frames_in_tab_01(self):
        parent_frame = self.tab1

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
        self.tab_01_frame_date_and_number = cls_Frame_date_and_number_of_slip(self.tab_01_Frame_container_date_and_number)
        self.tab_01_frame_date_and_number.pack(anchor="center")
    
    def _f_view_create_widgets_in_tab_01_container_frame_entries(self):
        # Create container for date and number of slip
        self.tab_01_Frame_container_date_and_number = tk.Frame(self.tab_01_container_frame_entries)
        self.tab_01_Frame_container_date_and_number.pack(side="top", 
                                                  fill="x"
                                                  )
        self._f_view_create_widgets_in_frame_date_and_number()

        # Create container for client and inventories
        self.tab_01_Frame_clients_and_inventories_information = tk.Frame(self.tab_01_container_frame_entries)
        self.tab_01_Frame_clients_and_inventories_information.pack(side="top",
                                                            fill="x",  
                                                            pady=(5,0)
                                                            )
        self._f_view_create_widgets_in_frame_clients_and_inventories()

        # Create frame inventories informations
        self.tab_01_frame_slip_informations = tk.Frame(self.tab_01_container_frame_entries)
        self.tab_01_frame_slip_informations.pack(side="top", 
                                          fill="x", 
                                          pady=(5,0)
                                          )
        self._f_view_create_widgets_in_frame_slip_informations()

    def _f_view_create_widgets_in_frame_clients_and_inventories(self):
        parent_frame = self.tab_01_Frame_clients_and_inventories_information

        # Configure grid layout for parent frame
        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_rowconfigure(0, weight=1)

        # Create frame clients informations
        self.tab_01_frame_clients_informations = cls_frame_client_information_view(parent_frame)
        self.tab_01_frame_clients_informations.config(bd=0, relief="flat")
        self.tab_01_frame_clients_informations.grid(row=0, column=0, sticky="nsew")
        self._f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01()
        
        # Create frame inventories informations
        self.tab_01_frame_inventories_informations = cls_frame_inventories_information_view(parent_frame)
        self.tab_01_frame_inventories_informations.config(bd=0, relief="flat")
        self.tab_01_frame_inventories_informations.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self._f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01()
            
    def _f_view_create_widgets_in_frame_slip_informations(self):
        # Input fields
        tk.Label(self.tab_01_frame_slip_informations, text="STT:").pack(side="left")
        self.tab_01_entry_id = tk.Entry(self.tab_01_frame_slip_informations,
                                        width=10)
        self.tab_01_entry_id.pack(side="left")
        self.tab_01_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.tab_01_frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_01_entry_note_for_slip = cls_my_text_entry_num_01(self.tab_01_frame_slip_informations)
        self.tab_01_entry_note_for_slip.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_note_for_slip.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_note_for_slip.pack(side="left", fill="x", expand=True, pady=10)
        
    def _f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = self.tab_01_frame_inventories_informations.frame_row_2
        
        self._tab_01_label_nhu_cau = tk.Label(parent_frame, text="nhu cầu:")
        self._tab_01_label_nhu_cau.grid(row=0, column=6, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_nhu_cau = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_nhu_cau.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_nhu_cau.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_nhu_cau.grid(row=0, column=7, padx=(0, 10), pady=5, sticky="w")
        
        self.tab_01_label_sl_giu_cho = tk.Label(parent_frame, text="SL giữ chỗ:")
        self.tab_01_label_sl_giu_cho.grid(row=0, column=8, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_giu_cho = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_giu_cho.config(state="readonly")
        self.tab_01_entry_sl_giu_cho.grid(row=0, column=9, padx=(0, 10), pady=5, sticky="w")
        
        self.tab_01_label_sl_YCDH = tk.Label(parent_frame, text="SL YCĐH:")
        self.tab_01_label_sl_YCDH.grid(row=0, column=10, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_YCDH = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_YCDH.config(state="readonly")
        self.tab_01_entry_sl_YCDH.grid(row=0, column=11, padx=(0, 10), pady=5, sticky="w")

        # Configure column weights for proper resizing
        parent_frame.columnconfigure(7, weight=1)  # Allow tab_01_entry_nhu_cau to expand
        parent_frame.columnconfigure(9, weight=1)  # Allow tab_01_entry_sl_giu_cho to expand
        parent_frame.columnconfigure(11, weight=1)  # Allow tab_01_entry_sl_YCDH to expand
        
        self._f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01()
    
    def _f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = tk.Frame(self.tab_01_frame_inventories_informations)
        parent_frame.pack(side="bottom", fill="x", expand=True)

        tk.Label(parent_frame, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_01_entry_ghi_chu_mat_hang = cls_my_text_entry_num_01(parent_frame)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
    def _f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01(self):
        # create parent_frame
        parent_frame = cls_frame_contracts_management_view(self.tab_01_frame_clients_informations)
        parent_frame.pack(side="bottom", fill="x", expand=True)

    def _f_view_create_widgets_in_tab_01_frame_button_of_treeview(self):
        # Create a sub-frame to organize buttons in the center
        tab_01_button_container_01 = tk.Frame(self.tab_01_frame_button_of_treeview)
        tab_01_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_01_button_add = tk.Button(tab_01_button_container_01, text="Add Row")
        self.tab_01_button_add.pack(side="left", padx=10)
        
        # Update button
        self.tab_01_button_update_row_in_treeview = tk.Button(tab_01_button_container_01, text="Update Row")
        self.tab_01_button_update_row_in_treeview.pack(side="left", padx=10)
        
        # Delete button
        self.tab_01_button_delete = tk.Button(tab_01_button_container_01, text="Delete Row")
        self.tab_01_button_delete.pack(side="left", padx=10)
        
        # Clear button
        self.tab_01_button_clear = tk.Button(tab_01_button_container_01, text="Clear Rows")
        self.tab_01_button_clear.pack(side="left", padx=10)
    
    def _f_view_create_widgets_in_tab_01_frame_treeview(self):
        self.tab_01_treeview_YCDH = self.tab_01_frame_treeview.treeview_normal
    
    def _f_view_create_widgets_in_tab_01_frame_button_02(self):
        parent_frame = self.tab_01_frame_button_02
        # Create a sub-frame on the right
        tab_01_button_container_02_on_the_right = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_01_button_container_02_on_the_left = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # BTN update slip
        self.tab_01_button_update_slip = tk.Button(tab_01_button_container_02_on_the_right, text="Update")
        self.tab_01_button_update_slip.pack(side="right", padx=10)
        
        # BTN save
        self.tab_01_button_save = tk.Button(tab_01_button_container_02_on_the_right, text="Save")
        self.tab_01_button_save.pack(side="right", padx=10)
        
        # BTN print
        self.tab_01_button_print = tk.Button(tab_01_button_container_02_on_the_right, text="Print")
        self.tab_01_button_print.pack(side="right", padx=10)
        
        # temp button
        self.tab_01_btn_template = tk.Button(tab_01_button_container_02_on_the_left, text="Template")
        self.tab_01_btn_template.pack(side="left", padx=10)
        
        # get file button
        self.tab_01_btn_get_import_file = tk.Button(tab_01_button_container_02_on_the_left, text="Get file")
        self.tab_01_btn_get_import_file.pack(side="left", padx=10)
    
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
    
    def _f_view_create_widgets_in_tab_02_frame_treeview(self):
        self.tab_02_treeview_log_of_YCDH = self.tab_02_frame_treeview.treeview_normal
    
    def _f_view_create_all_container_frames_in_tab_02(self):
        parent_frame = self.tab2

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
        self.tab_02_button_filter = tk.Button(tab_02_button_container_01, text="Filter")
        self.tab_02_button_filter.pack(side="left", padx=10)
        
        # Delete update
        self.tab_02_button_clear_filter = tk.Button(tab_02_button_container_01, text="Clear")
        self.tab_02_button_clear_filter.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_02_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        parent_frame_01 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        parent_frame_02 = tk.Frame(self.tab_02_frame_filter_entries)
        parent_frame_02.grid(row=0, column=2, sticky="nsew")
        
        # Create Number of slip and contract number
        tk.Label(parent_frame_00, text="Số phiếu").grid(row=0, column= 0, padx=(10, 0), pady=(10, 0), sticky="w")
        self.tab_02_entry_filter_slip_number = cls_my_text_entry_num_01(parent_frame_00)
        self.tab_02_entry_filter_slip_number.grid(row=0, column= 1, padx=(2, 10), pady=(10, 0), sticky="ew")
        tk.Label(parent_frame_00, text="Số hợp đồng").grid(row=1, column= 0, padx=(10, 0), pady=(15, 10), sticky="w")
        self.tab_02_entry_filter_contract_number = cls_my_text_entry_num_01(parent_frame_00)
        self.tab_02_entry_filter_contract_number.grid(row=1, column= 1, padx=(2, 10), pady=(15, 10), sticky="ew")
        
        # Create frame inventories informations
        self.tab_02_frame_seclect_date = cls_frame_DateSelector_view(parent_frame_01)
        self.tab_02_frame_seclect_date.config(bd=0, relief="flat")
        self.tab_02_frame_seclect_date.grid(row=0, column=0, sticky="ew")
        
        # Create frame clients informations
        self.tab_02_frame_clients_informations = cls_frame_client_information_view(parent_frame_02)
        self.tab_02_frame_clients_informations.config(bd=0, relief="flat")
        self.tab_02_frame_clients_informations.grid(row=0, column=0, sticky="ew")
        
        # Create frame inventories informations
        self.tab_02_frame_inventories_informations = cls_frame_inventories_information_view(parent_frame_02)
        self.tab_02_frame_inventories_informations.config(bd=0, relief="flat")
        self.tab_02_frame_inventories_informations.grid(row=1, column=0, pady=(10, 0), sticky="ew")
    
        # Allow stretching
        self.tab_02_frame_filter_entries.columnconfigure(2, weight=1)   # Stretch the column to fill the width
        parent_frame_02.columnconfigure(0, weight=1)                    # Stretch parent_frame_02
    
    def _f_view_create_widgets_in_tab_02_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_02 = tk.Frame(self.tab_02_frame_button_02)
        tab_02_button_container_02.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_02_button_export_all_data = tk.Button(tab_02_button_container_02, text="Export all data")
        self.tab_02_button_export_all_data.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_02_button_export_excel = tk.Button(tab_02_button_container_02, text="Export Excel")
        self.tab_02_button_export_excel.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_02_button_edit_slip = tk.Button(tab_02_button_container_02, text="Edit slip")
        self.tab_02_button_edit_slip.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_02_button_delete_slip = tk.Button(tab_02_button_container_02, text="Delete slip")
        self.tab_02_button_delete_slip.pack(side="left", padx=10)
    
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Adding handler
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    
    def event_tab_01_button_get_number_of_slip_click(self):        
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(self.tab_01_entry_so_phieu)
    
    def event_tab_01_button_add_row_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_button_add_row_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_YCDH, 
            self.tab_01_entry_id, 
            self.tab_01_entry_ma_hang, 
            self.tab_01_entry_ten_hang, 
            self.tab_01_entry_dvt, 
            self.tab_01_entry_sl_kha_dung, 
            self.tab_01_entry_nhu_cau, 
            self.tab_01_entry_sl_giu_cho, 
            self.tab_01_entry_sl_YCDH, 
            self.tab_01_entry_ghi_chu_mat_hang
            )
    
    def event_tab_01_button_update_row_click(self):
        Controller_handel_all_events.f_handle_event_update_selected_row_click(
        self.tab_01_label_footer_notification,
        self.tab_01_treeview_YCDH,
        self.tab_01_entry_ma_hang,
        self.tab_01_entry_ten_hang,
        self.tab_01_entry_dvt,
        self.tab_01_entry_sl_kha_dung,
        self.tab_01_entry_nhu_cau,
        self.tab_01_entry_sl_giu_cho,
        self.tab_01_entry_sl_YCDH,
        self.tab_01_entry_ghi_chu_mat_hang
        )
    
    def event_tab_01_button_delete_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_btn_delete_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_YCDH)
    
    def event_tab_01_button_clear_click(self):
        Controller_handel_all_events.f_handle_tab_01_button_clear_click(
            self.tab_01_label_footer_notification, 
            self.tab_01_treeview_YCDH)
        
    def event_tab_01_button_print_click(self):
        Controller_handel_all_events.f_handle_btn_print_click()
        
    def event_tab_01_button_save_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_btn_save_click(
            self.tab_01_label_footer_notification,
            self.tab_01_entry_so_phieu, 
            self.tab_01_entry_ma_khach_hang, 
            self.tab_01_entry_ten_khach_hang,
            self.tab_01_entry_mst,
            self.tab_01_entry_dia_chi,
            self._tab_01_entry_so_hop_dong,
            self.tab_01_entry_thong_tin_hop_dong,
            self.tab_01_entry_note_for_slip,
            self.tab_01_treeview_YCDH
        )    
    
    def event_tab_01_button_update_slip_click(self):
        elements_list = (
            self.tab_01_entry_so_phieu,
            self.tab_01_entry_ma_khach_hang,
            self.tab_01_entry_ten_khach_hang,
            self.tab_01_entry_mst,
            self.tab_01_entry_dia_chi,
            self._tab_01_entry_so_hop_dong,
            self.tab_01_entry_thong_tin_hop_dong,
            self.tab_01_entry_note_for_slip,
            self.tab_01_treeview_YCDH
            )
            
        Controller_handel_all_events.handle_event_tab_01_btn_update_slip_click(
            self.tab_01_label_footer_notification,
            elements_list
        )
    
    def event_tab_01_button_template_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_button_template_click(self.tab_01_label_footer_notification)
    
    def event_tab_01_button_get_import_file_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_button_get_import_file_click(self.tab_01_label_footer_notification)
    
    def event_tab_02_button_filter_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_button_filter_slip(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_log_of_YCDH,
            self.tab_02_entry_filter_slip_number, 
            self.tab_02_entry_filter_contract_number,
            self.tab_02_ngay_filter_bat_dau,
            self.tab_02_ngay_filter_ket_thuc,
            self.tab_02_entry_ma_khach_hang,
            self.tab_02_entry_ma_hang
            )
    
    def event_tab_02_button_clear_filter_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_button_clear_filter(
            self.tab_01_label_footer_notification, 
            self.tab_02_treeview_log_of_YCDH,
            self.tab_02_entry_filter_slip_number,
            self.tab_02_entry_filter_contract_number,
            self.tab_02_entry_ma_khach_hang,
            self.tab_02_entry_ten_khach_hang,
            self.tab_02_entry_ma_hang,
            self.tab_02_entry_ten_hang
        )
        
    def event_tab_02_button_export_excel_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_button_export_excel_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_log_of_YCDH
        )
        
    def event_tab_02_button_export_all_data_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_button_export_all_data_click(
            self.tab_01_label_footer_notification)
        
    def event_tab_02_button_edit_slip_click(self):
        elements_list = (
            self.tab_01_entry_ngay_tren_phieu,
            self.tab_01_entry_so_phieu,
            self.tab_01_entry_ma_khach_hang,
            self.tab_01_entry_ten_khach_hang,
            self.tab_01_entry_mst,
            self.tab_01_entry_dia_chi,
            self._tab_01_entry_so_hop_dong,
            self.tab_01_entry_thong_tin_hop_dong,
            self.tab_01_entry_note_for_slip,
            self.tab_02_treeview_log_of_YCDH,
            self.tab_01_treeview_YCDH
            )
            
        Controller_handel_all_events.handle_event_tab_02_button_edit_click(
            self.tab_01_label_footer_notification, 
            self.tab1,
            elements_list
        )
    
    def event_tab_02_button_delete_slip_click(self):
        Controller_handel_all_events.handle_event_tab_02_btn_delete_slip_click(
            self.tab_01_label_footer_notification, 
            self.tab_02_treeview_log_of_YCDH
        )
        # refresh data
        self.event_tab_02_button_filter_click()
    
    def f_view_treeview_of_tab_01_double_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_01_double_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_YCDH)

    def f_view_treeview_of_tab_01_single_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_01_single_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_YCDH,
            self.tab_01_entry_id,
            self.tab_01_entry_ma_hang,
            self.tab_01_entry_ten_hang,
            self.tab_01_entry_dvt,
            self.tab_01_entry_sl_kha_dung,
            self.tab_01_entry_nhu_cau,
            self.tab_01_entry_sl_giu_cho,
            self.tab_01_entry_sl_YCDH,
            self.tab_01_entry_ghi_chu_mat_hang)
        
    def f_view_treeview_of_tab_02_double_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_02_double_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_log_of_YCDH)

    def f_view_treeview_of_tab_02_single_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_02_single_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_log_of_YCDH)
        
