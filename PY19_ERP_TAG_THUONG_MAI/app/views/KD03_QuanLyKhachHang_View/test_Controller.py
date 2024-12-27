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
        """
        Load the table configuration (header, columns, and scrollbars) from the JSON file.
        Returns:
            columns (list): List of column definitions.
            scrollbars (dict): Scrollbar configuration for the table.
            general_settings (dict): General settings for table appearance.
        """
        return self.model.f_load_table_config_from_json()
    
    def f_export_data_to_SQL(self, table):
        data_array = self.f_get_data_from_table(table)
        self.model.f_goi_ham_Export_to_SQL(data_array)
        return "Data exported to SQL Server!"
    
    def f_select_item(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            for i in range(10):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, values[i])
                
            # Update the label with the selected row's index
            row_index = self.treeview.index(selected_item)
            self.selected_row_label.config(text=f"Selected Row: {row_index + 1}")