from utils import *
import time

class cls_test_Controller():
    def __init__(self):
        super().__init__()
        self.f_add_MVC_class()
        
    def f_add_MVC_class(self):
        # Import đối tượng cls_test_Controller
        from test_Model import cls_test_Model
        # Gọi cửa sổ Controller
        self.model = cls_test_Model()
        
    def f_check_input(self, id_value, name_value, age_value):    
        if not id_value or not name_value or not age_value:
            return False, "All fields are required!"

        try:
            int(id_value)  # Validate ID is an integer
            int(age_value)  # Validate Age is an integer
        except ValueError:
            return False, "ID and Age must be numbers!"
        
        return True, ""

    def f_get_data(self, table):
        """
        Retrieve all rows from the table and print them to the console.
        Args:
            table: The Treeview widget containing the data.
            result_label: The Label widget to display messages.
        """
        rows = []
        for child in table.get_children():
            rows.append(table.item(child)["values"])
        print("Current data array:", rows)
        return "Data printed to console!"
    
    def f_get_data_from_table(self, table):
        """
        Retrieve all rows from the table and print them to the console.
        Args:
            table: The Treeview widget containing the data.
            result_label: The Label widget to display messages.
        """
        rows = []
        for child in table.get_children():
            rows.append(table.item(child)["values"])
        print("Current data array:", rows)
        return rows
    
    # Function to add a row to the table
    def f_add_row(self, id_entry, name_entry, age_entry, table):
        
        # Validate input using the helper function
        is_valid, error_message = self.f_check_input(id_entry, name_entry, age_entry)
        if not is_valid:
            return is_valid, error_message
        
        # Add row to the treeview
        table.insert("", "end", values=(id_entry, name_entry, age_entry))
        error_message ="Row added successfully!"
        
        return is_valid, error_message
    
    def f_get_table_config(self):
        return self.model.f_load_table_config_from_json()
    
    def f_export_data_to_SQL(self, table):
        data_array = self.f_get_data_from_table(table)
        self.model.f_goi_ham_Export_to_SQL(data_array)
        return "Data exported to SQL Server!"
    
    def f_handle_event_click_on_table_of_tab_01(self, last_click_time, current_time, double_click_interval):
        if current_time - last_click_time < double_click_interval:
            return True  # Double click detected
        else:
            return False  # Single click detected
    
    
    def f_tab_01_button_config_click(self, treeview_widget):
        a, b = self.model.f_extract_from_json_columns_config()
        # print("this is columns config:")
        # print(a)
        # print(b)
        return a, b
        
    
    def f_tab_01_table_single_click(self, event):
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # print("Selected row values:", row_values)
            if len(row_values) >= 3:
                return row_values[0], row_values[1], row_values[2]
            else:
                return None, None, None
        else:
            # print("Warning: No row selected.")
            return None, None, None
    
    def f_tab_01_table_double_click(self, event):
        # Get the Treeview widget from the event
        treeview = event.widget
        # Get the selected row ID
        selected_item = treeview.selection()
        if selected_item:
            # Fetch the values of the selected row
            row_values = treeview.item(selected_item[0], "values")
            # Print the first and third values, if they exist
            if len(row_values) >= 3:
                print("First value:", row_values[0])
                print("Third value:", row_values[2])
            else:
                print("Insufficient data in row!")
        

        