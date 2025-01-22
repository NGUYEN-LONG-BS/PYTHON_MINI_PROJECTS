import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import json
from Components_View import *
from Components_View import cls_frame_normal
from Components_View.treeview import cls_Treeview_frame_number_01
from utils import *
from test_Controller import cls_test_Controller, cls_test_Controller_02_treeview, cls_test_Controller_03_auto_update_number


class cls_test_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD02 | QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        name = "QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        super().__init__(title_of_form=title, name_of_slip=name)
        # Create all functions
        self.f_view_add_MVC_class()
        # call reuse components
        self._f_view_thay_doi_gia_tri_cua_base_form()
        self._f_view_create_all_container_frames_of_window()
        # set up formats
        self._f_view_set_up_formats()
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        # Set up all global variants
        self._f_setup_all_global_variants()
        self._f_setup_all_binding()
        
        self.f_add_controller_02_treeview()
        self.f_add_controller_03_treeview()
    
    def _f_setup_all_binding(self):
        self.entry_sl_kha_dung = f_utils_tim_component_with_name(self, "entry_sl_kha_dung")
        # self.entry_sl_kha_dung.bind("<FocusOut>", lambda event: f_utils_on_entry_change(self.entry_sl_kha_dung))
        self.entry_sl_kha_dung.bind("<FocusOut>", self.f_view_clear_content_when_sl_kha_dung_change)
        
        self.entry_ma_hang = f_utils_tim_component_with_name(self, "entry_ma_hang")
        self.entry_ten_hang = f_utils_tim_component_with_name(self, "entry_sl_ten_hang")
        self.entry_dvt = f_utils_tim_component_with_name(self, "entry_dvt")
    
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
        
    def _f_setup_all_global_variants(self):    
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms
        self.label_footer = f_utils_tim_component_label_with_text(self, "Notification")

    def f_view_add_MVC_class(self):
        # Initialize controller_01
        self.controller_01 = cls_test_Controller()
        self.controller_01.view = self

    def f_add_controller_02_treeview(self):
        # Initialize controller_02
        tree = self.table_of_tab_01
        entry_ma_hh = self.tab_01_entry_nhu_cau
        entry_ten_hh = self.tab_01_entry_nhu_cau
        entry_so_luong = self.tab_01_entry_nhu_cau
        entry_ghi_chu = self.tab_01_entry_nhu_cau
        self.controller_02_treeview = cls_test_Controller_02_treeview(tree, entry_ma_hh, entry_ten_hh, entry_so_luong, entry_ghi_chu)
        self.controller_02_treeview.view = self
    
    def f_add_controller_03_treeview(self):
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
        self._f_view_create_in_tab_01_all_container_frames()
        self._f_view_create_in_tab_02_all_container_frames()
        
    def _f_view_create_in_tab_01_all_container_frames(self):
        # Frame H2
        self.tab_01_frame_H2 = cls_frame_normal(self.tab_01)
        # self.tab_01_frame_H2.pack(fill="both", expand=True)
        self.tab_01_frame_H2.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_H2()

        # Frame entries
        self.tab_01_frame_entries = cls_frame_normal(self.tab_01)
        self.tab_01_frame_entries.pack(side="top", fill="x")
        # self.tab_01_frame_entries.pack(padx=20, pady=20)
        self._f_view_create_widgets_in_tab_01_frame_entries()

        # Frame button
        self.tab_01_frame_button_of_treeview = tk.Frame(self.tab_01)
        self.tab_01_frame_button_of_treeview.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_button_of_treeview()

        # Frame treeview
        self.tab_01_frame_treeview = cls_Treeview_frame_number_01(self.tab_01)
        self.tab_01_frame_treeview.pack(side="top", fill="both", expand=True)
        self._f_view_create_widgets_in_tab_01_frame_treeview()
        
        # Frame button
        self.tab_01_frame_button_02 = tk.Frame(self.tab_01)
        self.tab_01_frame_button_02.pack(side="bottom", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_button_02()

    def _f_view_create_in_tab_02_all_container_frames(self):
        # Frame H2
        self.tab_02_frame_H2 = cls_frame_normal(self.tab_02)
        self.tab_02_frame_H2.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_02_frame_H2()

        # Frame entries
        self.tab_02_frame_entries = cls_frame_normal(self.tab_02)
        self.tab_02_frame_entries.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_02_frame_entries()

        # Frame button
        self.tab_02_frame_button_01 = tk.Frame(self.tab_02)
        self.tab_02_frame_button_01.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_02_frame_button_01()
        
        # Frame treeview
        self.tab_02_frame_treeview = cls_Treeview_frame_number_01(self.tab_02)
        self.tab_02_frame_treeview.pack(side="top", fill="both", expand=True)
        self._f_view_create_widgets_in_tab_02_frame_treeview()
        
        # Frame button
        self.tab_02_frame_button_02 = tk.Frame(self.tab_02)
        self.tab_02_frame_button_02.pack(side="bottom", fill="x")
        self._f_view_create_widgets_in_tab_02_frame_button_02()

    def _f_view_create_widgets_in_tab_01_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_01_frame_H2, text="PHIẾU YÊU CẦU ĐẶT HÀNG").pack(anchor="center")
    
    def _f_view_create_widgets_in_tab_02_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_02_frame_H2, text="NHẬT KÝ YÊU CẦU ĐẶT HÀNG").pack(anchor="center")
        
    def _f_view_create_widgets_in_tab_01_frame_entries(self):
        self.tab_01_container_frame_entries = tk.Frame(self.tab_01_frame_entries)
        self.tab_01_container_frame_entries.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_tab_01_container_frame_entries()

    def _f_view_create_widgets_in_tab_02_frame_entries(self):
        self.frame_entries_of_tab_02 = tk.Frame(self.tab_02_frame_entries)
        self.frame_entries_of_tab_02.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_frame_entries_of_tab_02()
        
    def _f_view_create_widgets_in_tab_01_container_frame_entries(self):
        # Create container for date and number of slip
        self.Frame_container_date_and_number = tk.Frame(self.tab_01_container_frame_entries)
        self.Frame_container_date_and_number.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_frame_date_and_number()

        # Create container for client and inventories
        self.Frame_clients_and_inventories_information = tk.Frame(self.tab_01_container_frame_entries)
        self.Frame_clients_and_inventories_information.pack(side="top", fill="x", expand=True, pady=(5,0))
        self._f_view_create_widgets_in_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(self.tab_01_container_frame_entries)
        self.frame_slip_informations.pack(side="top", fill="x", expand=True, pady=(5,0))
        self._f_view_create_widgets_in_frame_slip_informations()

    def _f_view_create_widgets_in_frame_entries_of_tab_02(self):
        # Create container for filter
        self.Frame_container_filter_entries = tk.Frame(self.frame_entries_of_tab_02)
        self.Frame_container_filter_entries.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_frame_filter_entries()
        
    def _f_view_create_widgets_in_frame_date_and_number(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number)
        self.frame_date_and_number.pack(anchor="center")

    def _f_view_create_widgets_in_frame_filter_entries(self):
        # Create frame clients informations
        self.frame_clients_informations_tab_02 = cls_frame_client_information_view(self.Frame_container_filter_entries)
        self.frame_clients_informations_tab_02.config(bd=0, relief="flat")
        self.frame_clients_informations_tab_02.pack(side="left", fill="both", expand=True)
        
        # Create frame inventories informations
        self.frame_inventories_informations_tab_02 = cls_frame_inventories_information_view(self.Frame_container_filter_entries)
        self.frame_inventories_informations_tab_02.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_02.pack(side="left", fill="both", expand=True, padx=(10,0))

    def _f_view_create_widgets_in_frame_clients_and_inventories(self):
        # Create frame clients informations
        self.frame_clients_informations_tab_01 = cls_frame_client_information_view(self.Frame_clients_and_inventories_information)
        self.frame_clients_informations_tab_01.config(bd=0, relief="flat")
        self.frame_clients_informations_tab_01.pack(side="left", fill="both", expand=True)
        self._f_view_add_row_03_into_frame_clients_informations_tab_01()
        
        # Create frame inventories informations
        self.frame_inventories_informations_tab_01 = cls_frame_inventories_information_view(self.Frame_clients_and_inventories_information)
        self.frame_inventories_informations_tab_01.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_01.pack(side="left", fill="both", expand=True, padx=(10,0))
        self._f_view_add_widget_into_frame_inventories_informations_tab_01()
        
        
    def _f_view_create_widgets_in_frame_slip_informations(self):
        # Input fields
        tk.Label(self.frame_slip_informations, text="STT:").pack(side="left")
        self.tab_01_entry_id = tk.Entry(self.frame_slip_informations)
        self.tab_01_entry_id.pack(side="left")
        self.tab_01_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_01_note_for_slip = cls_my_text_entry_num_01(self.frame_slip_informations)
        self.tab_01_note_for_slip.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_note_for_slip.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_note_for_slip.pack(side="left", fill="x", expand=True, pady=10)
        
    def _f_view_add_widget_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = self.frame_inventories_informations_tab_01.frame_row_2
        
        self.label13_nhu_cau = tk.Label(parent_frame, text="nhu cầu:").pack(side="left")
        self.tab_01_entry_nhu_cau = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_nhu_cau.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_nhu_cau.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_nhu_cau.pack(side="left")
        
        tk.Label(parent_frame, text="SL giữ chỗ:").pack(side="left")
        self.tab_01_entry_sl_giu_cho = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_giu_cho.config(state="readonly")
        self.tab_01_entry_sl_giu_cho.pack(side="left")
        
        tk.Label(parent_frame, text="SL YCĐH:").pack(side="left")
        self.tab_01_entry_sl_YCDH = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_YCDH.config(state="readonly")
        self.tab_01_entry_sl_YCDH.pack(side="left")
        
        self._f_view_add_row_03_into_frame_inventories_informations_tab_01()
    
    def _f_view_add_row_03_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = tk.Frame(self.frame_inventories_informations_tab_01)
        parent_frame.pack(side="bottom", fill="x", expand=True)

        tk.Label(parent_frame, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_01_entry_ghi_chu_mat_hang = cls_my_text_entry_num_01(parent_frame)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_ghi_chu_mat_hang.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
    def _f_view_add_row_03_into_frame_clients_informations_tab_01(self):
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
        
        # Delete update
        self.tab_01_button_update = tk.Button(tab_01_button_container_01, text="Update Row", command=self.f_view_tab_01_button_update_click)
        self.tab_01_button_update.pack(side="left", padx=10)
        
        # Delete button
        self.tab_01_button_delete = tk.Button(tab_01_button_container_01, text="Delete Row", command=self.f_view_tab_01_button_delete_click)
        self.tab_01_button_delete.pack(side="left", padx=10)
        
        # Clear button
        self.tab_01_button_clear = tk.Button(tab_01_button_container_01, text="Clear Rows", command=self.f_view_tab_01_button_clear_click)
        self.tab_01_button_clear.pack(side="left", padx=10)

    def _f_view_create_widgets_in_tab_02_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_01 = tk.Frame(self.tab_02_frame_button_01)
        tab_02_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_01_button_add = tk.Button(tab_02_button_container_01, text="Filter")
        self.tab_01_button_add.pack(side="left", padx=10)
        
        # Delete update
        self.tab_01_button_update = tk.Button(tab_02_button_container_01, text="Reset")
        self.tab_01_button_update.pack(side="left", padx=10)

    def f_view_tab_01_button_delete_click(self):
        print("Delete Row tab 01")

    def f_view_tab_01_button_update_click(self):
        print("Update Row tab 01")
        
    def f_view_tab_01_button_clear_click(self):
        print("Clear Rows tab 01")
        
    def _f_view_create_widgets_in_tab_01_frame_treeview(self):
        self.tab_01_frame_treeview = self.tab_01_frame_treeview
        self.table_of_tab_01 = self.tab_01_frame_treeview.treeview_normal
        self.treeview_test_of_tag_01 = self.tab_01_frame_treeview.treeview_normal
        self.treeview_test_of_tag_01.bind("<ButtonRelease-1>", self.f_view_table_of_tab_01_click)
        
    def _f_view_create_widgets_in_tab_02_frame_treeview(self):
        self.tab_02_frame_treeview = self.tab_02_frame_treeview
        self.table_of_tab_02 = self.tab_02_frame_treeview.treeview_normal
        self.treeview_test_of_tag_02 = self.tab_02_frame_treeview.treeview_normal
        self.treeview_test_of_tag_02.bind("<ButtonRelease-1>", self.f_view_table_of_tab_02_click)
    
    def _f_view_create_widgets_in_tab_01_frame_button_02(self):
        # Create a sub-frame on the right
        tab_01_button_container_02_on_the_right = tk.Frame(self.tab_01_frame_button_02)
        tab_01_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_01_button_container_02_on_the_left = tk.Frame(self.tab_01_frame_button_02)
        tab_01_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # Export Data button
        self.tab_01_button_save_03 = tk.Button(tab_01_button_container_02_on_the_right, text="SAVE 03", command=self.f_tab_01_button_save_03_click)
        self.tab_01_button_save_03.pack(side="right", padx=10)
        
        # Export Data button
        self.tab_01_button_save_02 = tk.Button(tab_01_button_container_02_on_the_right, text="SAVE 02", command=self.f_tab_01_button_save_02_click)
        self.tab_01_button_save_02.pack(side="right", padx=10)
        
        # Export Data button
        self.tab_01_button_export = tk.Button(tab_01_button_container_02_on_the_right, text="SAVE", command=self.f_tab_01_button_export_click)
        self.tab_01_button_export.pack(side="right", padx=10)
        
        # Get Data button
        self.tab_01_button_get = tk.Button(tab_01_button_container_02_on_the_right, text="Print Data Array", command=self.f_tab_01_button_get_click)
        self.tab_01_button_get.pack(side="right", padx=10)
        
        # print button
        self.tab_01_print_config = tk.Button(tab_01_button_container_02_on_the_right, text="in cấu hình của bảng", command=self.f_button_print_config_click)
        self.tab_01_print_config.pack(side="right", padx=10)
        
        # print button
        self.tab_01_config_num_02 = tk.Button(tab_01_button_container_02_on_the_right, text="Print", command=self.f_tab_01_button_print_click)
        self.tab_01_config_num_02.pack(side="right", padx=10)
        
        # print button
        self.tab_01_button_print_02 = tk.Button(tab_01_button_container_02_on_the_right, text="Print 02", command=self.f_tab_01_button_print_02_click)
        self.tab_01_button_print_02.pack(side="right", padx=10)
        
        # temp button
        self.tab_01_btn_template = tk.Button(tab_01_button_container_02_on_the_left, text="TEMPLATE", command=self.f_tab_01_button_template_click)
        self.tab_01_btn_template.pack(side="left", padx=10)
        
        # get file button
        self.tab_01_btn_get_import_file = tk.Button(tab_01_button_container_02_on_the_left, text="GET FILE", command=self.f_tab_01_button_get_import_file_click)
        self.tab_01_btn_get_import_file.pack(side="left", padx=10)
        
        # import button
        self.tab_01_btn_import = tk.Button(tab_01_button_container_02_on_the_left, text="Import Excel", command=self.f_tab_01_button_import_click)
        self.tab_01_btn_import.pack(side="left", padx=10)
        
        # star import button
        self.tab_01_btn_start_import_file = tk.Button(tab_01_button_container_02_on_the_left, text="START IMPORT")
        self.tab_01_btn_start_import_file.pack(side="left", padx=10)
        
    def _f_view_create_widgets_in_tab_02_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_02 = tk.Frame(self.tab_02_frame_button_02)
        tab_02_button_container_02.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_02_button_edit = tk.Button(tab_02_button_container_02, text="EDIT")
        self.tab_02_button_edit.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_02_button_DELETE = tk.Button(tab_02_button_container_02, text="DELETE")
        self.tab_02_button_DELETE.pack(side="left", padx=10)
        
    def f_tab_01_button_print_click(self):
        print("f_tab_01_button_print_click")
        f_utils_create_print_template()
        
    def f_tab_01_button_print_02_click(self):
        print("f_tab_01_button_print_02_click")
        self.controller_01.f_controller_handle_btn_print_02_click_()
    
    def f_tab_01_button_import_click(self):
        print("Import config")
        
    def f_tab_01_button_template_click(self):
        self._f_config_notification(f_utils_create_template_excel_file(),"black")
        
    def f_tab_01_button_get_import_file_click(self):
        self._f_config_notification(f_utils_open_file(),"black")
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Event Handlers of tab number 01
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def f_tab_01_button_get_click(self):
        self._f_config_notification(text=self.controller_01.f_get_data(self.table_of_tab_01), fg="blue")
        
    def f_view_tab_01_button_add_click(self):
        # Update the row count
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        id_value = self.tab_01_entry_id.get()
        ma_hang = self.entry_ma_hang.get()
        ten_hang = self.entry_ten_hang.get()
        dvt = self.entry_dvt.get()
        
        sl_kha_dung = float(self.entry_sl_kha_dung.get().replace(',', '') or 0)
        sl_nhu_cau = float(self.tab_01_entry_nhu_cau.get().replace(',', '') or 0)
        sl_giu_cho = float(self.tab_01_entry_sl_giu_cho.get().replace(',', '') or 0)
        sl_yeu_cau_dat_hang = float(self.tab_01_entry_sl_YCDH.get().replace(',', '') or 0)
        ghi_chu_mat_hang = self.tab_01_entry_ghi_chu_mat_hang.get()
        table = self.table_of_tab_01
        
        # Validate input using the helper function
        is_valid, error_message = self.controller_01.f_controller_add_row(id_value, ma_hang, ten_hang, dvt, sl_kha_dung, sl_nhu_cau, sl_giu_cho, sl_yeu_cau_dat_hang, ghi_chu_mat_hang, table)
        if not is_valid:
            # Show error message
            self._f_config_notification(text=error_message, fg="red")
            # return
        else:
            # Show success message
            self._f_config_notification(text=error_message, fg="green")
            self.f_clear_input_fileds_of_tab_01()
        
        # Update the row count
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        
    def _f_view_set_rows_count_of_treeview_01_when_add_new_row(self):
        row_count = 1 + self.controller_01.f_controller_get_row_count(self.table_of_tab_01)
        self.tab_01_entry_id.config(state="normal")  # Enable the Entry widget to update the value
        self.tab_01_entry_id.delete(0, tk.END)  # Clear the existing value
        self.tab_01_entry_id.insert(0, row_count)  # Insert the new value (ID)
        self.tab_01_entry_id.config(state="disabled")  # Disable the Entry widget again
    
    def _f_config_notification(self, text="", fg="black"):
        self.label_footer.config(text=text, fg=fg)
    
    def f_tab_01_button_export_click(self):
        text = self.controller_01.f_export_data_to_SQL(self.table_of_tab_01)
        self._f_config_notification(text=text, fg="blue")
        
    def f_tab_01_button_save_02_click(self):
        text = self.controller_01.f_controller_handle_btn_save_02_click_(self.table_of_tab_01)
        self._f_config_notification(text=text, fg="blue")
    
    def f_tab_01_button_save_03_click(self):        
        text = self.controller_02_treeview.print_data()
        self._f_config_notification(text=text, fg="blue")

    def _f_view_set_up_formats(self):
        self.f_tab_01_button_config_02_click()
        
    def f_tab_01_button_config_02_click(self):
        # Clear the existing columns
        self.treeview_test_of_tag_01.delete(*self.treeview_test_of_tag_01.get_children())
        for col in self.treeview_test_of_tag_01["columns"]:
            self.treeview_test_of_tag_01.heading(col, text="")  # Remove headings
        
        # Trước khi cấu hình, phải thiết lập cột cho Treeview
        tab_01_table_column_names = self.controller_01.f_get_table_config_name_only()
        self.treeview_test_of_tag_01["columns"] = tab_01_table_column_names
        
        # Treeview config
        list_table_of_tab_01_column_configs, list_table_of_tab_01_column_names, tuple_table_of_tab_01_header_font = self.controller_01.f_tab_01_button_config_click(self.table_of_tab_01)
        for config, col in zip(list_table_of_tab_01_column_configs, list_table_of_tab_01_column_names):
            # Configure each column
            self.treeview_test_of_tag_01.heading(col, text=col)  # Set header text
            self.treeview_test_of_tag_01.column(
                col,
                width=config["width"],
                minwidth=config["min_width"],
                anchor=config["anchor"],
                stretch=config["stretch"]
            )
            # Set the header font style
            style = ttk.Style()
            style.configure("Treeview.Heading", font=tuple_table_of_tab_01_header_font)
            
            # Apply the background and font settings
            # Apply row styles if needed
            for row in self.treeview_test_of_tag_01.get_children():
                self.treeview_test_of_tag_01.item(row, tags=(row,))
                self.treeview_test_of_tag_01.tag_configure(
                    row,
                    background=config["background_color"],
                    foreground=config["foreground_color"]
                    )
    
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
    
    def f_view_table_of_tab_01_click(self, event):
        # Call the controller_01 to handle the event
        self.current_time = time.time()
        is_double_click = self.controller_01.f_handle_event_click_on_table_of_tab_01(self.last_click_time, self.current_time, self.double_click_interval)
        # Update last click time only after handling
        self.last_click_time = self.current_time
        # Handle the action for single and double click
        if is_double_click:
            self.controller_01.f_tab_01_table_double_click(event)
        else:
            id_value, ma_hang, ten_hang, dvt, sl_giu_cho, sl_dat_hang, ghi_chu_mat_hang = self.controller_01.f_tab_01_table_single_click(event)
            # Clear and update the Entry widgets if values are returned
            if id_value is not None:
                self.tab_01_entry_id.config(state="normal")  # Enable the Entry widget to update the value
                self.tab_01_entry_id.delete(0, tk.END)
                self.tab_01_entry_id.insert(0, id_value)
                self.tab_01_entry_id.config(state="disabled")  # Disable the Entry widget again

            if ghi_chu_mat_hang is not None:
                self.tab_01_entry_ghi_chu_mat_hang.delete(0, tk.END)
                self.tab_01_entry_ghi_chu_mat_hang.insert(0, ghi_chu_mat_hang)

            if ma_hang is not None:
                self.entry_ma_hang.delete(0, tk.END)
                self.entry_ma_hang.insert(0, ma_hang)
                
            if ten_hang is not None:
                self.entry_ten_hang.delete(0, tk.END)
                self.entry_ten_hang.insert(0, ten_hang)
                
            if dvt is not None:
                self.entry_dvt.delete(0, tk.END)
                self.entry_dvt.insert(0, dvt)
            
            if sl_giu_cho is not None:
                self.tab_01_entry_sl_giu_cho.config(state="normal")
                self.tab_01_entry_sl_giu_cho.delete(0, tk.END)
                if float(sl_giu_cho).is_integer():  # Nếu là số nguyên
                    formatted_sl_giu_cho = f"{int(float(sl_giu_cho)):,}"
                else:  # Nếu là số thập phân
                    formatted_sl_giu_cho = f"{float(sl_giu_cho):,.2f}"
                self.tab_01_entry_sl_giu_cho.insert(0, formatted_sl_giu_cho)
                self.tab_01_entry_sl_giu_cho.config(state="disabled")
                
            if sl_dat_hang is not None:
                self.tab_01_entry_sl_YCDH.config(state="normal")
                self.tab_01_entry_sl_YCDH.delete(0, tk.END)
                if float(sl_dat_hang).is_integer():  # Nếu là số nguyên
                    formatted_sl_dat_hang = f"{int(float(sl_dat_hang)):,}"
                else:  # Nếu là số thập phân
                    formatted_sl_dat_hang = f"{float(sl_dat_hang):,.2f}"
                self.tab_01_entry_sl_YCDH.insert(0, formatted_sl_dat_hang)
                self.tab_01_entry_sl_YCDH.config(state="disabled")
            
            # Update the value of sl_nhu_cau
            sl_giu_cho = self.tab_01_entry_sl_giu_cho.get().replace(",", "")
            sl_dat_hang = self.tab_01_entry_sl_YCDH.get().replace(",", "")
            sl_nhu_cau = float(sl_giu_cho) + float(sl_dat_hang)
            if sl_nhu_cau.is_integer():  # Nếu là số nguyên
                formatted_sl_nhu_cau = f"{int(sl_nhu_cau):,}"
            else:  # Nếu là số thập phân
                formatted_sl_nhu_cau = f"{sl_nhu_cau:,.2f}"
            
            self.tab_01_entry_nhu_cau.delete(0, tk.END)
            self.tab_01_entry_nhu_cau.insert(0, formatted_sl_nhu_cau)
    
    def f_view_clear_content_when_sl_kha_dung_change(self, event):
        f_utils_on_entry_change(self.entry_sl_kha_dung)
        self.tab_01_entry_nhu_cau.delete(0, tk.END)
        self.tab_01_entry_sl_giu_cho.delete(0, tk.END)
        self.tab_01_entry_sl_YCDH.delete(0, tk.END)
    
    def f_view_table_of_tab_02_click(self, event):
        self.current_time = time.time()

    
    def f_tab_02_table_on_click(self, event):
        print("f_tab_02_table_on_click")    

    def f_clear_input_fileds_of_tab_01(self):
        self.tab_01_entry_id.delete(0, tk.END)
        self.tab_01_entry_ghi_chu_mat_hang.delete(0, tk.END)
        self.tab_01_entry_sl_YCDH.delete(0, tk.END)
        
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Event Handlers of tab number 02
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def f_tab_02_button_get_click(self):
        print("Get Data tab 02")

    def f_tab_02_button_add_click(self):
        print("Add Row tab 02")
        
    def f_tab_02_button_export_click(self):
        print("Export Data to SQL tab 02")
        
    def f_table_tab_02_click(self, event):
        print("Table tab 02 click")