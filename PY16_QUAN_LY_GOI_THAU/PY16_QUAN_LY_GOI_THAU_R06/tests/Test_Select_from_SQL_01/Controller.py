class Controller:
    def __init__(self, model):
        self.model = model

    def get_header(self):
        """Lấy header từ JSON"""
        return self.model.load_header_from_json()

    def get_data(self, query):
        """Lấy dữ liệu từ SQL Server"""
        return self.model.fetch_data_from_db(query)
