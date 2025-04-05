from tkinter import messagebox
from app.utils import *
from datetime import datetime
from collections import defaultdict
from . import controller_tab_01_PNK
from . import controller_tab_02_PXK
from . import controller_tab_03_new_id
from . import controller_tab_04
from . import controller_tab_05
from . import controller_tab_06

class controller_get_information_of_module:
    def load_loai_phieu_PNK():
        loai_phieu = "PNK"
        return loai_phieu
    
    def load_loai_phieu_PXK():
        loai_phieu = "PXK"
        return loai_phieu
    
    def load_column_name_so_phieu():
        column_name = "SO_PHIEU"
        return column_name
    
    def load_column_name_ma_khach_hang():
        column_name = "MA_DOI_TUONG"
        return column_name
    
    def load_column_name_ma_hang():
        column_name = "MA_HANG"
        return column_name
    
    def load_treeview_config_json_path():
        tab_01_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'PNK_table_input.json')
        tab_04_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'PNK_table_log.json')
        
        tab_02_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'PXK_table_input.json')
        tab_05_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'PXK_table_log.json')
        
        tab_06_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'inventories_report.json')
        return tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path

    def load_proc_update_xoa_sua():
        proc_name = "Proc_TB_KD02_YEU_CAU_DAT_HANG_UPDATE_XOA_SUA_250224_13h09"
        return proc_name
    
    def load_proc_mark_expired():
        proc_name = "Proc_TB_KD02_YEU_CAU_DAT_HANG_UPDATE_EXPIRED_250226_13h15"
        return proc_name
    
    def load_query_filter_data_to_treeview_tab_06():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = "VIEW_INVENTORY_REPORT_QUANTITY"
        query = f"""
                SELECT
                ROW_NUMBER() OVER(ORDER BY [MA_HANG]) as RowNumber
                ,[MA_HANG]
                ,[TEN_HANG]
                ,[DVT]
                ,[SL_DAU_KY]
                ,[TONG_SL_NHAP]
                ,[TONG_SL_XUAT]
                ,[TONG_SL_TON]
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE 
                (? IS NULL OR MA_HANG LIKE '%' + ? + '%')
            """
        return query
    
    def load_query_filter_data_to_treeview_tab_04():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = "TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05"
        query = f"""
                SELECT
                ROW_NUMBER() OVER(ORDER BY [SO_PHIEU]) as RowNumber
                ,[SO_PHIEU]
                ,[MA_DOI_TUONG]
                ,[MA_DOI_TUONG]
                ,[SO_PHIEU_DE_NGHI]
                ,[MA_HANG]
                ,[TEN_HANG]
                ,[DVT]
                ,[SO_LUONG]
                ,[GHI_CHU_SP]
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE 
                [PHAN_LOAI_NHAP_XUAT_HOAN] = 'IMPORT'
                AND
                (? IS NULL OR [SO_PHIEU] LIKE '%' + ? + '%')
            """
        return query
    
    def load_query_filter_data_to_treeview_tab_05():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = "TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05"
        query = f"""
                SELECT
                ROW_NUMBER() OVER(ORDER BY [SO_PHIEU]) as RowNumber
                ,[SO_PHIEU]
                ,[MA_DOI_TUONG]
                ,[MA_DOI_TUONG]
                ,[SO_PHIEU_DE_NGHI]
                ,[MA_HANG]
                ,[TEN_HANG]
                ,[DVT]
                ,[SO_LUONG]
                ,[GHI_CHU_SP]
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE 
                [PHAN_LOAI_NHAP_XUAT_HOAN] = 'EXPORT'
                AND
                (? IS NULL OR [SO_PHIEU] LIKE '%' + ? + '%')
            """
        return query
    
    def load_query_select_all_data():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05()
        danh_sach_id = utils_controller_get_information_of_database.load_danh_sach_id_duoc_phan_quyen()
        query = f"""
            SELECT *
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE 
                  [ID_NHAN_VIEN] IN ({danh_sach_id})
            ORDER BY [SO_PHIEU] DESC
            """
        
        # Tạo header cho file Excel
        header = ["ID",
                "DATE",
                "ID_NHAN_VIEN",
                "XOA_SUA",
                "NGAY_TREN_PHIEU",
                "SO_PHIEU",
                "MA_DOI_TUONG",
                "TEN_DOI_TUONG",
                "MA_SO_THUE",
                "DIA_CHI",
                "SO_HOP_DONG",
                "THONG_TIN_HOP_DONG",
                "GHI_CHU_PHIEU",
                "STT_DONG",
                "MA_HANG",
                "TEN_HANG",
                "DVT",
                "SO_LUONG_KHA_DUNG",
                "SO_LUONG_NHU_CAU",
                "SO_LUONG_GIU_CHO",
                "SO_LUONG_YEU_CAU_DAT_HANG",
                "GHI_CHU_SP",
                "EXPIRED"]
        
        return query, header
    
    def load_query_select_data_filtered_to_Excel(danh_sach_so_phieu):
        # Tạo câu query SQL với danh sách số phiếu
            database_name = utils_controller_get_information_of_database.load_database_name()
            table_name = utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05()
            danh_sach_id = utils_controller_get_information_of_database.load_danh_sach_id_duoc_phan_quyen()
            query = f"""
            SELECT 
                ROW_NUMBER() OVER(ORDER BY [SO_PHIEU]) as RowNumber,
                [SO_PHIEU],
                [NGAY_TREN_PHIEU],
                [MA_DOI_TUONG],
                [TEN_DOI_TUONG],
                [MA_SO_THUE],
                [DIA_CHI],
                [SO_HOP_DONG],
                [THONG_TIN_HOP_DONG],
                [GHI_CHU_PHIEU],
                [STT_DONG],
                [MA_HANG],
                [TEN_HANG],
                [DVT],
                [SO_LUONG_KHA_DUNG],
                [SO_LUONG_NHU_CAU],
                [SO_LUONG_GIU_CHO],
                [SO_LUONG_YEU_CAU_DAT_HANG],
                [GHI_CHU_SP]
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE [SO_PHIEU] IN ({danh_sach_so_phieu}) AND
                  [ID_NHAN_VIEN] IN ({danh_sach_id})
            ORDER BY [SO_PHIEU] DESC
            """
            # print(query)
            
            # Tạo header cho file Excel
            header = ["STT", 
                    "Số phiếu", 
                    "Ngày trên phiếu", 
                    "Mã đối tượng", 
                    "Tên đối tượng", 
                    "Mã số thuế", 
                    "Địa chỉ", 
                    "Số hợp đồng", 
                    "Thông tin hợp đồng", 
                    "Ghi chú phiếu", 
                    "STT dòng", 
                    "Mã hàng", 
                    "Tên hàng", 
                    "ĐVT", 
                    "Số lượng khả dụng", 
                    "Số lượng nhu cầu", 
                    "Số lượng giữ chỗ", 
                    "Số lượng yêu cầu đặt hàng", 
                    "Ghi chú sản phẩm"]   
            
            return query, header
    
    def load_query_get_list_number_of_slip(ma_phan_loai = "PNK"):
        column_name = controller_get_information_of_module.load_column_name_so_phieu()
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05()
        # Tạo câu query SQL với danh sách số phiếu
        if ma_phan_loai == "PNK":
            value_phan_loai = "IMPORT"
        elif ma_phan_loai == "PXK":
            value_phan_loai = "EXPORT"
        query = f"""
        SELECT DISTINCT
            {column_name}
        FROM {database_name}.[dbo].{table_name}
        WHERE [XOA_SUA] = ''
            AND [PHAN_LOAI_NHAP_XUAT_HOAN] = '{value_phan_loai}'
        """
        return query
    
    def load_print_template_path():
        path_template_file = os.path.join(PATH_ASSETS_TEMPLATES_EXCEL, "PRINT_KD0201.xlsx")
        return path_template_file
    
    def load_print_template_sheet_name():
        sheet_name = "KD0201_YEU_CAU_DAT_HANG"
        return sheet_name

