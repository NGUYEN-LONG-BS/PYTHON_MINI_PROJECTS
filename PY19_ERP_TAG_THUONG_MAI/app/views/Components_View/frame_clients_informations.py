import tkinter as tk
from tkinter import ttk
from entry import *
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
            ("BH06", "Công ty TNHH Nhà Kính Đẹp", "02641368626", "04 đường Nguyễn Trãi, Cần Thơ, Việt Nam"),
            ("BH07", "Công ty TNHH Trí Hiếu", "02641368125", "26 đường Nguyễn Duy Hưng, Đà Nẵng, Việt Nam"),
            ("BH08", "Công ty TNHH Một Thành Viên Ngại Nùng Chi", "0264151515", "04 đường Lê Lợi, TP. Hồ Chí Minh, Việt Nam"),
            ("BH09", "Công ty TNHH Nhận Thức Việt", "0264136516", "28 đường Trường Chinh, Bình Định, Việt Nam"),
            ("BH10", "Công ty CP Chat GPT", "02641361121", "297 đường Phan Bội Châu, Quy Nhơn, Bình Định, Việt Nam"),
            ("BH11", "Công ty TNHH Con Trí Tuệ", "02641368626", "04 đường Nguyễn Trãi, Cần Thơ, Việt Nam"),
            ("BH12", "Công ty TNHH Cửa Hàng Vũ Phong", "02641368125", "26 đường Nguyễn Duy Hưng, Đà Nẵng, Việt Nam"),
            ("BH13", "Công ty TNHH Một Thành Viên Nhất Nhất", "0264151515", "04 đường Lê Lợi, TP. Hồ Chí Minh, Việt Nam"),
            ("BH14", "Công ty TNHH Cổ Phần TTL", "0264136516", "28 đường Trường Chinh, Bình Định, Việt Nam"),
            ("BH15", "Công ty CP TNHH Khổng lồ", "02641361121", "297 đường Phan Bội Châu, Quy Nhơn, Bình Định, Việt Nam"),
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

        # Main cls_TreeviewCombobox_clients
        self.treeview_combobox = cls_TreeviewCombobox_clients(
            self.frame_row_1,
            columns=self.controller.get_header(),
            data=self.controller.get_data(),
            dropdown_width=1200,
            dropdown_height=300,
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
        self.active_fg_color = "black"

        # Set placeholder text color and the initial text
        self.insert(0, self.placeholder)
        self.config(foreground=self.default_fg_color)
        self.f_on_leaving(color=COLOR_WHITE)

        # Bind events to show and interact with dropdown
        self.bind("<Button-1>", self.f_handle_event_left_click)
        self.bind("<KeyRelease>", self.filter_data)
        self.master.bind("<Button-1>", self.on_click_outside)  # Bind click event to master frame to hide dropdown
        
        parent_widget = self.master.nametowidget(self.master.winfo_parent())
        parent_widget.bind("<Button-1>", self.on_click_outside)

    def on_click_outside(self, event):
        print("on_click_outside")
        self.hide_dropdown()
    
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

            # Biến để theo dõi dòng đang được highlight
            self.current_highlighted = None
            self.tree.bind("<Motion>", self.highlight_row)
            
            # Bind Treeview selection
            self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
            # self.tree.bind("leave", self.hide_dropdown)
            self.tree.bind("<Leave>", self.hide_dropdown)

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
            # Bỏ highlight dòng trước đó
            if self.current_highlighted:
                self.tree.item(self.current_highlighted, tags=())
            
            # Gắn highlight cho dòng hiện tại
            self.tree.item(row_id, tags=("highlighted",))
            self.tree.tag_configure("highlighted", background=HIGHLIGHT_COLOR)
            self.current_highlighted = row_id
        elif not row_id and self.current_highlighted:
            # Nếu không có dòng nào dưới con trỏ, bỏ highlight
            self.tree.item(self.current_highlighted, tags=())
            self.current_highlighted = None