import tkinter as tk
from app.views.Components_View import *
from app.utils import *
from utils.define import *

class cls_VT0102_DonDatHang_TM_View(cls_base_form_number_01_EntryForm):
    def __init__(self):
        title = "VT0102 | ĐƠN ĐẶT HÀNG TM"
        name = "ĐƠN ĐẶT HÀNG TM"
        super().__init__(title_of_form=title, name_of_slip=name)
        