import time
from test_Model import cls_test_Model
from test_Model import cls_test_Model_02
from test_Model import cls_test_Model_06_staticmenthod_get_config_of_table_YCDH_log_from_json
from test_Model import SQLModel
from test_Model import Model_get_data_from_SQL
from Components_View import *   # Tại sao lại phải import Components_View
from utils import *
import traceback
from datetime import datetime

class cls_test_Controller():
    def __init__(self):
        # super().__init__()
        self.model = None
        self.f_add_MVC_class()
        
    def f_add_MVC_class(self):
        """Initialize and bind Model and View classes to the controller."""
        try:
            # Initialize Model
            self.model = cls_test_Model()  
            # If model or view need controller reference
            self.model.controller = self  # Avoid recursion by passing after initialization
        except Exception as e:
            print(f"Error initializing MVC components: {e}")
        
    def f_check_input(self, id_value, ma_hang, ten_hang, sl_giu_cho, sl_yeu_cau_dat_hang):    
        # Kiểm tra các trường bắt buộc
        if not id_value or not ma_hang or not ten_hang:
            return False, "All fields are required: mã hàng, tên hàng"
        
        # Kiểm tra id_value có phải số nguyên hay không
        if not id_value.isdigit():
            return False, f"ID value '{id_value}' must be an integer!"
        
        # Kiểm tra sl_giu_cho và sl_yeu_cau_dat_hang có phải số hay không
        try:
            sl_giu_cho_value = float(sl_giu_cho)
            sl_yeu_cau_dat_hang_value = float(sl_yeu_cau_dat_hang)
        except ValueError:
            return False, f"Số lượng giữ chỗ '{sl_giu_cho}' và số lượng yêu cầu đặt hàng '{sl_yeu_cau_dat_hang}' phải là số."
        
        # Kiểm tra sl_giu_cho và sl_yeu_cau_dat_hang không đồng thời bằng không
        if sl_giu_cho_value == 0 and sl_yeu_cau_dat_hang_value == 0:
            return False, "Số lượng giữ chỗ và số lượng yêu cầu đặt hàng không được đồng thời bằng 0."
        
        # Kiểm tra số lượng giữ chỗ hoặc yêu cầu đặt hàng hợp lệ
        if sl_giu_cho_value < 0 or sl_yeu_cau_dat_hang_value < 0:
            return False, "Số lượng giữ chỗ và số lượng yêu cầu đặt hàng không được âm."
        
        return True, ""

    def f_get_data(self, table):
        """
        Retrieve all rows from the table and print them to the console.
        Args:
            table: The Treeview widget containing the data.
            result_label: The Label widget to display messages.
        """
        rows = []
        for child in table.get_children():
            rows.append(table.item(child)["values"])
        print("Current data array:", rows)
        return "Data printed to console!"
    
    def f_get_data_from_table(self, table):
        """
        Retrieve all rows from the table and print them to the console.
        Args:
            table: The Treeview widget containing the data.
            result_label: The Label widget to display messages.
        """
        rows = []
        for child in table.get_children():
            rows.append(table.item(child)["values"])
        print("Current data array:", rows)
        return rows
    
    # Function to add a row to the table
    def f_controller_add_row(self, id_value, ma_hang, ten_hang, dvt, sl_kha_dung, sl_nhu_cau, sl_giu_cho, sl_yeu_cau_dat_hang, ghi_chu_mat_hang, table):
        
        # Validate input using the helper function
        is_valid, error_message = self.f_check_input(id_value, ma_hang, ten_hang, sl_giu_cho, sl_yeu_cau_dat_hang)
        if not is_valid:
            return is_valid, error_message
        
        # Add row to the treeview
        table.insert("", "end", values=(id_value, ma_hang, ten_hang, dvt, sl_kha_dung, sl_nhu_cau, sl_giu_cho, sl_yeu_cau_dat_hang, ghi_chu_mat_hang))
        error_message ="Row added successfully!"
        
        return is_valid, error_message
    
    def f_get_table_config(self):
        return self.model.f_load_table_config_from_json()

    def f_get_table_config_name_only(self):
        return self.model.f_load_table_config_from_json_name_only()

    def f_get_scrollbar_config(self):
        return {
            "vertical": {"enabled": True, "command": "yscrollcommand"},
            "horizontal": {"enabled": True, "command": "xscrollcommand"},
        }

    def f_export_data_to_SQL(self, table):
        data_array = self.f_get_data_from_table(table)
        self.model.f_goi_ham_Export_to_SQL(data_array)
        return "Data exported to SQL Server!"
    
    def f_controller_handle_btn_save_02_click_(self, table):
        data_array = self.model.f_model_data_to_SQL_TB_KD02_YEU_CAU_DAT_HANG_ver_02_only_necessary_colmuns()
        self.f_controller_lay_list_ma_hang(data_array, 8)
        if self.model.f_validate_data_format(data_array):
            print("Data is valid. Ready for insertion.")
            database_name = "TEST_NE_TU_TD"
            table_name = "[TB_KD02_YEU_CAU_DAT_HANG]"
            self.model.f_goi_ham_Export_to_TB_KD02_YEU_CAU_DAT_HANG(data_array, database_name, table_name)
            return "Data exported to SQL Server KD02_YEU_CAU_DAT_HANG!"
        else:
            return "Data validation failed. Please fix the errors."
    
    def f_controller_handle_btn_print_00_click_(self):
        f_utils_create_print_template()

    def f_controller_handle_btn_print_02_click_(self):
        path_template_file = os.path.join(PATH_ASSETS_TEMPLATES_EXCEL, "PRINT_KD0201.xlsx")
        sheet_name = "KD0201_YEU_CAU_DAT_HANG"
        f_utils_open_print_template(path_template_file, sheet_name)
        
    def f_controller_get_all_info_of_slip(self):
        print("")
        
    def f_controller_lay_list_ma_hang(self, data, number_column):
        # print("danh sách mã hàng là:", self.model.f_model_get_unique_ma_hang(data, number_column))
        print("danh sách mã hàng là:", f_utils_get_unique_column_from_data(data, number_column))
        
    def f_handle_event_click_on_table_of_tab_01(self, last_click_time, current_time, double_click_interval):
        if current_time - last_click_time < double_click_interval:
            return True  # Double click detected
        else:
            return False  # Single click detected
    
    
    def f_tab_01_button_config_click(self, treeview_widget):
        var_01, var_02, var_03 = self.model.f_extract_from_json_columns_config()
        return var_01, var_02, var_03
        
    
    def f_tab_01_table_single_click(self, event):
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # print("Selected row values:", row_values)
            if len(row_values) >= 9:
                return row_values[0], row_values[1], row_values[2], row_values[3], row_values[4], row_values[5], row_values[6], row_values[7], row_values[8]
            else:
                return None, None, None, None, None, None, None, None, None
        else:
            # print("Warning: No row selected.")
            return None, None, None, None, None, None, None, None, None
    
    def f_tab_01_table_double_click(self, event):
        # Get the Treeview widget from the event
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # Print the first and third values, if they exist
            if len(row_values) >= 3:
                print("First value:", row_values[0])
                print("Third value:", row_values[2])
            else:
                print("Insufficient data in row!")
    
    def f_controller_show_get_items_of_combobox_01(self):
        # Fetch data from the model
        items_of_combobox_01 = self.model.f_model_get_items_to_combobox_01()
        return items_of_combobox_01
    
    def f_controller_get_row_count(self, treeview):
        # Get all child items (rows) and count them
        return len(treeview.get_children())    
    
    
    def clear_input_fields(entry_id, entry_ghi_chu_mat_hang, entry_sl_YCDH):
        entry_id.delete(0, tk.END)
        entry_ghi_chu_mat_hang.delete(0, tk.END)
        entry_sl_YCDH.delete(0, tk.END)


