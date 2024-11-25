from app.models.folder_manager import create_new_folder, list_directory_contents
from app.utils.theme_utils import load_theme

class MainController:
    def __init__(self):
        self.base_path = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"

    def create_folder(self):
        year = datetime.now().strftime("%y")
        folder_number = "0001"  # Example, should calculate dynamically
        notification_number = "0001"  # Example, should get from user input
        folder_path = create_new_folder(self.base_path, year, notification_number, folder_number)
        print(f"Created folder: {folder_path}")

    def get_directory_contents(self):
        return list_directory_contents(self.base_path)

    def change_theme(self, theme_name):
        load_theme(theme_name)
