import os
import json
import pyodbc
import uuid

class cls_test_Model():
    def __init__(self):
        # super().__init__()
        self.f_define_table_configurations_json_file()
    
    def f_define_table_configurations_json_file(self):
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(__file__)  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'test_table_input.JSON')
        
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
        self.f_insert_data_to_sql(server_name, database_name, login_name, login_pass, table_name, data_array)
        
    def f_model_get_items_to_combobox_01(self):
        # Simulate fetching data (from a database or API, for example)
        return ['Item 1', 'Item 2', 'Item 3', 'Item 4']
    
    def f_model_data_to_SQL_TB_KD02_YEU_CAU_DAT_HANG(self):
        # Define sample data
        sample_data = [
            {
                "ID": str(uuid.uuid4()),
                "ID_NHAN_VIEN": "NV001",
                "XOA_SUA": "Không",
                "SO_PHIEU": "SP001",
                "NGAY_TREN_PHIEU": "2025-01-09",
                "MA_DOI_TUONG": "KH001",
                "TEN_DOI_TUONG": "Nguyễn Văn A",
                "GHI_CHU_PHIEU": "Khách hàng yêu cầu giao gấp.",
                "STT_DONG": 1,
                "MA_HANG": "MH001",
                "TEN_HANG": "Sản phẩm A",
                "DVT": "Cái",
                "SO_LUONG": 100.50,
                "GHI_CHU_SP": "Sản phẩm chất lượng cao.",
            },
            {
                "ID": str(uuid.uuid4()),
                "ID_NHAN_VIEN": "NV002",
                "XOA_SUA": "Không",
                "SO_PHIEU": "SP002",
                "NGAY_TREN_PHIEU": "2025-01-10",
                "MA_DOI_TUONG": "KH002",
                "TEN_DOI_TUONG": "Trần Thị B",
                "GHI_CHU_PHIEU": "Khách hàng yêu cầu giao gấp.",
                "STT_DONG": 2,
                "MA_HANG": "MH002",
                "TEN_HANG": "Sản phẩm B",
                "DVT": "Thùng",
                "SO_LUONG": 50.00,
                "GHI_CHU_SP": "Giao hàng vào buổi sáng.",
            },
        ]
        return sample_data
