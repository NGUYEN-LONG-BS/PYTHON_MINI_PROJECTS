import os
from app.models.KD01QuanLyGoiThauModel import *
from app.utils.theme_utils import load_theme

class DashboardController:
    def __init__(self):
        # Base path where folders will be created
        self.base_path = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"