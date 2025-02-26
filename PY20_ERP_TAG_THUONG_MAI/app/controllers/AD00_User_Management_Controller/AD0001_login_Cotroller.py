from utils import *
from utils.define import *

class cls_Login_Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def handle_login(self, username, password):
        # Xử lý đăng nhập
        if self.model.validate_user(username, password):
            self.view.show_message(True)
        else:
            self.view.show_message(False)
