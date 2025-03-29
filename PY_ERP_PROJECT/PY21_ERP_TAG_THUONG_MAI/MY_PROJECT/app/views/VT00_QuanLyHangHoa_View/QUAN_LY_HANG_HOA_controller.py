from tkinter import messagebox
from app.utils import *
from datetime import datetime
from collections import defaultdict

class controller_get_information_of_module:
    def load_loai_phieu():
        loai_phieu = "PNK"
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
        table_name = "VIEW_INVENTORY_REPORT_QUANTITY_250214_09h40"
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
    
    def load_query_select_all_data():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
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
            table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
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
    
    def load_query_get_list_number_of_slip():
        column_name = controller_get_information_of_module.load_column_name_so_phieu()
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
        # Tạo câu query SQL với danh sách số phiếu
        query = f"""
        SELECT DISTINCT
            {column_name}
        FROM {database_name}.[dbo].{table_name}
        WHERE [XOA_SUA] = ''
        """
        return query
    
    def load_print_template_path():
        path_template_file = os.path.join(PATH_ASSETS_TEMPLATES_EXCEL, "PRINT_KD0201.xlsx")
        return path_template_file
    
    def load_print_template_sheet_name():
        sheet_name = "KD0201_YEU_CAU_DAT_HANG"
        return sheet_name

class Controller_handel_all_events:
    def update_entry_id_when_initializing(my_treeview, entry_id):
        Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
    
    def f_handle_event_get_the_latest_number_of_slip_PNK(entry_so_phieu_PNK):
        Controller_get_the_latest_number_of_slip.get_the_latest_number_of_slip(entry_so_phieu_PNK)
        
    def f_handle_event_get_the_latest_number_of_slip_PXK(entry_so_phieu_PXK):
        Controller_get_the_latest_number_of_slip.get_the_latest_number_of_slip(entry_so_phieu_PXK)
        
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
        # controller_create_new_inventory.start_create_new_inventory(entry_notification,
        #                                     entry_new_id_code
        #                                     , entry_new_id_name
        #                                     , entry_new_dvt)
        Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG.f_save_data_on_GUI_to_database(entry_notification,
                                                                                    entry_new_id_code
                                                                                    , entry_new_id_name
                                                                                    , entry_new_dvt)
    
    def f_handle_event_tab_06_button_filter_log_click(entry_notification, entry_ma_hang, my_treeview):
        Controller_filter_with_conditions_on_tab_06.filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview)
        
    def f_handle_event_tab_06_button_clear_filter(entry_notification, 
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho):
        Controller_clear_all_filter_condition.clear_filter_condition(entry_notification,
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
            entry_sl_thuc_nhap, 
            entry_ghi_chu_mat_hang):
        
        Controller_add_row_to_treeview.add_row(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_sl_thuc_nhap, 
            entry_ghi_chu_mat_hang)
        
    def f_handle_event_tab_02_button_add_row_click(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_sl_thuc_nhap, 
            entry_ghi_chu_mat_hang):
        
        Controller_add_row_to_treeview.add_row(entry_notification,
            my_treeview, 
            entry_id,
            entry_ma_hang, 
            entry_ten_hang, 
            entry_dvt, 
            entry_sl_thuc_nhap, 
            entry_ghi_chu_mat_hang)
    
    def f_handle_event_update_selected_row_click(*args):
        (
        entry_notification,
        my_treeview,
        entry_ma_hang_tab_01,
        entry_ten_hang_tab_01,
        entry_dvt,
        entry_sl_thuc_nhap,
        tab_01_entry_ghi_chu_mat_hang
        )= args
            
        Controller_update_selected_row.update_selected_row(entry_notification,
        my_treeview,
        entry_ma_hang_tab_01,
        entry_ten_hang_tab_01,
        entry_dvt,
        entry_sl_thuc_nhap,
        tab_01_entry_ghi_chu_mat_hang)
        
    def f_handle_event_treeview_of_tab_01_double_click(entry_notification, my_treeview):
        ma_hang = Controller_click_on_treeview.treeview_of_tab_01_double_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, ma_hang, "blue")
        
    def f_handle_event_treeview_of_tab_01_single_click(entry_notification, 
            my_treeview,
            entry_id,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_ghi_chu_mat_hang):
        
        Controller_click_on_treeview.treeview_of_tab_01_single_click(
        my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_thuc_nhap,
        entry_ghi_chu_mat_hang)
        
    def f_handle_event_tab_01_btn_delete_click(entry_notification, my_treeview):
        Controller_delete_row_in_treeview.delete_row(entry_notification, my_treeview)
    
    def f_handle_tab_01_button_clear_click(entry_notification, my_treeview):
        Controller_clear_all_rows_in_treeview.clear_all_rows(entry_notification, my_treeview)
        
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

