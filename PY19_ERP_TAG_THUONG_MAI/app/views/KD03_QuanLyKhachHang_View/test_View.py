import tkinter as tk
from tkinter import ttk

class cls_test_View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.f_create_main_window()
        self.f_create_MVC()
        self.f_create_widgets()    

    def f_create_main_window(self):
        self.title("Data Entry Table")
        self.geometry("500x500")
        
    def f_create_MVC(self):
        # Import đối tượng cls_test_Controller
        from test_Controller import cls_test_Controller
        # Gọi cửa sổ Controller
        self.controller = cls_test_Controller()
    
    def f_create_widgets(self):
        # Input fields
        tk.Label(self, text="ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.age_entry = tk.Entry(self)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        # Add button
        self.add_button = tk.Button(self, text="Add Row", command=self.f_add_button_click)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Table (Treeview)
        columns = ("ID", "Name", "Age")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=10)
        self.table.grid(row=4, column=0, columnspan=2, pady=10)

        # create headings
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=100)

        # Get Data button
        self.get_button = tk.Button(self, text="Print Data Array", command=self.f_get_button_click)
        self.get_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = tk.Label(self, text="")
        self.result_label.grid(row=6, column=0, columnspan=2)

    # Function to get all data from the table
    def f_get_button_click(self):
        self.result_label.config(text=self.controller.f_get_data(self.table), fg="blue")

    # Function to add a row to the table
    def f_add_button_click(self):
        """
        Handle the button click event to add a new row to the table.
        Args:
            id_entry: Entry widget for ID input.
            name_entry: Entry widget for Name input.
            age_entry: Entry widget for Age input.
            table: Treeview widget to add the new row.
            result_label: Label widget to display messages.
            f_check_input: Function to validate the input.
        """
        id_value = self.id_entry.get()
        name_value = self.name_entry.get()
        age_value = self.age_entry.get()
        table = self.table
        
        # Validate input using the helper function
        is_valid, error_message = self.controller.f_add_row(id_value, name_value, age_value, table)
        if not is_valid:
            self.result_label.config(text=error_message, fg="red")
            return
        else:
            # print the result_label
            self.result_label.config(text=error_message, fg="green")
            self.f_clear_input_fileds()

    def f_clear_input_fileds(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
