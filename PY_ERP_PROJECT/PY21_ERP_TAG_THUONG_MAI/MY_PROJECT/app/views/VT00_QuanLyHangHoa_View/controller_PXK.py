from tkinter import messagebox
from app.utils import *
from datetime import datetime
from collections import defaultdict
from . import controller_handle_events
from . import controller_PNK

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
            
            flag = controller_PNK.Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
            if flag == False:
                return False
            
            flag = Controller_add_row_to_treeview.clear_input_fields(entry_ghi_chu_mat_hang)
            if flag == False:
                return False
            
            return True
        except Exception as e:
            # Correct entry ID because adding fail
            controller_PNK.Controller_update_entry_id.update_entry_id_after_adding_new_row(my_treeview, entry_id)
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
        
