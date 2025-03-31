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
        
        # Step-01: create components
        self.f_view_thay_doi_gia_tri_cua_base_form()
        self.f_view_create_all_container_frames_of_window()
        self.f_define_all_elements()
        
        # # Step-02: setting and formating
        self.f_set_up_format_of_tree_view()
        self.f_set_up_when_initializing()
        self.f_set_command_for_elements()

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
        self.tab5_NHAT_KY_XUAT_KHO = ttk.Frame(notebook, name="tab_05")
        notebook.add(self.tab5_NHAT_KY_XUAT_KHO, text="NHẬT KÝ XUẤT KHO")
        # Tab: Báo cáo tồn kho
        self.tab6_BAO_CAO_TON_KHO = ttk.Frame(notebook, name="tab_06")
        notebook.add(self.tab6_BAO_CAO_TON_KHO, text="BÁO CÁO TỒN KHO")
        
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
        # Nhập kho
        self.f_view_create_all_container_frames_in_tab_01()
        self.f_view_create_all_container_frames_in_tab_04()
        # Xuất kho
        self.f_view_create_all_container_frames_in_tab_02()
        self.f_view_create_all_container_frames_in_tab_05()
        # Báo cáo tồn kho
        self.f_view_create_all_container_frames_in_tab_06()
        # Tạo mới mã hàng
        self.f_view_create_all_container_frames_in_tab_03()

    def f_set_up_when_initializing(self):
        # Update entry id
        Controller_handel_all_events.update_entry_id_when_initializing(self.tab_01_treeview_PNK, self.tab_01_entry_id)
        Controller_handel_all_events.update_entry_id_when_initializing(self.tab_02_treeview_PXK, self.tab_02_entry_id)
        # Update entry slip number
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip_PNK(self.tab_01_entry_so_phieu)
        Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip_PXK(self.tab_02_entry_so_phieu)
        # Load data to all treeviews
        self.event_tab_06_button_filter_click()
    
    def f_set_command_for_elements(self):
        # Tab 01
        self.tab_01_button_add.config(command=self.event_tab_01_button_add_row_click)
        self.tab_01_button_update_row_in_treeview.config(command=self.event_tab_01_button_update_row_click)
        self.tab_01_button_delete.config(command=self.event_tab_01_button_delete_click)
        self.tab_01_button_clear.config(command=self.event_tab_01_button_clear_click)
        
        self.tab_01_button_save.config(command=self.event_tab_01_button_save_click)
        
        # Tab 02
        self.tab_02_button_add.config(command=self.event_tab_02_button_add_row_click)
        self.tab_02_button_update_row_in_treeview.config(command=self.event_tab_02_button_update_row_click)
        self.tab_02_button_delete.config(command=self.event_tab_02_button_delete_click)
        self.tab_02_button_clear.config(command=self.event_tab_02_button_clear_click)
        
        # Tab 03
        self.tab_03_button_create_new_inventory.config(command=self.event_tab_03_button_create_new_inventory_click)
        
        # Tab 06
        self.tab_06_button_filter.config(command=self.event_tab_06_button_filter_click)
        self.tab_06_button_clear_filter.config(command=self.event_tab_06_button_clear_filter_click)
        
        # Gán sự kiện
        self.tab_01_treeview_PNK.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_01_single_click)  # Single click
        self.tab_01_treeview_PNK.bind("<Double-1>", self.f_view_treeview_of_tab_01_double_click)  # Double click
        
        self.tab_02_treeview_PXK.bind("<ButtonRelease-1>", self.f_view_treeview_of_tab_02_single_click)  # Single click
        self.tab_02_treeview_PXK.bind("<Double-1>", self.f_view_treeview_of_tab_02_double_click)  # Double click
        
    def f_define_all_elements(self):
        # Find in tab_01: Phiếu nhập kho
        tab_01_frame = self.tab1
        self.tab_01_entry_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "label_sl_ton_kho")
        self.tab_01_entry_sl_kha_dung.grid_forget()
        self.tab_01_entry_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "entry_sl_ton_kho")
        self.tab_01_entry_sl_kha_dung.grid_forget()
        self.tab_01_entry_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "entry_sl_kha_dung")
        self.tab_01_entry_sl_kha_dung.grid_forget()
        self.tab_01_label_sl_kha_dung = f_utils_tim_component_with_name(tab_01_frame, "label_sl_kha_dung")
        self.tab_01_label_sl_kha_dung.grid_forget()
        self.tab_01_entry_ma_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_hang")
        self.tab_01_entry_ten_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_hang")
        self.tab_01_entry_dvt = f_utils_tim_component_with_name(tab_01_frame, "entry_dvt")
        self.tab_01_label_don_gia_ton_kho = f_utils_tim_component_with_name(tab_01_frame, "label_don_gia_ton_kho")
        self.tab_01_label_don_gia_ton_kho.grid_forget()
        self.tab_01_entry_don_gia_ton_kho = f_utils_tim_component_with_name(tab_01_frame, "entry_don_gia_ton_kho")
        self.tab_01_entry_don_gia_ton_kho.grid_forget()

        # self.tab_01_treeview_inventories_dropdown = f_utils_tim_component_with_name(tab_01_frame, "treeview_toplevel_inventories_dropdown")
        
        # if self.tab_01_treeview_inventories_dropdown:
        #     print(self.tab_01_treeview_inventories_dropdown)
        # else:
        #     print("Error: không tìm thấy treeview")

        self.tab_01_entry_ngay_tren_phieu = f_utils_tim_component_with_name(tab_01_frame, "date_entry")
        self.tab_01_entry_so_phieu = f_utils_tim_component_with_name(tab_01_frame, "slips_entry")
        self.tab_01_btn_refresh_number_of_slip = f_utils_tim_component_with_name(tab_01_frame, "refresh_number_of_slip_button")
        self.tab_01_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ma_nha_cung_cap")
        self.tab_01_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_01_frame, "entry_ten_nha_cung_cap")
        self.tab_01_entry_mst = f_utils_tim_component_with_name(tab_01_frame, "entry_mst_nha_cung_cap")
        self.tab_01_entry_dia_chi = f_utils_tim_component_with_name(tab_01_frame, "entry_dia_chi_nha_cung_cap")
        self._tab_01_entry_so_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_so_hop_dong")
        self.tab_01_entry_thong_tin_hop_dong = f_utils_tim_component_with_name(tab_01_frame, "entry_thong_tin_ngan_cua_hop_dong")
        
        self.tab_01_label_footer_notification = f_utils_tim_component_label_with_text(self, "Notification")
        
        # Find in tab_04: Nhật ký phiếu nhập kho
        tab_04_frame = self.tab4_NHAT_KY_NHAP_KHO
        self.tab_04_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ma_nha_cung_cap")
        self.tab_04_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ten_nha_cung_cap")
        self.tab_04_entry_mst = f_utils_tim_component_with_name(tab_04_frame, "entry_mst_nha_cung_cap")
        self.tab_04_entry_mst.pack_forget()
        self.tab_04_entry_dia_chi = f_utils_tim_component_with_name(tab_04_frame, "entry_dia_chi_nha_cung_cap")
        self.tab_04_entry_dia_chi.pack_forget()
        self.tab_04_frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_04_frame, "frame_row_2_of_inventories_info")
        self.tab_04_frame_row_2_of_inventories_info.pack_forget()
        self.tab_04_entry_ma_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ma_hang")
        self.tab_04_entry_ten_hang = f_utils_tim_component_with_name(tab_04_frame, "entry_ten_hang")
        self.tab_04_ngay_filter_bat_dau = f_utils_tim_component_with_name(tab_04_frame, "start_date_entry")
        self.tab_04_ngay_filter_ket_thuc = f_utils_tim_component_with_name(tab_04_frame, "end_date_entry")
        
        # Find in tab_02: Phiếu xuất kho
        tab_02_frame = self.tab2
        
        self.tab_02_entry_sl_kha_dung = f_utils_tim_component_with_name(tab_02_frame, "entry_sl_kha_dung")
        self.tab_02_entry_sl_kha_dung.grid_forget()
        self.tab_02_label_sl_kha_dung = f_utils_tim_component_with_name(tab_02_frame, "label_sl_kha_dung")
        self.tab_02_label_sl_kha_dung.grid_forget()
        self.tab_02_entry_ma_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_hang")
        self.tab_02_entry_ten_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_hang")
        self.tab_02_entry_dvt = f_utils_tim_component_with_name(tab_02_frame, "entry_dvt")
        self.tab_02_label_don_gia_ton_kho = f_utils_tim_component_with_name(tab_02_frame, "label_don_gia_ton_kho")
        self.tab_02_label_don_gia_ton_kho.config(text="ĐG xuất:")
        self.tab_02_label_don_gia_ton_kho.grid(row=0, column=8)
        self.tab_02_entry_don_gia_ton_kho = f_utils_tim_component_with_name(tab_02_frame, "entry_don_gia_ton_kho")
        self.tab_02_entry_don_gia_ton_kho.grid(row=0, column=9)
        self.tab_02_entry_ngay_tren_phieu = f_utils_tim_component_with_name(tab_02_frame, "date_entry")
        self.tab_02_entry_so_phieu = f_utils_tim_component_with_name(tab_02_frame, "slips_entry")
        self.tab_02_btn_refresh_number_of_slip = f_utils_tim_component_with_name(tab_02_frame, "refresh_number_of_slip_button")
        self.tab_02_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ma_khach_hang")
        self.tab_02_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_02_frame, "entry_ten_khach_hang")
        self.tab_02_entry_mst = f_utils_tim_component_with_name(tab_02_frame, "entry_mst_khach_hang")
        self.tab_02_entry_dia_chi = f_utils_tim_component_with_name(tab_02_frame, "entry_dia_chi_khach_hang")
        self._tab_02_entry_so_hop_dong = f_utils_tim_component_with_name(tab_02_frame, "entry_so_hop_dong")
        self.tab_02_entry_thong_tin_hop_dong = f_utils_tim_component_with_name(tab_02_frame, "entry_thong_tin_ngan_cua_hop_dong")
        
        # Find in tab_05: Nhật ký phiếu xuất kho
        tab_05_frame = self.tab5_NHAT_KY_XUAT_KHO
        self.tab_05_entry_ma_khach_hang = f_utils_tim_component_with_name(tab_05_frame, "entry_ma_khach_hang")
        self.tab_05_entry_ten_khach_hang = f_utils_tim_component_with_name(tab_05_frame, "entry_ten_khach_hang")
        self.tab_05_entry_mst = f_utils_tim_component_with_name(tab_05_frame, "entry_mst_khach_hang")
        self.tab_05_entry_mst.pack_forget()
        self.tab_05_entry_dia_chi = f_utils_tim_component_with_name(tab_05_frame, "entry_dia_chi_khach_hang")
        self.tab_05_entry_dia_chi.pack_forget()
        self._tab_05_frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_05_frame, "frame_row_2_of_inventories_info")
        self._tab_05_frame_row_2_of_inventories_info.pack_forget()
        self.tab_05_entry_ma_hang = f_utils_tim_component_with_name(tab_05_frame, "entry_ma_hang")
        self.tab_05_entry_ten_hang = f_utils_tim_component_with_name(tab_05_frame, "entry_ten_hang")
        self.tab_05_ngay_filter_bat_dau = f_utils_tim_component_with_name(tab_05_frame, "start_date_entry")
        self.tab_05_ngay_filter_ket_thuc = f_utils_tim_component_with_name(tab_05_frame, "end_date_entry")
        
        # Find in tab_06: Báo cáo tồn kho
        tab_06_frame = self.tab6_BAO_CAO_TON_KHO
        self._tab_06_frame_row_2_of_inventories_info = f_utils_tim_component_with_name(tab_06_frame, "frame_row_2_of_inventories_info")
        self._tab_06_frame_row_2_of_inventories_info.pack_forget()
        self.tab_06_entry_ma_hang = f_utils_tim_component_with_name(tab_06_frame, "entry_ma_hang")
        self.tab_06_entry_ten_hang = f_utils_tim_component_with_name(tab_06_frame, "entry_ten_hang")
        
    
    def f_set_up_format_of_tree_view(self):
        # Nhập kho
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_01(self.tab_01_treeview_PNK)
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_04(self.tab_04_treeview_log_of_PNK)
        # Xuất kho
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_02(self.tab_02_treeview_PXK)
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_05(self.tab_05_treeview_log_of_PXK)
        # Báo cáo tồn kho
        Controller_handel_all_events.f_handle_event_initializing_format_of_treeview_of_tab_06(self.tab_06_treeview_report)
    
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
        parent_frame = self.tab1

        # Frame H2
        self.tab_01_frame_H2 = tk.Frame(parent_frame)
        self.tab_01_frame_H2.grid(row=0, column=0, sticky="ew")
        cls_my_label_num_03_title_H2(self.tab_01_frame_H2, text="PHIẾU NHẬP KHO").pack(anchor="center")

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
        self.tab_01_treeview_PNK = self.tab_01_frame_treeview.treeview_normal
        
        # Frame button
        self.tab_01_frame_button_02 = tk.Frame(parent_frame)
        self.tab_01_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_01_frame_button_02()

        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)
     
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
        self.f_view_create_widgets_in_frame_date_and_number_in_tab_01()

        # Create container for client and inventories
        self.tab_01_Frame_clients_and_inventories_information = tk.Frame(parent_frame)
        self.tab_01_Frame_clients_and_inventories_information.pack(side="top",
                                                            fill="x",  
                                                            pady=(5,0)
                                                            )
        self.f_view_create_widgets_in_tab_01_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(parent_frame)
        self.frame_slip_informations.pack(side="top", 
                                          fill="x", 
                                          pady=(5,0)
                                          )
        self.f_view_create_widgets_in_frame_slip_informations_in_tab_01()
    
    def f_view_create_widgets_in_frame_date_and_number_in_tab_01(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number)
        self.frame_date_and_number.pack(anchor="center")

    def f_view_create_widgets_in_tab_01_frame_clients_and_inventories(self):
        parent_frame = self.tab_01_Frame_clients_and_inventories_information

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
        columns_to_display = [0, 1, 2]
        self.frame_inventories_informations_tab_01 = cls_frame_inventories_information_view(parent_frame, columns_to_display=columns_to_display)
        self.frame_inventories_informations_tab_01.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_01.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01()
            
    def f_view_create_widgets_in_frame_slip_informations_in_tab_01(self):
        # Input fields
        tk.Label(self.frame_slip_informations, text="STT:").pack(side="left")
        self.tab_01_entry_id = tk.Entry(self.frame_slip_informations,
                                        width=10)
        self.tab_01_entry_id.pack(side="left")
        self.tab_01_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_01_entry_note_for_slip = cls_my_text_entry_num_01(self.frame_slip_informations)
        self.tab_01_entry_note_for_slip.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_note_for_slip.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_note_for_slip.pack(side="left", fill="x", expand=True, pady=10)
        
    def f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_01(self):
        # create parent_frame
        parent_frame = self.frame_inventories_informations_tab_01.frame_row_2
        
        self.tab_01_label_sl_thuc_nhap = tk.Label(parent_frame, text="SL thực nhập:")
        self.tab_01_label_sl_thuc_nhap.grid(row=0, column=4, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_sl_thuc_nhap = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_sl_thuc_nhap.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_sl_thuc_nhap.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_sl_thuc_nhap.grid(row=0, column=5, padx=(0, 10), pady=5, sticky="w")
        
        self.tab_01_label_don_gia_nhap_kho = tk.Label(parent_frame, text="ĐG nhập:")
        self.tab_01_label_don_gia_nhap_kho.grid(row=0, column=6, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_entry_don_gia_nhap_kho = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_01_entry_don_gia_nhap_kho.f_on_leaving(color=COLOR_WHITE)
        self.tab_01_entry_don_gia_nhap_kho.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_01_entry_don_gia_nhap_kho.grid(row=0, column=7, padx=(0, 10), pady=5, sticky="w")
        
        # Create a combobox with the options 'Kho A' and 'Kho B'
        values = ["Kho A", "Kho B"]
        self.tab_01_kho_nhap = tk.Label(parent_frame, text="Kho nhập:")
        self.tab_01_kho_nhap.grid(row=0, column=8, padx=(10, 2), pady=5, sticky="w")
        self.tab_01_combobox_ma_kho = cls_my_combobox_num_01(parent_frame, values=values)
        self.tab_01_combobox_ma_kho.grid(row=0, column=9, padx=(0, 10), pady=5, sticky="w")
        # Set the default value to the first item in the list
        self.tab_01_combobox_ma_kho.set(values[0])
        
        # Configure column weights for proper resizing
        # Allow these colunms to expand
        parent_frame.columnconfigure(5, weight=1)  
        parent_frame.columnconfigure(7, weight=1)
        parent_frame.columnconfigure(9, weight=1)
        
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
        parent_frame = cls_frame_request_management_view(self.tab_01_frame_suppliers_information)
        parent_frame.pack(side="bottom", fill="x", expand=True)

    def f_view_create_widgets_in_tab_01_frame_button_of_treeview(self):
        # Create a sub-frame to organize buttons in the center
        tab_01_button_container_01 = tk.Frame(self.tab_01_frame_button_of_treeview)
        tab_01_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_01_button_add = cls_my_button_num_01(tab_01_button_container_01, text="Add Row")
        self.tab_01_button_add.pack(side="left", padx=10)
        
        # Update button
        self.tab_01_button_update_row_in_treeview = cls_my_button_num_01(tab_01_button_container_01, text="Update Row")
        self.tab_01_button_update_row_in_treeview.pack(side="left", padx=10)
        
        # Delete button
        self.tab_01_button_delete = cls_my_button_num_01(tab_01_button_container_01, text="Delete Row")
        self.tab_01_button_delete.pack(side="left", padx=10)
        
        # Clear button
        self.tab_01_button_clear = cls_my_button_num_01(tab_01_button_container_01, text="Clear Rows")
        self.tab_01_button_clear.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_01_frame_button_02(self):
        parent_frame = self.tab_01_frame_button_02
        # Create a sub-frame on the right
        tab_01_button_container_02_on_the_right = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_01_button_container_02_on_the_left = tk.Frame(parent_frame)
        tab_01_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # BTN update slip
        self.tab_01_button_update_slip = cls_my_button_num_01(tab_01_button_container_02_on_the_right, text="Update")
        self.tab_01_button_update_slip.pack(side="right", padx=10)
        
        # BTN save
        self.tab_01_button_save = cls_my_button_num_01(tab_01_button_container_02_on_the_right, text="Save")
        self.tab_01_button_save.pack(side="right", padx=10)
        
        # BTN print
        self.tab_01_button_print = cls_my_button_num_01(tab_01_button_container_02_on_the_right, text="Print")
        self.tab_01_button_print.pack(side="right", padx=10)
        
        # temp button
        self.tab_01_btn_template = cls_my_button_num_01(tab_01_button_container_02_on_the_left, text="Template")
        self.tab_01_btn_template.pack(side="left", padx=10)
        
        # get file button
        self.tab_01_btn_get_import_file = cls_my_button_num_01(tab_01_button_container_02_on_the_left, text="Get file")
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

    def f_view_create_all_container_frames_in_tab_02(self):
        parent_frame = self.tab2

        # Frame H2
        self.tab_02_frame_H2 = tk.Frame(parent_frame)
        self.tab_02_frame_H2.grid(row=0, column=0, sticky="ew")
        cls_my_label_num_03_title_H2(self.tab_02_frame_H2, text="PHIẾU NHẬP KHO").pack(anchor="center")

        # Frame entries
        self.tab_02_frame_entries = tk.Frame(parent_frame)
        self.tab_02_frame_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_02_frame_entries()

        # Frame button
        self.tab_02_frame_button_of_treeview = tk.Frame(parent_frame)
        self.tab_02_frame_button_of_treeview.grid(row=2, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_02_frame_button_of_treeview()

        # Frame treeview
        self.tab_02_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_02_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self.tab_02_treeview_PXK = self.tab_02_frame_treeview.treeview_normal
        
        # Frame button
        self.tab_02_frame_button_02 = tk.Frame(parent_frame)
        self.tab_02_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_02_frame_button_02()

        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)
     
    def f_view_create_widgets_in_tab_02_frame_entries(self):
        self.tab_02_container_frame_entries = tk.Frame(self.tab_02_frame_entries)
        self.tab_02_container_frame_entries.pack(side="top", 
                                                 fill="x"
                                                 )

        parent_frame = self.tab_02_container_frame_entries
        # Create container for date and number of slip
        self.Frame_container_date_and_number = tk.Frame(parent_frame)
        self.Frame_container_date_and_number.pack(side="top", 
                                                  fill="x"
                                                  )
        self.f_view_create_widgets_in_frame_date_and_number_in_tab_02()

        # Create container for client and inventories
        self.tab_02_Frame_clients_and_inventories_information = tk.Frame(parent_frame)
        self.tab_02_Frame_clients_and_inventories_information.pack(side="top",
                                                            fill="x",  
                                                            pady=(5,0)
                                                            )
        self.f_view_create_widgets_in_tab_02_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(parent_frame)
        self.frame_slip_informations.pack(side="top", 
                                          fill="x", 
                                          pady=(5,0)
                                          )
        self.f_view_create_widgets_in_frame_slip_informations_in_tab_02()
    
    def f_view_create_widgets_in_frame_date_and_number_in_tab_02(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number)
        self.frame_date_and_number.pack(anchor="center")

    def f_view_create_widgets_in_tab_02_frame_clients_and_inventories(self):
        parent_frame = self.tab_02_Frame_clients_and_inventories_information

        # Configure grid layout for parent frame
        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_rowconfigure(0, weight=1)

        # Create frame clients informations
        self.tab_02_frame_suppliers_information = cls_frame_client_information_view(parent_frame)
        self.tab_02_frame_suppliers_information.config(bd=0, relief="flat")
        self.tab_02_frame_suppliers_information.grid(row=0, column=0, sticky="nsew")
        self.f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_02()
        
        # Create frame inventories informations
        columns_to_display = [0, 1, 2, 3, 5]
        self.frame_inventories_informations_tab_02 = cls_frame_inventories_information_view(parent_frame, columns_to_display=columns_to_display)
        self.frame_inventories_informations_tab_02.config(bd=0, relief="flat")
        self.frame_inventories_informations_tab_02.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        self.f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_02()
            
    def f_view_create_widgets_in_frame_slip_informations_in_tab_02(self):
        # Input fields
        tk.Label(self.frame_slip_informations, text="STT:").pack(side="left")
        self.tab_02_entry_id = tk.Entry(self.frame_slip_informations,
                                        width=10)
        self.tab_02_entry_id.pack(side="left")
        self.tab_02_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_02_note_for_slip = cls_my_text_entry_num_01(self.frame_slip_informations)
        self.tab_02_note_for_slip.f_on_leaving(color=COLOR_WHITE)
        self.tab_02_note_for_slip.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_02_note_for_slip.pack(side="left", fill="x", expand=True, pady=10)
        
    def f_view_create_widgets_add_widget_into_frame_inventories_informations_tab_02(self):
        # create parent_frame
        parent_frame = self.frame_inventories_informations_tab_02.frame_row_2
        
        self.tab_02_label_sl_thuc_xuat = tk.Label(parent_frame, text="SL thực xuất:")
        self.tab_02_label_sl_thuc_xuat.grid(row=0, column=6, padx=(10, 2), pady=5, sticky="w")
        self.tab_02_entry_sl_thuc_xuat = cls_my_number_entry_num_01(parent_frame, width=10)
        self.tab_02_entry_sl_thuc_xuat.f_on_leaving(color=COLOR_WHITE)
        self.tab_02_entry_sl_thuc_xuat.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_02_entry_sl_thuc_xuat.grid(row=0, column=7, padx=(0, 10), pady=5, sticky="w")
        
        # Create a combobox with the options 'Kho A' and 'Kho B'
        values = ["Kho A", "Kho B"]
        self.tab_02_kho_nhap = tk.Label(parent_frame, text="Kho xuất:")
        self.tab_02_kho_nhap.grid(row=0, column=10, padx=(12, 2), pady=5, sticky="w")
        self.tab_02_combobox_ma_kho = cls_my_combobox_num_01(parent_frame, values=values)
        self.tab_02_combobox_ma_kho.grid(row=0, column=11, padx=(0, 10), pady=5, sticky="w")
        # Set the default value to the first item in the list
        self.tab_02_combobox_ma_kho.set(values[0])

        # Configure column weights for proper resizing
        # Allow these colunms to expand
        parent_frame.columnconfigure(7, weight=1)
        parent_frame.columnconfigure(9, weight=1)
        parent_frame.columnconfigure(11, weight=1)
        
        self.f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_02()
    
    def f_view_create_widgets_add_row_03_into_frame_inventories_informations_tab_02(self):
        # create parent_frame
        parent_frame = tk.Frame(self.frame_inventories_informations_tab_02)
        parent_frame.pack(side="bottom", fill="x", expand=True)

        tk.Label(parent_frame, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_02_entry_ghi_chu_mat_hang = cls_my_text_entry_num_01(parent_frame)
        self.tab_02_entry_ghi_chu_mat_hang.f_on_leaving(color=COLOR_WHITE)
        self.tab_02_entry_ghi_chu_mat_hang.f_on_not_selecting(color=COLOR_WHITE)
        self.tab_02_entry_ghi_chu_mat_hang.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
    def f_view_create_widgets_add_row_03_into_frame_clients_informations_tab_02(self):
        # create parent_frame
        parent_frame = cls_frame_request_management_view(self.tab_02_frame_suppliers_information)
        parent_frame.pack(side="bottom", fill="x", expand=True)

    def f_view_create_widgets_in_tab_02_frame_button_of_treeview(self):
        # Create a sub-frame to organize buttons in the center
        tab_02_button_container_01 = tk.Frame(self.tab_02_frame_button_of_treeview)
        tab_02_button_container_01.pack(expand=True, pady=10)
        
        # Add button
        self.tab_02_button_add = cls_my_button_num_01(tab_02_button_container_01, text="Add Row")
        self.tab_02_button_add.pack(side="left", padx=10)
        
        # Update button
        self.tab_02_button_update_row_in_treeview = cls_my_button_num_01(tab_02_button_container_01, text="Update Row")
        self.tab_02_button_update_row_in_treeview.pack(side="left", padx=10)
        
        # Delete button
        self.tab_02_button_delete = cls_my_button_num_01(tab_02_button_container_01, text="Delete Row")
        self.tab_02_button_delete.pack(side="left", padx=10)
        
        # Clear button
        self.tab_02_button_clear = cls_my_button_num_01(tab_02_button_container_01, text="Clear Rows")
        self.tab_02_button_clear.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_02_frame_button_02(self):
        parent_frame = self.tab_02_frame_button_02
        # Create a sub-frame on the right
        tab_02_button_container_02_on_the_right = tk.Frame(parent_frame)
        tab_02_button_container_02_on_the_right.pack(side="right", expand=True, pady=10)
        # Create a sub-frame on the left
        tab_02_button_container_02_on_the_left = tk.Frame(parent_frame)
        tab_02_button_container_02_on_the_left.pack(side="left", expand=True, pady=10)
        
        # BTN update slip
        self.tab_02_button_update_slip = cls_my_button_num_01(tab_02_button_container_02_on_the_right, text="Update")
        self.tab_02_button_update_slip.pack(side="right", padx=10)
        
        # BTN save
        self.tab_02_button_save = cls_my_button_num_01(tab_02_button_container_02_on_the_right, text="Save")
        self.tab_02_button_save.pack(side="right", padx=10)
        
        # BTN print
        self.tab_02_button_print = cls_my_button_num_01(tab_02_button_container_02_on_the_right, text="Print")
        self.tab_02_button_print.pack(side="right", padx=10)
        
        # temp button
        self.tab_02_btn_template = cls_my_button_num_01(tab_02_button_container_02_on_the_left, text="Template")
        self.tab_02_btn_template.pack(side="left", padx=10)
        
        # get file button
        self.tab_02_btn_get_import_file = cls_my_button_num_01(tab_02_button_container_02_on_the_left, text="Get file")
        self.tab_02_btn_get_import_file.pack(side="left", padx=10)
    
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_03: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================

    def f_view_create_all_container_frames_in_tab_03(self):
        parent_frame = self.tab3
        # Frame H2
        self.tab_03_frame_H2 = tk.Frame(parent_frame)
        self.tab_03_frame_H2.grid(row=0, column=0, sticky="ew")
        cls_my_label_num_03_title_H2(self.tab_03_frame_H2, text="TẠO MỚI MÃ HÀNG").pack(anchor="center")

        # Frame entries
        self.tab_03_frame_entries = tk.Frame(parent_frame)
        self.tab_03_frame_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_03_frame_entries()

        # parent_frame.grid_rowconfigure(2, weight=1)
        parent_frame.grid_columnconfigure(0, weight=1)
     
    def f_view_create_widgets_in_tab_03_frame_entries(self):
        parent_frame = tk.Frame(self.tab_03_frame_entries)
        parent_frame.pack(side="top")
        
        self.tab_03_label_new_id_code = tk.Label(parent_frame, text="Mã hàng")
        self.tab_03_label_new_id_code.grid(row=0, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_new_id_code = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_new_id_code.grid(row=0, column=1, padx=(10, 2), pady=5, sticky="w")
        
        self.tab_03_label_new_id_name = tk.Label(parent_frame, text="Tên hàng")
        self.tab_03_label_new_id_name.grid(row=1, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_new_id_name = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_new_id_name.grid(row=1, column=1, padx=(10, 2), pady=5, sticky="w")
        
        self.tab_03_label_new_dvt = tk.Label(parent_frame, text="Đvt")
        self.tab_03_label_new_dvt.grid(row=2, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_new_dvt = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_new_dvt.grid(row=2, column=1, padx=(10, 2), pady=5, sticky="w")
        
        self.tab_03_label_ma_phan_loai_01 = tk.Label(parent_frame, text="Mã phân loại 01")
        self.tab_03_label_ma_phan_loai_01.grid(row=3, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_ma_phan_loai_01 = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_ma_phan_loai_01.grid(row=3, column=1, padx=(10, 2), pady=5, sticky="w")
        
        self.tab_03_label_ma_phan_loai_02 = tk.Label(parent_frame, text="Mã phân loại 02")
        self.tab_03_label_ma_phan_loai_02.grid(row=4, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_ma_phan_loai_02 = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_ma_phan_loai_02.grid(row=4, column=1, padx=(10, 2), pady=5, sticky="w")
        
        self.tab_03_label_ma_phan_loai_03 = tk.Label(parent_frame, text="Mã phân loại 03")
        self.tab_03_label_ma_phan_loai_03.grid(row=5, column=0, padx=(10, 2), pady=5, sticky="w")
        self.tab_03_entry_ma_phan_loai_03 = cls_my_text_entry_num_01(parent_frame)
        self.tab_03_entry_ma_phan_loai_03.grid(row=5, column=1, padx=(10, 2), pady=5, sticky="w")
        
        # BTN save
        self.tab_03_button_create_new_inventory = cls_my_button_num_01(parent_frame, text="Save")
        self.tab_03_button_create_new_inventory.grid(row=6, column=1, padx=10, pady=5, sticky="ew")    
    
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
        cls_my_label_num_03_title_H2(self.tab_04_frame_H2, text="NHẬT KÝ NHẬP KHO").pack(anchor="center")

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
        self.tab_04_treeview_log_of_PNK = self.tab_04_frame_treeview.treeview_normal
        
        # Frame button
        self.tab_04_frame_button_02 = tk.Frame(parent_frame)
        self.tab_04_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_04_frame_button_02()
        
        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)
     
    def f_view_create_widgets_in_tab_04_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        parent_frame = tk.Frame(self.tab_04_frame_button_01)
        parent_frame.pack(expand=True, pady=10)
        
        # Add button
        self.tab_04_button_filter = cls_my_button_num_01(parent_frame, text="Filter")
        self.tab_04_button_filter.pack(side="left", padx=10)
        
        # Delete update
        self.tab_04_button_clear_filter = cls_my_button_num_01(parent_frame, text="Clear")
        self.tab_04_button_clear_filter.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_04_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_04_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        parent_frame_01 = tk.Frame(self.tab_04_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        parent_frame_02 = tk.Frame(self.tab_04_frame_filter_entries)
        parent_frame_02.grid(row=0, column=2, sticky="nsew")
        
        # Create Number of slip and contract number
        tk.Label(parent_frame_00, text="Số phiếu").grid(row=0, column= 0, padx=(10, 0), pady=(10, 0), sticky="w")
        self.filter_entry_slip_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_slip_number.grid(row=0, column= 1, padx=(2, 10), pady=(10, 0), sticky="ew")
        tk.Label(parent_frame_00, text="Số đề nghị").grid(row=1, column= 0, padx=(10, 0), pady=(15, 10), sticky="w")
        self.filter_entry_contract_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_contract_number.grid(row=1, column= 1, padx=(2, 10), pady=(15, 10), sticky="ew")
        
        # Create frame inventories informations
        self.tab_04_frame_seclect_date = cls_frame_DateSelector_view(parent_frame_01)
        self.tab_04_frame_seclect_date.config(bd=0, relief="flat")
        self.tab_04_frame_seclect_date.grid(row=0, column=0, sticky="ew")
        
        # Create frame clients informations
        self.tab_04_frame_clients_informations = cls_frame_suppliers_information_view(parent_frame_02)
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
        parent_frame = tk.Frame(self.tab_04_frame_button_02)
        parent_frame.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_04_button_export_all_data = cls_my_button_num_01(parent_frame, text="Export all data")
        self.tab_04_button_export_all_data.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_04_button_export_excel = cls_my_button_num_01(parent_frame, text="Export Excel")
        self.tab_04_button_export_excel.pack(side="left", padx=10)
        
        # Edit Slip button
        self.tab_04_button_edit_slip = cls_my_button_num_01(parent_frame, text="Edit slip")
        self.tab_04_button_edit_slip.pack(side="left", padx=10)
        
        # Delete Slip button
        self.tab_04_button_delete_slip = cls_my_button_num_01(parent_frame, text="Delete slip")
        self.tab_04_button_delete_slip.pack(side="left", padx=10)
        
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_05: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    
    def f_view_create_all_container_frames_in_tab_05(self):
        parent_frame = self.tab5_NHAT_KY_XUAT_KHO

        # Frame H2
        self.tab_05_frame_H2 = tk.Frame(parent_frame)
        self.tab_05_frame_H2.grid(row=0, column=0, sticky="ew")
        cls_my_label_num_03_title_H2(self.tab_05_frame_H2, text="NHẬT KÝ XUẤT KHO").pack(anchor="center")

        # Frame entries
        self.tab_05_frame_filter_entries = tk.Frame(parent_frame)
        self.tab_05_frame_filter_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_05_frame_filter_entries()

        # Frame button
        self.tab_05_frame_button_01 = tk.Frame(parent_frame)
        self.tab_05_frame_button_01.grid(row=2, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_05_frame_button_01()
        
        # Frame treeview
        self.tab_05_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_05_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self.tab_05_treeview_log_of_PXK = self.tab_05_frame_treeview.treeview_normal
        
        # Frame button
        self.tab_05_frame_button_02 = tk.Frame(parent_frame)
        self.tab_05_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_05_frame_button_02()
        
        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)
     
    def f_view_create_widgets_in_tab_05_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        parent_frame = tk.Frame(self.tab_05_frame_button_01)
        parent_frame.pack(expand=True, pady=10)
        
        # Add button
        self.tab_05_button_filter = cls_my_button_num_01(parent_frame, text="Filter")
        self.tab_05_button_filter.pack(side="left", padx=10)
        
        # Delete update
        self.tab_05_button_clear_filter = cls_my_button_num_01(parent_frame, text="Clear")
        self.tab_05_button_clear_filter.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_05_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_05_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        parent_frame_01 = tk.Frame(self.tab_05_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        parent_frame_02 = tk.Frame(self.tab_05_frame_filter_entries)
        parent_frame_02.grid(row=0, column=2, sticky="nsew")
        
        # Create Number of slip and contract number
        tk.Label(parent_frame_00, text="Số phiếu").grid(row=0, column= 0, padx=(10, 0), pady=(10, 0), sticky="w")
        self.filter_entry_slip_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_slip_number.grid(row=0, column= 1, padx=(2, 10), pady=(10, 0), sticky="ew")
        tk.Label(parent_frame_00, text="Số đề nghị").grid(row=1, column= 0, padx=(10, 0), pady=(15, 10), sticky="w")
        self.filter_entry_contract_number = cls_my_text_entry_num_01(parent_frame_00)
        self.filter_entry_contract_number.grid(row=1, column= 1, padx=(2, 10), pady=(15, 10), sticky="ew")
        
        # Create frame inventories informations
        self.tab_05_frame_seclect_date = cls_frame_DateSelector_view(parent_frame_01)
        self.tab_05_frame_seclect_date.config(bd=0, relief="flat")
        self.tab_05_frame_seclect_date.grid(row=0, column=0, sticky="ew")
        
        # Create frame clients informations
        self.tab_05_frame_clients_informations = cls_frame_client_information_view(parent_frame_02)
        self.tab_05_frame_clients_informations.config(bd=0, relief="flat")
        self.tab_05_frame_clients_informations.grid(row=0, column=0, sticky="ew")
        
        # Create frame inventories informations
        self.tab_05_frame_inventories_information = cls_frame_inventories_information_view(parent_frame_02)
        self.tab_05_frame_inventories_information.config(bd=0, relief="flat")
        self.tab_05_frame_inventories_information.grid(row=1, column=0, pady=(10, 0), sticky="ew")
    
        # Allow stretching
        self.tab_05_frame_filter_entries.columnconfigure(2, weight=1)   # Stretch the column to fill the width
        parent_frame_02.columnconfigure(0, weight=1)                    # Stretch parent_frame_02
    
    def f_view_create_widgets_in_tab_05_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        parent_frame = tk.Frame(self.tab_05_frame_button_02)
        parent_frame.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_05_button_export_all_data = cls_my_button_num_01(parent_frame, text="Export all data")
        self.tab_05_button_export_all_data.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_05_button_export_excel = cls_my_button_num_01(parent_frame, text="Export Excel")
        self.tab_05_button_export_excel.pack(side="left", padx=10)
        
        # Edit Slip button
        self.tab_05_button_edit_slip = cls_my_button_num_01(parent_frame, text="Edit slip")
        self.tab_05_button_edit_slip.pack(side="left", padx=10)
        
        # Delete Slip button
        self.tab_05_button_delete_slip = cls_my_button_num_01(parent_frame, text="Delete slip")
        self.tab_05_button_delete_slip.pack(side="left", padx=10)

    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Tab_06: create widgets
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    
    def f_view_create_all_container_frames_in_tab_06(self):
        parent_frame = self.tab6_BAO_CAO_TON_KHO

        # Frame H2
        self.tab_06_frame_H2 = tk.Frame(parent_frame)
        self.tab_06_frame_H2.grid(row=0, column=0, sticky="ew")
        cls_my_label_num_03_title_H2(self.tab_06_frame_H2, text="BÁO CÁO TỒN KHO").pack(anchor="center")

        # Frame entries
        self.tab_06_frame_filter_entries = tk.Frame(parent_frame)
        self.tab_06_frame_filter_entries.grid(row=1, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_06_frame_filter_entries()

        # Frame button
        self.tab_06_frame_button_01 = tk.Frame(parent_frame)
        self.tab_06_frame_button_01.grid(row=2, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_06_frame_button_01()
        
        # Frame treeview
        self.tab_06_frame_treeview = cls_Treeview_frame_number_01(parent_frame)
        self.tab_06_frame_treeview.grid(row=3, column=0, sticky="nsew")
        self.tab_06_treeview_report = self.tab_06_frame_treeview.treeview_normal
        
        # Frame button
        self.tab_06_frame_button_02 = tk.Frame(parent_frame)
        self.tab_06_frame_button_02.grid(row=4, column=0, sticky="ew")
        self.f_view_create_widgets_in_tab_06_frame_button_02()
        
        parent_frame.grid_rowconfigure(3, weight=1) # cho phép giãn nở
        parent_frame.grid_columnconfigure(0, weight=1)
     
    def f_view_create_widgets_in_tab_06_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        parent_frame = tk.Frame(self.tab_06_frame_button_01)
        parent_frame.pack(expand=True, pady=10)
        
        # Add button
        self.tab_06_button_filter = cls_my_button_num_01(parent_frame, text="Filter")
        self.tab_06_button_filter.pack(side="left", padx=10)
        
        # Delete update
        self.tab_06_button_clear_filter = cls_my_button_num_01(parent_frame, text="Clear")
        self.tab_06_button_clear_filter.pack(side="left", padx=10)
    
    def f_view_create_widgets_in_tab_06_frame_filter_entries(self):
        parent_frame_00 = tk.Frame(self.tab_06_frame_filter_entries)
        parent_frame_00.grid(row=0, column=0, sticky="nsew")
        
        # Create frame inventories informations
        self.tab_06_frame_inventories_information = cls_frame_inventories_information_view(parent_frame_00)
        self.tab_06_frame_inventories_information.config(bd=0, relief="flat")
        self.tab_06_frame_inventories_information.grid(row=0, column=0, pady=(10, 0), sticky="ew")
        
        parent_frame_01 = tk.Frame(self.tab_06_frame_filter_entries)
        parent_frame_01.grid(row=0, column=1, sticky="nsew")
        
        self.tab_06_label_ma_kho = tk.Label(parent_frame_01, text="Kho tồn")
        self.tab_06_label_ma_kho.grid(row=0, column=0, padx=(10, 2), pady=(10, 0), sticky="w")
        values_ma_kho = ["Tất cả", "Kho A", "Kho B", "Kho C"]
        self.tab_06_combobox_ma_kho = cls_my_combobox_num_01(parent_frame_01, values=values_ma_kho)
        self.tab_06_combobox_ma_kho.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
    
        # Allow stretching
        self.tab_06_frame_filter_entries.columnconfigure(0, weight=1)   # Stretch the column to fill the width
        parent_frame_00.columnconfigure(0, weight=1)                    # Stretch parent_frame_02
    
    def f_view_create_widgets_in_tab_06_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        parent_frame = tk.Frame(self.tab_06_frame_button_02)
        parent_frame.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_06_button_export_all_data = cls_my_button_num_01(parent_frame, text="Export all data")
        self.tab_06_button_export_all_data.pack(side="left", padx=10)
        
        # Get Data button
        self.tab_06_button_export_excel = cls_my_button_num_01(parent_frame, text="Export Excel")
        self.tab_06_button_export_excel.pack(side="left", padx=10)
    
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
    
    def event_tab_03_button_create_new_inventory_click(self):        
        Controller_handel_all_events.f_handle_event_create_new_inventory(self.tab_01_label_footer_notification,
                                                                         self.tab_03_entry_new_id_code
                                                                         , self.tab_03_entry_new_id_name
                                                                         , self.tab_03_entry_new_dvt)
        
    def event_tab_06_button_filter_click(self):
        Controller_handel_all_events.f_handle_event_tab_06_button_filter_log_click(
            self.tab_01_label_footer_notification,
            self.tab_06_entry_ma_hang,
            self.tab_06_treeview_report)
        
    
    def event_tab_06_button_clear_filter_click(self):
        Controller_handel_all_events.f_handle_event_tab_06_button_clear_filter(
            self.tab_01_label_footer_notification, 
            self.tab_06_treeview_report,
            self.tab_06_entry_ma_hang,
            self.tab_06_entry_ten_hang,
            self.tab_06_combobox_ma_kho)
    
    def event_tab_01_button_add_row_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_button_add_row_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_PNK, 
            self.tab_01_entry_id, 
            self.tab_01_entry_ma_hang, 
            self.tab_01_entry_ten_hang, 
            self.tab_01_entry_dvt, 
            self.tab_01_entry_sl_thuc_nhap,
            self.tab_01_entry_don_gia_nhap_kho,
            self.tab_01_entry_ghi_chu_mat_hang)
    
    def event_tab_02_button_add_row_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_button_add_row_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_PXK, 
            self.tab_02_entry_id, 
            self.tab_02_entry_ma_hang, 
            self.tab_02_entry_ten_hang, 
            self.tab_02_entry_dvt, 
            self.tab_02_entry_sl_thuc_xuat, 
            self.tab_02_entry_don_gia_ton_kho,
            self.tab_02_entry_ghi_chu_mat_hang)
    
    def event_tab_01_button_update_row_click(self):
        Controller_handel_all_events.f_handle_event_update_selected_row_click(
        self.tab_01_label_footer_notification,
        self.tab_01_treeview_PNK,
        self.tab_01_entry_ma_hang,
        self.tab_01_entry_ten_hang,
        self.tab_01_entry_dvt,
        self.tab_01_entry_sl_thuc_nhap,
        self.tab_01_entry_ghi_chu_mat_hang)
        
    def event_tab_02_button_update_row_click(self):
        Controller_handel_all_events.f_handle_event_update_selected_row_click(
        self.tab_01_label_footer_notification,
        self.tab_02_treeview_PXK,
        self.tab_02_entry_ma_hang,
        self.tab_02_entry_ten_hang,
        self.tab_02_entry_dvt,
        self.tab_02_entry_sl_thuc_xuat,
        self.tab_02_entry_ghi_chu_mat_hang)
        
    def f_view_treeview_of_tab_01_double_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_01_double_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_PNK)
    
    def f_view_treeview_of_tab_02_double_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_02_double_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_PXK)

    def f_view_treeview_of_tab_01_single_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_01_single_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_PNK,
            self.tab_01_entry_id,
            self.tab_01_entry_ma_hang,
            self.tab_01_entry_ten_hang,
            self.tab_01_entry_dvt,
            self.tab_01_entry_sl_thuc_nhap,
            self.tab_01_entry_ghi_chu_mat_hang)
    
    def f_view_treeview_of_tab_02_single_click(self, event):
        Controller_handel_all_events.f_handle_event_treeview_of_tab_02_single_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_PXK,
            self.tab_02_entry_id,
            self.tab_02_entry_ma_hang,
            self.tab_02_entry_ten_hang,
            self.tab_02_entry_dvt,
            self.tab_02_entry_sl_thuc_xuat,
            self.tab_02_entry_ghi_chu_mat_hang)
    
    def event_tab_01_button_delete_click(self):
        Controller_handel_all_events.f_handle_event_tab_01_btn_delete_click(
            self.tab_01_label_footer_notification,
            self.tab_01_treeview_PNK)
        
    def event_tab_02_button_delete_click(self):
        Controller_handel_all_events.f_handle_event_tab_02_btn_delete_click(
            self.tab_01_label_footer_notification,
            self.tab_02_treeview_PXK)
    
    def event_tab_01_button_clear_click(self):
        Controller_handel_all_events.f_handle_tab_01_button_clear_click(
            self.tab_01_label_footer_notification, 
            self.tab_01_treeview_PNK)
    
    def event_tab_02_button_clear_click(self):
        Controller_handel_all_events.f_handle_tab_02_button_clear_click(
            self.tab_01_label_footer_notification, 
            self.tab_02_treeview_PXK)
        
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
            self.tab_01_treeview_PNK)