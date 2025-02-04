import os
import json
import pyodbc
from datetime import datetime
from Components_View import *
from utils import *

class cls_test_Model():
    def __init__(self):
        # super().__init__()
        self.f_define_table_configurations_json_file()
    
    def f_define_table_configurations_json_file(self):
        # Define the path to the JSON file
        self.json_file = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'TEST_VIEW_01', 'test_table_input.JSON')
        
    def f_load_table_config_from_json(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.data_to_config_table = json.load(file)  # Load the JSON data
            column_names = self.f_extract_from_json_column_names(self.data_to_config_table)
            column_width = self.f_extract_from_json_column_width(self.data_to_config_table)
            column_min_width = self.f_extract_from_json_column_min_width(self.data_to_config_table)
            column_anchor = self.f_extract_from_json_column_anchor(self.data_to_config_table)
            column_stretch = self.f_extract_from_json_column_stretch(self.data_to_config_table)
            
            # print("Extracted column names:", column_names)
            # print("Extracted column width:", column_width)
            return column_names, column_width, column_min_width, column_anchor, column_stretch

        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_load_table_config_from_json_name_only(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.data_to_config_table = json.load(file)  # Load the JSON data
            column_names = self.f_extract_from_json_column_names(self.data_to_config_table)
            return column_names

        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_extract_from_json_columns_config(self):
        # Extract column configurations from the JSON
        columns_config = self.data_to_config_table["table"]["columns"]
        column_names = [col["name"] for col in columns_config]
        header_font_config = self.data_to_config_table["table"]["headings"]
        header_font_tuple = (header_font_config['family'], header_font_config['size'], header_font_config['weight'])
        return columns_config, column_names, header_font_tuple
    
    def f_extract_from_json_column_names(self, data):
        try:
            if "columns" in data["table"]:
                columns_names = data["table"]["columns"]
                column_names = [column.get("name", "Unknown") for column in columns_names]
                return column_names
            else:
                print("Warning: 'columns names' key not found in JSON.")
                return []
        except KeyError:
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_width(self, data):
        try:
            if "columns" in data["table"]:
                columns_width = data["table"]["columns"]
                column_width = [column.get("width", 100) for column in columns_width]  # Default width is 100
                return column_width
            else:
                print("Warning: 'columns width' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_min_width(self, data):
        try:
            if "columns" in data["table"]:
                columns_min_width = data["table"]["columns"]
                column_min_width = [column.get("width", 50) for column in columns_min_width]  # Default min_width is 50
                return column_min_width
            else:
                print("Warning: 'columns min_width' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_anchor(self, data):
        try:
            if "columns" in data["table"]:
                columns_anchor = data["table"]["columns"]
                column_anchor = [column.get("anchor", "w") for column in columns_anchor]  # Default width is w
                return column_anchor
            else:
                print("Warning: 'columns anchor' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []

    def f_extract_from_json_column_stretch(self, data):
        try:
            if "columns" in data["table"]:
                columns_stretch = data["table"]["columns"]
                column_stretch = [column.get("stretch", "True") for column in columns_stretch]  # Default width is True
                return column_stretch
            else:
                print("Warning: 'columns stretch' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_font(self, data):
        try:
            if "columns" in data["table"]:
                columns_font = data["table"]["columns"]
                column_font = [column.get("font", {"family": "Arial", "size": 12, "weight": "normal"}) for column in columns_font]  # Default width is {"family": "Arial", "size": 12, "weight": "normal"}
                return column_font
            else:
                print("Warning: 'columns_font' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []

    # ============================================================================
    def f_insert_data_to_sql(self, server_name, database_name, login_name, login_pass, table_name, data_array):
        """
        Hàm kết nối SQL Server và chèn dữ liệu từ mảng vào bảng.
        
        :param server_name: Tên hoặc địa chỉ IP của máy chủ SQL Server.
        :param database_name: Tên cơ sở dữ liệu.
        :param login_name: Tên người dùng SQL Server.
        :param login_pass: Mật khẩu SQL Server.
        :param table_name: Tên bảng trong cơ sở dữ liệu.
        :param data_array: Mảng chứa dữ liệu cần chèn (list of lists).
        """
        # Kết nối đến SQL Server
        connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={login_name};PWD={login_pass}"
        try:
            conn = pyodbc.connect(connection_string)
            print("Kết nối thành công đến cơ sở dữ liệu.")
        except Exception as e:
            print("Lỗi khi kết nối:", e)
            return
        
        cursor = conn.cursor()
        
        # Lấy danh sách cột của bảng
        try:
            cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
            columns = [column[0] for column in cursor.description]  # Lấy tên cột
            print("Danh sách cột trong bảng:", columns)
        except Exception as e:
            print("Lỗi khi lấy thông tin bảng:", e)
            return

        # Kiểm tra số cột trong bảng khớp với số cột trong dữ liệu
        num_columns = len(columns)
        if not all(len(row) == num_columns for row in data_array):
            print("Dữ liệu không khớp số cột của bảng.")
            return

        # Chèn dữ liệu
        try:
            placeholders = ", ".join(["?" for _ in range(num_columns)])  # Tạo chuỗi placeholder "?, ?, ?"
            query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
            
            for row in data_array:
                cursor.execute(query, row)
            
            conn.commit()
            print("Dữ liệu đã được chèn thành công.")
        except Exception as e:
            print("Lỗi khi chèn dữ liệu:", e)
        finally:
            cursor.close()
            conn.close()
            print("Kết nối đã được đóng.")

    def f_02_insert_data_to_sql(self, server_name, database_name, login_name, login_pass, table_name, data_array):
        """
        Hàm kết nối SQL Server và chèn dữ liệu từ mảng vào bảng, bỏ qua các cột có giá trị mặc định (ID, NGAY_TAO_PHIEU).
        
        :param server_name: Tên hoặc địa chỉ IP của máy chủ SQL Server.
        :param database_name: Tên cơ sở dữ liệu.
        :param login_name: Tên người dùng SQL Server.
        :param login_pass: Mật khẩu SQL Server.
        :param table_name: Tên bảng trong cơ sở dữ liệu.
        :param data_array: Mảng chứa dữ liệu cần chèn (list of lists).
        """
        # Kết nối đến SQL Server
        connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={login_name};PWD={login_pass}"
        try:
            conn = pyodbc.connect(connection_string)
            print("Kết nối thành công đến cơ sở dữ liệu.")
        except Exception as e:
            print("Lỗi khi kết nối:", e)
            return

        cursor = conn.cursor()
        
        # Lấy danh sách cột của bảng
        try:
            cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
            columns = [column[0] for column in cursor.description]  # Lấy tên cột
            print("Danh sách cột trong bảng:", columns)
        except Exception as e:
            print("Lỗi khi lấy thông tin bảng:", e)
            return

        # Loại bỏ các cột có giá trị mặc định (ID, NGAY_TAO_PHIEU)
        columns_to_insert = [col for col in columns if col not in ['ID', 'NGAY_TAO_PHIEU']]
        print("Danh sách cột cần chèn:", columns_to_insert)
        
        # Kiểm tra số cột trong dữ liệu khớp với số cột cần chèn
        num_columns_to_insert = len(columns_to_insert)
        if not all(len(row) == num_columns_to_insert for row in data_array):
            print("Dữ liệu không khớp số cột cần chèn.")
            return

        # Chèn dữ liệu
        try:
            placeholders = ", ".join(["?" for _ in range(num_columns_to_insert)])  # Tạo chuỗi placeholder "?, ?, ?"
            query = f"INSERT INTO {table_name} ({', '.join(columns_to_insert)}) VALUES ({placeholders})"
            
            for row in data_array:
                cursor.execute(query, row)
            
            conn.commit()
            print("Dữ liệu đã được chèn thành công.")
        except Exception as e:
            print("Lỗi khi chèn dữ liệu:", e)
        finally:
            cursor.close()
            conn.close()
            print("Kết nối đã được đóng.")
        
    def f_goi_ham_Export_to_SQL(self, data_array):
        server_name = "14.225.192.238, 1433"  # Địa chỉ IP của SQL Server
        database_name = "TEST_NE_TU_TD"
        login_name = "sa"
        login_pass = "Ta#9999"
        table_name = "ID_INFO"

        print("Chuẩn bị chèn dữ liệu vào SQL Server...")
        print("Dữ liệu cần chèn:", data_array)
        # Dữ liệu cần chèn (mỗi danh sách bên trong là một dòng dữ liệu)
        # data_array = [
        #     ["1", "Alice", 25],
        #     ["2", "Bob", 30],
        #     ["3", "Charlie", 35]
        # ]
        
        # data_array = [
        #     ["1", "Alice nè", 25]
        # ]
        
        self.f_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        
    def f_goi_ham_Export_to_TB_KD02_YEU_CAU_DAT_HANG(self, data_array, database_name, table_name):
        server_name = "14.225.192.238, 1433"  # Địa chỉ IP của SQL Server
        database_name = database_name
        login_name = "sa"
        login_pass = "Ta#9999"
        table_name = table_name

        print("Chuẩn bị chèn dữ liệu vào SQL Server...")
        print("Dữ liệu cần chèn:", data_array)
        # self.f_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        self.f_02_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        
    def f_model_get_items_to_combobox_01(self):
        # Simulate fetching data (from a database or API, for example)
        return ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    
    def f_model_data_to_SQL_TB_KD02_YEU_CAU_DAT_HANG_ver_01_full_colmuns(self):
        # Define sample data
        sample_data = [
            (
            '9F2C1421-7B7F-4F8A-B12A-012F5D3D7C3C',
            '2025-01-09 00:00:00',
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            1,
            'MH001',
            'Sản phẩm A',
            'Cái',
            100.50,
            'Sản phẩm chất lượng cao.'
            ),
            (
            '9F2C1421-7B7F-4F8A-B12A-012F5D3D7C3C',
            '2025-01-09 00:00:00',
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            2,
            'MH001',
            'Sản phẩm B phức tạp',
            'Cái',
            100.50,
            'Loại có kính mica.'
            )
        ]
        return sample_data

    def f_model_data_to_SQL_TB_KD02_YEU_CAU_DAT_HANG_ver_02_only_necessary_colmuns(self):
        # Define sample data
        sample_data = [
            (
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            1,
            'MH001',
            'Sản phẩm A',
            'Cái',
            100.50,
            'Sản phẩm chất lượng cao.'
            ),
            (
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            2,
            'MH001',
            'Sản phẩm B phức tạp',
            'Cái',
            1100.50,
            'Loại có kính mica.'
            ),
            (
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            3,
            'MH003',
            'Sản phẩm B phức tạp',
            'Cái',
            1100.50,
            'Loại có kính mica.'
            ),
            (
            'NV001',
            '',
            'SP001',
            '2025-01-09',
            'KH001',
            'Nguyễn Văn A',
            'Khách hàng yêu cầu giao gấp.',
            4,
            'MH002',
            'Sản phẩm B phức tạp',
            'Cái',
            1100.50,
            'Loại có kính mica.'
            )
        ]
        return sample_data
    
    def f_validate_data_format(self, data_array):
        """
        Validate the format of data before inserting into SQL Server.
        :param data_array: List of tuples containing the data to validate.
        :return: True if all data is valid, otherwise False with error messages.
        """
        is_valid = True
        for idx, row in enumerate(data_array):
            try:
                # Validate each field
                if not isinstance(row[0], str) or len(row[0]) > 10:
                    raise ValueError(f"ID_NHAN_VIEN (Row {idx+1}, Value: {row[0]}) must be a string with a maximum length of 10.")
                if not isinstance(row[1], str):
                    raise ValueError(f"XOA_SUA (Row {idx+1}, Value: {row[1]}) must be a string.")
                if not isinstance(row[2], str) or len(row[2]) > 50:
                    raise ValueError(f"SO_PHIEU (Row {idx+1}, Value: {row[2]}) must be a string with a maximum length of 50.")
                try:
                    datetime.strptime(row[3], '%Y-%m-%d')
                except ValueError:
                    raise ValueError(f"NGAY_TREN_PHIEU (Row {idx+1}, Value: {row[3]}) must be a valid date in 'YYYY-MM-DD' format.")
                if not isinstance(row[4], str) or len(row[4]) > 50:
                    raise ValueError(f"MA_DOI_TUONG (Row {idx+1}, Value: {row[4]}) must be a string with a maximum length of 50.")
                if not isinstance(row[5], str):
                    raise ValueError(f"TEN_DOI_TUONG (Row {idx+1}, Value: {row[5]}) must be a string.")
                if not isinstance(row[6], str):
                    raise ValueError(f"GHI_CHU_PHIEU (Row {idx+1}, Value: {row[6]}) must be a string.")
                if not isinstance(row[7], int) or row[7] < 1:
                    raise ValueError(f"STT_DONG (Row {idx+1}, Value: {row[7]}) must be an integer greater than 0.")
                if not isinstance(row[8], str):
                    raise ValueError(f"MA_HANG (Row {idx+1}, Value: {row[8]}) must be a string.")
                if not isinstance(row[9], str):
                    raise ValueError(f"TEN_HANG (Row {idx+1}, Value: {row[9]}) must be a string.")
                if not isinstance(row[10], str):
                    raise ValueError(f"DVT (Row {idx+1}, Value: {row[10]}) must be a string.")
                if not isinstance(row[11], (int, float)) or row[11] <= 0:
                    raise ValueError(f"SO_LUONG (Row {idx+1}, Value: {row[11]}) must be a positive number.")
                if not isinstance(row[12], str):
                    raise ValueError(f"GHI_CHU_SP (Row {idx+1}, Value: {row[12]}) must be a string.")
            
            except ValueError as e:
                is_valid = False
                print(e)

        return is_valid

class cls_test_Model_02():
    def f_validate_data_format(self, data_array):
        """
        Validate the format of data before inserting into SQL Server.
        :param data_array: List of tuples containing the data to validate.
        :return: True if all data is valid, otherwise False with error messages.
        """
        is_valid = True
        # for idx, row in enumerate(data_array):
        #     try:
        #         # Validate each field
        #         if not isinstance(row[0], str) or len(row[0]) > 10:
        #             raise ValueError(f"ID_NHAN_VIEN (Row {idx+1}, Value: {row[0]}) must be a string with a maximum length of 10.")
        #         if not isinstance(row[1], str):
        #             raise ValueError(f"XOA_SUA (Row {idx+1}, Value: {row[1]}) must be a string.")
        #         if not isinstance(row[2], str) or len(row[2]) > 50:
        #             raise ValueError(f"SO_PHIEU (Row {idx+1}, Value: {row[2]}) must be a string with a maximum length of 50.")
        #         try:
        #             datetime.strptime(row[3], '%Y-%m-%d')
        #         except ValueError:
        #             raise ValueError(f"NGAY_TREN_PHIEU (Row {idx+1}, Value: {row[3]}) must be a valid date in 'YYYY-MM-DD' format.")
        #         if not isinstance(row[4], str) or len(row[4]) > 50:
        #             raise ValueError(f"MA_DOI_TUONG (Row {idx+1}, Value: {row[4]}) must be a string with a maximum length of 50.")
        #         if not isinstance(row[5], str):
        #             raise ValueError(f"TEN_DOI_TUONG (Row {idx+1}, Value: {row[5]}) must be a string.")
        #         if not isinstance(row[6], str):
        #             raise ValueError(f"GHI_CHU_PHIEU (Row {idx+1}, Value: {row[6]}) must be a string.")
        #         if not isinstance(row[7], int) or row[7] < 1:
        #             raise ValueError(f"STT_DONG (Row {idx+1}, Value: {row[7]}) must be an integer greater than 0.")
        #         if not isinstance(row[8], str):
        #             raise ValueError(f"MA_HANG (Row {idx+1}, Value: {row[8]}) must be a string.")
        #         if not isinstance(row[9], str):
        #             raise ValueError(f"TEN_HANG (Row {idx+1}, Value: {row[9]}) must be a string.")
        #         if not isinstance(row[10], str):
        #             raise ValueError(f"DVT (Row {idx+1}, Value: {row[10]}) must be a string.")
        #         if not isinstance(row[11], (int, float)) or row[11] <= 0:
        #             raise ValueError(f"SO_LUONG (Row {idx+1}, Value: {row[11]}) must be a positive number.")
        #         if not isinstance(row[12], str):
        #             raise ValueError(f"GHI_CHU_SP (Row {idx+1}, Value: {row[12]}) must be a string.")
            
        #     except ValueError as e:
        #         is_valid = False
        #         print(e)

        return is_valid
    
    def f_goi_ham_Export_to_TB_KD02_YEU_CAU_DAT_HANG(self, data_array, database_name, table_name):
        server_name = "14.225.192.238, 1433"  # Địa chỉ IP của SQL Server
        database_name = database_name
        login_name = "sa"
        login_pass = "Ta#9999"
        table_name = table_name

        print("Chuẩn bị chèn dữ liệu vào SQL Server...")
        print("Dữ liệu cần chèn:", data_array)
        # self.f_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        self.f_02_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        
    def f_02_insert_data_to_sql(self, server_name, database_name, login_name, login_pass, table_name, data_array):
        """
        Hàm kết nối SQL Server và chèn dữ liệu từ mảng vào bảng, bỏ qua các cột có giá trị mặc định (ID, NGAY_TAO_PHIEU).
        
        :param server_name: Tên hoặc địa chỉ IP của máy chủ SQL Server.
        :param database_name: Tên cơ sở dữ liệu.
        :param login_name: Tên người dùng SQL Server.
        :param login_pass: Mật khẩu SQL Server.
        :param table_name: Tên bảng trong cơ sở dữ liệu.
        :param data_array: Mảng chứa dữ liệu cần chèn (list of lists).
        """
        # Kết nối đến SQL Server
        connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={login_name};PWD={login_pass}"
        try:
            conn = pyodbc.connect(connection_string)
            print("Kết nối thành công đến cơ sở dữ liệu.")
        except Exception as e:
            print("Lỗi khi kết nối:", e)
            return

        cursor = conn.cursor()
        
        # Lấy danh sách cột của bảng
        try:
            cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
            columns = [column[0] for column in cursor.description]  # Lấy tên cột
            print("Danh sách cột trong bảng:", columns)
        except Exception as e:
            print("Lỗi khi lấy thông tin bảng:", e)
            return

        # Loại bỏ các cột có giá trị mặc định (ID, NGAY_TAO_PHIEU)
        columns_to_insert = [col for col in columns if col not in ['ID', 'DATE']]
        print("Danh sách cột cần chèn:", columns_to_insert)
        
        # Kiểm tra số cột trong dữ liệu khớp với số cột cần chèn
        num_columns_to_insert = len(columns_to_insert)
        if not all(len(row) == num_columns_to_insert for row in data_array):
            print("Dữ liệu không khớp số cột cần chèn.")
            return

        # Chèn dữ liệu
        try:
            placeholders = ", ".join(["?" for _ in range(num_columns_to_insert)])  # Tạo chuỗi placeholder "?, ?, ?"
            query = f"INSERT INTO {table_name} ({', '.join(columns_to_insert)}) VALUES ({placeholders})"
            
            for row in data_array:
                cursor.execute(query, row)
            
            conn.commit()
            print("Dữ liệu đã được chèn thành công.")
        except Exception as e:
            print("Lỗi khi chèn dữ liệu:", e)
        finally:
            cursor.close()
            conn.close()
            print("Kết nối đã được đóng.")

class cls_test_Model_05_staticmenthod_get_data_from_SQL:
    @staticmethod
    def get_data_from_SQL(server_name, database_name, login_name, login_pass, table_name, data_array):
        """
        Hàm kết nối SQL Server và lấy dữ liệu.
        
        :param server_name: Tên hoặc địa chỉ IP của máy chủ SQL Server.
        :param database_name: Tên cơ sở dữ liệu.
        :param login_name: Tên người dùng SQL Server.
        :param login_pass: Mật khẩu SQL Server.
        :param table_name: Tên bảng trong cơ sở dữ liệu.
        """
        # Kết nối đến SQL Server
        connection_string = f"DRIVER={{SQL Server}};SERVER={server_name};DATABASE={database_name};UID={login_name};PWD={login_pass}"
        try:
            conn = pyodbc.connect(connection_string)
            print("Kết nối thành công đến cơ sở dữ liệu.")
        except Exception as e:
            print("Lỗi khi kết nối:", e)
            return
        
        cursor = conn.cursor()
        
        # Lấy danh sách cột của bảng
        try:
            # cursor.execute(f"SELECT * FROM {table_name} WHERE 1=0")
            cursor.execute(f"SELECT * FROM [TBD_2024].[dbo].[TB_KD02_YEU_CAU_DAT_HANG]")
            
            columns = [column[0] for column in cursor.description]  # Lấy tên cột
            print("Danh sách cột trong bảng:", columns)
        except Exception as e:
            print("Lỗi khi lấy thông tin bảng:", e)
            return

        # Kiểm tra số cột trong bảng khớp với số cột trong dữ liệu
        num_columns = len(columns)
        if not all(len(row) == num_columns for row in data_array):
            print("Dữ liệu không khớp số cột của bảng.")
            return

        # Thêm dữ liệu vào bảng nhật ký
        try:
            # in dữ liệu vào bảng nhật ký
            print("Dữ liệu đã được chèn thành công.")
        except Exception as e:
            print("Lỗi khi chèn dữ liệu:", e)
        finally:
            cursor.close()
            conn.close()
            print("Kết nối đã được đóng.")

class cls_test_Model_06_staticmenthod_get_config_of_table_YCDH_log_from_json():
    def __init__(self):
        self.f_define_table_configurations_json_file()
    
    def f_define_table_configurations_json_file(self):
        # Define the path to the JSON file
        self.json_file = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'TEST_VIEW_01', 'test_table_log.JSON')
        # return table_config_json_path
    
    def f_load_table_config_from_json(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.data_to_config_table = json.load(file)  # Load the JSON data
            column_names = self.f_extract_from_json_column_names(self.data_to_config_table)
            column_width = self.f_extract_from_json_column_width(self.data_to_config_table)
            column_min_width = self.f_extract_from_json_column_min_width(self.data_to_config_table)
            column_anchor = self.f_extract_from_json_column_anchor(self.data_to_config_table)
            column_stretch = self.f_extract_from_json_column_stretch(self.data_to_config_table)
            
            # print("Extracted column names:", column_names)
            # print("Extracted column width:", column_width)
            return column_names, column_width, column_min_width, column_anchor, column_stretch

        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_load_table_config_from_json_name_only(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.data_to_config_table = json.load(file)  # Load the JSON data
            column_names = self.f_extract_from_json_column_names(self.data_to_config_table)
            return column_names

        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_extract_from_json_columns_config(self):
        # Extract column configurations from the JSON
        columns_config = self.data_to_config_table["table"]["columns"]
        column_names = [col["name"] for col in columns_config]
        header_font_config = self.data_to_config_table["table"]["headings"]
        header_font_tuple = (header_font_config['family'], header_font_config['size'], header_font_config['weight'])
        return columns_config, column_names, header_font_tuple
    
    def f_extract_from_json_column_names(self, data):
        try:
            if "columns" in data["table"]:
                columns_names = data["table"]["columns"]
                column_names = [column.get("name", "Unknown") for column in columns_names]
                return column_names
            else:
                print("Warning: 'columns names' key not found in JSON.")
                return []
        except KeyError:
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_width(self, data):
        try:
            if "columns" in data["table"]:
                columns_width = data["table"]["columns"]
                column_width = [column.get("width", 100) for column in columns_width]  # Default width is 100
                return column_width
            else:
                print("Warning: 'columns width' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_min_width(self, data):
        try:
            if "columns" in data["table"]:
                columns_min_width = data["table"]["columns"]
                column_min_width = [column.get("width", 50) for column in columns_min_width]  # Default min_width is 50
                return column_min_width
            else:
                print("Warning: 'columns min_width' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_anchor(self, data):
        try:
            if "columns" in data["table"]:
                columns_anchor = data["table"]["columns"]
                column_anchor = [column.get("anchor", "w") for column in columns_anchor]  # Default width is w
                return column_anchor
            else:
                print("Warning: 'columns anchor' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []

    def f_extract_from_json_column_stretch(self, data):
        try:
            if "columns" in data["table"]:
                columns_stretch = data["table"]["columns"]
                column_stretch = [column.get("stretch", "True") for column in columns_stretch]  # Default width is True
                return column_stretch
            else:
                print("Warning: 'columns stretch' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
    
    def f_extract_from_json_column_font(self, data):
        try:
            if "columns" in data["table"]:
                columns_font = data["table"]["columns"]
                column_font = [column.get("font", {"family": "Arial", "size": 12, "weight": "normal"}) for column in columns_font]  # Default width is {"family": "Arial", "size": 12, "weight": "normal"}
                return column_font
            else:
                print("Warning: 'columns_font' key not found in JSON.")
                return []
        except KeyError:    
            print("Error: Key 'table' is missing from JSON.")
            return []
        except TypeError:
            print("Error: Invalid data structure for 'columns'.")
            return []
        
class SQLModel:
    @staticmethod
    def fetch_data(server_name, database_name, login_name, login_pass, query):
        """
        Kết nối đến SQL Server và lấy dữ liệu từ bảng.
        """
        # connection_string = (
        #     f"DRIVER={{SQL Server}};"
        #     f"SERVER={server_name};"
        #     f"DATABASE={database_name};"
        #     f"UID={login_name};"
        #     f"PWD={login_pass}"
        # )
        # try:
        #     conn = pyodbc.connect(connection_string)
        #     cursor = conn.cursor()
        #     # query = f"SELECT * FROM {table_name}"
        #     # query = f"[Proc_TB_KD02_YEU_CAU_DAT_HANG_FILTER_BY_MANY_ARGUMENTS_250204_110h38]'','',''"
        #     cursor.execute(query)
        #     columns = [column[0] for column in cursor.description]
        #     data = cursor.fetchall()
        #     cursor.close()
        #     conn.close()
        #     return data
        # except Exception as e:
        #     print("Lỗi khi lấy dữ liệu:", e)
        #     return []
        
        try:
            data = f_utils_fetch_data_from_database(query)
            return data
        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return []
        
        