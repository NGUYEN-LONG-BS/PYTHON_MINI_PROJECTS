# Model.py
import os
import json
import pyodbc

class Model:
    def __init__(self):
        self.json_file = r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY16_QUAN_LY_GOI_THAU\PY16_QUAN_LY_GOI_THAU_R06\tests\Test_02\KD01_TABLE_ABC.JSON"
        print(f"đường dẫn file json: {os.path.abspath(self.json_file)}")

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
        query = "[BAN_KINH_DOANH].[dbo].[Proc_TB_QUAN_LY_GOI_THAU_SELECT_241129_09h07] '1'"  # Thay thế với câu lệnh SQL của bạn
        cursor.execute(query)
        rows = cursor.fetchall()

        return rows
        
    