import tkinter as tk
from tkinter import ttk
# from PIL import Image, ImageTk

# Model: cls_frame_client_information_model
class cls_frame_client_information_model:
    def __init__(self):
        # Sample data to simulate the model
        self.header = ["Mã KH", "Tên KH", "MST", "Địa chỉ"]
        self.data = [
            ("BH01", "Công ty TNHH Con số", "02641368626", "04 đường Nguyễn Trãi, Cần Thơ, Việt Nam"),
            ("BH02", "Công ty TNHH Cửa Hàng", "02641368125", "26 đường Nguyễn Duy Hưng, Đà Nẵng, Việt Nam"),
            ("BH03", "Công ty TNHH Một Thành Viên", "0264151515", "04 đường Lê Lợi, TP. Hồ Chí Minh, Việt Nam"),
            ("BH04", "Công ty TNHH TTL", "0264136516", "28 đường Trường Chinh, Bình Định, Việt Nam"),
            ("BH05", "Công ty CP Khổng lồ", "02641361121", "297 đường Phan Bội Châu, Quy Nhơn, Bình Định, Việt Nam"),
        ]
        

    def get_data(self):
        return self.data
    
    def get_header(self):
        return self.header

    def filter_data(self, query):
        filtered_data = []
        for row in self.data:
            if query in row[0].lower() or query in row[1].lower() or query in row[2].lower():
                filtered_data.append(row)
        return filtered_data

# Controller: cls_frame_client_information_controller
class cls_frame_client_information_controller:
    def __init__(self):
        self.model = cls_frame_client_information_model()  # Create an instance of the model
        # self.view = cls_frame_client_information_view
        # self.view.controller = self

    def get_data(self):
        return self.model.get_data()
    
    def get_header(self):
        return self.model.get_header()

    def filter_data(self, query):
        filtered_data = self.model.filter_data(query)
        self.view.update_combobox_data(filtered_data)
        
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

        # Main cls_TreeviewCombobox
        self.treeview_combobox = cls_TreeviewCombobox(
            self.frame_row_1,
            columns=self.controller.get_header(),
            data=self.controller.get_data(),
            dropdown_width=1200,
            dropdown_height=300,
            width=15,
        )
        self.treeview_combobox.pack(side="left", padx=(5, 2), pady=5)

        # Additional Entry widgets for other column values
        self.additional_entries = []
        
        entry_client_names = ttk.Entry(self.frame_row_1)
        entry_client_names.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=5)
        self.additional_entries.append(entry_client_names)
    
    def _f_create_widgets_of_frame_row_2(self):    
        entry_client_tax_numbers = ttk.Entry(
            self.frame_row_2, 
            width=15
        )
        entry_client_tax_numbers.pack(side="left", padx=(10, 2), pady=5)
        self.additional_entries.append(entry_client_tax_numbers)

        entry_client_address = ttk.Entry(self.frame_row_2)
        entry_client_address.pack(side="left", fill="x", expand=True, padx=(0, 10), pady=5)
        self.additional_entries.append(entry_client_address)

        # Link additional Entry widgets to the cls_TreeviewCombobox
        self.treeview_combobox.set_additional_entries(self.additional_entries)

    def update_combobox_data(self, data):
        self.treeview_combobox.data = data
        self.treeview_combobox.refresh_data()


class cls_TreeviewCombobox(ttk.Entry):
    def __init__(self, master, columns, data, dropdown_width=800, dropdown_height=600, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns
        self.data = data
        self.dropdown_width = dropdown_width
        self.dropdown_height = dropdown_height
        self.dropdown = None
        
        # Placeholder setup
        self.placeholder = "search here"
        self.default_fg_color = "gray"  # Color for placeholder text

        # Set placeholder text color and the initial text
        self.insert(0, self.placeholder)
        self.config(foreground=self.default_fg_color)

        # Bind events to show and interact with dropdown
        # self.bind("<FocusIn>", self.show_dropdown)
        self.bind("<Button-1>", self.show_dropdown)
        self.bind("<KeyRelease>", self.filter_data)
        self.master.bind("<Button-1>", self.on_click_outside)  # Bind click event to master frame to hide dropdown
        # self.bind("<FocusOut>", self.hide_dropdown)

    def on_click_outside(self, event):
        print("on_click_outside")
        # Check if the click is outside the dropdown or the Entry widget
        if self.dropdown and not self.dropdown.winfo_containing(event.x_root, event.y_root):
            self.hide_dropdown()

    def show_dropdown(self, event=None):
        if not self.dropdown:
            # Create a Toplevel dropdown
            self.dropdown = tk.Toplevel(self)
            self.dropdown.overrideredirect(True)
            self.dropdown.geometry(self.get_dropdown_geometry())

            # Create a Treeview in the dropdown
            self.tree = ttk.Treeview(self.dropdown, columns=self.columns, show="headings")
            for col in self.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=120, anchor="w")
            self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Add a scrollbar
            scrollbar = ttk.Scrollbar(self.dropdown, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Populate Treeview with data
            self.refresh_data()

            # Bind Treeview selection
            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
            self.tree.bind("leave", self.hide_dropdown)

        else:
            self.dropdown.lift()

    def hide_dropdown(self, event=None):
        if self.dropdown:
            self.dropdown.destroy()
            self.dropdown = None

    def get_dropdown_geometry(self):
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        return f"{self.dropdown_width}x{self.dropdown_height}+{x}+{y}"

    def filter_data(self, event):
        query = self.get().lower()
        self.refresh_data(query)

    def refresh_data(self, query=""):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert filtered rows
        for row in self.data:
            if query in row[0].lower() or query in row[1].lower() or query in row[2].lower():  # Filter by the first or second column or third column
                self.tree.insert("", "end", values=row)

    def on_tree_select(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")
        if values:
            # Set the selected value in the Entry widget
            self.delete(0, tk.END)
            self.insert(0, values[0])  # Set the first column value

            # Populate additional Entry widgets with other column values
            for i, entry in enumerate(self.additional_entries):
                entry.delete(0, tk.END)
                entry.insert(0, values[i + 1])

            self.hide_dropdown()

    def set_additional_entries(self, entries):
        self.additional_entries = entries