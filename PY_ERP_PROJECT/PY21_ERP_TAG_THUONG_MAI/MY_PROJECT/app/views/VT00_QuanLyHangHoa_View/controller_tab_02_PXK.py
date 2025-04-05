from tkinter import messagebox
from app.utils import *
from datetime import datetime
from collections import defaultdict
from . import controller_handle_events
from . import controller_tab_01_PNK

class Controller_add_row_to_treeview:
    def start_process_add_row(entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang):
        try:
            flag = Controller_add_row_to_treeview.f_add_new_row_and_renew_the_tree_view(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap, 
                entry_don_gia,
                entry_ghi_chu_mat_hang
            )

        # Notification
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Adding row successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())

    def f_add_new_row_and_renew_the_tree_view(entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang):
        try:
            # Step 2: add new row
            flag = Controller_add_row_to_treeview.f_add_new_row(
                entry_notification,
                my_treeview, 
                entry_id,
                entry_ma_hang, 
                entry_ten_hang, 
                entry_dvt, 
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang
                )
            if flag == False:
                return False
            # Step 3: renew the treeview
            flag = Controller_add_row_to_treeview.Kiem_tra_lai_data_trong_treeview(
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
                entry_don_gia,
                entry_ghi_chu_mat_hang):
        try:
            # Get values from elements
            id_value = entry_id.get()
            ma_hang_value = entry_ma_hang.get()
            ten_hang_value = entry_ten_hang.get()
            dvt_value = entry_dvt.get()
            sl_thuc_nhap_value = entry_sl_thuc_nhap.get()
            don_gia_value = entry_don_gia.get()
            gia_tri_value = float(sl_thuc_nhap_value.replace(',', '') or 0) * float(don_gia_value.replace(',', '') or 0)
            ghi_chu_mat_hang_value = entry_ghi_chu_mat_hang.get()
            
            # Start controller
            flag = Controller_add_row_to_treeview.f_add_row_into_treeview(
                entry_notification,
                id_value, 
                ma_hang_value, 
                ten_hang_value, 
                dvt_value, 
                sl_thuc_nhap_value,
                don_gia_value,
                gia_tri_value,
                ghi_chu_mat_hang_value, 
                my_treeview
                )
            if flag == False:
                return False
            
            flag = controller_tab_01_PNK.Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            if flag == False:
                return False
            
            flag = Controller_add_row_to_treeview.clear_input_fields(entry_ghi_chu_mat_hang)
            if flag == False:
                return False
            
            return True
        except Exception as e:
            # Correct entry ID because adding fail
            controller_tab_01_PNK.Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
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
            grouped_data = defaultdict(lambda: [None, "", "", "", 0, 0, 0, set()])  # Dùng set() để lưu nhiều ghi chú

            for row in rows:
                ma_hang = row[1]  # Cột số 2 - Mã hàng
                if ma_hang not in grouped_data:
                    grouped_data[ma_hang][0] = len(grouped_data) + 1  # STT mới
                    grouped_data[ma_hang][1] = ma_hang  # Mã hàng
                    grouped_data[ma_hang][2] = row[2]  # Tên hàng
                    grouped_data[ma_hang][3] = row[3]  # Đơn vị tính (Đvt)
                    grouped_data[ma_hang][5] = float(row[5].replace(',', '')) if row[5] else 0  # đơn giá
                
                # Cộng tổng SL thực nhập
                grouped_data[ma_hang][4] += float(row[4].replace(',', '')) if row[4] else 0

                # Lưu lại ghi chú (nếu có)
                if row[7].strip():
                    grouped_data[ma_hang][7].add(row[7].strip())  # Dùng set để tránh trùng lặp ghi chú

            # Tính toán giá trị cuối cùng và gộp ghi chú
            for ma_hang, values in grouped_data.items():
                # Tính giá trị cuối cùng
                sl_hang = values[4]
                don_gia = values[5]
                gia_tri = sl_hang * don_gia
                values[6] = gia_tri
                
                # Gộp tất cả ghi chú thành một chuỗi, cách nhau bởi "; "    
                values[7] = "; ".join(values[7])

            # Xóa dữ liệu cũ trong Treeview
            for item in my_treeview.get_children():
                my_treeview.delete(item)

            # Cập nhật dữ liệu mới vào Treeview
            for i, (key, values) in enumerate(grouped_data.items(), start=1):
                # Cập nhật lại số thứ tự
                values[0] = i  
                
                # Định dạng số lượng SL thực nhập
                if values[4].is_integer():  # Kiểm tra xem có phải là số nguyên không
                    formatted_quantity = f"{int(values[4]):,}"  # Định dạng số nguyên với dấu phân cách nghìn
                else:
                    formatted_quantity = f"{values[4]:,.2f}"  # Định dạng số thập phân với 2 chữ số sau dấu phẩy

                # Cập nhật lại giá trị số lượng đã được định dạng vào Treeview
                values[4] = formatted_quantity
                
                # Định dạng đơn giá
                if values[5].is_integer():  # Kiểm tra xem có phải là số nguyên không
                    formatted_quantity = f"{int(values[5]):,}"  # Định dạng số nguyên với dấu phân cách nghìn
                else:
                    formatted_quantity = f"{values[5]:,.2f}"  # Định dạng số thập phân với 2 chữ số sau dấu phẩy

                # Cập nhật lại giá trị số lượng đã được định dạng vào Treeview
                values[5] = formatted_quantity
                
                # Định dạng giá trị
                if values[6].is_integer():  # Kiểm tra xem có phải là số nguyên không
                    formatted_quantity = f"{int(values[6]):,}"  # Định dạng số nguyên với dấu phân cách nghìn
                else:
                    formatted_quantity = f"{values[6]:,.2f}"  # Định dạng số thập phân với 2 chữ số sau dấu phẩy

                # Cập nhật lại giá trị số lượng đã được định dạng vào Treeview
                values[6] = formatted_quantity
                
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
                                don_gia_value,
                                gia_tri_value,
                                ghi_chu_mat_hang, 
                                my_treeview):
        try:
            # Validate input using the helper function
            flag = Controller_add_row_to_treeview.f_check_input_of_treeview(entry_notification, 
                                                                           id_value, 
                                                                           ma_hang, 
                                                                           ten_hang,
                                                                           sl_thuc_nhap,
                                                                           don_gia_value)
            if flag == False:
                return False
            
            # Add row to the treeview
            my_treeview.insert("", "end", values=(id_value, 
                                                  ma_hang, 
                                                  ten_hang, 
                                                  dvt, 
                                                  sl_thuc_nhap, 
                                                  don_gia_value, 
                                                  gia_tri_value, 
                                                  ghi_chu_mat_hang))
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

    def f_check_input_of_treeview(entry_notification, id_value, ma_hang, ten_hang, sl_thuc_nhap, don_gia_value):    
        try:
            # Kiểm tra các trường bắt buộc
            if not id_value or not ma_hang or not ten_hang:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "All fields are required: mã hàng, tên hàng", "red")
                return False
            
            # Kiểm tra id_value có phải số nguyên hay không
            if not id_value.isdigit():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"ID value '{id_value}' must be an integer!", "red")
                return False
            
            # sl_thuc_nhap
            # Kiểm tra có phải số hay không
            try:
                sl_thuc_nhap_value = float(sl_thuc_nhap.replace(',', '') or 0)
            except ValueError:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Số lượng nhập/xuất '{sl_thuc_nhap}' phải là số.", "red")
                return False
            
            # Kiểm tra sl_thuc_nhap khác 0
            if sl_thuc_nhap_value == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng nhập/xuất không được bằng 0.", "red")
                return False
            
            # Kiểm tra số lượng không âm
            if sl_thuc_nhap_value < 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số lượng nhập/xuất không được âm.", "red")
                return False
            
            # don_gia_value
            # Kiểm tra có phải số hay không
            try:
                don_gia_value = float(don_gia_value.replace(',', '') or 0)
            except ValueError:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, f"Đơn giá '{don_gia_value}' phải là số.", "red")
                return False
            
            # Kiểm tra khác 0
            if don_gia_value == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Đơn giá không được bằng 0.", "red")
                return False
            
            # Kiểm tra số lượng không âm
            if don_gia_value < 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Đơn giá không được âm.", "red")
                return False
            
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
class Controller_click_on_treeview:
    def treeview_double_click(my_treeview):
        result_value = utils_controller_TreeviewHandler_click_250217_22h34.treeview_double_click(my_treeview, column_return=1)
        if result_value:
            return result_value
    
    def treeview_single_click(my_treeview,
        entry_id,
        entry_ma_hang,
        entry_ten_hang,
        entry_dvt,
        entry_sl_thuc_nhap,
        entry_don_gia,
        entry_ghi_chu_mat_hang):
        
        result_tuple = utils_controller_TreeviewHandler_click_250217_22h34.treeview_single_click(my_treeview)
        # print("result_tuple:", result_tuple)
        if not result_tuple:
            return
        id_value, ma_hang, ten_hang, dvt, sl_thuc_nhap, don_gia, gia_tri, ghi_chu_mat_hang = result_tuple
        
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
                
        if don_gia is not None:
            # Loại bỏ dấu phân cách nghìn nếu có
            sl_clean = don_gia.replace(',', '')  # Xóa dấu phân cách nghìn
            
            # Thực hiện chuyển đổi thành float
            try:
                float_value = float(sl_clean)
                
                entry_don_gia.delete(0, tk.END)
                
                if float_value.is_integer():  # Nếu là số nguyên
                    formatted_value = f"{int(float_value):,}"
                else:  # Nếu là số thập phân
                    formatted_value = f"{float_value:,.2f}"
                    
                entry_don_gia.insert(0, formatted_value)
            except ValueError:
                # Nếu không thể chuyển thành float, có thể hiển thị thông báo lỗi hoặc xử lý trường hợp này
                print("Error: Không thể chuyển đổi giá trị thành số.")
            
        if ghi_chu_mat_hang is not None:
            entry_ghi_chu_mat_hang.delete(0, tk.END)
            entry_ghi_chu_mat_hang.insert(0, ghi_chu_mat_hang)