class cls_test_Controller_02_treeview():
    def __init__(self, tree, entry_ma_kh, entry_ten_kh, entry_so_phieu, entry_ghi_chu_phieu):
        self.tree = tree
        self.entry_ma_kh = entry_ma_kh
        self.entry_ten_kh = entry_ten_kh
        self.entry_so_phieu = entry_so_phieu
        self.entry_ghi_chu_phieu = entry_ghi_chu_phieu
        
        self.model = None
        self.f_add_MVC_class()
    
    def f_add_MVC_class(self):
        """Initialize and bind Model and View classes to the controller."""
        try:
            # Initialize Model
            self.model = cls_test_Model_02()  
            # If model or view need controller reference
            self.model.controller = self  # Avoid recursion by passing after initialization
        except Exception as e:
            print(f"Error initializing MVC components: {e}")
    
    def add_to_treeview(self):
        ma_kh = self.entry_ma_kh.get()
        ten_kh = self.entry_ten_kh.get()
        so_phieu = self.entry_so_phieu.get()
        ghi_chu_phieu = self.entry_ghi_chu_phieu.get()

        if ma_kh and ten_kh and so_phieu:
            self.tree.insert("", "end", values=(
                self.tree.get_children().__len__() + 1, ma_kh, ten_kh, so_phieu, ghi_chu_phieu
            ))
            self.clear_entries()

    # Method to clear entry fields
    def clear_entries(self):
        self.entry_ma_kh.delete(0, tk.END)
        self.entry_ten_kh.delete(0, tk.END)
        self.entry_so_phieu.delete(0, tk.END)
        self.entry_ghi_chu_phieu.delete(0, tk.END)
    
    def f_controller_handle_btn_save_03_click_(self, table):
        # Step_01: Get data
        notification_text, data_array = self.print_data()
        # Step_02: validate data
        f_utils_get_unique_column_from_data(data_array, 8)
        # Step_03: Export data to SQL
        if self.model.f_validate_data_format(data_array):
            print("Data is valid. Ready for insertion.")
            database_name = "TBD_2024"
            table_name = "[TB_KD02_YEU_CAU_DAT_HANG]"
            self.model.f_goi_ham_Export_to_TB_KD02_YEU_CAU_DAT_HANG(data_array, database_name, table_name)
            return "Data exported to SQL Server KD02_YEU_CAU_DAT_HANG!"
        else:
            return "Data validation failed. Please fix the errors."

    # Function to update the selected row
    def validate_data_before_updating_row_in_tree_view(self, tree, *args):
        selected_item = tree.selection()  # Get the selected item
        if not selected_item:
            error_message = "No item selected to update."
            fg="red"
            return False, error_message, fg

        # Lấy các giá trị theo thứ tự truyền vào
        stt, new_ma_hang, new_ten_hang, new_dvt, new_sl_kha_dung, new_nhu_cau, new_sl_giu_cho, new_sl_YCDH, new_ghi_chu = args

        # Kiểm tra các giá trị bắt buộc không được rỗng
        if not new_ma_hang.strip():
            error_message = "Mã hàng không được để trống."
            fg="red"
            return False, error_message, fg

        if not new_ten_hang.strip():
            error_message = "Tên hàng không được để trống."
            fg="red"
            return False, error_message, fg
            
        if not str(new_nhu_cau).strip():  # Đảm bảo giá trị số không bị rỗng
            error_message = "Số lượng nhu cầu không được để trống."
            fg="red"
            return False, error_message, fg

    # Function to update the selected row
    def begin_updating_row_in_tree_view(self, tree, *args):
        selected_item = tree.selection()  # Get the selected item
        tree.item(selected_item, values=args)
        # notification
        success_message = "Update successfully!"
        fg="blue"
        return success_message, fg

    def update_selected_row(self, tree, *args):
        """
        Updates the selected row in the given treeview with the provided arguments.
        :param tree: The Treeview widget where the data is updated.
        :param args: Variable-length argument list for column values.
        """
        self.validate_data_before_updating_row_in_tree_view(tree, *args)
        self.begin_updating_row_in_tree_view(tree, *args)
    
    # Function to print data from the Treeview
    def print_data(self):
        try:
            data = []
            for child in self.tree.get_children():
                row = self.tree.item(child, "values")
                data.append((
                    "NV01"                          # [ID_NHAN_VIEN]
                    ,""                             # [XOA_SUA]
                    ,"2025-01-23"                   # [NGAY_TREN_PHIEU]
                    ,self.entry_so_phieu.get()      # [SO_PHIEU]
                    ,self.entry_ma_kh.get()
                    ,self.entry_ten_kh.get()
                    ,"MST"
                    ,"DIA_CHI"
                    ,"SO_HOP_DONG"
                    ,"THONG_TIN_HOP_DONG"
                    ,"GHI_CHU_CUA_PHIEU"
                    ,row[0]
                    ,row[1]
                    ,row[2]
                    ,row[3]
                    ,float(row[4])
                    ,float(row[5])
                    ,float(row[6])
                    ,float(row[7])
                    ,row[8]
                ))
            print(data)
            notification_text = "Data chuẩn bị để gửi đi đã được in!"
            return notification_text, data
        except Exception as e:
            error_details = traceback.format_exc()
            print("Chi tiết lỗi:")
            print(error_details)
            notification_text = f"Data validation failed. Error details:\n{error_details}"
            data = []
            return notification_text, data
        
        # Function to delete the selected row
    def f_controller_02_delete_selected(self, tree):
        selected_item = tree.selection()  # Get selected item
        if selected_item:  # Check if an item is selected
            tree.delete(selected_item)  # Delete the selected item
        else:  # If no item is selected
            children = tree.get_children()
            if children:  # Check if there are rows in the Treeview
                last_item = children[-1]  # Get the last item
                tree.delete(last_item)  # Delete the last item
        self.f_controller_02_renumber_rows(tree)

    # Function to re-number the rows
    def f_controller_02_renumber_rows(self, tree):
        for index, item in enumerate(tree.get_children(), start=1):
            values = tree.item(item, "values")  # Get the current values of the row
            new_values = (index,) + values[1:]  # Update the first column with the new number
            tree.item(item, values=new_values)  # Set the updated values
        
