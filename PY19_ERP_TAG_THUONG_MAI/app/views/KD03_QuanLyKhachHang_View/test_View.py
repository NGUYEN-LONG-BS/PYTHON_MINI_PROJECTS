import tkinter as tk
from tkinter import ttk
import time
import json
from Components_View import *
from Components_View import cls_frame_normal
from Components_View.treeview import cls_Treeview_frame_number_01
from test_Controller import cls_test_Controller

class cls_test_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD02 | QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        name = "QUẢN LÝ YÊU CẦU ĐẶT HÀNG"
        super().__init__(title_of_form=title, name_of_slip=name)
        # Create all functions
        self.f_view_add_MVC_class()
        # call reuse components
        self._f_view_thay_doi_gia_tri_cua_base_form()
        self._f_view_create_all_container_frames_of_window()
        # set up formats
        self._f_view_set_up_formats()
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        # Set up all global variants
        self._f_setup_all_global_variants()
        # Set up all events
        self._f_setup_all_events()
        self._f_hide_components_when_initialzing()
    
    def _f_view_thay_doi_gia_tri_cua_base_form(self):
        # Thay đổi thông tin các tab
        notebook = None
        def find_notebook(widget):
            nonlocal notebook
            for child in widget.winfo_children():
                if isinstance(child, ttk.Notebook):
                    notebook = child
                    return True
                if find_notebook(child):
                    return True
            return False

        find_notebook(self) 

        if not notebook:
            print("Error: notebook not found!")
            return

        # Change the text of the second tabs
        notebook.tab(0, text="TẠO MỚI YÊU CẦU ĐẶT HÀNG")
        notebook.tab(1, text="QUẢN LÝ YÊU CẦU ĐẶT HÀNG")
        
        # Delete the third tab
        notebook.forget(2)
        
        # Change the title of TieuDeTab_01
        for child in self.tab1.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-01":
                        grandchild.destroy()
                        break
        # Change the title of TieuDeTab_01
        for child in self.tab2.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-02":
                        grandchild.destroy()
                        break
        return notebook

    def _f_setup_all_global_variants(self):    
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms
        
    def _f_setup_all_events(self):
        # Bind the <Configure> event to the root window
        self.bind("<Configure>", lambda event: self._f_config_position_of_tab_01_frame_notification())

    def f_view_add_MVC_class(self):
        # Import controller
        self.controller = cls_test_Controller()
        self.controller.view = self
    
    def _f_view_create_all_container_frames_of_window(self):
        # Create tabs
        self.tab_01 = self.tab1
        self.tab_02 = self.tab2
        # Settings tab content
        self._f_view_create_all_container_frames_of_tab_01()
        self._f_view_create_all_container_frames_of_tab_02()
        
    def _f_view_create_all_container_frames_of_tab_01(self):
        # Frame entries
        self.tab_01_frame_H2 = cls_frame_normal(self.tab_01)
        # self.tab_01_frame_H2.pack(fill="both", expand=True)
        self.tab_01_frame_H2.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_H2()

        # Frame entries
        self.tab_01_frame_entries = cls_frame_normal(self.tab_01)
        self.tab_01_frame_entries.pack(side="top", fill="x")
        # self.tab_01_frame_entries.pack(padx=20, pady=20)
        self._f_view_create_widgets_in_tab_01_frame_entries()

        # Frame button
        self.tab_01_frame_button_01 = tk.Frame(self.tab_01)
        self.tab_01_frame_button_01.pack(side="top", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_button_01()

        # Frame treeview
        self.tab_01_frame_treeview_02 = cls_Treeview_frame_number_01(self.tab_01)
        self.tab_01_frame_treeview_02.pack(side="top", fill="both", expand=True)
        self._f_view_create_widgets_in_tab_01_frame_treeview()
        
        # Frame button
        self.tab_01_frame_button_02 = tk.Frame(self.tab_01)
        self.tab_01_frame_button_02.pack(side="bottom", fill="x")
        self._f_view_create_widgets_in_tab_01_frame_button_02()
        
        # Frame notication
        self.tab_01_frame_notification = tk.Frame(self.tab_01)
        self._f_view_create_widgets_in_tab_01_frame_notification()
    
    def _f_view_create_widgets_in_tab_01_frame_H2(self):
        # Title H2
        cls_my_label_num_03_title_H2(self.tab_01_frame_H2, text="PHIẾU YÊU CẦU ĐẶT HÀNG").pack(anchor="center")
        
    def _f_view_create_widgets_in_tab_01_frame_entries(self):
        self.frame_entries_of_slip = tk.Frame(self.tab_01_frame_entries)
        self.frame_entries_of_slip.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_frame_entries_of_slip()
        
        
    def _f_view_create_widgets_in_frame_entries_of_slip(self):
        # Create container for date and number of slip
        self.Frame_container_date_and_number = tk.Frame(self.frame_entries_of_slip, bd=1, relief="solid")
        self.Frame_container_date_and_number.pack(side="top", fill="x", expand=True)
        self._f_view_create_widgets_in_frame_date_and_number()

        # Create container for client and inventories
        self.Frame_clients_and_inventories_information = tk.Frame(self.frame_entries_of_slip, bd=1, relief="solid")
        self.Frame_clients_and_inventories_information.pack(side="top", fill="x", expand=True, pady=(5,0))
        self._f_view_create_widgets_in_frame_clients_and_inventories()

        # Create frame inventories informations
        self.frame_slip_informations = tk.Frame(self.frame_entries_of_slip)
        self.frame_slip_informations.pack(side="top", fill="x", expand=True, pady=(5,0))
        self._f_view_create_widgets_in_frame_slip_informations()

    def _f_view_create_widgets_in_frame_date_and_number(self):
        # Create frame date and number of slip 
        self.frame_date_and_number = cls_Frame_date_and_number_of_slip(self.Frame_container_date_and_number, bd=1, relief="solid")
        self.frame_date_and_number.pack(anchor="center")

    def _f_view_create_widgets_in_frame_clients_and_inventories(self):
        # Create frame clients informations
        self.frame_clients_informations = cls_frame_client_information_view(self.Frame_clients_and_inventories_information)
        self.frame_clients_informations.pack(side="left", fill="both", pady=10)
        
        # Create frame inventories informations
        self.frame_inventories_informations = cls_frame_inventories_information_view(self.Frame_clients_and_inventories_information)
        self.frame_inventories_informations.pack(side="left", fill="both", pady=10)
        self._f_view_add_widget_into_frame_inventories_informations()
        
    def _f_view_create_widgets_in_frame_slip_informations(self):
        # Input fields
        tk.Label(self.frame_slip_informations, text="STT:").pack(side="left")
        self.tab_01_entry_id = tk.Entry(self.frame_slip_informations)
        self.tab_01_entry_id.pack(side="left")
        self.tab_01_entry_id.config(state="disabled")  # This makes the entry non-editable

        # Input fields
        tk.Label(self.frame_slip_informations, text="Thông tin thêm:").pack(side="left")
        self.tab_01_note_for_slip = tk.Entry(self.frame_slip_informations)
        self.tab_01_note_for_slip.pack(side="left", fill="x", pady=10)
        

    def _f_view_add_widget_into_frame_inventories_informations(self):
        self.Sub_frame_01_in_frame_inventories_informations = tk.Frame(self.frame_inventories_informations)
        self.Sub_frame_01_in_frame_inventories_informations.pack(side="bottom")

        tk.Label(self.Sub_frame_01_in_frame_inventories_informations, text="SL YCĐH:").pack(side="left")
        self.tab_01_entry_age = tk.Entry(self.Sub_frame_01_in_frame_inventories_informations)
        self.tab_01_entry_age.pack(side="left")

        tk.Label(self.Sub_frame_01_in_frame_inventories_informations, text="Ghi chú mặt hàng:").pack(side="left")
        self.tab_01_entry_name = tk.Entry(self.Sub_frame_01_in_frame_inventories_informations)
        self.tab_01_entry_name.pack(side="left")

    def _f_view_create_widgets_in_tab_01_frame_button_01(self):
        # Create a sub-frame to organize buttons in the center
        button_container = tk.Frame(self.tab_01_frame_button_01)
        button_container.pack(expand=True, pady=10)
        
        # Add button
        self.tab_01_button_add = tk.Button(button_container, text="Add Row", command=self.f_view_tab_01_button_add_click)
        self.tab_01_button_add.pack(side="left", padx=10)
        
        # Delete update
        self.tab_01_button_update = tk.Button(button_container, text="Update Row", command=self.f_view_tab_01_button_update_click)
        self.tab_01_button_update.pack(side="left", padx=10)
        
        # Delete button
        self.tab_01_button_delete = tk.Button(button_container, text="Delete Row", command=self.f_view_tab_01_button_delete_click)
        self.tab_01_button_delete.pack(side="left", padx=10)

    def f_view_tab_01_button_delete_click(self):
        print("Delete Row tab 01")

    def f_view_tab_01_button_update_click(self):
        print("Update Row tab 01")
        
    def _f_view_create_widgets_in_tab_01_frame_treeview(self):
        self.tab_01_frame_treeview_01 = self.tab_01_frame_treeview_02
        self.table_of_tab_01 = self.tab_01_frame_treeview_02.treeview_normal
        self.treeview_test_of_tag_01 = self.tab_01_frame_treeview_02.treeview_normal
        self.treeview_test_of_tag_01.bind("<ButtonRelease-1>", self.f_view_table_of_tab_01_click)
    
    def _f_view_create_widgets_in_tab_01_frame_button_02(self):
        # Create a sub-frame to organize buttons in the center
        button_container = tk.Frame(self.tab_01_frame_button_02)
        button_container.pack(expand=True, pady=10)
        
        # Get Data button
        self.tab_01_button_get = tk.Button(button_container, text="Print Data Array", command=self.f_tab_01_button_get_click)
        self.tab_01_button_get.pack(side="left", padx=10)
        
        # Export Data button
        self.tab_01_button_export = tk.Button(button_container, text="Export Data to SQL", command=self.f_tab_01_button_export_click)
        self.tab_01_button_export.pack(side="left", padx=10)
        
        # Table config
        self.tab_01_config_num_02 = tk.Button(button_container, text="Print", command=self.f_tab_01_button_print_click)
        self.tab_01_config_num_02.pack(side="left", padx=10)
        
        # Table config
        self.tab_01_btn_import = tk.Button(button_container, text="Import Excel", command=self.f_tab_01_button_import_click)
        self.tab_01_btn_import.pack(side="left", padx=10)
        
        # print config
        self.tab_01_print_config = tk.Button(button_container, text="in cấu hình của bảng", command=self.f_button_print_config_click)
        self.tab_01_print_config.pack(side="left", padx=10)

    def f_tab_01_button_print_click(self):
        print("Print config")
    
    def f_tab_01_button_import_click(self):
        print("Import config")
    
    def _f_view_create_widgets_in_tab_01_frame_notification(self):
        # Result label
        self.tab_01_label_result = tk.Label(self.tab_01_frame_notification, text="")
        self.tab_01_label_result.pack()
        
    def _f_view_create_all_container_frames_of_tab_02(self):
        print("Create tab 02")
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Event Handlers of tab number 01
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def f_tab_01_button_get_click(self):
        self.tab_01_label_result.config(text=self.controller.f_get_data(self.table_of_tab_01), fg="blue")
        self._f_show_and_hide_the_notification_frame()
        
    def f_view_tab_01_button_add_click(self):
        # Update the row count
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        id_value = self.tab_01_entry_id.get()
        name_value = self.tab_01_entry_name.get()
        age_value = self.tab_01_entry_age.get()
        table = self.table_of_tab_01
        
        # Validate input using the helper function
        is_valid, error_message = self.controller.f_controller_add_row(id_value, name_value, age_value, table)
        if not is_valid:
            # Show error message
            self._f_config_notification(text=error_message, fg="red")
            # return
        else:
            # Show success message
            self._f_config_notification(text=error_message, fg="green")
            self.f_clear_input_fileds_of_tab_01()
        # Update the row count
        self._f_view_set_rows_count_of_treeview_01_when_add_new_row()
        
    def _f_view_set_rows_count_of_treeview_01_when_add_new_row(self):
        row_count = 1 + self.controller.f_controller_get_row_count(self.table_of_tab_01)
        self.tab_01_entry_id.config(state="normal")  # Enable the Entry widget to update the value
        self.tab_01_entry_id.delete(0, tk.END)  # Clear the existing value
        self.tab_01_entry_id.insert(0, row_count)  # Insert the new value (ID)
        self.tab_01_entry_id.config(state="disabled")  # Disable the Entry widget again
    
    def _f_config_notification(self, text="", fg="black"):
        self.tab_01_label_result.config(text=text, fg=fg)
        self._f_show_and_hide_the_notification_frame()
        
    def _f_show_and_hide_the_notification_frame(self):
        # Show the notification frame
        self._f_config_position_of_tab_01_frame_notification()
        self.tab_01_frame_notification.after(3000, self.tab_01_frame_notification.place_forget)
        
    def _f_hide_components_when_initialzing(self):
        # Show the notification frame
        self._f_config_position_of_tab_01_frame_notification()
        self.tab_01_frame_notification.after(50, self.tab_01_frame_notification.place_forget)
    
    def f_tab_01_button_export_click(self):
        text = self.controller.f_export_data_to_SQL(self.table_of_tab_01)
        self._f_config_notification(text=text, fg="blue")
    
    def _f_config_position_of_tab_01_frame_notification(self):        
        self.update_idletasks()
        frame_notification_top = self.tab_01.winfo_height() - 25
        frame_notification_left = self.tab_01.winfo_width()/2 - self.tab_01_frame_notification.winfo_width()/2
        self.tab_01_frame_notification.place(x=frame_notification_left, y=frame_notification_top)

    def _f_view_set_up_formats(self):
        self.f_tab_01_button_config_02_click()
        
    def f_tab_01_button_config_02_click(self):
        # Clear the existing columns
        self.treeview_test_of_tag_01.delete(*self.treeview_test_of_tag_01.get_children())
        for col in self.treeview_test_of_tag_01["columns"]:
            self.treeview_test_of_tag_01.heading(col, text="")  # Remove headings
        
        # Trước khi cấu hình, phải thiết lập cột cho Treeview
        tab_01_table_column_names = self.controller.f_get_table_config_name_only()
        self.treeview_test_of_tag_01["columns"] = tab_01_table_column_names
        
        # Treeview config
        list_table_of_tab_01_column_configs, list_table_of_tab_01_column_names, tuple_table_of_tab_01_header_font = self.controller.f_tab_01_button_config_click(self.table_of_tab_01)
        for config, col in zip(list_table_of_tab_01_column_configs, list_table_of_tab_01_column_names):
            # Configure each column
            self.treeview_test_of_tag_01.heading(col, text=col)  # Set header text
            self.treeview_test_of_tag_01.column(
                col,
                width=config["width"],
                minwidth=config["min_width"],
                anchor=config["anchor"],
                stretch=config["stretch"]
            )
            # Set the header font style
            style = ttk.Style()
            style.configure("Treeview.Heading", font=tuple_table_of_tab_01_header_font)
            
            # Apply the background and font settings
            # Apply row styles if needed
            for row in self.treeview_test_of_tag_01.get_children():
                self.treeview_test_of_tag_01.item(row, tags=(row,))
                self.treeview_test_of_tag_01.tag_configure(
                    row,
                    background=config["background_color"],
                    foreground=config["foreground_color"]
                    )
    
    def f_button_print_config_click(self):
        self.f_print_table_of_tab_01_config()
        
    def f_print_table_of_tab_01_config(self):
        # Get the Treeview configuration
        config = self.table_of_tab_01.config()

        # Convert Tcl objects to JSON-serializable Python objects
        json_serializable_config = {}
        for key, value in config.items():
            # Attempt to convert each value
            try:
                if isinstance(value, (list, tuple)):
                    # Recursively convert list or tuple
                    json_serializable_config[key] = [str(item) for item in value]
                else:
                    # Convert single value to string
                    json_serializable_config[key] = str(value)
            except Exception as e:
                # Handle unconvertible values (optional)
                json_serializable_config[key] = f"Error converting: {e}"

        # Save the configuration to a JSON file
        with open("treeview_config.json", "w" ,encoding='utf-8') as json_file:
            json.dump(json_serializable_config, json_file, indent=4, ensure_ascii=False)
    
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
                self.tab_01_entry_id.config(state="normal")  # Enable the Entry widget to update the value
                self.tab_01_entry_id.delete(0, tk.END)
                self.tab_01_entry_id.insert(0, id_value)
                self.tab_01_entry_id.config(state="disabled")  # Disable the Entry widget again

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
        
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    # Event Handlers of tab number 02
    #==========================================================================================================================================================================================================================================================================================================================================================================================================================================
    def f_tab_02_button_get_click(self):
        print("Get Data tab 02")

    def f_tab_02_button_add_click(self):
        print("Add Row tab 02")
        
    def f_tab_02_button_export_click(self):
        print("Export Data to SQL tab 02")
        
    def f_table_tab_02_click(self, event):
        print("Table tab 02 click")