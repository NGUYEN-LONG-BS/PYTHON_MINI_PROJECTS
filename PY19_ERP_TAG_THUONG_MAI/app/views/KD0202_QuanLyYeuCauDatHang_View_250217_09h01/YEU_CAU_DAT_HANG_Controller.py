from tkinter import messagebox
from utils import *
import traceback
from datetime import datetime
from collections import defaultdict

class controller_get_information_of_module:
    
    def load_loai_phieu():
        loai_phieu = "YCDH"
        return loai_phieu
    
    def load_column_name_so_phieu():
        column_name = "SO_PHIEU"
        return column_name
    
    def load_column_name_ma_khach_hang():
        column_name = "MA_DOI_TUONG"
        return column_name
    
    def load_treeview_config_json_path():
        tab_01_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'KD_YEU_CAU_DAT_HANG', 'treeview_tab_01_YCDH_input.json')
        tab_02_treeview_config_json_path = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'KD_YEU_CAU_DAT_HANG', 'treeview_tab_02_YCDH_log.json')
        return tab_01_treeview_config_json_path, tab_02_treeview_config_json_path

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
    
class Controller_action_after_event:
    
    # Function to update the selected row
    def validate_data_before_updating_row_in_tree_view(*args):
        try:
            # Lấy các giá trị theo thứ tự truyền vào
            (
                entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                tab_01_entry_nhu_cau
                )= args
            
            selected_item = my_treeview.selection()
            new_ma_hang = entry_ma_hang_tab_01.get()
            new_ten_hang = entry_ten_hang_tab_01.get()
            new_nhu_cau = float(tab_01_entry_nhu_cau.get().replace(',', '') or 0)
            
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
                
            if not str(new_nhu_cau).strip():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng nhu cầu không được để trống.", "red")
                return False
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

    # Function to update the selected row
    def begin_updating_row_in_tree_view(*args):
        try:
            (
                entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_kha_dung,
                tab_01_entry_nhu_cau,
                tab_01_entry_sl_giu_cho,
                tab_01_entry_sl_YCDH,
                tab_01_entry_ghi_chu_mat_hang
                )= args
            
            selected_item = my_treeview.selection()
            value_col_00 = my_treeview.item(selected_item, "values")[0] if my_treeview.item(selected_item, "values") else None
            value_col_01 = entry_ma_hang_tab_01.get()
            value_col_02 = entry_ten_hang_tab_01.get()
            value_col_03 = entry_dvt.get()
            value_col_04 = float(entry_sl_kha_dung.get().replace(',', '') or 0)
            value_col_05 = float(tab_01_entry_nhu_cau.get().replace(',', '') or 0)
            value_col_06 = float(tab_01_entry_sl_giu_cho.get().replace(',', '') or 0)
            value_col_07 = float(tab_01_entry_sl_YCDH.get().replace(',', '') or 0)
            value_col_08 = tab_01_entry_ghi_chu_mat_hang.get()
            
            value_to_update = (value_col_00, value_col_01, value_col_02, value_col_03, value_col_04, value_col_05, value_col_06, value_col_07, value_col_08)
            
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

    def update_selected_row(*args):
        try:
            (
                entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_kha_dung,
                tab_01_entry_nhu_cau,
                tab_01_entry_sl_giu_cho,
                tab_01_entry_sl_YCDH,
                tab_01_entry_ghi_chu_mat_hang
                )= args
            
            flag = Controller_action_after_event.validate_data_before_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                tab_01_entry_nhu_cau)
            if flag == False:
                return False
            
            flag = Controller_action_after_event.begin_updating_row_in_tree_view(
                entry_notification,
                my_treeview,
                entry_ma_hang_tab_01,
                entry_ten_hang_tab_01,
                entry_dvt,
                entry_sl_kha_dung,
                tab_01_entry_nhu_cau,
                tab_01_entry_sl_giu_cho,
                tab_01_entry_sl_YCDH,
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
    
    def f_Check_duplicate_and_auto_update_slip_number(entry_so_phieu):
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
        column_name = controller_get_information_of_module.load_column_name_so_phieu()
        try:
            kiem_tra_trung_so_phieu = f_utils_check_duplicate(entry_so_phieu, database_name, table_name, column_name)
            if kiem_tra_trung_so_phieu == False:    # có trùng phiếu
                Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip(entry_so_phieu)
                messagebox.showinfo("Thông báo", "Số phiếu đã tồn tại, đã tự động lấy số phiếu mới. Vui lòng thực hiện lưu lại!")
                return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def f_Check_exist_ma_khach_hang(entry_ma_khach_hang):
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_AD00_DANH_SACH_KHACH_HANG()
        column_name = controller_get_information_of_module.load_column_name_ma_khach_hang()
        try:
            kiem_tra_trung_so_phieu = f_utils_check_exist(entry_ma_khach_hang, database_name, table_name, column_name)
            if kiem_tra_trung_so_phieu == False:    # Chưa có mã khách hàng
                return False
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def f_Check_duplicate_value(entry_so_phieu, database_name, table_name, column_name):
        return f_utils_check_duplicate(entry_so_phieu, database_name, table_name, column_name)
    
    def f_add_new_row(*args):
        try:
            # Get the arguments
            (
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_kha_dung, 
                entry_sl_nhu_cau, 
                entry_sl_giu_cho, 
                entry_sl_yeu_cau_dat_hang, 
                entry_ghi_chu_mat_hang
            )= args
            
            # Get values from elements
            id_value = entry_id.get()
            ma_hang_value = entry_ma_hang.get()
            ten_hang_value = entry_ten_hang.get()
            dvt_value = entry_dvt.get()
            sl_kha_dung_value = float(entry_sl_kha_dung.get().replace(',', '') or 0)
            sl_nhu_cau_value = float(entry_sl_nhu_cau.get().replace(',', '') or 0)
            sl_giu_cho_value = float(entry_sl_giu_cho.get().replace(',', '') or 0)
            sl_yeu_cau_dat_hang_value = float(entry_sl_yeu_cau_dat_hang.get().replace(',', '') or 0)
            ghi_chu_mat_hang_value = entry_ghi_chu_mat_hang.get()
            
            # Start controller
            flag = Controller_action_after_event.f_add_row_into_treeview(
                entry_notification,
                id_value, 
                ma_hang_value, 
                ten_hang_value, 
                dvt_value, 
                sl_kha_dung_value, 
                sl_nhu_cau_value, 
                sl_giu_cho_value, 
                sl_yeu_cau_dat_hang_value, 
                ghi_chu_mat_hang_value, 
                my_treeview
                )
            if flag == False:
                return False
            
            flag = Controller_action_after_event.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            if flag == False:
                return False
            
            flag = Controller_action_after_event.clear_input_fields(
                entry_ghi_chu_mat_hang, 
                entry_sl_nhu_cau,
                entry_sl_giu_cho,
                entry_sl_yeu_cau_dat_hang
                )
            if flag == False:
                return False
            
            return True
        except Exception as e:
            # Correct entry ID because adding fail
            Controller_action_after_event.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def f_add_new_row_and_renew_the_tree_view(*args):
        try:
            # Step 1: get the arguments
            (
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_kha_dung, 
                entry_sl_nhu_cau, 
                entry_sl_giu_cho, 
                entry_sl_yeu_cau_dat_hang, 
                entry_ghi_chu_mat_hang
            )= args
            # Step 2: add new row
            flag = Controller_action_after_event.f_add_new_row(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_kha_dung, 
                entry_sl_nhu_cau, 
                entry_sl_giu_cho, 
                entry_sl_yeu_cau_dat_hang, 
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
    
    def f_save_data_to_sql(*args):
        # Step 1: get value from args
        (
            entry_so_phieu,
            entry_ma_kh,
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            tree
        ) = args
        
        # Step 2.1: get ID_nhan_vien và Xoa_sua
        SQLController.f_controller_handle_btn_save_click(
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            tree
        )
    
    def clear_all_contents_in_treeview(treeview):
        try:
            for item in treeview.get_children():
                treeview.delete(item)
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
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
        
    def f_check_input_of_treeview(entry_notification, id_value, ma_hang, ten_hang, sl_giu_cho, sl_yeu_cau_dat_hang):    
        try:
            # Kiểm tra các trường bắt buộc
            if not id_value or not ma_hang or not ten_hang:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "All fields are required: mã hàng, tên hàng", "red")
                return False
            
            # Kiểm tra id_value có phải số nguyên hay không
            if not id_value.isdigit():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"ID value '{id_value}' must be an integer!", "red")
                return False
            
            # Kiểm tra sl_giu_cho và sl_yeu_cau_dat_hang có phải số hay không
            try:
                sl_giu_cho_value = float(sl_giu_cho)
                sl_yeu_cau_dat_hang_value = float(sl_yeu_cau_dat_hang)
            except ValueError:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Số lượng giữ chỗ '{sl_giu_cho}' và số lượng yêu cầu đặt hàng '{sl_yeu_cau_dat_hang}' phải là số.", "red")
                return False
            
            # Kiểm tra sl_giu_cho và sl_yeu_cau_dat_hang không đồng thời bằng không
            if sl_giu_cho_value == 0 and sl_yeu_cau_dat_hang_value == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng giữ chỗ và số lượng yêu cầu đặt hàng không được đồng thời bằng 0.", "red")
                return False
            
            # Kiểm tra số lượng giữ chỗ hoặc yêu cầu đặt hàng hợp lệ
            if sl_giu_cho_value < 0 or sl_yeu_cau_dat_hang_value < 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng giữ chỗ và số lượng yêu cầu đặt hàng không được âm.", "red")
                return False
            
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
                                sl_kha_dung, 
                                sl_nhu_cau, 
                                sl_giu_cho, 
                                sl_yeu_cau_dat_hang, 
                                ghi_chu_mat_hang, 
                                my_treeview):
        try:
            # Validate input using the helper function
            flag = Controller_action_after_event.f_check_input_of_treeview(entry_notification, 
                                                                           id_value, 
                                                                           ma_hang, 
                                                                           ten_hang, 
                                                                           sl_giu_cho, 
                                                                           sl_yeu_cau_dat_hang)
            if flag == False:
                return False
            
            # Add row to the treeview
            my_treeview.insert("", "end", values=(id_value, ma_hang, ten_hang, dvt, sl_kha_dung, sl_nhu_cau, sl_giu_cho, sl_yeu_cau_dat_hang, ghi_chu_mat_hang))
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def clear_input_fields(entry_ghi_chu_mat_hang, entry_sl_nhu_cau, entry_sl_giu_cho, entry_sl_YCDH):
        try:
            entry_ghi_chu_mat_hang.delete(0, tk.END)
            entry_sl_nhu_cau.delete(0, tk.END)

            entry_sl_giu_cho.config(state='normal')
            entry_sl_giu_cho.delete(0, tk.END)
            entry_sl_giu_cho.config(state='disabled')

            entry_sl_YCDH.config(state='normal')
            entry_sl_YCDH.delete(0, tk.END)
            entry_sl_YCDH.config(state='disabled')
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

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
        
    def set_format_of_treeview_of_tab_01(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_01_treeview_config_json_path)
        
    def set_format_of_treeview_of_tab_02(my_treeview):
        tab_01_treeview_config_json_path, tab_02_treeview_config_json_path = controller_get_information_of_module.load_treeview_config_json_path()
        utils_controller_TreeviewConfigurator_250217_13h20.apply_treeview_config(my_treeview, tab_02_treeview_config_json_path)
    
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
    
    def treeview_of_tab_01_single_click(
        my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_kha_dung,
        entry_sl_nhu_cau,
        entry_sl_giu_cho,
        entry_sl_YCDH,
        entry_ghi_chu_mat_hang):
        
        result_tuple = utils_controller_TreeviewHandler_click_250217_22h34.treeview_single_click(my_treeview)
        if not result_tuple:
            return
        id_value, ma_hang, ten_hang, dvt, sl_kha_dung, sl_nhu_cau, sl_giu_cho, sl_dat_hang, ghi_chu_mat_hang = result_tuple
        
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
        
        if sl_kha_dung is not None:
            entry_sl_kha_dung.delete(0, tk.END)
            if float(sl_kha_dung).is_integer():  # Nếu là số nguyên
                formatted_sl_kha_dung = f"{int(float(sl_kha_dung)):,}"
            else:  # Nếu là số thập phân
                formatted_sl_kha_dung = f"{float(sl_kha_dung):,.2f}"
            entry_sl_kha_dung.insert(0, formatted_sl_kha_dung)
            
        if sl_nhu_cau is not None:
            entry_sl_nhu_cau.delete(0, tk.END)
            if float(sl_nhu_cau).is_integer():  # Nếu là số nguyên
                formatted_sl_nhu_cau = f"{int(float(sl_nhu_cau)):,}"
            else:  # Nếu là số thập phân
                formatted_sl_nhu_cau = f"{float(sl_nhu_cau):,.2f}"
            entry_sl_nhu_cau.insert(0, formatted_sl_nhu_cau)
        
        if sl_giu_cho is not None:
            entry_sl_giu_cho.config(state="normal")
            entry_sl_giu_cho.delete(0, tk.END)
            if float(sl_giu_cho).is_integer():  # Nếu là số nguyên
                formatted_sl_giu_cho = f"{int(float(sl_giu_cho)):,}"
            else:  # Nếu là số thập phân
                formatted_sl_giu_cho = f"{float(sl_giu_cho):,.2f}"
            entry_sl_giu_cho.insert(0, formatted_sl_giu_cho)
            entry_sl_giu_cho.config(state="disabled")
            
        if sl_dat_hang is not None:
            entry_sl_YCDH.config(state="normal")
            entry_sl_YCDH.delete(0, tk.END)
            if float(sl_dat_hang).is_integer():  # Nếu là số nguyên
                formatted_sl_dat_hang = f"{int(float(sl_dat_hang)):,}"
            else:  # Nếu là số thập phân
                formatted_sl_dat_hang = f"{float(sl_dat_hang):,.2f}"
            entry_sl_YCDH.insert(0, formatted_sl_dat_hang)
            entry_sl_YCDH.config(state="disabled")
            
        if ghi_chu_mat_hang is not None:
            entry_ghi_chu_mat_hang.delete(0, tk.END)
            entry_ghi_chu_mat_hang.insert(0, ghi_chu_mat_hang)
            
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
            # Gom lại các cột có trùng mã hàng - cột số 2
            # Cột số 4 giữ lại một dòng duy nhất
            # Cộng tổng các giá trị của các dòng có trùng mã hàng - cột số 5, 6, 7
            # Cột nào có ghi chú thì giữ lại một dòng duy nhất: cột số 8
            
            # Gom nhóm theo mã hàng (cột số 2)
            grouped_data = defaultdict(lambda: [None, "", "", "", 0, 0, 0, 0, set()])  # Dùng set() để lưu nhiều ghi chú

            for row in rows:
                ma_hang = row[1]  # Cột số 2 - Mã hàng
                if ma_hang not in grouped_data:
                    grouped_data[ma_hang][0] = len(grouped_data) + 1  # STT mới
                    grouped_data[ma_hang][1] = ma_hang  # Mã hàng
                    grouped_data[ma_hang][2] = row[2]  # Tên hàng
                    grouped_data[ma_hang][3] = row[3]  # Đơn vị tính (Đvt)
                    grouped_data[ma_hang][4] = float(row[4]) if row[4] else 0  # SL khả dụng

                # Cộng tổng SL nhu cầu
                grouped_data[ma_hang][5] += float(row[5]) if row[5] else 0

                # Lưu lại ghi chú (nếu có)
                if row[8].strip():
                    grouped_data[ma_hang][8].add(row[8].strip())  # Dùng set để tránh trùng lặp ghi chú

            # Tính toán SL giữ chỗ và SL YCDH
            for ma_hang, values in grouped_data.items():
                sl_kha_dung = values[4]
                sl_nhu_cau = values[5]
                values[6] = min(sl_kha_dung, sl_nhu_cau)  # SL giữ chỗ
                values[7] = max(sl_nhu_cau - sl_kha_dung, 0)  # SL YCDH

                # Gộp tất cả ghi chú thành một chuỗi, cách nhau bởi "; "
                values[8] = "; ".join(values[8])

            # Xóa dữ liệu cũ trong Treeview
            for item in my_treeview.get_children():
                my_treeview.delete(item)

            # Cập nhật dữ liệu mới vào Treeview
            for i, (key, values) in enumerate(grouped_data.items(), start=1):
                values[0] = i  # Cập nhật lại số thứ tự
                my_treeview.insert("", "end", values=values)

            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