class cls_test_Controller_03_auto_update_number():
    def __init__(self, entry_sl_kha_dung, entry_sl_nhu_cau, entry_sl_giu_cho, entry_sl_yeu_cau_dat_hang):
        self.entry_sl_kha_dung = entry_sl_kha_dung
        self.entry_sl_nhu_cau = entry_sl_nhu_cau
        self.entry_sl_giu_cho = entry_sl_giu_cho
        self.entry_sl_yeu_cau_dat_hang = entry_sl_yeu_cau_dat_hang
        
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
    
class cls_test_Controller_05_staticmenthod:
    @staticmethod
    def clear_input_fields(entry_ghi_chu_mat_hang, entry_sl_nhu_cau, entry_sl_giu_cho, entry_sl_YCDH):
        
        entry_ghi_chu_mat_hang.delete(0, tk.END)
        entry_sl_nhu_cau.delete(0, tk.END)

        entry_sl_giu_cho.config(state='normal')
        entry_sl_giu_cho.delete(0, tk.END)
        entry_sl_giu_cho.config(state='disabled')

        entry_sl_YCDH.config(state='normal')
        entry_sl_YCDH.delete(0, tk.END)
        entry_sl_YCDH.config(state='disabled')

    @staticmethod
    def update_entry_id_after_adding_new_row(tree, entry_id):
        row_count = 1 + len(tree.get_children())    
        entry_id.config(state="normal")  # Enable the Entry widget to update the value
        entry_id.delete(0, tk.END)  # Clear the existing value
        entry_id.insert(0, row_count)  # Insert the new value (ID)
        entry_id.config(state="disabled")  # Disable the Entry widget again
        
