import tkinter as tk
from Components_View import *
from utils import *
from utils.define import *

class cls_VT0101_DonDatHang_View(cls_base_form_number_01):
    def __init__(self):
        title = "VT0101 | ĐƠN ĐẶT HÀNG"
        name = "ĐƠN ĐẶT HÀNG TALA"
        super().__init__(title_of_form=title, name_of_slip=name)
        