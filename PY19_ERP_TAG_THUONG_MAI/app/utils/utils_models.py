import os
import json
import pyodbc
from datetime import datetime
from utils import *

class utils_model_get_config_of_treeview_from_json_file_250217_10h19:

    def f_get_data_to_config_table_from_json(config_json_path):
        """Load table and column configurations from JSON"""
        try:
            with open(config_json_path, 'r', encoding='utf-8') as file:
                data_to_config_table = json.load(file)  # Load the JSON data
            return data_to_config_table
        except FileNotFoundError:
            print(f"Error: The file '{config_json_path}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def f_load_table_config_from_json(config_json_path):
        """Load table and column configurations from JSON"""
        try:
            data_to_config_table = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_get_data_to_config_table_from_json(config_json_path)
            column_names = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_names(data_to_config_table)
            column_width = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_width(data_to_config_table)
            column_min_width = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_min_width(data_to_config_table)
            column_anchor = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_anchor(data_to_config_table)
            column_stretch = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_stretch(data_to_config_table)

            return column_names, column_width, column_min_width, column_anchor, column_stretch

        except FileNotFoundError:
            print(f"Error: The file '{config_json_path}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_load_table_config_from_json_name_only(config_json_path):
        """Load table and column configurations from JSON"""
        try:
            data_to_config_table = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_get_data_to_config_table_from_json(config_json_path)
            column_names = utils_model_get_config_of_treeview_from_json_file_250217_10h19.f_extract_from_json_column_names(data_to_config_table)
            return column_names

        except FileNotFoundError:
            print(f"Error: The file '{config_json_path}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def f_extract_from_json_columns_config(data_to_config_table):
        # Extract column configurations from the JSON
        columns_config = data_to_config_table["table"]["columns"]
        column_names = [col["name"] for col in columns_config]
        header_font_config = data_to_config_table["table"]["headings"]
        header_font_tuple = (header_font_config['family'], header_font_config['size'], header_font_config['weight'])
        return columns_config, column_names, header_font_tuple
    
    def f_extract_from_json_column_names(data):
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
    
    def f_extract_from_json_column_width(data):
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
    
    def f_extract_from_json_column_min_width(data):
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
    
    def f_extract_from_json_column_anchor(data):
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

    def f_extract_from_json_column_stretch(data):
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
    
    def f_extract_from_json_column_font(data):
        try:
            if "columns" in data["table"]:
                columns_font = data["table"]["columns"]
                column_font = [column.get("font", {"family": "Arial", "size": 12, "weight": "normal"}) for column in columns_font]
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