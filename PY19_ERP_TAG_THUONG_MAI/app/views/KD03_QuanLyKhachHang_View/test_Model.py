import os
import json
class cls_test_Model():
    def __init__(self):
        super().__init__()
        
    def load_table_config_from_json(self):
        """Load table and column configurations from JSON"""
        
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(__file__)  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'test_table.JSON')
        try:
            # with open(self.json_file, 'r', encoding='utf-8') as f:
            #     data = json.load(f)
            #     table_info = data.get("table", {})
            #     columns = table_info.get("columns", [])
            #     scrollbars = table_info.get("scrollbars", {})
            #     general_settings = table_info.get("general", {})
            #     return columns, scrollbars, general_settings
            with open(self.json_file, 'r', encoding='utf-8') as file:
                config = json.load(file)
            return config["columns"], config["scrollbars"], config["general_settings"]
        except FileNotFoundError:
            print(f"File {self.json_file} not found!")
            return [], {}, {}