import os
import json
import pyodbc
from datetime import datetime

# Import từ chính thư mục utils
from . import utils_functions

class utils_model_TreeviewConfigLoader_250217_13h20:
    """Class để load cấu hình Treeview từ JSON"""

    def load_json(config_json_path):
        """Đọc dữ liệu từ file JSON"""
        try:
            with open(config_json_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error at function: ", utils_functions.f_utils_get_current_function_name())
            print(f"Error: File '{config_json_path}' không tồn tại.")
        except json.JSONDecodeError:
            print("Error at function: ", utils_functions.f_utils_get_current_function_name())
            print("Error: JSON bị lỗi hoặc không hợp lệ.")
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", utils_functions.f_utils_get_current_function_name())
        return None

    def get_column_config(data):
        """Lấy cấu hình cột từ JSON"""
        try:
            columns = data["table"]["columns"]
            column_names = [col["name"] for col in columns]
            return columns, column_names
        except KeyError:
            print("Error: Thiếu key 'table' hoặc 'columns' trong JSON.")
            return [], []

    def get_header_font(data):
        """Lấy cấu hình font của tiêu đề"""
        try:
            font_config = data["table"]["headings"]
            return (font_config["family"], font_config["size"], font_config["weight"])
        except KeyError:
            print("Warning: Không tìm thấy cấu hình font. Dùng mặc định.")
            return ("Arial", 12, "normal")

    def extract_column_attribute(data, attribute, default_value):
        """Trích xuất thuộc tính của cột"""
        try:
            columns = data["table"]["columns"]
            return [column.get(attribute, default_value) for column in columns]
        except KeyError:
            print(f"Warning: Không tìm thấy key '{attribute}' trong JSON.")
            return []

class utils_model_get_data_from_SQL:
    
    def get_data_with_query(query):
        try:
            data = utils_model_get_data_from_SQL.fetch_data(query)
            if not data:
                return []
            return data
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", utils_functions.f_utils_get_current_function_name())
            return []
    
    def fetch_data(query):
        try:
            data = utils_functions.f_utils_fetch_data_from_database(query)
            if data:
                return data
            else:
                return []
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", utils_functions.f_utils_get_current_function_name())
            return []