class Controller_update_selected_row:
    def start_process_update_selected_row(entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang):
        try:
            flag = Controller_update_selected_row.update_selected_row(
            entry_notification,
            my_treeview,
            entry_ma_hang,
            entry_ten_hang,
            entry_dvt,
            entry_sl_thuc_nhap,
            entry_don_gia,
            entry_ghi_chu_mat_hang)
            if flag == False:
                return False
                
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Row updated successfully!", "blue")
                return True
    
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

    def update_selected_row(entry_notification,
                my_treeview,
                entry_ma_hang,
                entry_ten_hang,
                entry_dvt,
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang):
        try:
            flag = Controller_update_selected_row.validate_data_before_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang,
                entry_ten_hang,
                entry_sl_thuc_nhap,
                entry_don_gia)
            if flag == False:
                return False
            
            flag = Controller_update_selected_row.begin_updating_row_in_tree_view(
                entry_notification,
                my_treeview,
                entry_ma_hang,
                entry_ten_hang,
                entry_dvt,
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang)
            if flag == False:
                return False
            
            flag = Controller_add_row_to_treeview.Kiem_tra_lai_data_trong_treeview(entry_notification, my_treeview)
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
                entry_ma_hang,
                entry_ten_hang,
                entry_sl_thuc_nhap,
                entry_don_gia):
        # Function to update the selected row
        try:
            selected_item = my_treeview.selection()
            new_ma_hang = entry_ma_hang.get()
            new_ten_hang = entry_ten_hang.get()
            new_thuc_nhap = float(entry_sl_thuc_nhap.get().replace(',', '') or 0)
            new_don_gia = float(entry_don_gia.get().replace(',', '') or 0)
            
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
            
            if not str(new_don_gia).strip():
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Đơn giá không được để trống.", "red")
                return False
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def begin_updating_row_in_tree_view(entry_notification,
                my_treeview,
                entry_ma_hang,
                entry_ten_hang,
                entry_dvt,
                entry_sl_thuc_nhap,
                entry_don_gia,
                entry_ghi_chu_mat_hang):
        # Function to update the selected row
        try:
            selected_item = my_treeview.selection()
            value_col_00 = my_treeview.item(selected_item, "values")[0] if my_treeview.item(selected_item, "values") else None
            value_col_01 = entry_ma_hang.get()
            value_col_02 = entry_ten_hang.get()
            value_col_03 = entry_dvt.get()
            value_col_04 = float(entry_sl_thuc_nhap.get().replace(',', '') or 0)
            value_col_05 = float(entry_don_gia.get().replace(',', '') or 0)
            value_col_06 = value_col_04 * value_col_05
            value_col_07 = entry_ghi_chu_mat_hang.get()
            
            value_to_update = (value_col_00, value_col_01, value_col_02, value_col_03, value_col_04, value_col_05, value_col_06, value_col_07)
            
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
     
