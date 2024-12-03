import json
from db_connection import create_connection  # Import hàm kết nối từ db_connection.py

class Model:
    def __init__(self, json_file):
        self.json_file = json_file

    def load_header_from_json(self):
        """Đọc header từ file JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("header", [])
        except FileNotFoundError:
            return []

    def fetch_data_from_db(self, query):
        """Truy vấn dữ liệu từ SQL Server"""
        conn = create_connection()  # Gọi hàm kết nối từ db_connection.py
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return rows
