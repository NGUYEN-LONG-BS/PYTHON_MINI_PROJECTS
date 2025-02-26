# Model.py
import os
import json
import pyodbc
import pandas as pd
from utils import *

class cls_model:
    def __init__(self):
        """Define the JSON file"""
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'KD01_TABLE_ABC_FULL.JSON')
        
        # debug
        print(os.path.join(current_dir, 'KD01_TABLE_ABC_FULL.JSON'))

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
        
    