class Controller_auto_update_sl_giu_cho_va_sl_ycdh():
    def __init__(self, *args):
        # Get arguments
        (self.entry_sl_kha_dung,
        self.entry_sl_nhu_cau,
        self.entry_sl_giu_cho,
        self.entry_sl_yeu_cau_dat_hang) = args
        
        # Trace to monitor changes in entry_sl_kha_dung
        self.var_sl_kha_dung = tk.StringVar()
        self.entry_sl_kha_dung.config(textvariable=self.var_sl_kha_dung)
        self.var_sl_kha_dung.trace_add("write", lambda *args: self.update_entries())
        
        # Bind updates to changes in the first two entries
        self.entry_sl_nhu_cau.bind("<KeyRelease>", self.update_entries)
            
    def validate_and_update(self, proposed_value):
        self.update_entries()
        return True
    
    def update_entries(self, event=None):
        try:
            # Loại bỏ dấu phẩy ngăn cách phần ngàn
            sl_kha_dung = self.entry_sl_kha_dung.get().replace(",", "")
            sl_nhu_cau = self.entry_sl_nhu_cau.get().replace(",", "")
            
            # Retrieve and convert the input values
            num_kha_dung = float(sl_kha_dung or 0)
            num_nhu_cau = float(sl_nhu_cau or 0)

            # Calculate the values for the dependent entries
            min_value = min(num_kha_dung, num_nhu_cau)
            difference = max((num_nhu_cau - num_kha_dung), 0)

            if min_value.is_integer():  # Nếu là số nguyên
                formatted_text_01 = f"{int(min_value):,}"
            else:  # Nếu là số thập phân
                formatted_text_01 = f"{min_value:,.2f}"
            
            if difference.is_integer():  # Nếu là số nguyên
                formatted_text_02 = f"{int(difference):,}"
            else:  # Nếu là số thập phân
                formatted_text_02 = f"{difference:,.2f}"

            # Update the dependent entries
            self.entry_sl_giu_cho.config(state="normal")
            self.entry_sl_giu_cho.delete(0, tk.END)
            self.entry_sl_giu_cho.insert(0, f"{formatted_text_01}")
            self.entry_sl_giu_cho.config(state="readonly")

            self.entry_sl_yeu_cau_dat_hang.config(state="normal")
            self.entry_sl_yeu_cau_dat_hang.delete(0, tk.END)
            self.entry_sl_yeu_cau_dat_hang.insert(0, f"{formatted_text_02}")
            self.entry_sl_yeu_cau_dat_hang.config(state="readonly")
        except ValueError:
            # Handle invalid input gracefully
            self.entry_sl_giu_cho.config(state="normal")
            self.entry_sl_giu_cho.delete(0, tk.END)
            self.entry_sl_giu_cho.insert(0, "Error")
            self.entry_sl_giu_cho.config(state="readonly")

            self.entry_sl_yeu_cau_dat_hang.config(state="normal")
            self.entry_sl_yeu_cau_dat_hang.delete(0, tk.END)
            self.entry_sl_yeu_cau_dat_hang.insert(0, "Error")
            self.entry_sl_yeu_cau_dat_hang.config(state="readonly")
            