class cls_test_Controller_06_treeview_tab_02():
    def __init__(self):
        # super().__init__()
        self.model = None
        self.f_add_MVC_class()
        
    def f_add_MVC_class(self):
        """Initialize and bind Model and View classes to the controller."""
        try:
            # Initialize Model
            self.model = cls_test_Model_06_staticmenthod_get_config_of_table_YCDH_log_from_json()  
            # If model or view need controller reference
            self.model.controller = self  # Avoid recursion by passing after initialization
        except Exception as e:
            print(f"Error initializing MVC components: {e}")
    
    def f_get_table_config(self):
        return self.model.f_load_table_config_from_json()

    def f_get_table_config_name_only(self):
        return self.model.f_load_table_config_from_json_name_only()

    def f_tab_01_button_config_click(self, treeview_widget):
        var_01, var_02, var_03 = self.model.f_extract_from_json_columns_config()
        return var_01, var_02, var_03
    
    def f_tab_01_table_single_click(self, event):
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # print("Selected row values:", row_values)
            if len(row_values) >= 9:
                return row_values[0], row_values[1], row_values[2], row_values[3], row_values[4], row_values[5], row_values[6], row_values[7], row_values[8]
            else:
                return None, None, None, None, None, None, None, None, None
        else:
            # print("Warning: No row selected.")
            return None, None, None, None, None, None, None, None, None
    
    def f_tab_01_table_double_click(self, event):
        # Get the Treeview widget from the event
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # Print the first and third values, if they exist
            if len(row_values) >= 3:
                print("First value:", row_values[0])
                print("Third value:", row_values[2])
            else:
                print("Insufficient data in row!")
                

