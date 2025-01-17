import tkinter as tk
from Components_View import *
from utils import *

class cls_Dashboard_kinhdoanh_View(cls_base_form_number_04_dashboard):
    def __init__(self):
        title = "KD00 - DashboardKinhDoanhView"
        name_of_slip = "KINH DOANH"
        super().__init__(title_of_form=title, name_of_slip=name_of_slip)