class cls_test_Controller_04_validate_before_saving():
    def __init__(self, tree):
        self.data_sl_kha_dung = []
            
    def validate_and_update(self):
        print("Kiểm tra số lượng khả dụng khớp thì mới cho lưu!")
        return True
                
class Controller_delete_row_in_SQL:
    def update_deleted(so_phieu):
        # Create query
        database_name = f_utils_get_DB_NAME()
        proc_name = controller_get_information_of_module.load_proc_update_xoa_sua()
        status = "deleted"
        query = f"EXEC [{database_name}].[dbo].[{proc_name}] '{so_phieu}', '{status}'"
        # Sent SQL query
        utils_model_SQL_server.sent_SQL_query(query)

class Controller_mark_expired_slip:
    def mark_expired(so_phieu):
        # Create query
        database_name = f_utils_get_DB_NAME()
        proc_name = controller_get_information_of_module.load_proc_mark_expired()
        status = "1"
        query = f"EXEC [{database_name}].[dbo].[{proc_name}] '{so_phieu}', '{status}'"
        # Sent SQL query
        utils_model_SQL_server.sent_SQL_query(query)

class Controller_edit_row_in_SQL:
    def update_edited(so_phieu):
        # Create query
        database_name = f_utils_get_DB_NAME()
        proc_name = controller_get_information_of_module.load_proc_update_xoa_sua()
        status = "edited"
        query = f"EXEC [{database_name}].[dbo].[{proc_name}] '{so_phieu}', '{status}'"
        # Sent SQL query
        utils_model_SQL_server.sent_SQL_query(query)

