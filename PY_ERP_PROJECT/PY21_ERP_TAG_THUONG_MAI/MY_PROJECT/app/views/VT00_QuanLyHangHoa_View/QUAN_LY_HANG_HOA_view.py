import tkinter as tk
from tkinter import ttk
from app.views.Components_View import *
from app.utils import *
from .QUAN_LY_HANG_HOA_controller import Controller_handel_all_events

class cls_QuanLyHangHoa_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "VT00 | QUẢN LÝ DANH MỤC HÀNG HOÁ"
        name = "QUẢN LÝ DANH MỤC HÀNG HOÁ"
        super().__init__(title_of_form=title, name_of_slip=name)
        
        # call reuse components
        self.f_view_thay_doi_gia_tri_cua_base_form()
        self.f_view_create_all_container_frames_of_window()
        # set up formats
        self.f_set_up_format_of_tree_view()
        
        # Set up all global variants
        self.f_define_all_elements()
        # Set up when initializing
        self.f_set_up_when_initializing()
        self.f_set_command_for_elements()
        
    def f_set_up_when_initializing(self):
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(self.entry_so_phieu)
    
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
        
        self.tab_02_button_filter.config(command=self.event_tab_02_button_filter_click)
        self.tab_02_button_clear_filter.config(command=self.event_tab_02_button_clear_filter_click)
        self.tab_02_button_export_excel.config(command=self.event_tab_02_button_export_excel_click)
        self.tab_02_button_export_all_data.config(command=self.event_tab_02_button_export_all_data_click)
        
        self.tab_02_button_edit_slip.config(command=self.event_tab_02_button_edit_slip_click)
        self.tab_02_button_delete_slip.config(command=self.event_tab_02_button_delete_slip_click)
        self.tab_02_button_mark_expired.config(command=self.event_tab_02_button_mark_expired_click)
        
        # Gán sự kiện
        self.tab_01_treeview_YCDH.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_01_single_click)  # Single click
        self.tab_01_treeview_YCDH.bind("<Double-1>", self.f_view_treeview_of_tab_01_double_click)  # Double click
        
        self.tab_02_treeview_log_of_YCDH.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_02_single_click)  # Single click
        self.tab_02_treeview_log_of_YCDH.bind("<Double-1>", self.f_view_treeview_of_tab_02_double_click)  # Double click
        
    def f_define_all_elements(self):
        # Find in tab_01: Phiếu nhập kho
        tab_01_frame = self.tab1
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
        
        # Find in tab_04: Nhật ký phiếu nhập kho
        tab_04_frame = self.tab4_NHAT_KY_NHAP_KHO
        self.tab_04_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ma_khach_hang")
        self.tab_04_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ten_khach_hang")
        self.tab_04_entry_mst = f_utils_tim_component_with_name(tab_04_frame, "entry_mst")
        self.tab_04_entry_mst.pack_forget()
        self.tab_04_entry_dia_chi = f_utils_tim_component_with_name(tab_04_frame, "entry_dia_chi")
        self.tab_04_entry_dia_chi.pack_forget()
        self._tab_04_frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_04_frame, "frame_row_2_of_inventories_info")
        self._tab_04_frame_row_2_of_inventories_info.pack_forget()
        self.tab_04_entry_ma_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ma_hang")
        self.tab_04_entry_ten_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ten_hang")
        self.tab_04_ngay_filter_bat_dau = f_utils_tim_component_with_name(tab_04_frame, "start_date_entry")
        self.tab_04_ngay_filter_ket_thuc = f_utils_tim_component_with_name(tab_04_frame, "end_date_entry")
        
    def f_view_clear_content_when_sl_kha_dung_change(self, event):
        f_utils_on_entry_change(self.entry_sl_kha_dung)
        self.tab_01_entry_sl_thuc_nhap.delete(0, tk.END)
    
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
        notebook.tab(0, text="NHẬP KHO")
        notebook.tab(1, text="XUẤT KHO")
        notebook.tab(2, text="TẠO MỚI MÃ HÀNG")
        
        # Tab: Nhật ký nhập kho
        self.tab4_NHAT_KY_NHAP_KHO = ttk.Frame(notebook, name="tab_04")
        notebook.add(self.tab4_NHAT_KY_NHAP_KHO, text="NHẬT KÝ NHẬP KHO")
        # Tab: Nhật ký xuất kho
        self.tab5_frame_NHAT_KY_XUAT_KHO = ttk.Frame(notebook, name="tab_05")
        notebook.add(self.tab5_frame_NHAT_KY_XUAT_KHO, text="NHẬT KÝ XUẤT KHO")
        # Tab: Báo cáo tồn kho
        self.tab6_frame_BAO_CAO_TON_KHO = ttk.Frame(notebook, name="tab_06")
        notebook.add(self.tab6_frame_BAO_CAO_TON_KHO, text="BÁO CÁO TỒN KHO")
        
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
    
    def f_view_create_all_container_frames_of_window(self):
        # Create tabs
        self.tab_01_PHIEU_NHAP_KHO = self.tab1
        self.tab_02_PHIEU_XUAT_KHO = self.tab2
        self.tab_03_PHIEU_TAO_MOI_MA_HANG = self.tab3
        
        # Settings tab content
        self.f_view_create_all_container_frames_in_tab_01()
        self.f_view_create_all_container_frames_in_tab_04()
    
    def f_set_up_format_of_tree_view(self):
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_01(self.tab_01_treeview_PNK)
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_04(self.tab_04_treeview_log_of_PNK)
    
    def _f_setup_all_global_variants(self):    
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms
        self.label_footer = f_utils_tim_component_label_with_text(self, "Notification")

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

    def f_view_create_all_container_frames_in_tab_01(self):
        parent_frame = self.tab_01_PHIEU_NHAP_KHO

        # Frame H2
        self.tab_01_frame_H2 = tk.Frame(parent_frame)
        self.tab_01_frame_H2.grid(row=0, column=0, sticky="ew")

        self.f_view_create_widgets_in_tab_01_frame_H2()

        # Frame entries
        self.tab_01_frame_entries = tk.Frame(parent_frame)
        self.tab_01_frame_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_01_frame_entries()

        # Frame button
        self.tab_01_frame_button_of_treeview = tk.Frame(parent_frame)
        self.tab_01_frame_button_of_treeview.grid(row=2, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_01_frame_button_of_treeview()

        # Frame treeview
        self.tab_01_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_01_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self.f_view_create_widgets_in_tab_01_frame_treeview()
        
        # Frame button
        self.tab_01_frame_button_02 = tk.Frame(parent_frame)
        self.tab_01_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_01_frame_button_02()

        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)

    def f_view_create_widgets_in_tab_01_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_01_frame_H2, text="PHIẾU NHẬP KHO").pack(anchor="center")
     
    def f_view_create_widgets_in_tab_01_frame_entries(self):
        self.tab_01_container_frame_entries = tk.Frame(self.tab_01_frame_entries)
        self.tab_01_container_frame_entries.pack(side="top", 
                                                 fill="x"
                                                 )

        parent_frame = self.tab_01_container_frame_entries
        # Create container for date and number of slip
        self.Frame_container_date_and_number = tk.Frame(parent_frame)
        self.Frame_container_date_and_number.pack(side="top", 
                                                  fill="x"
                                                  )
        self.f_view_create_widgets_in_frame_date_and_number()

        # Create container for client and inventories
        self.Frame_clients_and_inventories_information = tk.Frame(parent_frame)
        self.Frame_clients_and_inventories_information.pack(side="top",
                                                            fill="x",  
                                                            pady=(5,0)
                                                            )
        self.f_view_create_widgets_in_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(parent_frame)
        self.frame_slip_informations.pack(side="top", 
                                          fill="x", 
                                          pady=(5,0)
                                          )
        self.f_view_create_widgets_in_frame_slip_informations()
    
    def f_view_create_widgets_in_frame_date_and_number(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number)
        self.frame_date_and_number.pack(anchor="center")

    def f_view_create_widgets_in_frame_clients_and_inventories(self):
        parent_frame = self.Frame_clients_and_inventories_information

        # Configure grid layout for parent frame
        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_rowconfigure(0, weight=1)

        # Create frame clients informations
        self.tab_01_frame_suppliers_information = cls_frame_suppliers_information_view(parent_frame)
        self.tab_01_frame_suppliers_information.config(bd=0, relief="flat")
        self.tab_01_frame_suppliers_information.grid(row=0, column=0, sticky="nsew")
        self.f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01()
        
        # Create frame inventories informations
        self.frame_inventories_informations_tab_01 = cls_frame_inventories_information_view(parent_frame)
        self.frame_inventories_informations_tab_01.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_01.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01()
            
    def f_view_create_widgets_in_frame_slip_informations(self):
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
        
    def f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = self.frame_inventories_informations_tab_01.frame_row_2
        
        self.tab_01_label_sl_thuc_nhap = tk.Label(parent_frame, text="SL thực nhập:")
        self.tab_01_label_sl_thuc_nhap.grid(row=0, column=4, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_thuc_nhap = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_thuc_nhap.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_sl_thuc_nhap.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_sl_thuc_nhap.grid(row=0, column=5, padx=(0, 10), pady=5, sticky="w")
        
        # Create a combobox with the options 'Kho A' and 'Kho B'
        values = ["Kho A", "Kho B"]
        self.tab_01_kho_nhap = tk.Label(parent_frame, text="Mã kho:")
        self.tab_01_kho_nhap.grid(row=0, column=6, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_combobox_ma_kho = cls_my_combobox_num_01(parent_frame, values=values)
        self.tab_01_combobox_ma_kho.grid(row=0, column=7, padx=(0, 10), pady=5, sticky="w")
        # Set the default value to the first item in the list
        self.tab_01_combobox_ma_kho.set(values[0])

        # Configure column weights for proper resizing
        parent_frame.columnconfigure(5, weight=1)  # Allow tab_01_entry_nhu_cau to expand
        parent_frame.columnconfigure(7, weight=1)  # Allow tab_01_entry_sl_giu_cho to expand
        parent_frame.columnconfigure(9, weight=1)  # Allow tab_01_entry_sl_YCDH to expand
        
        self.f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01()
    
    def f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = tk.Frame(self.frame_inventories_informations_tab_01)
        parent_frame.pack(side="bottom", fill="x", expand=True)

        tk.Label(parent_frame, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_01_entry_ghi_chu_mat_hang = cls_my_text_entry_num_01(parent_frame)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
    def f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_01(self):
        # create parent_frame
        parent_frame = cls_frame_contracts_management_view(self.tab_01_frame_suppliers_information)
        parent_frame.pack(side="bottom", fill="x", expand=True)

    def f_view_create_widgets_in_tab_01_frame_button_of_treeview(self):
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
    
    def f_view_create_widgets_in_tab_01_frame_treeview(self):
        self.tab_01_frame_treeview = self.tab_01_frame_treeview
        self.table_of_tab_01 = self.tab_01_frame_treeview.treeview_normal
        self.treeview_test_of_tag_01 = self.tab_01_frame_treeview.treeview_normal
        # self.treeview_test_of_tag_01.bind("<ButtonRelease-1>", self.f_view_table_of_tab_01_click)
        
    def f_view_create_widgets_in_tab_04_frame_treeview(self):
        self.tab_04_frame_treeview = self.tab_04_frame_treeview
        self.treeview_of_tab_04 = self.tab_04_frame_treeview.treeview_normal
        self.tab_04_treeview = self.tab_04_frame_treeview.treeview_normal
        self.tab_04_treeview.bind("<ButtonRelease-1>", self.f_view_table_of_tab_04_click)
    
    def f_view_create_widgets_in_tab_01_frame_button_02(self):
        parent_frame = self.tab_01_frame_button_02
        # Create a sub-frame on the right
        tab_01_button_container_02_on_the_right = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_01_button_container_02_on_the_left = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # BTN test
        self.tab_01_button_save_02 = tk.Button(tab_01_button_container_02_on_the_right, 
                                               text="Test save 02", 
                                               background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
                                               command=self.f_tab_01_button_save_02_click)
        
        # BTN test
        self.tab_01_button_export = tk.Button(tab_01_button_container_02_on_the_right, 
                                              text="Test save 01", 
                                              background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
                                              command=self.f_tab_01_button_export_click)
        
        # BTN test
        self.tab_01_print_config = tk.Button(tab_01_button_container_02_on_the_right, 
                                             text="Test in cấu hình của bảng", 
                                             background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
                                             )
        # self.tab_01_print_config.config(command=self.f_button_print_config_click)
        
        # BTN test
        self.tab_01_config_num_02 = tk.Button(tab_01_button_container_02_on_the_right, 
                                              text="Test print form print từ code", 
                                              background=COLOR_BACKGROUND_NUM_02_DARK_GRAY, 
                                              command=self.f_tab_01_button_print_form_tu_tao_tu_code_click)
        
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

    def f_view_set_up_formats_of_tab_01(self):
        print("self.f_view_set_format_of_treeview_of_tab_01()")
    
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_04: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    
    def f_view_create_all_container_frames_in_tab_04(self):
        parent_frame = self.tab4_NHAT_KY_NHAP_KHO

        # Frame H2
        self.tab_04_frame_H2 = tk.Frame(parent_frame)
        self.tab_04_frame_H2.grid(row=0, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_04_frame_H2()

        # Frame entries
        self.tab_04_frame_filter_entries = tk.Frame(parent_frame)
        self.tab_04_frame_filter_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_04_frame_filter_entries()

        # Frame button
        self.tab_04_frame_button_01 = tk.Frame(parent_frame)
        self.tab_04_frame_button_01.grid(row=2, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_04_frame_button_01()
        
        # Frame treeview
        self.tab_04_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_04_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self.f_view_create_widgets_in_tab_04_frame_treeview()
        
        # Frame button
        self.tab_04_frame_button_02 = tk.Frame(parent_frame)
        self.tab_04_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_04_frame_button_02()
        
        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)

    def f_view_create_widgets_in_tab_04_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_04_frame_H2, text="NHẬT KÝ NHẬP KHO").pack(anchor="center")
     
    def f_view_create_widgets_in_tab_04_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        tab_04_button_container_01 = tk.Frame(self.tab_04_frame_button_01)
        tab_04_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_04_button_add = tk.Button(tab_04_button_container_01, text="Filter")
        self.tab_04_button_add.config(command=self.f_tab_04_button_filter_click)
        self.tab_04_button_add.pack(side="left", padx=10)
        
        # Delete update
        self.tab_04_button_clear = tk.Button(tab_04_button_container_01, text="Clear")
        self.tab_04_button_clear.config(command=self.f_tab_04_button_clear_click)
        self.tab_04_button_clear.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_04_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_04_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        parent_frame_01 = tk.Frame(self.tab_04_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        parent_frame_02 = tk.Frame(self.tab_04_frame_filter_entries)
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
        self.tab_04_frame_seclect_date = cls_frame_DateSelector_view(parent_frame_01)
        self.tab_04_frame_seclect_date.config(bd=0, relief="flat")
        self.tab_04_frame_seclect_date.grid(row=0, column=0, sticky="ew")
        
        # Create frame clients informations
        self.tab_04_frame_clients_informations = cls_frame_client_information_view(parent_frame_02)
        self.tab_04_frame_clients_informations.config(bd=0, relief="flat")
        self.tab_04_frame_clients_informations.grid(row=0, column=0, sticky="ew")
        
        # Create frame inventories informations
        self.tab_04_frame_inventories_information = cls_frame_inventories_information_view(parent_frame_02)
        self.tab_04_frame_inventories_information.config(bd=0, relief="flat")
        self.tab_04_frame_inventories_information.grid(row=1, column=0, pady=(10, 0), sticky="ew")
    
        # Allow stretching
        self.tab_04_frame_filter_entries.columnconfigure(2, weight=1)   # Stretch the column to fill the width
        parent_frame_02.columnconfigure(0, weight=1)                    # Stretch parent_frame_02
    
    def f_view_create_widgets_in_tab_04_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        tab_04_button_container_02 = tk.Frame(self.tab_04_frame_button_02)
        tab_04_button_container_02.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_04_button_export_excel = tk.Button(tab_04_button_container_02, text="Export Excel")
        self.tab_04_button_export_excel.config(command=self.f_tab_04_button_export_excel_click)
        self.tab_04_button_export_excel.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_04_button_edit = tk.Button(tab_04_button_container_02, text="EDIT")
        self.tab_04_button_edit.config(command=self.f_tab_04_button_edit_click)
        self.tab_04_button_edit.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_04_button_DELETE = tk.Button(tab_04_button_container_02, text="DELETE")
        self.tab_04_button_DELETE.config(command=self.f_tab_04_button_delete_click)
        self.tab_04_button_DELETE.pack(side="left", padx=10)
    
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # All click event
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    
    def f_view_tab_01_button_clear_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)

    def f_tab_01_button_print_form_tu_tao_tu_code_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_01_button_print_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_01_button_get_number_of_slip_click(self):        
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_01_button_import_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_01_button_template_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_01_button_get_import_file_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)

    def f_view_tab_01_button_add_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_view_tab_01_button_delete_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_view_tab_01_button_update_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_01_button_export_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_01_button_save_02_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_01_button_save_03_click(self):        
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)

    def f_tab_04_button_filter_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_04_button_clear_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_04_button_export_excel_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_tab_04_button_edit_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_04_button_delete_click(self):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
        
    def f_view_table_of_tab_04_click(self, event):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)
    
    def f_tab_04_table_on_click(self, event):
        if not notification_text and not fg:
            notification_text = "..."
            fg = "blue"
        utils_controller_config_notification_250220_10h05.f_config_notification(self.label_footer, notification_text, fg=fg)


    