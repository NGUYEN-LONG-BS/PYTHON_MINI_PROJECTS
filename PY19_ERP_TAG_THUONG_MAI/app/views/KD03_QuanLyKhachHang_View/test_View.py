import tkinter as tk
from tkinter import ttk
import time

class cls_test_View(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.f_create_main_window()
        self.f_add_MVC_class()
        self.f_create_widgets()
        
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms

    def f_create_main_window(self):
        self.title("Data Entry Table")
        self.geometry("700x550")
        
    def f_add_MVC_class(self):
        # Import đối tượng cls_test_Controller
        from test_Controller import cls_test_Controller
        # Gọi cửa sổ Controller
        self.controller = cls_test_Controller()
    
    def f_create_widgets(self):
        # Create a notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create tabs
        self.tab_01 = ttk.Frame(self.notebook)
        self.tab_02 = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.tab_01, text="Tạo mới")
        self.notebook.add(self.tab_02, text="Danh sách")
        
        # Settings tab content
        self._f_create_widgets_of_tab_01()
        self._f_create_widgets_of_tab_02()
        
    def _f_create_widgets_of_tab_01(self):
        # Title
        tk.Label(self.tab_01, text="PHIẾU YÊU CẦU ĐẶT HÀNG").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        # Input fields
        tk.Label(self.tab_01, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.tab_01_entry_id = tk.Entry(self.tab_01)
        self.tab_01_entry_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.tab_01, text="Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.tab_01_entry_name = tk.Entry(self.tab_01)
        self.tab_01_entry_name.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.tab_01, text="Age:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.tab_01_entry_age = tk.Entry(self.tab_01)
        self.tab_01_entry_age.grid(row=3, column=1, padx=10, pady=5)

        # Add button
        self.tab_01_button_add = tk.Button(self.tab_01, text="Add Row", command=self.f_tab_01_button_add_click)
        self.tab_01_button_add.grid(row=4, column=0, columnspan=2, pady=10)

        # Table (Treeview)
        tab_01_table_column_names, tab_01_table_column_widths, tab_01_table_column_min_widths, tab_01_table_column_anchors, tab_01_table_column_stretchs = self.controller.f_get_table_config()
        self.table_of_tab_01 = ttk.Treeview(self.tab_01, columns=tab_01_table_column_names, show="headings", height=10)
        # self.table_of_tab_01 = ttk.Treeview(self.tab_01, columns=[], show="headings", height=10)
        self.table_of_tab_01.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.table_of_tab_01.bind("<ButtonRelease-1>", self.f_tab_01_table_on_click)
        
        # print(tab_01_table_column_names)
        # print(tab_01_table_column_widths)
        
        # create headings
        for col, width, min_width, anchor, stretch in zip(tab_01_table_column_names, tab_01_table_column_widths, tab_01_table_column_min_widths, tab_01_table_column_anchors, tab_01_table_column_stretchs):
            self.table_of_tab_01.heading(col, text=col)
            self.table_of_tab_01.column(col, width=width, minwidth=min_width, anchor=anchor, stretch=stretch)

        # Get Data button
        self.tab_01_button_get = tk.Button(self.tab_01, text="Print Data Array", command=self.f_tab_01_button_get_click)
        self.tab_01_button_get.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Export Data button
        self.tab_01_button_export = tk.Button(self.tab_01, text="Export Data to SQL", command=self.f_tab_01_button_export_click)
        self.tab_01_button_export.grid(row=6, column=2, columnspan=2, pady=10)

        # Result label
        self.tab_01_label_result = tk.Label(self.tab_01, text="")
        self.tab_01_label_result.grid(row=7, column=0, columnspan=2)
        
    def _f_create_widgets_of_tab_02(self):
        # Title
        tk.Label(self.tab_02, text="NHẬT KÝ YÊU CẦU ĐẶT HÀNG").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        
        # Input fields
        tk.Label(self.tab_02, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.tab_02_entry_id = tk.Entry(self.tab_02)
        self.tab_02_entry_id.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.tab_02, text="Name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.tab_02_entry_name = tk.Entry(self.tab_02)
        self.tab_02_entry_name.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.tab_02, text="Age:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.tab_02_entry_age = tk.Entry(self.tab_02)
        self.tab_02_entry_age.grid(row=3, column=1, padx=10, pady=5)

        # Add button
        self.tab_02_button_add = tk.Button(self.tab_02, text="Add Row", command=self.f_tab_02_button_add_click)
        self.tab_02_button_add.grid(row=4, column=0, columnspan=2, pady=10)

        # Table (Treeview)
        tab_02_table_columns = self.controller.f_get_table_config()
        self.table_of_tab_02 = ttk.Treeview(self.tab_02, columns=tab_02_table_columns, show="headings", height=10)
        # Gắn sự kiện click vào Treeview
        self.table_of_tab_02.bind("<ButtonRelease-1>", self.f_table_tab_02_click)
        self.table_of_tab_02.grid(row=5, column=0, columnspan=2, pady=10)
        
        # create headings
        for col in tab_02_table_columns:
            self.table_of_tab_01.heading(col, text=col)
            self.table_of_tab_01.column(col, width=100)

        # Get Data button
        self.tab_02_button_get = tk.Button(self.tab_02, text="Print Data Array", command=self.f_tab_02_button_get_click)
        self.tab_02_button_get.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Export Data button
        self.tab_02_button_export = tk.Button(self.tab_02, text="Export Data to SQL", command=self.f_tab_02_button_export_click)
        self.tab_02_button_export.grid(row=6, column=2, columnspan=2, pady=10)

        # Result label
        self.tab_02_label_result = tk.Label(self.tab_02, text="")
        self.tab_02_label_result.grid(row=7, column=0, columnspan=2)

    #===================================================================================================================
    # Event Handlers of tab number 01
    #===================================================================================================================
    def f_tab_01_button_get_click(self):
        self.tab_01_label_result.config(text=self.controller.f_get_data(self.table_of_tab_01), fg="blue")
        
    def f_tab_01_button_add_click(self):
        id_value = self.tab_01_entry_id.get()
        name_value = self.tab_01_entry_name.get()
        age_value = self.tab_01_entry_age.get()
        table = self.table_of_tab_01
        
        # Validate input using the helper function
        is_valid, error_message = self.controller.f_add_row(id_value, name_value, age_value, table)
        if not is_valid:
            self.tab_01_label_result.config(text=error_message, fg="red")
            return
        else:
            # print the tab_01_label_result
            self.tab_01_label_result.config(text=error_message, fg="green")
            self.f_clear_input_fileds_of_tab_01()
    
    def f_tab_01_button_export_click(self):
        self.tab_01_label_result.config(text=self.controller.f_export_data_to_SQL(self.table_of_tab_01), fg="blue")
        
    def f_tab_01_table_on_click(self, event):
        # Call the controller to handle the event
        self.current_time = time.time()
        is_double_click = self.controller.f_handle_event_click_on_table_of_tab_01(self.last_click_time, self.current_time, self.double_click_interval)
        # Update last click time only after handling
        self.last_click_time = self.current_time
        # Handle the action for single and double click
        if is_double_click:
            self.controller.f_tab_01_table_double_click(event)
        else:
            id_value, name_value, age_value = self.controller.f_tab_01_table_single_click(event)
            # Clear and update the Entry widgets if values are returned
            if id_value is not None:
                self.tab_01_entry_id.delete(0, tk.END)
                self.tab_01_entry_id.insert(0, id_value)

            if name_value is not None:
                self.tab_01_entry_name.delete(0, tk.END)
                self.tab_01_entry_name.insert(0, name_value)

            if age_value is not None:
                self.tab_01_entry_age.delete(0, tk.END)
                self.tab_01_entry_age.insert(0, age_value)
    
    def f_clear_input_fileds_of_tab_01(self):
        self.tab_01_entry_id.delete(0, tk.END)
        self.tab_01_entry_name.delete(0, tk.END)
        self.tab_01_entry_age.delete(0, tk.END)
        
    #===================================================================================================================
    # Event Handlers of tab number 02
    #===================================================================================================================
    def f_tab_02_button_get_click(self):
        print("Get Data tab 02")

    def f_tab_02_button_add_click(self):
        print("Add Row tab 02")
        
    def f_tab_02_button_export_click(self):
        print("Export Data to SQL tab 02")
        
    def f_table_tab_02_click(self, event):
        print("Table tab 02 click")