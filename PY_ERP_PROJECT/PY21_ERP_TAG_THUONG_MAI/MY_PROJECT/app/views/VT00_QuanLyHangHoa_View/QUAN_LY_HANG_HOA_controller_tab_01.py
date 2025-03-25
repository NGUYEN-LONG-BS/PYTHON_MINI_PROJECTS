from app.utils import *

class Controller_handel_all_events:
    def update_entry_id_when_initializing(my_treeview, entry_id):
        utils_controller_action_after_event_250216_14h57.update_entry_id_after_adding_new_row(my_treeview, entry_id)

    def f_handle_event_get_the_latest_number_of_slip(entry_so_phieu):
        ma_thanh_vien = "TB"
        loai_phieu = "PNK"
        try:
            utils_controller_action_after_event_250216_14h57.f_get_the_latest_number_of_slip(entry_so_phieu, ma_thanh_vien, loai_phieu)
            return "Have gotten the latest number of slip!"
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return f"Error: {e}"