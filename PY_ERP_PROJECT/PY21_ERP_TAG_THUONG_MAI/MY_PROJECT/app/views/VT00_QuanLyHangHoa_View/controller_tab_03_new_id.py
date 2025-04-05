from app.utils import *

class Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG:
    def f_save_data_on_GUI_to_database(entry_notification,
                            entry_new_id_code
                            , entry_new_id_name
                            , entry_new_dvt):
        
        # Step_01: Get data
        flag, data_array = Controller_save_data_on_GUI_into_database_THEM_MOI_MA_HANG.get_data_from_GUI_tab_03(entry_notification,
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

        
    def get_data_from_GUI_tab_03(entry_notification
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
        