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
        """
        Load the table configuration (header, columns, and scrollbars) from the JSON file.
        Returns:
            columns (list): List of column definitions.
            scrollbars (dict): Scrollbar configuration for the table.
            general_settings (dict): General settings for table appearance.
        """
        return self.model.f_load_table_config_from_json()