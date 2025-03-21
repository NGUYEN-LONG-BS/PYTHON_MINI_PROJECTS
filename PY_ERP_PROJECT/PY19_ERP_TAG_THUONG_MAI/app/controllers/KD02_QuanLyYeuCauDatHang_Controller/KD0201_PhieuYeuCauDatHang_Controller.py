from app.models.KD02_QuanLyYeuCauDatHang_Model import *

class cls_KD0201_PhieuYeuCauDatHang_Controller:
    def __init__(self):
        self.model = cls_KD0201_PhieuYeuCauDatHang_Model()  # Model sẽ chịu trách nhiệm đọc file JSON và cơ sở dữ liệu

    def get_data(self):
        """Lấy dữ liệu từ Model (SQL hoặc JSON nếu cần)"""
        return self.model.fetch_data_from_db()  # Lấy dữ liệu từ DB

    def get_table_config(self):
        """
        Load the table configuration (header, columns, and scrollbars) from the JSON file.
        Returns:
            columns (list): List of column definitions.
            scrollbars (dict): Scrollbar configuration for the table.
            general_settings (dict): General settings for table appearance.
        """
        return self.model.load_table_config_from_json()