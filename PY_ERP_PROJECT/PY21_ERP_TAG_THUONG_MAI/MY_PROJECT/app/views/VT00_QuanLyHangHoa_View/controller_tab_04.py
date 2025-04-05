from app.utils import *
from . import controller_handle_events

class Controller_filter_with_conditions_on_tab_04:  
    def filter_log_with_conditions(entry_notification, entry_ma_hang, my_treeview):
        try:
            ma_hang = entry_ma_hang.get()

            if ma_hang == 'search here':
                ma_hang = ''
                    
            query = controller_handle_events.controller_get_information_of_module.load_query_filter_data_to_treeview_tab_04()
            
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
            
            query = controller_handle_events.controller_get_information_of_module.load_query_filter_data_to_treeview_tab_04()
            
            utils_controller_get_data_from_SQL_to_treeview_with_quey_and_params_list.load_data_with_quey_and_params(my_treeview, query, (ma_hang, ma_hang))
            
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Clear all filter!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())