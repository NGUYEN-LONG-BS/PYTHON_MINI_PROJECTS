from Model import Model

class Controller:
    def __init__(self):
        self.model = Model()  # Model sẽ chịu trách nhiệm đọc file JSON và cơ sở dữ liệu

    def get_data(self):
        """Lấy dữ liệu từ Model (SQL hoặc JSON nếu cần)"""
        return self.model.fetch_data_from_db()  # Lấy dữ liệu từ DB

    def get_header(self):
        """Lấy header từ file JSON trong Model"""
        return self.model.load_header_from_json()  # Lấy header từ file JSON