class Controller_update_entry_id:
    def update_entry_id_after_adding_new_row(tree, entry_id):
        try:
            row_count = 1 + len(tree.get_children())    
            entry_id.config(state="normal")  # Enable the Entry widget to update the value
            entry_id.delete(0, tk.END)  # Clear the existing value
            entry_id.insert(0, row_count)  # Insert the new value (ID)
            entry_id.config(state="disabled")  # Disable the Entry widget again
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False        

class Controller_get_the_latest_number_of_slip:

    def f_get_the_latest_number_of_slip(entry_so_phieu):
        ma_thanh_vien = utils_controller_get_information_of_database.load_ma_thanh_vien()
        loai_phieu = controller_get_information_of_module.load_loai_phieu()
        # Get the latest number of slip
        so_phieu = Controller_get_the_latest_number_of_slip.handle_button_get_number_of_slip_click()
        # Create the connection string
        connection_number_of_slip = f"{ma_thanh_vien}-{loai_phieu}-{so_phieu + 1}"
        # Config the entry_so_phieu
        entry_so_phieu.config(state="normal")
        entry_so_phieu.delete(0, tk.END)
        entry_so_phieu.insert(0, connection_number_of_slip)
        entry_so_phieu.config(state="readonly")


    def get_the_latest_number_of_slip(tab_01_entry_so_phieu):
        try:
            Controller_get_the_latest_number_of_slip.f_get_the_latest_number_of_slip(tab_01_entry_so_phieu)
            return "Have gotten the latest number of slip!"
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return f"Error: {e}"
    
    def handle_button_get_number_of_slip_click():
        # Lấy danh sách số phiếu từ SQL
        data_01 = Controller_get_the_latest_number_of_slip.get_list_number_of_slip()
        # Lấy số phiếu cuối cùng
        data_02 = Controller_get_the_latest_number_of_slip.extract_numbers_from_data_SQL_num_01(data_01)
        return data_02
    
    def get_list_number_of_slip():
        # Tạo câu query SQL với danh sách số phiếu
        query = controller_get_information_of_module.load_query_get_list_number_of_slip()
        # print("query", query)
        
        # lấy danh sách số phiếu từ SQL
        danh_sach_so_phieu = utils_model_get_data_from_SQL.get_data_with_query(query)
        
        return danh_sach_so_phieu
        
    def extract_numbers_from_data_SQL_num_01(data):
        data_01 = data
        data_02 = tuple(int(item[0].split('-')[-1]) for item in data_01)
        if not data_02:
            current_year = str(datetime.now().year)[-2:]  # Lấy 2 số cuối của năm hiện tại
            data_final = int(f'{current_year}0000')
        else:
            data_final = max(data_02)
        return data_final

class Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG:
    def f_save_data_on_GUI_to_database(entry_notification,
                            entry_new_id_code
                            , entry_new_id_name
                            , entry_new_dvt):
        
        # Step_01: Get data
        flag, data_array = Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG.get_data_from_GUI_view(entry_notification,
                            entry_new_id_code
                            , entry_new_id_name
                            , entry_new_dvt
                                                                    )
        if flag == False:
            return
        
        # Step_02: Export data to SQL
        flag, notification_text = utils_model_SQL_server.f_validate_data_format_TB_INVENTORY_CATEGORIES_250214_09h05(data_array)
        
        if flag == False:
            utils_controllers.utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, notification_text, "red")
            return
        
        if flag == True:
            # If data is valid
            table_name = utils_controllers.utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_CATEGORIES()
            flag = utils_model_SQL_server.f_goi_ham_Export_to_table(data_array, table_name)
            if flag == False:
                utils_controllers.utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Thêm dữ liệu không thành công!", "red")
                return
            else:
                utils_controllers.utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Thêm dữ liệu thành công!", "blue")

        
    def get_data_from_GUI_view(entry_notification
                            , entry_new_id_code
                            , entry_new_id_name
                            , entry_new_dvt):
        
        # Các giá trị mặc định
        ID_nhan_vien = utils_controller_get_information_of_database.load_id_nhan_vien()
        Xoa_Sua = utils_controller_get_information_of_database.load_xoa_sua_mac_dinh()
        
        # Tạo một list chứa dữ liệu để export
        try:
            data = []
            
            data.append((
                ID_nhan_vien
                ,Xoa_Sua
                ,entry_new_id_code.get()
                ,entry_new_id_name.get()
                ,entry_new_dvt.get()
                ,0
                ,0
                ,''
            ))
            # print(data)
            return True, data
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            data = []
            return False, data
        
class Controller_filter_with_conditions_on_tab_06:  
    def filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview):
        try:
            ma_hang = entry_ma_hang.get()

            if ma_hang == 'search here':
                ma_hang = ''
                    
            query = controller_get_information_of_module.load_query_filter_data_to_treeview_tab_06()
            
            utils_controller_get_data_from_SQL_to_treeview_with_quey_and_params_list.load_data_with_quey_and_params(my_treeview, query, (ma_hang, ma_hang))
            
            # Notification
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Data loaded!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())

class Controller_clear_all_filter_condition:
    def clear_filter_condition(
            entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            combobox_ma_kho):
        
        try:
            # clear all entries
            entry_ma_hang.delete(0, tk.END)
            entry_ten_hang.delete(0, tk.END)
            kho_list = combobox_ma_kho['values']
            combobox_ma_kho.set(kho_list[0])
            
            # Create value to filter and fetch data
            ma_hang = None
            combo_ma_kho = ""
            
            query = controller_get_information_of_module.load_query_filter_data_to_treeview_tab_06()
            
            utils_controller_get_data_from_SQL_to_treeview_with_quey_and_params_list.load_data_with_quey_and_params(my_treeview, query, (ma_hang, ma_hang))
            
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Clear all filter!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            
class Controller_add_row_to_treeview:
    def add_row(*args):
        try:
            # Get the arguments
            (
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_ghi_chu_mat_hang
            )= args
            flag = Controller_action_after_event.f_add_new_row_and_renew_the_tree_view(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_ghi_chu_mat_hang
            )

        # Notification
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Adding row successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())




