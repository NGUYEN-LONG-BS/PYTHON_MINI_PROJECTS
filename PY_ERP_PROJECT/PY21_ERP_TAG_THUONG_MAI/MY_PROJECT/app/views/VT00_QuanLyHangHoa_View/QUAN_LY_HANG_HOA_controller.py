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
    
    def load_query_filter_data_to_treeview():
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
        danh_sach_id = utils_controller_get_information_of_database.load_danh_sach_id_duoc_phan_quyen()
        query = f"""
                SELECT
                ROW_NUMBER() OVER(ORDER BY [SO_PHIEU] DESC, [NGAY_TREN_PHIEU] DESC) as RowNumber
                ,FORMAT([NGAY_TREN_PHIEU], 'dd-MM-yyyy') as NGAY_TREN_PHIEU
                ,[SO_PHIEU]
                ,[MA_DOI_TUONG]
                ,[TEN_DOI_TUONG]
                ,[SO_HOP_DONG]
                ,[GHI_CHU_PHIEU]
                ,[STT_DONG]
                ,[MA_HANG]
                ,[TEN_HANG]
                ,[DVT]
                ,[SO_LUONG_KHA_DUNG]
                ,[SO_LUONG_NHU_CAU]
                ,[SO_LUONG_GIU_CHO]
                ,[SO_LUONG_YEU_CAU_DAT_HANG]
                ,[GHI_CHU_SP]	
            FROM [{database_name}].[dbo].[{table_name}]
            WHERE 
                [ID_NHAN_VIEN] IN ({danh_sach_id}) AND
                [XOA_SUA] = '' AND
                [EXPIRED] = ? AND
                (? IS NULL OR SO_PHIEU LIKE '%' + ? + '%') AND
                (? IS NULL OR SO_HOP_DONG LIKE '%' + ? + '%') AND
                (? IS NULL OR ? IS NULL OR NGAY_TREN_PHIEU BETWEEN ? AND ?) AND
                (? IS NULL OR MA_DOI_TUONG LIKE '%' + ? + '%') AND
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
        Cotroller_get_the_latest_number_of_slip.get_the_latest_number_of_slip(entry_so_phieu_PNK)
        
    def f_handle_event_get_the_latest_number_of_slip_PXK(entry_so_phieu_PXK):
        Cotroller_get_the_latest_number_of_slip.get_the_latest_number_of_slip(entry_so_phieu_PXK)
        
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
                                            , entry_ma_hang
                                            , entry_new_dvt):
        controller_create_new_inventory.start_create_new_inventory(entry_notification,
                                            entry_new_id_code
                                            , entry_new_id_name
                                            , entry_ma_hang
                                            , entry_new_dvt)

class controller_create_new_inventory:
    def start_create_new_inventory(entry_notification,
                            entry_new_id_code
                            , entry_new_id_name
                            , entry_new_dvt):
        try:
            # call controller to handle event
            flag = controller_create_new_inventory.validate_data( 
                entry_notification,
                entry_new_id_code,
                entry_new_id_name,
                entry_new_dvt
            )
            if flag == False:
                return False
            
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Data created successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def validate_data(entry_notification,
                entry_new_id_code,
                entry_new_id_name,
                entry_new_dvt):
        try:
            # Check if the entry is empty
            if entry_new_id_code.get() == "" or entry_new_id_name.get() == "" or entry_new_dvt.get() == "":
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "All fields are required: mã hàng, tên hàng, đvt", "red")
                return False
            
            # pass the validation
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

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

class Cotroller_get_the_latest_number_of_slip:
    def get_the_latest_number_of_slip(tab_01_entry_so_phieu):
        try:
            Controller_action_after_event.f_get_the_latest_number_of_slip(tab_01_entry_so_phieu)
            return "Have gotten the latest number of slip!"
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return f"Error: {e}"

class Controller_action_after_event:
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
        

class Controller_get_the_latest_number_of_slip:
    
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

