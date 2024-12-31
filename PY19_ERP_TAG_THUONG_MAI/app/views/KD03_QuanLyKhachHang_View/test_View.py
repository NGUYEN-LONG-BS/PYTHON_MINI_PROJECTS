import tkinter as tk
from tkinter import ttk
import time
import json

class cls_test_View(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Create all function
        self.f_view_create_main_window()
        self.f_view_add_MVC_class()
        self.f_view_create_widgets()
        
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms
        self.column_names_02, self.columns_config_02 = [], []

    def f_view_create_main_window(self):
        self.title("Data Entry Table")
        self.geometry("700x550")
        
    def f_view_add_MVC_class(self):
        # Import đối tượng cls_test_Controller
        from test_Controller import cls_test_Controller
        # Gọi cửa sổ Controller
        self.controller = cls_test_Controller()
    
    def f_view_create_widgets(self):
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
        self._f_view_create_widgets_of_tab_01()
        self._f_view_create_widgets_of_tab_02()
        
    def _f_view_create_widgets_of_tab_01(self):
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
        self.tab_01_button_add = tk.Button(self.tab_01, text="Add Row", command=self.f_view_tab_01_button_add_click)
        self.tab_01_button_add.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame treeview
        self.tab_01_frame_treeview = tk.Frame(self.tab_01)
        self.tab_01_frame_treeview.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Table (Treeview)
        tab_01_table_column_names = ["Col_01","Col_02","Col_03"]
        self.table_of_tab_01 = ttk.Treeview(self.tab_01_frame_treeview, columns=tab_01_table_column_names, show="headings", height=10)
        self.table_of_tab_01.grid(row=5, column=0, columnspan=2, pady=10)
        self.table_of_tab_01.bind("<ButtonRelease-1>", self.f_view_table_of_tab_01_click)

        # Treeview config
        for col in tab_01_table_column_names:
            self.table_of_tab_01.heading(col, text=col)

        # Frame button
        self.tab_01_frame_button = tk.Frame(self.tab_01)
        self.tab_01_frame_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Get Data button
        self.tab_01_button_get = tk.Button(self.tab_01_frame_button, text="Print Data Array", command=self.f_tab_01_button_get_click)
        # self.tab_01_button_get.grid(row=6, column=0, columnspan=2, pady=10)
        self.tab_01_button_get.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_01_button_export = tk.Button(self.tab_01_frame_button, text="Export Data to SQL", command=self.f_tab_01_button_export_click)
        self.tab_01_button_export.pack(side="left", padx=10)
        
        # Table config
        self.tab_01_config_num_01 = tk.Button(self.tab_01_frame_button, text="cấu hình bảng cách 01", command=self.f_tab_01_button_config_01_click)
        self.tab_01_config_num_01.pack(side="left", padx=10)
        
        # Table config
        self.tab_01_config_num_02 = tk.Button(self.tab_01_frame_button, text="cấu hình bảng cách 02", command=self.f_tab_01_button_config_02_click)
        self.tab_01_config_num_02.pack(side="left", padx=10)
        
        # print config
        self.tab_01_print_config = tk.Button(self.tab_01_frame_button, text="in cấu hình của bảng", command=self.f_button_print_config_click)
        self.tab_01_print_config.pack(side="left", padx=10)

        # Result label
        self.tab_01_label_result = tk.Label(self.tab_01, text="")
        self.tab_01_label_result.grid(row=7, column=0, columnspan=2)
        
    def _f_view_create_widgets_of_tab_02(self):
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
        tab_02_table_column_names = ["Col_01","Col_02","Col_03"]
        self.table_of_tab_02 = ttk.Treeview(self.tab_02, columns=tab_02_table_column_names, show="headings", height=10)
        self.table_of_tab_02.grid(row=5, column=0, columnspan=2, pady=10)
        self.table_of_tab_02.bind("<ButtonRelease-1>", self.f_tab_02_table_on_click)
        
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
        
    def f_view_tab_01_button_add_click(self):
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
    
    def f_tab_01_button_config_01_click(self):
        # Clear the existing columns
        self.table_of_tab_01.delete(*self.table_of_tab_01.get_children())
        for col in self.table_of_tab_01["columns"]:
            self.table_of_tab_01.heading(col, text="")  # Remove headings
        
        # Trước khi cấu hình, phải thiết lập cột cho Treeview
        tab_01_table_column_names, tab_01_table_column_widths, tab_01_table_column_min_widths, tab_01_table_column_anchors, tab_01_table_column_stretchs = self.controller.f_get_table_config()
        self.table_of_tab_01["columns"] = tab_01_table_column_names     
        
        # Treeview config
        for col in tab_01_table_column_names:
            self.table_of_tab_01.heading(col, text=col)
        
        for col, width, min_width, anchor, stretch in zip(
            tab_01_table_column_names, 
            tab_01_table_column_widths, 
            tab_01_table_column_min_widths, 
            tab_01_table_column_anchors, 
            tab_01_table_column_stretchs
        ):    
            self.table_of_tab_01.heading(col, text=col)  # Set header text
            self.table_of_tab_01.column(
                col, 
                width=width, 
                minwidth=min_width, 
                anchor=anchor, 
                stretch=stretch
                )
    
    def f_tab_01_button_config_02_click(self):
        # Clear the existing columns
        self.table_of_tab_01.delete(*self.table_of_tab_01.get_children())
        for col in self.table_of_tab_01["columns"]:
            self.table_of_tab_01.heading(col, text="")  # Remove headings
        
        # Trước khi cấu hình, phải thiết lập cột cho Treeview
        tab_01_table_column_names, tab_01_table_column_widths, tab_01_table_column_min_widths, tab_01_table_column_anchors, tab_01_table_column_stretchs = self.controller.f_get_table_config()
        self.table_of_tab_01["columns"] = tab_01_table_column_names     
        
        
        self.column_names_02, self.columns_config_02 = self.controller.f_tab_01_button_config_click(self.table_of_tab_01)
        # Configure the columns based on the JSON data
        print(zip(self.column_names_02, self.columns_config_02))
        
        for config, col in zip(self.column_names_02, self.columns_config_02):
            print(col)
            print("col nè")
            print(config)
            print("config nè")
            # Configure each column
            self.table_of_tab_01.heading(col, text=col)  # Set header text
            self.table_of_tab_01.column(
                col,
                width=config["width"],
                minwidth=config["min_width"],
                anchor=config["anchor"],
                stretch=config["stretch"]
            )

            # Apply the background and font settings
            self.table_of_tab_01.tag_configure(col, background=config["background_color"], foreground=config["foreground_color"])
    
    def f_button_print_config_click(self):
        self.f_print_table_of_tab_01_config()
        
    def f_print_table_of_tab_01_config(self):
        # Get the Treeview configuration
        config = self.table_of_tab_01.config()

        # Save the configuration to a JSON file
        with open("treeview_config.json", "w") as json_file:
            json.dump(config, json_file, indent=4)
    
    def f_view_table_of_tab_01_click(self, event):
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
    
    def f_tab_02_table_on_click(self, event):
        print("f_tab_02_table_on_click")    

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