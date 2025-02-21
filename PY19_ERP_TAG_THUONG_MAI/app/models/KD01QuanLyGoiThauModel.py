import os
from utils import *

def create_new_folder(base_path, folder_name):
    """
    Creates a new folder and necessary subfolders based on the provided folder name.
    """
    new_folder_path = os.path.join(base_path, folder_name)

    sub_folders = [
        "1.THONG_BAO_MOI_THAU",
        "2.DUYET_GIA",
        "3.MO_THAU",
        "4.TRUNG_THAU"
    ]
    
    try:
        # Create the main folder and subfolders if they don't exist
        os.makedirs(new_folder_path, exist_ok=True)
        for sub_folder in sub_folders:
            os.makedirs(os.path.join(new_folder_path, sub_folder), exist_ok=True)

        print(f"Folder created at: {new_folder_path}")
        return new_folder_path  # Return the full path of the created folder
    except Exception as e:
        print(f"Error: {e}")
        print("Error at function: ", f_utils_get_current_function_name())
        return None

def list_directory_contents(directory):
    """
    Lists the contents of a directory and sorts them in reverse order.
    """
    try:
        return sorted(os.listdir(directory), reverse=True)
    except Exception as e:
        print(f"Error: {e}")
        print("Error at function: ", f_utils_get_current_function_name())
        return []

def check_folder_exists(base_path, folder_name):
    """
    Checks if a folder already exists in the specified base path.
    """
    folder_path = os.path.join(base_path, folder_name)
    return os.path.exists(folder_path)




import os
import json
import pyodbc
import pandas as pd

class Model:
    def __init__(self):
        """Define the JSON file"""
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'KD01_01KD01_TABLE_ABC_FULL.JSON')
        
        # debug
        print(os.path.join(current_dir, 'KD01_01KD01_TABLE_ABC_FULL.JSON'))

    # def load_header_from_json(self):
    #     """Đọc header từ file JSON"""
    #     try:
    #         with open(self.json_file, 'r', encoding='utf-8') as f:
    #             data = json.load(f)
    #             return data.get("header", [])
    #     except FileNotFoundError:
    #         print(f"File {self.json_file} không tìm thấy!")
    #         return []

    def load_table_config_from_json(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                table_info = data.get("table", {})
                columns = table_info.get("columns", [])
                scrollbars = table_info.get("scrollbars", {})
                general_settings = table_info.get("general", {})
                return columns, scrollbars, general_settings
        except FileNotFoundError:
            print(f"File {self.json_file} not found!")
            return [], {}, {}

    
    def fetch_data_from_db(self):
        conn = f_utils_create_a_connection_string_to_SQL_Server()
        
        cursor = conn.cursor()
        query = "[BAN_KINH_DOANH].[dbo].[Proc_TB_QUAN_LY_GOI_THAU_SELECT_241130_11h09] 'NV01'"  # Thay thế với câu lệnh SQL của bạn
        cursor.execute(query)
        rows = cursor.fetchall()

        # Đóng kết nối
        conn.close()
        
        # return df
        return rows
        