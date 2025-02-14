import os
import json
import pyodbc
from datetime import datetime
from utils import *


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