import time
from .utils_models import *
from utils import *
import traceback
from datetime import datetime

class utils_controller_get_the_latest_number_of_slip:
    
    def get_list_number_of_slip(database_name, table_name, slip_column_name):
        
        # Tạo câu query SQL với danh sách số phiếu
        query = f"""
        SELECT DISTINCT
            {slip_column_name}
        FROM [{database_name}].[dbo].[{table_name}]
        WHERE [XOA_SUA] = ''
        """
        # print("query", query)
        
        # lấy danh sách số phiếu từ SQL
        danh_sach_so_phieu = utils_model_get_data_from_SQL.get_data_with_query(query)
        # print("danh_sach_so_phieu", danh_sach_so_phieu)
        
        return danh_sach_so_phieu
        
    def extract_numbers_from_data_SQL_num_01(data):
        data_01 = data
        data_02 = tuple(int(item[0].split('-')[-1]) for item in data_01)
        if not data_02:
            current_year = str(datetime.now().year)[-2:]  # Lấy 2 số cuối của năm hiện tại
            data_final = int(f'{current_year}0000')
        else:
            data_final = max(data_02)
        return data_final
        
    def handle_button_get_number_of_slip_click(database_name, table_name):
        # Lấy danh sách số phiếu từ SQL
        data_01 = utils_controller_get_the_latest_number_of_slip.get_list_number_of_slip(database_name, table_name)
        # Lấy số phiếu cuối cùng
        data_02 = utils_controller_get_the_latest_number_of_slip.extract_numbers_from_data_SQL_num_01(data_01)
        
        return data_02