class Controller_save_slip:
    def start_process_save_slip(entry_notification,
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
        try:            
            # call controller to handle event
            flag = Controller_event_btn_save_click.f_handle_event_tab_02_btn_save_click(
                entry_notification,
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
            if flag == False:
                return False
            
            if flag == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Data saved successfully!", "blue")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_event_btn_save_click:
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
        try:
            flag = Controller_validate_data_on_GUI.validate_number_of_slip( 
                entry_notification,
                entry_so_phieu
            )
            if flag == False:
                return False
            
            flag = Controller_validate_data_on_GUI.validate_data_when_saving(
                entry_notification,
                entry_ma_kh,
                tree,
                column_index=1
            )
            if flag == False:
                return False
            
            # Controller_action_after_event.f_save_data_to_sql(
            Controller_save_data_on_GUI_into_database.f_save_data_on_GUI_to_database(
                entry_so_phieu, 
                entry_ma_kh, 
                entry_ten_kh,
                entry_mst,
                entry_dia_chi,
                entry_so_de_nghi,
                entry_ngay_de_nghi,
                entry_ghi_chu_cua_phieu,
                combobox_ma_kho,
                tree
                )
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_validate_data_on_GUI:
    def validate_data_when_saving(entry_notification, entry_ma_khach_hang, my_treeview, column_index):
        
        flag = Controller_validate_data_on_GUI.validate_data_orther_information(entry_notification, entry_ma_khach_hang, my_treeview)
        if flag == False:
            return False
        
        flag = Controller_validate_data_on_GUI.validate_danh_sach_ma_hang(entry_notification, my_treeview, column_index)
        if flag == False:
            return False
        
        return True
    
    def validate_number_of_slip(entry_notification, entry_so_phieu):
        try:
            # Check duplicate slip number
            if Controller_check_duplicate_and_auto_update_slip_number.f_Check_duplicate_and_update_slip_number(entry_so_phieu) == True:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Số phiếu bị trùng, vui lòng thử lại!", "red")
                return False
            
            # pass the validation
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def validate_danh_sach_ma_hang(entry_notification, my_treeview, column_index):
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_CATEGORIES()
        column_name = controller_handle_events.controller_get_information_of_module.load_column_name_ma_hang()
        value_to_check = utils_controller_check_exist.get_unique_column_values(my_treeview, column_index)
        
        try:
            flag, notification_text = utils_controller_check_exist.check_exist_values(value_to_check, database_name, table_name, column_name)
            if flag == False:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã hàng chưa tồn tại!", "red")
                return False
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
        
    def validate_data_orther_information(entry_notification, entry_ma_khach_hang, my_treeview):
        try:
            # Check if the client id is empty
            if entry_ma_khach_hang.get() == "" or entry_ma_khach_hang.get() == "search here":
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã đối tượng không được để trống!", "red")
                return False
            
            if len(my_treeview.get_children()) == 0:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Bảng không có dữ liệu", "red")
                return False
            
            # Check exist client id
            if Controller_validate_data_on_GUI.f_Check_exist_ma_doi_tuong(entry_ma_khach_hang) == False:
                utils_controller_config_notification_250220_10h05.f_config_notification(entry_notification, "Mã đối tượng chưa tồn tại!", "red")
                return False
            
            # pass the validation
            return True
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
    def f_Check_exist_ma_doi_tuong(entry_ma_khach_hang):
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_AD00_DANH_SACH_KHACH_HANG()
        column_name = controller_handle_events.controller_get_information_of_module.load_column_name_ma_khach_hang()
        value_to_check = entry_ma_khach_hang.get().strip()

        try:
            flag, notification_text = utils_controller_check_exist.check_exist_values(value_to_check, database_name, table_name, column_name)
            if flag == False:
                return False
            return True
        
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False
    
class Controller_check_duplicate_and_auto_update_slip_number:
    def f_Check_duplicate_and_update_slip_number(entry_so_phieu):
        database_name = utils_controller_get_information_of_database.load_database_name()
        table_name = utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05()
        column_name = controller_handle_events.controller_get_information_of_module.load_column_name_so_phieu()
        try:
            kiem_tra_trung_so_phieu = f_utils_check_duplicate(entry_so_phieu, database_name, table_name, column_name)
            if kiem_tra_trung_so_phieu == False:    # có trùng phiếu
                result = f_utils_ask_yes_no("Thông báo", "Số phiếu đã tồn tại, bạn có muốn tự động lấy số phiếu mới không?")
                # Kiểm tra kết quả
                if result:
                    # Nếu người dùng chọn Yes
                    controller_handle_events.Controller_handel_all_events.f_handle_event_get_the_latest_number_of_slip_PXK(entry_so_phieu)
                    return True
                else:
                    # Nếu người dùng chọn No
                    return False
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            return False

class Controller_save_data_on_GUI_into_database:
    def get_data_from_GUI_tab_02(entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree):
        
        # Các giá trị mặc định
        ID_nhan_vien = utils_controller_get_information_of_database.load_id_nhan_vien()
        Xoa_Sua = utils_controller_get_information_of_database.load_xoa_sua_mac_dinh()
        
        value_ma_khach_hang = "" if entry_ma_kh.get() == "search here" else entry_ma_kh.get()
        value_so_de_nghi = "" if entry_so_de_nghi.get() == "search here" else entry_so_de_nghi.get()
        
        value_so_phieu = entry_so_phieu.get()
        value_MA_KHO = combobox_ma_kho.get()
        if "PNK" in value_so_phieu:
            value_phan_loai_import_export = "IMPORT"
            value_ma_kho_nhan = value_MA_KHO
            value_ma_kho_xuat = ""
        elif "PXK" in value_so_phieu:
            value_phan_loai_import_export = "EXPORT"
            value_ma_kho_nhan = ""
            value_ma_kho_xuat = value_MA_KHO
        else:
            return False, []
        
        # Tạo một list chứa dữ liệu để export
        try:
            data = []
            for child in tree.get_children():
                row = tree.item(child, "values")
                data.append((
                    ID_nhan_vien
                    ,Xoa_Sua
                    ,value_so_phieu
                    ,value_phan_loai_import_export
                    ,value_ma_khach_hang
                    ,f_utils_get_formatted_today_YYYY_MM_DD()
                    ,value_so_de_nghi
                    ,entry_ghi_chu_cua_phieu.get()
                    ,int(row[0])
                    ,row[1]
                    ,row[2]
                    ,row[3]
                    ,float(row[4].replace(",", ""))
                    ,float(row[5].replace(",", ""))
                    ,float(row[6].replace(",", ""))
                    ,row[7]
                    ,value_ma_kho_nhan
                    ,value_ma_kho_xuat
                ))
            # print(data)
            return True, data
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
            data = []
            return False, data
    
    def f_save_data_on_GUI_to_database(entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_de_nghi,
            entry_ngay_de_nghi,
            entry_ghi_chu_cua_phieu,
            combobox_ma_kho,
            tree):
        
        # Step_01: Get data
        flag, data_array = Controller_save_data_on_GUI_into_database.get_data_from_GUI_tab_02(entry_so_phieu, 
                                                                    entry_ma_kh, 
                                                                    entry_ten_kh,
                                                                    entry_mst,
                                                                    entry_dia_chi,
                                                                    entry_so_de_nghi,
                                                                    entry_ngay_de_nghi,
                                                                    entry_ghi_chu_cua_phieu,
                                                                    combobox_ma_kho,
                                                                    tree
                                                                    )
        if flag == False:
            return
        
        # Step_02: Export data to SQL
        if utils_model_SQL_server.f_validate_data_format_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05(data_array):
            # If data is valid
            table_name = utils_controllers.utils_controller_get_information_of_database.load_table_name_TB_INVENTORY_STOCK_RECEIVED_ISSSUED_RETURNED_250214_09h05()
            utils_model_SQL_server.f_goi_ham_Export_to_table(data_array, table_name)
            return
        else:
            return

        