class SQLController:
    def load_data(tree, query):
        data = utils_model_SQL_server.fetch_data(query)
        
        # tree = self.treeview_test_of_tag_02
        for item in tree.get_children():
            tree.delete(item)
        for row in data:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4],
                                           row[5], row[6], row[7], row[8], row[9],
                                           row[10], row[11], row[12], row[13], row[14],
                                           row[15]))
        
    def load_data_with_quey_and_params(tree, query, params_list):
        data = utils_model_SQL_server.fetch_data_with_quey_and_params(query, params_list)
        
        # tree = self.treeview_test_of_tag_02
        for item in tree.get_children():
            tree.delete(item)
        for row in data:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4],
                                           row[5], row[6], row[7], row[8], row[9],
                                           row[10], row[11], row[12], row[13], row[14],
                                           row[15]))    
    
    # Function to print data from the Treeview
    def get_data_to_import_to_SQL(*args):
        (
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            tree
        ) = args
        
        # Các giá trị mặc định
        ID_nhan_vien = utils_controller_get_information_of_database.load_id_nhan_vien()
        Xoa_Sua = utils_controller_get_information_of_database.load_xoa_sua_mac_dinh()
        Expired = utils_controller_get_information_of_database.load_expired_mac_dinh()
        
        value_ma_khach_hang = "" if entry_ma_kh.get() == "search here" else entry_ma_kh.get()
        value_so_hop_dong = "" if entry_so_hop_dong.get() == "search here" else entry_so_hop_dong.get()
        # Tạo một list chứa dữ liệu để export
        try:
            data = []
            for child in tree.get_children():
                row = tree.item(child, "values")
                data.append((
                    ID_nhan_vien
                    ,Xoa_Sua
                    ,f_utils_get_formatted_today_YYYY_MM_DD()
                    ,entry_so_phieu.get()
                    ,value_ma_khach_hang
                    ,entry_ten_kh.get()
                    ,entry_mst.get()
                    ,entry_dia_chi.get()
                    ,value_so_hop_dong
                    ,entry_thong_tin_hop_dong.get()
                    ,entry_ghi_chu_cua_phieu.get()
                    ,int(row[0])
                    ,row[1]
                    ,row[2]
                    ,row[3]
                    ,float(row[4])
                    ,float(row[5])
                    ,float(row[6])
                    ,float(row[7])
                    ,row[8],
                    Expired
                ))
            return True, data
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            data = []
            return False, data
    
    def f_controller_handle_btn_save_click(*args):
        (
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            tree
        ) = args
        
        # Step_01: Get data
        flag, data_array = SQLController.get_data_to_import_to_SQL(entry_so_phieu, 
                                                                    entry_ma_kh, 
                                                                    entry_ten_kh,
                                                                    entry_mst,
                                                                    entry_dia_chi,
                                                                    entry_so_hop_dong,
                                                                    entry_thong_tin_hop_dong,
                                                                    entry_ghi_chu_cua_phieu,
                                                                    tree
                                                                    )
        if flag == False:
            return "Data validation failed (01). Please fix the errors."
        
        # Step_02: validate data
        f_utils_get_unique_column_from_data(data_array, 8)
        # Step_03: Export data to SQL
        if utils_model_SQL_server.f_validate_data_format_KD02_YEU_CAU_DAT_HANG(data_array):
            # If data is valid
            database_name = utils_controller_get_information_of_database.load_database_name()
            table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
            utils_model_SQL_server.f_goi_ham_Export_to_table(data_array, database_name, table_name)
            return "Data exported"
        else:
            return "Data validation failed (02). Please fix the errors."
        
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