class Controller_delete_row_in_SQL:
    def update_deleted(so_phieu):
        # Create query
        database_name = f_utils_get_DB_NAME()
        query = f"EXEC [{database_name}].[dbo].[Proc_TB_KD02_YEU_CAU_DAT_HANG_UPDATE_DELETED_250208_23h29] '{so_phieu}'"
        # Sent SQL query
        SQLModel.sent_SQL_query(query)

    @staticmethod
    def handle_event_btn_delete_click(tree):
        # Get the selected items
        selected_items = tree.selection()
        
        # Check if more than one row is selected
        if len(selected_items) > 1:
            return f"Selection Error", "Please select only one row."
        
        # Check if no row is selected
        if not selected_items:
            return f"Selection Error", "No row selected."
            
        # Get the selected row
        for item in selected_items:
            row_values = tree.item(item, 'values')
            if len(row_values) > 1:  # Ensure the row has at least 2 columns
                so_phieu = row_values[1]
                Controller_delete_row_in_SQL.update_deleted(so_phieu)
                return f"{so_phieu}, Slip deleted."


        
class SQLController:
    
    @staticmethod
    def load_data(tree):
        query = f"[Proc_TB_KD02_YEU_CAU_DAT_HANG_FILTER_BY_MANY_ARGUMENTS_250204_110h38]'','',''"
        data = SQLModel.fetch_data(query)
        # update_treeview_test_of_tag_02(data)
        
        # tree = self.treeview_test_of_tag_02
        for item in tree.get_children():
            tree.delete(item)
        for row in data:
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4],
                                           row[5], row[6], row[7], row[8], row[9],
                                           row[10], row[11], row[12], row[13], row[14]))
        
    # Function to print data from the Treeview
    @staticmethod
    def get_data_to_import_to_SQL(*args):
        (
            ID_nhan_vien,
            Xoa_Sua,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            entry_ma_hang,
            entry_ten_hang,
            tree
        ) = args
        
        # # print tên hàm và hàm cha
        # print("Tên hàm đang chạy là:", f_utils_get_current_function_name())
        # print("Hàm cha gọi nó là:", f_utils_get_caller_function_name())
        
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
                    ,entry_ma_kh.get()
                    ,entry_ten_kh.get()
                    ,entry_mst.get()
                    ,entry_dia_chi.get()
                    ,entry_so_hop_dong.get()
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
                    ,row[8]
                ))
            notification_text = "Data exported"
            return notification_text, data
        except Exception as e:
            error_details = traceback.format_exc()
            print("Chi tiết lỗi:")
            print(error_details)
            notification_text = f"Data validation failed. Error details:\n{error_details}"
            data = []
            return notification_text, data
    
    @staticmethod
    def f_controller_handle_btn_save_03_click_(*args):
        (
            ID_nhan_vien,
            Xoa_Sua,
            entry_so_phieu, 
            entry_ma_kh, 
            entry_ten_kh,
            entry_mst,
            entry_dia_chi,
            entry_so_hop_dong,
            entry_thong_tin_hop_dong,
            entry_ghi_chu_cua_phieu,
            entry_ma_hang,
            entry_ten_hang,
            tree
        ) = args
        # Step_01: Get data
        notification_text, data_array = SQLController.get_data_to_import_to_SQL(ID_nhan_vien,
                                                                                Xoa_Sua,
                                                                                entry_so_phieu, 
                                                                                entry_ma_kh, 
                                                                                entry_ten_kh,
                                                                                entry_mst,
                                                                                entry_dia_chi,
                                                                                entry_so_hop_dong,
                                                                                entry_thong_tin_hop_dong,
                                                                                entry_ghi_chu_cua_phieu,
                                                                                entry_ma_hang,
                                                                                entry_ten_hang,
                                                                                tree
                                                                                )
        # Step_02: validate data
        f_utils_get_unique_column_from_data(data_array, 8)
        # Step_03: Export data to SQL
        if SQLModel.f_validate_data_format(data_array):
            # If data is valid
            database_name = "TBD_2024"
            table_name = "[TB_KD02_YEU_CAU_DAT_HANG]"
            SQLModel.f_goi_ham_Export_to_TB_KD02_YEU_CAU_DAT_HANG(data_array, database_name, table_name)
            return "Data exported"
        else:
            return notification_text

