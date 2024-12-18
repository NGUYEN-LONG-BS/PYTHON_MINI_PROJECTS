import os
from app.models.KD01QuanLyGoiThauModel import *
from app.utils.theme_utils import load_theme


class cls_KD01QuanLyGoiThauController:
    def __init__(self):
        # Base path where folders will be created
        self.base_path = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"

    def create_folder(self, folder_name):
        """
        Creates a folder based on the folder_name passed from the view.
        """
        if check_folder_exists(self.base_path, folder_name):
            print(f"Folder '{folder_name}' already exists.")
            return None  # Or you could handle it differently, e.g., notify the user
        folder_path = create_new_folder(self.base_path, folder_name)
        print(f"Created folder: {folder_path}")
        return folder_path  # Return the folder path, can be used for further processing in the view

    def get_directory_contents(self):
        """
        Returns the contents of the base directory.
        """
        return list_directory_contents(self.base_path)

    def change_theme(self, theme_name):
        """
        Changes the application's theme using the specified theme name.
        """
        load_theme(theme_name)
        
class cls_Controller_config_treeview:
    def __init__(self):
        self.model = Model()  # Model sẽ chịu trách nhiệm đọc file JSON và cơ sở dữ liệu

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