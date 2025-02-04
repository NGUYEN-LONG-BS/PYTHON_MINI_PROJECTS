# Model.py
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
        """Lấy dữ liệu từ SQL Server"""
        # Kết nối và truy vấn SQL Server ở đây
        # server = '103.90.227.154'  # Replace with your server name
        server = '14.225.192.238'  # Replace with your server name
        database = 'BAN_KINH_DOANH'  # Replace with your database name
        username = 'sa'  # Replace with your SQL Server username
        password = 'Ta#9999'  # Replace with your password

        # SQL-Server connection string with Server Authentication
        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};PORT=1433'
        )
        cursor = conn.cursor()
        query = "[BAN_KINH_DOANH].[dbo].[Proc_TB_QUAN_LY_GOI_THAU_SELECT_241130_11h09] 'NV01'"  # Thay thế với câu lệnh SQL của bạn
        cursor.execute(query)
        rows = cursor.fetchall()

        # Đóng kết nối
        conn.close()
        
        # return df
        return rows
        
    