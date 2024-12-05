# Model.py
import os
import json
import pyodbc
import pandas as pd

class Model:
    def __init__(self):
        # Define the JSON file
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'KD01_TABLE_ABC.JSON')
        
        # # Debug
        # print(f"đường dẫn file json: {os.path.abspath(self.json_file)}")

    def load_header_from_json(self):
        """Đọc header từ file JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("header", [])
        except FileNotFoundError:
            print(f"File {self.json_file} không tìm thấy!")
            return []

    
    def fetch_data_from_db(self):
        """Lấy dữ liệu từ SQL Server"""
        # Kết nối và truy vấn SQL Server ở đây
        server = '103.90.227.154'  # Replace with your server name
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
        
        # # Lấy dữ liệu và tên cột từ cursor
        # columns = [column[0] for column in cursor.description]
        # rows = cursor.fetchall()
        
        # # Chuyển dữ liệu từ rows thành DataFrame pandas
        # df = pd.DataFrame.from_records(rows, columns=columns)

        # Đóng kết nối
        conn.close()
        
        # # Debug
        # print(rows)
        
        # return df
        return rows
        
    