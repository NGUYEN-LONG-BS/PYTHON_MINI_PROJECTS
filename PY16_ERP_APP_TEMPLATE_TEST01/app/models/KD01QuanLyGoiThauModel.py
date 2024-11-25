import os

def create_new_folder(base_path, year, notification_number, folder_number):
    folder_name = f"{year}_GOI_THAU_{folder_number.zfill(4)}_{notification_number.zfill(4)}"
    new_folder_path = os.path.join(base_path, folder_name)

    sub_folders = [
        "1.THONG_BAO_MOI_THAU",
        "2.DUYET_GIA",
        "3.MO_THAU",
        "4.TRUNG_THAU"
    ]
    for sub_folder in sub_folders:
        os.makedirs(os.path.join(new_folder_path, sub_folder), exist_ok=True)

    return new_folder_path

def list_directory_contents(directory):
    try:
        return sorted(os.listdir(directory), reverse=True)
    except Exception as e:
        print(f"Error listing directory contents: {e}")
        return []