class Controller_SQL_to_excel:
    
    @staticmethod
    def export_log_to_excel(treeview):
        # lấy danh sách số phiếu từ treeview
        danh_sach_so_phieu = f_utils_get_unique_column_from_treeview(treeview, 1)
        # print("danh_sach_so_phieu", danh_sach_so_phieu)
        
        # Chuyển danh sách số phiếu thành chuỗi SQL, đảm bảo các giá trị dạng chuỗi được bao trong dấu nháy đơn
        so_phieu_str = ', '.join([f"'{str(x)}'" for x in danh_sach_so_phieu])
        # print("so_phieu_str", so_phieu_str)
        
        # Tạo câu query SQL với danh sách số phiếu
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
        FROM [TBD_2024].[dbo].[TB_KD02_YEU_CAU_DAT_HANG]
        WHERE [SO_PHIEU] IN ({so_phieu_str})
        """
        # print("query", query)
        
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
        
        # Truyền câu query vào model để lấy dữ liệu từ SQL (Giả sử hàm này trả về DataFrame)
        df = Model_get_data_from_SQL.get_data_with_query(query)
        
        # Kiểm tra nếu có dữ liệu trả về
        if isinstance(df, list) and df:
            f_utils_export_data_to_excel(header, df)
            print(f"Data exported successfully")
        else:
            print("No data found for the selected SO_PHIEU.")
        

class Controller_get_the_latest_number_of_slip:
    
    @staticmethod
    def get_list_number_of_slip(database_name, table_name):
        
        # Tạo câu query SQL với danh sách số phiếu
        query = f"""
        SELECT DISTINCT
            [SO_PHIEU]
        FROM [{database_name}].[dbo].[{table_name}]
        WHERE [XOA_SUA] = ''
        """
        # print("query", query)
        
        # lấy danh sách số phiếu từ SQL
        danh_sach_so_phieu = Model_get_data_from_SQL.get_data_with_query(query)
        # print("danh_sach_so_phieu", danh_sach_so_phieu)
        
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
        
    @staticmethod
    def handle_button_get_number_of_slip_click():
        database_name, table_name = "TBD_2024", "TB_KD02_YEU_CAU_DAT_HANG"
        # Lấy danh sách số phiếu từ SQL
        data_01 = Controller_get_the_latest_number_of_slip.get_list_number_of_slip(database_name, table_name)
        # Lấy số phiếu cuối cùng
        data_02 = Controller_get_the_latest_number_of_slip.extract_numbers_from_data_SQL_num_01(data_01)
        # print("data", data_02)
        
        return data_02