class Controller_format_treeview:
    def set_format_of_treeview_of_tab_01(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_01_treeview_config_json_path)
        
    def set_format_of_treeview_of_tab_04(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_04_treeview_config_json_path)
        
    def set_format_of_treeview_of_tab_02(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_02_treeview_config_json_path)
    
    def set_format_of_treeview_of_tab_05(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_05_treeview_config_json_path)
        
    def set_format_of_treeview_of_tab_06(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path, tab_04_treeview_config_json_path, tab_05_treeview_config_json_path, tab_06_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_06_treeview_config_json_path)

class Controller_handel_all_events:
    def update_entry_id_when_initializing(my_treeview, entry_id):
        controller_tab_01_PNK.Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
    
    def f_handle_event_get_the_latest_number_of_slip_PNK(entry_so_phieu_PNK):
        controller_tab_01_PNK.Controller_get_the_latest_number_of_slip.start_process_get_the_latest_number_of_slip(entry_so_phieu_PNK, ma_phan_loai = "PNK")
        
    def f_handle_event_get_the_latest_number_of_slip_PXK(entry_so_phieu_PXK):
        controller_tab_01_PNK.Controller_get_the_latest_number_of_slip.start_process_get_the_latest_number_of_slip(entry_so_phieu_PXK, ma_phan_loai = "PXK")
    
    def f_handle_event_get_today_is_date_of_slip(entry_ngay_tren_phieu):
        controller_tab_01_PNK.Controller_get_today.start_process_get_today(entry_ngay_tren_phieu)
    
    def f_handle_event_initializing_format_of_treeview_of_tab_01(my_treeview):
        Controller_format_treeview.set_format_of_treeview_of_tab_01(my_treeview)
    
    def f_handle_event_initializing_format_of_treeview_of_tab_04(my_treeview):
        Controller_format_treeview.set_format_of_treeview_of_tab_04(my_treeview)
        
    def f_handle_event_initializing_format_of_treeview_of_tab_02(my_treeview):
        Controller_format_treeview.set_format_of_treeview_of_tab_02(my_treeview)
    
    def f_handle_event_initializing_format_of_treeview_of_tab_05(my_treeview):
        Controller_format_treeview.set_format_of_treeview_of_tab_05(my_treeview)
    
    def f_handle_event_initializing_format_of_treeview_of_tab_06(my_treeview):
        Controller_format_treeview.set_format_of_treeview_of_tab_06(my_treeview)
        
    def f_handle_event_create_new_inventory(entry_notification,
                                            entry_new_id_code
                                            , entry_new_id_name
                                            , entry_new_dvt):
        controller_tab_03_new_id.Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG.f_save_data_on_GUI_to_database(entry_notification,
                                                                                    entry_new_id_code
                                                                                    , entry_new_id_name
                                                                                    , entry_new_dvt)
    
    def f_handle_event_tab_06_button_filter_log_click(entry_notification, entry_ma_hang, my_treeview):
        controller_tab_06.Controller_filter_with_conditions_on_tab_06.filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview)
        
    def f_handle_event_tab_04_button_filter_log_click(entry_notification, entry_ma_hang, my_treeview):
        controller_tab_04.Controller_filter_with_conditions_on_tab_04.filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview)
        
    def f_handle_event_tab_05_button_filter_log_click(entry_notification, entry_ma_hang, my_treeview):
        controller_tab_05.Controller_filter_with_conditions_on_tab_05.filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview)
    
    def f_handle_event_tab_04_button_clear_filter(entry_notification, 
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho):
        controller_tab_04.Controller_clear_all_filter_condition.clear_filter_condition(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho
            )
    
    def f_handle_event_tab_06_button_clear_filter(entry_notification, 
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho):
        controller_tab_06.Controller_clear_all_filter_condition.clear_filter_condition(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho
            )
        
    
    def f_handle_event_tab_01_button_add_row_click(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_so_luong, 
            entry_don_gia,
            entry_ghi_chu_mat_hang):
        
        controller_tab_01_PNK.Controller_add_row_to_treeview.start_process_add_row(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_so_luong,
            entry_don_gia,
            entry_ghi_chu_mat_hang)
        
    def f_handle_event_tab_02_button_add_row_click(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_so_luong,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
        
        controller_tab_02_PXK.Controller_add_row_to_treeview.start_process_add_row(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_so_luong,
            entry_don_gia,
            entry_ghi_chu_mat_hang)
    
    def f_handle_event_tab_01_update_selected_row_click(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
            
        controller_tab_01_PNK.Controller_update_selected_row.start_process_update_selected_row(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang)
        
    def f_handle_event_tab_02_update_selected_row_click(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
            
        controller_tab_02_PXK.Controller_update_selected_row.start_process_update_selected_row(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang)
        
    def f_handle_event_treeview_of_tab_01_double_click(entry_notification, my_treeview):
        ma_hang = controller_tab_01_PNK.Controller_click_on_treeview.treeview_double_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, ma_hang, "blue")
        
    def f_handle_event_treeview_of_tab_02_double_click(entry_notification, my_treeview):
        ma_hang = controller_tab_02_PXK.Controller_click_on_treeview.treeview_double_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, ma_hang, "blue")
        
    def f_handle_event_treeview_of_tab_01_single_click(entry_notification, 
            my_treeview,
            entry_id,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
        
        controller_tab_01_PNK.Controller_click_on_treeview.treeview_single_click(
        my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_thuc_nhap,
        entry_don_gia,
        entry_ghi_chu_mat_hang)
    
    def f_handle_event_treeview_of_tab_02_single_click(entry_notification, 
            my_treeview,
            entry_id,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
        
        controller_tab_02_PXK.Controller_click_on_treeview.treeview_single_click(
        my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_thuc_nhap,
        entry_don_gia,
        entry_ghi_chu_mat_hang)
        
    def f_handle_event_tab_01_btn_delete_click(entry_notification, my_treeview):
        controller_tab_01_PNK.Controller_delete_row_in_treeview.delete_row(entry_notification, my_treeview)
    
    def f_handle_event_tab_02_btn_delete_click(entry_notification, my_treeview):
        controller_tab_01_PNK.Controller_delete_row_in_treeview.delete_row(entry_notification, my_treeview)
    
    def f_handle_tab_01_button_clear_click(entry_notification, my_treeview):
        controller_tab_01_PNK.Controller_clear_all_rows_in_treeview.clear_all_rows(entry_notification, my_treeview)
        
    def f_handle_tab_02_button_clear_click(entry_notification, my_treeview):
        controller_tab_01_PNK.Controller_clear_all_rows_in_treeview.clear_all_rows(entry_notification, my_treeview)
        
    def f_handle_event_tab_01_btn_save_click(entry_notification,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree):
        
        controller_tab_01_PNK.Controller_save_slip.start_process_save_slip(entry_notification,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree)
    
    def f_handle_event_tab_02_btn_save_click(entry_notification,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree):
        
        controller_tab_02_PXK.Controller_save_slip.start_process_save_slip(entry_notification,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree)
        
   