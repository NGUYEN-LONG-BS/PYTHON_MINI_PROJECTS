import os
import json
class cls_test_Model():
    def __init__(self):
        super().__init__()
        self.f_define_table_configurations_json_file()
    
    def f_define_table_configurations_json_file(self):
        # Get the absolute path of the current directory
        current_dir = os.path.dirname(__file__)  
        # Define the relative path to the JSON file
        self.json_file = os.path.join(current_dir, 'test_table.JSON')
        
    def f_load_table_config_from_json(self):
        """Load table and column configurations from JSON"""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.data_to_config_table = json.load(file)  # Load the JSON data

            # Extract column names using the helper function
            # column_names = self.f_extract_column_names(self.data_to_config_table)
            
            # # Extract column names using the helper function
            column_names = self.extract_column_names(self.data_to_config_table)
            # scrollbars = self.data_to_config_table["table"]["scrollbars"]
            # general_settings = self.data_to_config_table["table"]["general"]
            
            
            print("Extracted column names:", column_names)
            return column_names

        except FileNotFoundError:
            print(f"Error: The file '{self.json_file}' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Function to extract column names
    def extract_column_names(self, data):
        if "columns" in data["table"]:
            column_names = [column["name"] for column in data["table"]["columns"]]
            print("Column names:", column_names)
            return column_names
        else:
            return []
        
        # except Exception as e:
        #     print(f"An error occurred: {e}")


    def f_extract_column_names(self):
        """Extract column names from the provided JSON data"""
        if "columns" in self.data_to_config_table:
            # Extract the "name" field from each column in the "columns" list
            column_names = tuple(column["name"] for column in self.data_to_config_table["columns"])
            return column_names
        else:
            print("Error: 'columns' key not found in the JSON data.")
            return ()
       