class Controller_action_after_event:
    def f_add_new_row_and_renew_the_tree_view(entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_ghi_chu_mat_hang):
        try:
            # Step 2: add new row
            flag = Controller_action_after_event.f_add_new_row(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_ghi_chu_mat_hang
                )
            if flag == False:
                return False
            # Step 3: renew the treeview
            flag = Controller_action_after_event.Kiem_tra_lai_data_trong_treeview(
                entry_notification,
                my_treeview)
            if flag == False:
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
            
    def f_add_new_row(entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_ghi_chu_mat_hang):
        try:
            # Get values from elements
            id_value = entry_id.get()
            ma_hang_value = entry_ma_hang.get()
            ten_hang_value = entry_ten_hang.get()
            dvt_value = entry_dvt.get()
            sl_thuc_nhap_value = entry_sl_thuc_nhap.get()
            ghi_chu_mat_hang_value = entry_ghi_chu_mat_hang.get()
            
            # Start controller
            flag = Controller_action_after_event.f_add_row_into_treeview(
                entry_notification,
                id_value, 
                ma_hang_value, 
                ten_hang_value, 
                dvt_value, 
                sl_thuc_nhap_value, 
                ghi_chu_mat_hang_value, 
                my_treeview
                )
            if flag == False:
                return False
            
            flag = Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            if flag == False:
                return False
            
            flag = Controller_action_after_event.clear_input_fields(entry_ghi_chu_mat_hang)
            if flag == False:
                return False
            
            return True
        except Exception as e:
            # Correct entry ID because adding fail
            Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def Kiem_tra_lai_data_trong_treeview(entry_notification, my_treeview):
        try:
            # step: Lấy data trong treeview
            rows = []
            for item in my_treeview.get_children():
                row_data = my_treeview.item(item, "values")
                rows.append(row_data)

            # Nếu không có dữ liệu thì thoát
            if not rows:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Vui lòng chọn dòng để update!", "red")
                return False

            # step: 
            # Gom lại các cột có trùng mã hàng
            # Cột số lượng tồn (nếu có): giữ lại một dòng duy nhất
            # Cộng tổng các giá trị của các dòng có trùng mã hàng
            # Cột nào có ghi chú thì giữ lại một dòng duy nhất
            
            # Gom nhóm theo mã hàng (cột số 2)
            grouped_data = defaultdict(lambda: [None, "", "", "", 0, set()])  # Dùng set() để lưu nhiều ghi chú

            for row in rows:
                ma_hang = row[1]  # Cột số 2 - Mã hàng
                if ma_hang not in grouped_data:
                    grouped_data[ma_hang][0] = len(grouped_data) + 1  # STT mới
                    grouped_data[ma_hang][1] = ma_hang  # Mã hàng
                    grouped_data[ma_hang][2] = row[2]  # Tên hàng
                    grouped_data[ma_hang][3] = row[3]  # Đơn vị tính (Đvt)
                
                # Cộng tổng SL thực nhập
                grouped_data[ma_hang][4] += float(row[4].replace(',', '')) if row[4] else 0

                # Lưu lại ghi chú (nếu có)
                if row[5].strip():
                    grouped_data[ma_hang][5].add(row[5].strip())  # Dùng set để tránh trùng lặp ghi chú

            # Tính toán SL giữ chỗ và SL YCDH
            for ma_hang, values in grouped_data.items():
                # Gộp tất cả ghi chú thành một chuỗi, cách nhau bởi "; "
                values[5] = "; ".join(values[5])

            # Xóa dữ liệu cũ trong Treeview
            for item in my_treeview.get_children():
                my_treeview.delete(item)

            # Cập nhật dữ liệu mới vào Treeview
            for i, (key, values) in enumerate(grouped_data.items(), start=1):
                values[0] = i  # Cập nhật lại số thứ tự
                
                # Định dạng số lượng SL thực nhập
                if values[4].is_integer():  # Kiểm tra xem có phải là số nguyên không
                    formatted_quantity = f"{int(values[4]):,}"  # Định dạng số nguyên với dấu phân cách nghìn
                else:
                    formatted_quantity = f"{values[4]:,.2f}"  # Định dạng số thập phân với 2 chữ số sau dấu phẩy

                # Cập nhật lại giá trị số lượng đã được định dạng vào Treeview
                values[4] = formatted_quantity
                
                my_treeview.insert("", "end", values=values)

            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def f_add_row_into_treeview(entry_notification, 
                                id_value, 
                                ma_hang, 
                                ten_hang, 
                                dvt, 
                                sl_thuc_nhap, 
                                ghi_chu_mat_hang, 
                                my_treeview):
        try:
            # Validate input using the helper function
            flag = Controller_action_after_event.f_check_input_of_treeview(entry_notification, 
                                                                           id_value, 
                                                                           ma_hang, 
                                                                           ten_hang,
                                                                           sl_thuc_nhap)
            if flag == False:
                return False
            
            # Add row to the treeview
            my_treeview.insert("", "end", values=(id_value, ma_hang, ten_hang, dvt, sl_thuc_nhap, ghi_chu_mat_hang))
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def clear_input_fields(entry_ghi_chu_mat_hang):
        try:
            entry_ghi_chu_mat_hang.delete(0, tk.END)
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def f_check_input_of_treeview(entry_notification, id_value, ma_hang, ten_hang, sl_thuc_nhap):    
        try:
            # Kiểm tra các trường bắt buộc
            if not id_value or not ma_hang or not ten_hang:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "All fields are required: mã hàng, tên hàng", "red")
                return False
            
            # Kiểm tra id_value có phải số nguyên hay không
            if not id_value.isdigit():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"ID value '{id_value}' must be an integer!", "red")
                return False
            
            # Kiểm tra sl_thuc_nhap có phải số hay không
            try:
                sl_thuc_nhap_value = float(sl_thuc_nhap.replace(',', '') or 0)
            except ValueError:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Số lượng thực nhập '{sl_thuc_nhap}' phải là số.", "red")
                return False
            
            # Kiểm tra sl_thuc_nhap khác 0
            if sl_thuc_nhap_value == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng thực nhập không được bằng 0.", "red")
                return False
            
            # Kiểm tra số lượng giữ chỗ hoặc yêu cầu đặt hàng hợp lệ
            if sl_thuc_nhap_value < 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng thực nhập không được âm.", "red")
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def update_selected_row(entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_thuc_nhap,
                tab_01_entry_ghi_chu_mat_hang):
        try:
            flag = Controller_action_after_event.validate_data_before_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_sl_thuc_nhap)
            if flag == False:
                return False
            
            flag = Controller_action_after_event.begin_updating_row_in_tree_view(
                entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_thuc_nhap,
                tab_01_entry_ghi_chu_mat_hang)
            if flag == False:
                return False
            
            flag = Controller_action_after_event.Kiem_tra_lai_data_trong_treeview(entry_notification, my_treeview)
            if flag == False:
                return False
            else:
                return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def validate_data_before_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_sl_thuc_nhap):
        # Function to update the selected row
        try:
            selected_item = my_treeview.selection()
            new_ma_hang = entry_ma_hang_tab_01.get()
            new_ten_hang = entry_ten_hang_tab_01.get()
            new_thuc_nhap = float(entry_sl_thuc_nhap.get().replace(',', '') or 0)
            
            selected_item = my_treeview.selection()  # Get the selected item
            if not selected_item:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Chưa chọn dòng cần cập nhật.", "red")
                return False

            # Kiểm tra các giá trị bắt buộc không được rỗng
            if not new_ma_hang.strip():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã hàng không được để trống.", "red")
                return False

            if not new_ten_hang.strip():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Tên hàng không được để trống.", "red")
                return False
            
            if not str(new_thuc_nhap).strip():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng thực nhập không được để trống.", "red")
                return False
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def begin_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_thuc_nhap,
                tab_01_entry_ghi_chu_mat_hang):
        # Function to update the selected row
        try:
            
            selected_item = my_treeview.selection()
            value_col_00 = my_treeview.item(selected_item, "values")[0] if my_treeview.item(selected_item, "values") else None
            value_col_01 = entry_ma_hang_tab_01.get()
            value_col_02 = entry_ten_hang_tab_01.get()
            value_col_03 = entry_dvt.get()
            value_col_04 = float(entry_sl_thuc_nhap.get().replace(',', '') or 0)
            value_col_05 = tab_01_entry_ghi_chu_mat_hang.get()
            
            value_to_update = (value_col_00, value_col_01, value_col_02, value_col_03, value_col_04, value_col_05)
            
            selected_item = my_treeview.selection()  # Get the selected item
            
            try:
                my_treeview.item(selected_item, values=value_to_update)  # Update the selected item
            except Exception as e:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Cập nhật dòng bị lỗi!", "red")
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def f_delete_one_row_in_treeview(my_treeview):
        try:
            selected_item = my_treeview.selection()  # Get selected item
            if selected_item:  # Check if an item is selected
                my_treeview.delete(selected_item)  # Delete the selected item
            else:  # If no item is selected
                children = my_treeview.get_children()
                if children:  # Check if there are rows in the Treeview
                    last_item = children[-1]  # Get the last item
                    my_treeview.delete(last_item)  # Delete the last item
            
            flag = Controller_action_after_event.f_controller_02_renumber_rows(my_treeview)
            if flag == False:
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def f_controller_02_renumber_rows(my_treeview):
        try:
            for index, item in enumerate(my_treeview.get_children(), start=1):
                values = my_treeview.item(item, "values")  # Get the current values of the row
                new_values = (index,) + values[1:]  # Update the first column with the new number
                my_treeview.item(item, values=new_values)  # Set the updated values
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def clear_all_contents_in_treeview(treeview):
        try:
            for item in treeview.get_children():
                treeview.delete(item)
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
class Controller_update_selected_row:
    def update_selected_row(entry_notification,
            my_treeview,
            entry_ma_hang_tab_01,
            entry_ten_hang_tab_01,
            entry_dvt,
            entry_sl_thuc_nhap,
            tab_01_entry_ghi_chu_mat_hang):
        try:
            flag = Controller_action_after_event.update_selected_row(
            entry_notification,
            my_treeview,
            entry_ma_hang_tab_01,
            entry_ten_hang_tab_01,
            entry_dvt,
            entry_sl_thuc_nhap,
            tab_01_entry_ghi_chu_mat_hang)
            if flag == False:
                return False
                
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Row updated successfully!", "blue")
                return True
    
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_click_on_treeview:
    def treeview_of_tab_01_double_click(my_treeview):
        result_value = utils_controller_TreeviewHandler_click_250217_22h34.treeview_double_click(my_treeview, column_return=1)
        if result_value:
            return result_value
        
    def treeview_of_tab_02_double_click(my_treeview):
        result_value = utils_controller_TreeviewHandler_click_250217_22h34.treeview_double_click(my_treeview, column_return=2)
        if result_value:
            return result_value

    def treeview_of_tab_02_single_click(my_treeview):
        result_value = utils_controller_TreeviewHandler_click_250217_22h34.treeview_double_click(my_treeview, column_return=2)
        if result_value:
            return result_value
    
    def treeview_of_tab_01_single_click(my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_thuc_nhap,
        entry_ghi_chu_mat_hang):
        
        result_tuple = utils_controller_TreeviewHandler_click_250217_22h34.treeview_single_click(my_treeview)
        if not result_tuple:
            return
        id_value, ma_hang, ten_hang, dvt, sl_thuc_nhap, ghi_chu_mat_hang = result_tuple
        
        # Clear and update the Entry widgets if values are returned
        if id_value is not None:
            entry_id.config(state="normal")  # Enable the Entry widget to update the value
            entry_id.delete(0, tk.END)
            entry_id.insert(0, id_value)
            entry_id.config(state="disabled")  # Disable the Entry widget again

        if ma_hang is not None:
            entry_ma_hang.delete(0, tk.END)
            entry_ma_hang.insert(0, ma_hang)
            
        if ten_hang is not None:
            entry_ten_hang.delete(0, tk.END)
            entry_ten_hang.insert(0, ten_hang)
            
        if dvt is not None:
            entry_dvt.delete(0, tk.END)
            entry_dvt.insert(0, dvt)
        
        if sl_thuc_nhap is not None:
            # Loại bỏ dấu phân cách nghìn nếu có
            sl_clean = sl_thuc_nhap.replace(',', '')  # Xóa dấu phân cách nghìn
            
            # Thực hiện chuyển đổi thành float
            try:
                float_value = float(sl_clean)
                
                entry_sl_thuc_nhap.delete(0, tk.END)
                
                if float_value.is_integer():  # Nếu là số nguyên
                    formatted_value = f"{int(float_value):,}"
                else:  # Nếu là số thập phân
                    formatted_value = f"{float_value:,.2f}"
                    
                entry_sl_thuc_nhap.insert(0, formatted_value)
            except ValueError:
                # Nếu không thể chuyển thành float, có thể hiển thị thông báo lỗi hoặc xử lý trường hợp này
                print("Error: Không thể chuyển đổi giá trị thành số.")
            
        if ghi_chu_mat_hang is not None:
            entry_ghi_chu_mat_hang.delete(0, tk.END)
            entry_ghi_chu_mat_hang.insert(0, ghi_chu_mat_hang)

class Controller_delete_row_in_treeview:
    def delete_row(entry_notification, my_treeview):
        try:
            flag = Controller_action_after_event.f_delete_one_row_in_treeview(my_treeview)
            if flag == False:
                return False
            
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Row deleted successfully!", "blue")
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_clear_all_rows_in_treeview:
    def clear_all_rows(entry_notification, my_treeview):
        try:
            flag = Controller_action_after_event.clear_all_contents_in_treeview(my_treeview)
            if flag == False:
                return False
            else:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Clear all rows successfully!", "blue")
                return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False