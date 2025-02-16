import os
import json
import pyodbc
from datetime import datetime
from utils import *

class utils_model_get_config_of_treeview_from_json_file:

    def f_load_table_config_from_json():
        """Load table and column configurations from JSON"""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data_to_config_table = json.load(file)  # Load the JSON data
            column_names = f_extract_from_json_column_names(data_to_config_table)
            column_width = f_extract_from_json_column_width(data_to_config_table)
            column_min_width = f_extract_from_json_column_min_width(data_to_config_table)
            column_anchor = f_extract_from_json_column_anchor(data_to_config_table)
            column_stretch = f_extract_from_json_column_stretch(data_to_config_table)
            
            # print("Extracted column names:", column_names)
            # print("Extracted column width:", column_width)
            return column_names, column_width, column_min_width, column_anchor, column_stretch

        except FileNotFoundError:
            print(f"Error: The file '{json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_load_table_config_from_json_name_only():
        """Load table and column configurations from JSON"""
        json_file = os.path.join(PATH_ASSETS_TEMPLATES_JSON, 'VT_QUAN_LY_HANG_HOA', 'PNK_table_input.JSON')
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data_to_config_table = json.load(file)  # Load the JSON data
            column_names = f_extract_from_json_column_names(data_to_config_table)
            return column_names

        except FileNotFoundError:
            print(f"Error: The file '{json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

class utils_model_get_data_from_SQL:
    
    def get_data_with_query(query):
        data = utils_model_get_data_from_SQL.fetch_data(query)
        return data
    
    def fetch_data(query):
        try:
            data = f_utils_fetch_data_from_database(query)
            # print(data)
            return data
        except Exception as e:
            print("Lỗi khi lấy dữ liệu:", e)
            return []