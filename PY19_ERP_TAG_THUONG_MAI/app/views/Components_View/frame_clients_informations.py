import tkinter as tk
from tkinter import ttk
from entry import *

# Model: cls_frame_client_information_model
class cls_frame_client_information_model:
        
    def get_data(query=''):
        query = f""" 
            SELECT 
                [MA_DOI_TUONG] AS [Mã KH],
                [TEN_DOI_TUONG] AS [Tên KH],
                [MA_SO_THUE] AS [MST],
                [DIA_CHI] AS [Địa chỉ]
            FROM [TBD_2024].[dbo].[TB_AD00_DANH_SACH_KHACH_HANG]
            WHERE [XOA_SUA] = ''
            ORDER BY [MA_DOI_TUONG]
            """
        data = SQLModel.fetch_data(query)
        # print(data)
        return data
    
    def get_column_width():
        width_of_columns = (80, 400, 100, 200)
        return width_of_columns

    def get_width_of_dropdown():
        width_of_dropdown = 850
        return width_of_dropdown
    
    def get_height_of_dropdown():
        height_of_dropdown = 300
        return height_of_dropdown
    
    def get_header(query=''):
        header = ["Mã KH", "Tên KH", "MST", "Địa chỉ"]
        return header

    def filter_data(query):
        filtered_data = []
        data = cls_frame_client_information_model.get_data()
        for row in data:
            if (query in row[0].lower() or 
                query in row[1].lower() or 
                query in row[2].lower()):
                filtered_data.append(row)
        return filtered_data

# Controller: cls_frame_client_information_controller
class cls_frame_client_information_controller:
    def __init__(self):
        self.model = cls_frame_client_information_model()  # Create an instance of the model

    def get_data(self):
        return self.model.get_data()
    
    def get_width_of_dropdown(self):
        return cls_frame_client_information_model.get_width_of_dropdown()
        # return self.model.width_of_dropdown
    
    def get_height_of_dropdown(self):
        return cls_frame_client_information_model.get_height_of_dropdown()
        # return self.model.height_of_dropdown
    
    def get_column_width(self):
        return cls_frame_client_information_model.get_column_width()
    
    def get_header(self):
        return self.model.get_header()

    def filter_data(self, query):
        filtered_data = self.model.filter_data(query)
        cls_frame_client_information_view.update_combobox_data(filtered_data)
        
# View: cls_frame_client_information_view
class cls_frame_client_information_view(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # setup first
        self._f_setup_geometry()
        # setup second
        self._f_setup_MVC()
        # setup third
        self._f_create_widgets_all_container_frames()
        
    def _f_setup_geometry(self):
        self.config(bd=2, relief="groove")
    
    def _f_create_widgets_all_container_frames(self):
        # row 1
        self.frame_row_1 = tk.Frame(self)
        self.frame_row_1.pack(side="top", fill="x", pady=0)
        self._f_create_widgets_of_frame_row_1()
        # row 2
        self.frame_row_2 = tk.Frame(self)
        self.frame_row_2.pack(side="top", fill="x", pady=0)
        self._f_create_widgets_of_frame_row_2()
        
    def _f_setup_MVC(self):
        self.controller = cls_frame_client_information_controller()  # Create an instance of the controller

    def _f_create_widgets_of_frame_row_1(self):
        # Create label and TreeviewCombobox
        label = ttk.Label(self.frame_row_1, text="Khách hàng:")
        label.pack(side="left", padx=10, pady=5)

        # Load data from the model
        # data=self.controller.get_data(),
        data=self.controller.get_data()         # bỏ dấu phẩy đi
        columns = self.controller.get_header()
        column_width = self.controller.get_column_width()
        dropdown_width = self.controller.get_width_of_dropdown()
        dropdown_height = self.controller.get_height_of_dropdown()
        
        # Main cls_TreeviewCombobox_clients
        self.treeview_combobox = cls_TreeviewCombobox_clients(
            self.frame_row_1,
            columns=columns,
            data=data,
            dropdown_width=dropdown_width,
            dropdown_height=dropdown_height,
            column_width=column_width,
            width=15,
            name="entry_ma_khach_hang"
        )
        self.treeview_combobox.pack(side="left", padx=(5, 2), pady=5)

        # Additional Entry widgets for other column values
        self.additional_entries = []
        
        entry_client_names = cls_my_text_entry_num_01(self.frame_row_1, width=50,
                                                      name="entry_ten_khach_hang")
        entry_client_names.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=5)
        self.additional_entries.append(entry_client_names)
    
    def _f_create_widgets_of_frame_row_2(self):    
        entry_client_tax_numbers = cls_my_text_entry_num_01(
            self.frame_row_2, 
            width=15,
            name="entry_mst"
        )
        entry_client_tax_numbers.pack(side="left", padx=(10, 2), pady=5)
        self.additional_entries.append(entry_client_tax_numbers)

        entry_client_address = cls_my_text_entry_num_01(self.frame_row_2,
                                                        name="entry_dia_chi")
        entry_client_address.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=5)
        self.additional_entries.append(entry_client_address)

        # Link additional Entry widgets to the cls_TreeviewCombobox_clients
        self.treeview_combobox.set_additional_entries(self.additional_entries)

    def update_combobox_data(self, data):
        self.treeview_combobox.data = data
        self.treeview_combobox.refresh_data()

