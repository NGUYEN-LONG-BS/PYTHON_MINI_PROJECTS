import os
from app.models.folder_manager import create_new_folder, list_directory_contents
from app.utils.theme_utils import load_theme
from datetime import datetime

class KD01QuanLyGoiThauController:
    def __init__(self):
        self.base_path = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"
        folder_name = LABEL_TenThuMucSeKhoiTao

    def create_folder(self, folder_name="24_GOI_THAU_0000_0000"):
        # Call the model function to create a new folder
        folder_path = create_new_folder(self.base_path, folder_name)
        print(f"Created folder: {folder_path}")
        return folder_path  # Optional: return the folder path for further processing in the view

    def get_directory_contents(self):
        # Call the model function to get directory contents
        return list_directory_contents(self.base_path)

    def change_theme(self, theme_name):
        # Apply the theme using utility function
        load_theme(theme_name)


# ==================================================================================================
# Folder Manager Functions (move this to models/folder_manager.py if not already)
# ==================================================================================================

def create_new_folder(base_path, year, notification_number, folder_number):
    """
    Creates a new folder and necessary subfolders based on the provided details.
    """
    folder_name = f"{year}_GOI_THAU_{folder_number.zfill(4)}_{notification_number.zfill(4)}"
    new_folder_path = os.path.join(base_path, folder_name)

    sub_folders = [
        "1.THONG_BAO_MOI_THAU",
        "2.DUYET_GIA",
        "3.MO_THAU",
        "4.TRUNG_THAU"
    ]
    
    try:
        # Create the main folder and subfolders if they don't exist
        os.makedirs(new_folder_path, exist_ok=True)
        for sub_folder in sub_folders:
            os.makedirs(os.path.join(new_folder_path, sub_folder), exist_ok=True)

        print(f"Folder created at: {new_folder_path}")
        return new_folder_path
    except Exception as e:
        print(f"Error creating folder: {e}")
        return None

def list_directory_contents(directory):
    """
    Lists the contents of a directory and sorts them in reverse order.
    """
    try:
        return sorted(os.listdir(directory), reverse=True)
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        return []

