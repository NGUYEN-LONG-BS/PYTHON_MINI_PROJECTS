
class cls_Login_Model:
    def __init__(self, username="", password=""):
        # Example credentials, can be replaced with a database or file storage
        self.credentials = {
            "admin": "123",     # admin
            "kd1": "123",       # kinh doanh
            "vt1": "123",       # vật tư
            "tc1": "123",       # tài chính
            "kt1": "123"        # kỹ thuật
        }

    def validate_user(self, username, password):
        # Validate the user's credentials
        return self.credentials.get(username) == password