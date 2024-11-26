import os
from app.models.KD01QuanLyGoiThauModel import create_new_folder, list_directory_contents
from app.utils.theme_utils import load_theme

class KD01QuanLyGoiThauController:
    def __init__(self):
        # Base path where folders will be created
        self.base_path = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"

    def create_folder(self, folder_name):
        """
        Creates a folder based on the folder_name passed from the view.
        """
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
        