class Controller_handel_all_events:
    
    def handle_event_tab_02_button_edit_click(entry_notification, active_tab, elements_list):
        
        # Active tab
        notebook = active_tab.master  # Get the Notebook that contains the tab
        notebook.select(active_tab)  # Select the correct tab
        
        (
            entry_ngay_tren_phieu,
            entry_so_phieu,
            entry_ma_khach_hang,
            entry_ten_hhach_hang,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_note_for_slip,
            my_treeview_to_get_data,
            my_treeview_to_load_data
            ) = elements_list

        # Get the selected items
        selected_items = my_treeview_to_get_data.selection()
        
        # Check if more than one row is selected
        if len(selected_items) > 1:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, Please select only one row.", "blue")
            return
        
        # Check if no row is selected
        if not selected_items:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, No row selected.", "blue")
            return
        
        # Get the selected row
        for item in selected_items:
            row_values = my_treeview_to_get_data.item(item, 'values')
            if len(row_values) > 2:  # Ensure the row has at least 2 columns
                so_phieu = row_values[2]
                Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.begin_editing_slip(elements_list, so_phieu)
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Begin editing slip {so_phieu}.", "blue")
                return
    
    def handle_event_tab_02_btn_delete_slip_click(entry_notification, my_treeview):
        # Get the selected items
        selected_items = my_treeview.selection()
        
        # Check if more than one row is selected
        if len(selected_items) > 1:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, Please select only one row.", "blue")
            return
        
        # Check if no row is selected
        if not selected_items:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, No row selected.", "blue")
            return 
            
        # Get the selected row
        for item in selected_items:
            row_values = my_treeview.item(item, 'values')
            if len(row_values) > 2:  # Ensure the row has at least 2 columns
                so_phieu = row_values[2]
                Controller_delete_row_in_SQL.update_deleted(so_phieu)
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"{so_phieu}, Slip deleted.", "blue")
                return 

    def handle_event_tab_02_btn_mark_expired_click(entry_notification, my_treeview):
        # Get the selected items
        selected_items = my_treeview.selection()
        
        # Check if more than one row is selected
        if len(selected_items) > 1:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, Please select only one row.", "blue")
            return
        
        # Check if no row is selected
        if not selected_items:
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Selection Error, No row selected.", "blue")
            return 
            
        # Get the selected row
        for item in selected_items:
            row_values = my_treeview.item(item, 'values')
            if len(row_values) > 2:  # Ensure the row has at least 2 columns
                so_phieu = row_values[2]
                Controller_mark_expired_slip.mark_expired(so_phieu)
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"{so_phieu}, Slip deleted.", "blue")
                return 

    def handle_event_tab_01_btn_update_slip_click(entry_notification, entries_list):
        (
            entry_so_phieu,
            entry_ma_kh,
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            my_treeview
            ) = entries_list
        # Get the selected items
        so_phieu = entry_so_phieu.get().strip()
        if not so_phieu:
            return
        
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
        column_name = controller_get_information_of_module.load_column_name_so_phieu()
        
        # Kiểm tra số phiếu đã tồn tại chưa
        flag = f_utils_check_exist(entry_so_phieu, database_name, table_name, column_name)
        if flag == False:
            return
        
        # validate data
        flag = Controller_event_tab_01_btn_save_click.validate_data( 
                database_name, 
                table_name, 
                column_name,
                entry_notification,
                entry_ma_kh,
                my_treeview
            )
        if flag == False:
            return
        
        # cập nhật thông tin cũ thành edited
        Controller_edit_row_in_SQL.update_edited(so_phieu)
        
        # create new record
        Controller_action_after_event.f_save_data_to_sql(
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_hop_dong,
                entry_thong_tin_hop_dong,
                entry_ghi_chu_cua_phieu,
                my_treeview
                )
        
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"{so_phieu}, Slip updated.", "blue")
        return 

    def f_handle_event_tab_02_button_export_all_data_click(entry_notification):
        try:
            # Tạo câu query SQL với danh sách số phiếu
            query, header = controller_get_information_of_module.load_query_select_all_data()

            flag, path = utils_controller_Export_data_to_Excel_250222_09h16.export_log_to_excel(query, header)
            if flag == False:
                return False
            
            # Notification
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, path, "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
        
    def f_handle_event_tab_02_button_export_excel_click(entry_notification, my_treeview):
        try:
            # Export log to Excel
            # lấy danh sách số phiếu từ treeview
            danh_sach_so_phieu = f_utils_get_unique_column_from_treeview(my_treeview, 2)
            # print("danh_sach_so_phieu", danh_sach_so_phieu)
            
            # Chuyển danh sách số phiếu thành chuỗi SQL, đảm bảo các giá trị dạng chuỗi được bao trong dấu nháy đơn
            so_phieu_str = ', '.join([f"'{str(x)}'" for x in danh_sach_so_phieu])
            # print("so_phieu_str", so_phieu_str)
            
            query, header = controller_get_information_of_module.load_query_select_data_filtered_to_Excel(so_phieu_str)
            
            flag, path = utils_controller_Export_data_to_Excel_250222_09h16.export_log_to_excel(query, header)
            if flag == False:
                return False
            
            # Notification
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, path, "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
    
    def f_handle_event_tab_01_button_template_click(entry_notification):
        try:
            
            # Load the column headers from SQL
            database_name = utils_controller_get_information_of_database.load_database_name()
            table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
            
            column_names = utils_controller_get_the_header_of_table_in_SQL_250221_11h01.get_column_names(database_name, table_name)
            
            if not column_names:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Error: No data found!", "red")
                return False
            
            flag, text = f_utils_create_template_excel_file(file_name="template_YCDH.xlsx", sheet_name="template_YCDH", column_names=column_names)
            if flag == False:
                return False
            else:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, text, "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
        
    def f_handle_event_tab_01_button_get_import_file_click(entry_notification):
        try:
            file_name, file_bath = f_utils_open_file()
            if not file_name:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "No excel file selected!", "red")
                return False
            
            # load data from excel file
            # Bắt đầu từ ô A1
            data = utils_model_get_data_from_Excel_250221_16h45.get_data_from_excel(file_bath, "template_YCDH", start_row=1, start_col=1)
            if not data:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "No data found in the selected file!", "red")
                return False

            # Chuyển dữ liệu từ list thành DataFrame
            df = pd.DataFrame(data[1:], columns=data[0])

            # Bỏ 2 cột đầu tiên
            df = df.iloc[:, 2:]

            # Chuyển DataFrame thành list
            data_list = df.values.tolist()

            # validate data
            flag = Controller_validate_data_from_Excel_file_to_import_to_SQL_250221_17h05.validate_data_from_Excel(entry_notification, data_list)
            if flag == False:
                return False
            
            response = messagebox.askyesno("Xác nhận", "Dữ liệu đã hợp lệ. Bạn có muốn tiếp tục lưu không?")
            if response == False:
                return False

            # Load data to database
            server_name = f_utils_get_DB_HOST()
            database_name = f_utils_get_DB_NAME()
            login_name, login_pass = f_utils_get_DB_USER_AND_DB_PASSWORD()
            table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
            data_array = data_list
            flag = utils_model_import_data_to_SQL_SERVER_250221_16h45.f_insert_data_to_sql(entry_notification,
                                                                                           server_name, 
                                                                                           database_name, 
                                                                                           login_name, 
                                                                                           login_pass, 
                                                                                           table_name, 
                                                                                           data_array)
            if flag == False:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Import to Database fail!", "red")
                messagebox.showinfo("Thông báo", "Lưu không thành công!")
                return False
            else:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Save data successfully!", "blue")
                messagebox.showinfo("Thông báo", "Dữ liệu đã được lưu thành công!")
                return True
                
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def f_handle_event_update_selected_row_click(*args):
        try:
            (
            entry_notification,
            my_treeview,
            entry_ma_hang_tab_01,
            entry_ten_hang_tab_01,
            entry_dvt,
            entry_sl_kha_dung,
            tab_01_entry_nhu_cau,
            tab_01_entry_sl_giu_cho,
            tab_01_entry_sl_YCDH,
            tab_01_entry_ghi_chu_mat_hang
            )= args
            
            flag = Controller_action_after_event.update_selected_row(
            entry_notification,
            my_treeview,
            entry_ma_hang_tab_01,
            entry_ten_hang_tab_01,
            entry_dvt,
            entry_sl_kha_dung,
            tab_01_entry_nhu_cau,
            tab_01_entry_sl_giu_cho,
            tab_01_entry_sl_YCDH,
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
    
    def f_handle_event_tab_01_btn_delete_click(entry_notification, my_treeview):
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
    
    def f_handle_tab_01_button_clear_click(entry_notification, my_treeview):
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

    def f_handle_btn_print_click():
        try:
            path_template_file = os.path.join(PATH_ASSETS_TEMPLATES_EXCEL, "PRINT_KD0201.xlsx")
            sheet_name = "KD0201_YEU_CAU_DAT_HANG"
            f_utils_open_print_template(path_template_file, sheet_name)
            return "Print template opened successfully!"
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return f"Error: {e}"
    
    def f_handle_event_get_the_latest_number_of_slip(tab_01_entry_so_phieu):
        try:
            Controller_action_after_event.f_get_the_latest_number_of_slip(tab_01_entry_so_phieu)
            return "Have gotten the latest number of slip!"
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return f"Error: {e}"
        
    def f_handle_event_tab_01_button_add_row_click(*args):
        try:
            # Get the arguments
            (
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_kha_dung, 
                entry_sl_nhu_cau, 
                entry_sl_giu_cho, 
                entry_sl_yeu_cau_dat_hang, 
                entry_ghi_chu_mat_hang
            )= args
            flag = Controller_action_after_event.f_add_new_row_and_renew_the_tree_view(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_kha_dung, 
                entry_sl_nhu_cau, 
                entry_sl_giu_cho, 
                entry_sl_yeu_cau_dat_hang, 
                entry_ghi_chu_mat_hang
            )

        # Notification
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Adding row successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
        
    def f_handle_event_tab_02_button_filter_slip(entry_notification, my_treeview, *args):
        try:
            # Get the arguments
            (
                entry_so_phieu, 
                entry_so_hop_dong,
                entry_ngay_bat_dau,
                entry_ngay_ket_thuc,
                entry_ma_doi_tuong,
                entry_ma_hang,
                combo_trang_thai
            )= args
            
            so_phieu = entry_so_phieu.get()
            so_hop_dong = entry_so_hop_dong.get()
            ngay_bat_dau = entry_ngay_bat_dau.get()
            ngay_ket_thuc = entry_ngay_ket_thuc.get()
            ma_doi_tuong = entry_ma_doi_tuong.get()
            ma_hang = entry_ma_hang.get()
            
            # Reformat the value
            formated_ngay_bat_dau = f_utils_change_format_date_from_ddmmyyyy_to_yyyymmdd(ngay_bat_dau)
            formated_ngay_ket_thuc = f_utils_change_format_date_from_ddmmyyyy_to_yyyymmdd(ngay_ket_thuc)
            if ma_doi_tuong == 'search here':
                ma_doi_tuong = ''
            if ma_hang == 'search here':
                ma_hang = ''

            if combo_trang_thai.get() == "Còn hạn":
                combo_trang_thai = 0
            else:
                combo_trang_thai = 1
                    
            query = controller_get_information_of_module.load_query_filter_data_to_treeview()
            
            # SQLController.load_data(my_treeview, query)
            SQLController.load_data_with_quey_and_params(my_treeview, query, (combo_trang_thai, so_phieu, so_phieu, so_hop_dong, so_hop_dong, formated_ngay_bat_dau, formated_ngay_ket_thuc, formated_ngay_bat_dau, formated_ngay_ket_thuc, ma_doi_tuong, ma_doi_tuong, ma_hang, ma_hang))
            
            # Notification
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Data loaded!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
        
    def f_handle_event_tab_02_button_clear_filter(
            entry_notification, 
            my_treeview,
            tab_02_entry_filter_slip_number,
            tab_02_entry_filter_contract_number,
            tab_02_entry_ma_khach_hang,
            tab_02_entry_ten_khach_hang,
            tab_02_entry_ma_hang,
            tab_02_entry_ten_hang,
            tab_02_combo_trang_thai):
        
        try:
            # clear all entries
            tab_02_entry_filter_slip_number.delete(0, tk.END)
            tab_02_entry_filter_contract_number.delete(0, tk.END)
            tab_02_entry_ma_khach_hang.delete(0, tk.END)
            tab_02_entry_ten_khach_hang.delete(0, tk.END)
            tab_02_entry_ma_hang.delete(0, tk.END)
            tab_02_entry_ten_hang.delete(0, tk.END)
            tab_02_combo_trang_thai.set("Còn hạn")
            
            # Create value to filter and fetch data
            so_phieu = None
            so_hop_dong = None
            formated_ngay_bat_dau = None
            formated_ngay_ket_thuc = None
            ma_doi_tuong = None
            ma_hang = None
            combo_trang_thai = 0
            
            query = controller_get_information_of_module.load_query_filter_data_to_treeview()
            
            # SQLController.load_data(my_treeview, query)
            SQLController.load_data_with_quey_and_params(my_treeview, query, (combo_trang_thai, so_phieu, so_phieu, so_hop_dong, so_hop_dong, formated_ngay_bat_dau, formated_ngay_ket_thuc, formated_ngay_bat_dau, formated_ngay_ket_thuc, ma_doi_tuong, ma_doi_tuong, ma_hang, ma_hang))
            
            utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Clear all filter!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
        
    def update_entry_id_when_initializing(my_treeview, entry_id):
        Controller_action_after_event.update_entry_id_after_adding_new_row(my_treeview, entry_id)
        
    def f_handle_event_initializing_format_of_treeview_of_tab_01(my_treeview):
        Controller_action_after_event.set_format_of_treeview_of_tab_01(my_treeview)
    
    def f_handle_event_initializing_format_of_treeview_of_tab_02(my_treeview):
        Controller_action_after_event.set_format_of_treeview_of_tab_02(my_treeview)

    def f_handle_event_treeview_of_tab_01_double_click(entry_notification, my_treeview):
        ma_hang = Controller_action_after_event.treeview_of_tab_01_double_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, ma_hang, "blue")
        
    def f_handle_event_treeview_of_tab_02_double_click(entry_notification, my_treeview):
        So_phieu = Controller_action_after_event.treeview_of_tab_02_double_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, So_phieu, "blue")

    def f_handle_event_treeview_of_tab_01_single_click(
            entry_notification,
            my_treeview,
            entry_id,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_kha_dung,
            entry_sl_nhu_cau,
            entry_sl_giu_cho,
            entry_sl_YCDH,
            entry_ghi_chu_mat_hang):
        
        Controller_action_after_event.treeview_of_tab_01_single_click(
        my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_kha_dung,
        entry_sl_nhu_cau,
        entry_sl_giu_cho,
        entry_sl_YCDH,
        entry_ghi_chu_mat_hang)
        
    def f_handle_event_treeview_of_tab_02_single_click(entry_notification, 
                                                       my_treeview):
        so_phieu = Controller_action_after_event.treeview_of_tab_02_single_click(my_treeview)
        utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, so_phieu, "blue")
        
    def f_handle_event_tab_01_btn_save_click(*args):
        try:
            (
                entry_notification,
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_hop_dong,
                entry_thong_tin_hop_dong,
                entry_ghi_chu_cua_phieu,
                tree
            ) = args
            
            # call controller to handle event
            flag = Controller_event_tab_01_btn_save_click.f_handle_event_tab_01_btn_save_click(
                entry_notification,
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_hop_dong,
                entry_thong_tin_hop_dong,
                entry_ghi_chu_cua_phieu,
                tree)
            if flag == False:
                return False
            
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Data saved successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
class Controller_event_tab_01_btn_save_click:
    def f_handle_event_tab_01_btn_save_click(*args):
        try:
            # Step get data and validate data
            (   entry_notification,
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_hop_dong,
                entry_thong_tin_hop_dong,
                entry_ghi_chu_cua_phieu,
                tree
            ) = args
            flag = Controller_event_tab_01_btn_save_click.validate_data(
                entry_notification,
                entry_ma_kh,
                tree
            )
            if flag == False:
                return False
            
            flag = Controller_event_tab_01_btn_save_click.validate_number_of_slip( 
                entry_notification,
                entry_so_phieu
            )
            if flag == False:
                return False
            
            Controller_action_after_event.f_save_data_to_sql(
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_hop_dong,
                entry_thong_tin_hop_dong,
                entry_ghi_chu_cua_phieu,
                tree
                )
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

    def validate_number_of_slip(entry_notification, entry_so_phieu):
        try:
            # Check duplicate slip number
            if Controller_action_after_event.f_Check_duplicate_and_auto_update_slip_number(entry_so_phieu) == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số phiếu bị trùng, vui lòng thử lại!", "red")
                # print("Error at function: ", f_utils_get_current_function_name())
                return False
            
            # pass the validation
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def validate_data(entry_notification, entry_ma_khach_hang, my_treeview):
        try:
            # Check if the client id is empty
            if entry_ma_khach_hang.get() == "" or entry_ma_khach_hang.get() == "search here":
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã khách hàng không được để trống!", "red")
                # print("Error at function: ", f_utils_get_current_function_name())
                return False
            
            if len(my_treeview.get_children()) == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Bảng không có dữ liệu", "red")
                # print("Error at function: ", f_utils_get_current_function_name())
                return False
            
            # Check exist client id
            if Controller_action_after_event.f_Check_exist_ma_khach_hang(entry_ma_khach_hang) == False:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã khách hàng chưa tồn tại!", "red")
                # print("Error at function: ", f_utils_get_current_function_name())
                return False
            
            # pass the validation
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
class Controller_validate_data_from_Excel_file_to_import_to_SQL_250221_17h05:
    def validate_data_from_Excel(entry_notification, data):
        try:
            # Check if the data is empty
            if not data:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "No data found in the selected file!", "red")
                # print("Error at function: ", f_utils_get_current_function_name())
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG:
    def begin_editing_slip(elements_list, so_phieu):
        (
            entry_ngay_tren_phieu,
            entry_so_phieu,
            entry_ma_khach_hang,
            entry_ten_hhach_hang,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_note_for_slip,
            my_treeview_to_get_data,
            my_treeview_to_load_data
            ) = elements_list
        data = Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.get_data_want_to_edit(so_phieu)
        if not data:
            return
        
        first_row = Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.get_first_row(data)
        
        # update entries
        entries_list = (
            entry_ngay_tren_phieu,
            entry_so_phieu,
            entry_ma_khach_hang,
            entry_ten_hhach_hang,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_note_for_slip
            )
        Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.Insert_data_into_entries(entries_list, first_row)
        Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.Insert_data_into_treeview(my_treeview_to_load_data, data)
    
    def get_data_want_to_edit(so_phieu):
        # Create query
        database_name = f_utils_get_DB_NAME()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_KD02_YEU_CAU_DAT_HANG()
        query = f"""
        SELECT * FROM [{database_name}].[dbo].[{table_name}]
        WHERE SO_PHIEU = '{so_phieu}' AND XOA_SUA = ''
        """
        # Sent SQL query
        data = utils_model_SQL_server.fetch_data(query)
        Controller_inherit_to_edit_slip_YEU_CAU_DAT_HANG.get_first_row(data)
        return data
    
    def get_first_row(data):
        """
        Extracts the first row from a dataset and returns it as a dictionary.

            -param data: List of tuples containing the dataset
            -return: Dictionary with field names as keys and corresponding values
        """
        try:
            if not data:
                return None  # Return None if the data list is empty

            first_row = data[0]
            return first_row
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return None
    
    def Insert_data_into_entries(entries_list, data):
        (
            entry_ngay_tren_phieu,
            entry_so_phieu,
            entry_ma_khach_hang,
            entry_ten_hhach_hang,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_note_for_slip
            ) = entries_list
        try:
            
            # Handle the case where the date might be stored as a string instead of a datetime object
            if isinstance(data[4], datetime):
                value_ngay_tren_phieu = data[4].strftime('%d-%m-%Y')  # Convert datetime to 'DD-MM-YYYY'
            else:
                # If it's a string, try to parse it to a datetime object before formatting
                value_ngay_tren_phieu = datetime.strptime(data[4], '%Y-%m-%d %H:%M:%S.%f').strftime('%d-%m-%Y')
            value_so_phieu = data[5]
            value_ma_khach_hang = data[6]
            value_ten_khach_hang = data[7]
            value_mst = data[8]
            value_dia_chi = data[9]
            value_so_hop_dong = data[10]
            value_thong_tin_hop_dong = data[11]
            value_note_for_slip = data[12]
            
            # Beging insert into entries
            entry_ngay_tren_phieu.config(state="normal")
            entry_ngay_tren_phieu.delete(0, tk.END)
            entry_ngay_tren_phieu.insert(0, value_ngay_tren_phieu)
            entry_ngay_tren_phieu.config(state="readonly")
            
            entry_so_phieu.config(state="normal")
            entry_so_phieu.delete(0, tk.END)
            entry_so_phieu.insert(0, value_so_phieu)
            entry_so_phieu.config(state="readonly")
            
            entry_ma_khach_hang.delete(0, tk.END)
            entry_ma_khach_hang.insert(0, value_ma_khach_hang)
            
            entry_ten_hhach_hang.delete(0, tk.END)
            entry_ten_hhach_hang.insert(0, value_ten_khach_hang)
            
            entry_mst.delete(0, tk.END)
            entry_mst.insert(0, value_mst)
            
            entry_dia_chi.delete(0, tk.END)
            entry_dia_chi.insert(0, value_dia_chi)
            
            entry_so_hop_dong.delete(0, tk.END)
            entry_so_hop_dong.insert(0, value_so_hop_dong)
            
            entry_thong_tin_hop_dong.delete(0, tk.END)
            entry_thong_tin_hop_dong.insert(0, value_thong_tin_hop_dong)
            
            entry_note_for_slip.delete(0, tk.END)
            entry_note_for_slip.insert(0, value_note_for_slip)
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def Insert_data_into_treeview(my_treeview, data):
        # Xóa tất cả dữ liệu cũ trước khi thêm mới
        my_treeview.delete(*my_treeview.get_children())
        try:
            for item in data:
                # Đảm bảo item có đủ số lượng phần tử
                item = list(item) + [''] * (22 - len(item))  

                # Chuyển đổi các kiểu dữ liệu đặc biệt thành chuỗi
                values = (
                    str(item[13]) if len(item) > 13 else '',
                    str(item[14]) if len(item) > 14 else '',
                    str(item[15]) if len(item) > 15 else '',
                    str(item[16]) if len(item) > 16 else '',
                    str(item[17]) if len(item) > 17 else '',
                    str(item[18]) if len(item) > 18 else '0',  # Decimal -> str
                    str(item[19]) if len(item) > 19 else '0',  # Decimal -> str
                    str(item[20]) if len(item) > 20 else '0',  # Decimal -> str
                    str(item[21]) if len(item) > 21 else ''    # Giá trị cuối cùng (trống)
                )
                
                # Chèn dữ liệu vào Treeview
                my_treeview.insert("", "end", values=values)
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    
    