class cls_TreeviewCombobox_clients(cls_my_text_entry_num_01):
    def __init__(self, master, columns, data, dropdown_width=800, dropdown_height=600, column_width=(100, 300, 80, 120), **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns
        self.data = data
        self.dropdown_width = dropdown_width
        self.dropdown_height = dropdown_height
        self.column_width = column_width
        self.dropdown = None
        
        # Placeholder setup
        self.placeholder = "search here"
        self.default_fg_color = "gray"  # Color for placeholder text
        self.active_fg_color = "black"

        # Set placeholder text color and the initial text
        self.insert(0, self.placeholder)
        self.config(foreground=self.default_fg_color)
        self.f_on_leaving(color=COLOR_WHITE)

        # Bind events to show and interact with dropdown
        self.bind("<Button-1>", self.f_handle_event_left_click)
        self.bind("<KeyRelease>", self.filter_data)
    
    def f_handle_event_left_click(self, event):
        self.f_on_click_clear_placeholder(event)
        self.f_show_dropdown(event)
    
    def f_show_dropdown(self, event=None):
        if not self.dropdown:
            # Create a Toplevel dropdown
            self.dropdown = tk.Toplevel(self)
            self.dropdown.overrideredirect(True)
            self.dropdown.geometry(self.get_dropdown_geometry())

            # Create a Treeview in the dropdown
            self.tree = ttk.Treeview(self.dropdown, columns=self.columns, show="headings")
            
            column_widths = self.column_width
            
            for idx, col in enumerate(self.columns):
                self.tree.heading(col, text=col)
                self.tree.column(col, width=column_widths[idx], anchor="w")  # Set width based on the column index
            self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Add a scrollbar
            scrollbar = ttk.Scrollbar(self.dropdown, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Populate Treeview with data
            self.refresh_data()

            # Biến để theo dõi dòng đang được highlight
            self.current_highlighted = None
            self.tree.bind("<Motion>", self.highlight_row)
            
            # Bind Treeview selection
            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
            self.tree.bind("<Leave>", self.hide_dropdown)

        else:
            self.dropdown.lift()

    def hide_dropdown(self, event=None):
        if self.dropdown:
            if hasattr(self, 'tree') and self.tree:
                self.tree.destroy()
            self.dropdown.destroy()
            self.dropdown = None

    def get_dropdown_geometry(self):
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        return f"{self.dropdown_width}x{self.dropdown_height}+{x}+{y}"

    def filter_data(self, event):
        try:
            query = self.get().lower()
            self.refresh_data(query)
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())

    def refresh_data(self, query=""):
        if not hasattr(self, 'tree') or not self.tree:
            return  # Tránh lỗi nếu self.tree không tồn tại
        
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert filtered rows
        for row in self.data:
            # print(row)
            if (query in str(row[0]).lower() or 
                query in str(row[1]).lower() or 
                query in str(row[2]).lower()):  # Filter by the first or second column or third column
                self.tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
            

    def on_tree_select(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        if values:
            # Set the selected value in the Entry widget
            self.delete(0, tk.END)
            self.insert(0, values[0])  # Set the first column value

            # Populate additional Entry widgets with other column values
            for i, entry in enumerate(self.additional_entries):
                if i + 1 < len(values):  # Ensure there are enough values to access
                    entry.delete(0, tk.END)
                    entry.insert(0, values[i + 1])

            self.hide_dropdown()

    def set_additional_entries(self, entries):
        self.additional_entries = entries
        
    def f_on_click_clear_placeholder(self, event):
        """Clear placeholder text when clicking on the entry."""
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(foreground=self.active_fg_color)
            
    def highlight_row(self, event):
        # Lấy ID của dòng dưới con trỏ chuột
        row_id = self.tree.identify_row(event.y)

        # Nếu có dòng mới dưới con trỏ, highlight nó
        if row_id and row_id != self.current_highlighted:
            # Bỏ highlight dòng trước đó, nếu có
            if self.current_highlighted:
                # Kiểm tra nếu dòng hiện tại còn tồn tại
                if self.tree.exists(self.current_highlighted):
                    self.tree.item(self.current_highlighted, tags=())
            
            # Gắn highlight cho dòng hiện tại
            self.tree.item(row_id, tags=("highlighted",))
            self.tree.tag_configure("highlighted", background=HIGHLIGHT_COLOR)
            self.current_highlighted = row_id
        elif not row_id and self.current_highlighted:
            # Nếu không có dòng nào dưới con trỏ, bỏ highlight
            if self.tree.exists(self.current_highlighted):
                self.tree.item(self.current_highlighted, tags=())
            self.current_highlighted = None