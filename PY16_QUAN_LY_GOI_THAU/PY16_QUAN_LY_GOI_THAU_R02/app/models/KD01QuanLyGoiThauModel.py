import os

def create_new_folder(base_path, folder_name):
    """
    Creates a new folder and necessary subfolders based on the provided folder name.
    """
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
        return new_folder_path  # Return the full path of the created folder
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

def check_folder_exists(base_path, folder_name):
    """
    Checks if a folder already exists in the specified base path.
    """
    folder_path = os.path.join(base_path, folder_name)
    return os.path.exists(folder_path)