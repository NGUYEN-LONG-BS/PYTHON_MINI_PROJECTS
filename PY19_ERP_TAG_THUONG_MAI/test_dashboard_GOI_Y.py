import tkinter as tk
from tkinter import ttk

# Model: cls_client_information_frame_model
class cls_client_information_frame_model:
    def __init__(self):
        # Sample data to simulate the model
        self.data = [
            ("BH01", "Công ty TNHH Con số", "02641368626", "04 đường Nguyễn Trãi, Cần Thơ, Việt Nam"),
            ("BH02", "Công ty TNHH Cửa Hàng", "02641368125", "26 đường Nguyễn Duy Hưng, Đà Nẵng, Việt Nam"),
            ("BH03", "Công ty TNHH Một Thành Viên", "0264151515", "04 đường Lê Lợi, TP. Hồ Chí Minh, Việt Nam"),
            ("BH04", "Công ty TNHH TTL", "0264136516", "28 đường Trường Chinh, Bình Định, Việt Nam"),
            ("BH05", "Công ty CP Khổng lồ", "02641361121", "297 đường Phan Bội Châu, Quy Nhơn, Bình Định, Việt Nam"),
        ]

    def get_data(self):
        return self.data

    def filter_data(self, query):
        filtered_data = []
        for row in self.data:
            if query in row[0].lower() or query in row[1].lower() or query in row[2].lower():
                filtered_data.append(row)
        return filtered_data


# View: cls_client_information_frame_view
class cls_client_information_frame_view(tk.Frame):
    def __init__(self, master, columns, controller, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns
        self.controller = controller

        # Create label and TreeviewCombobox
        label = ttk.Label(self, text="Select an item:")
        label.pack(padx=10, pady=5)

        # Main cls_TreeviewCombobox
        self.treeview_combobox = cls_TreeviewCombobox(
            self,
            columns=self.columns,
            data=self.controller.get_data(),
            dropdown_width=1200,
            dropdown_height=300,
            width=30,
        )
        self.treeview_combobox.pack(padx=10, pady=5)

        # Additional Entry widgets for other column values
        self.additional_entries = []
        for i in range(1, len(self.columns)):
            label = ttk.Label(self, text=f"{self.columns[i]}:")
            label.pack(side="left", padx=10, pady=5)

            entry = ttk.Entry(self, width=30)
            entry.pack(side="left", padx=10, pady=5)
            self.additional_entries.append(entry)

        # Link additional Entry widgets to the cls_TreeviewCombobox
        self.treeview_combobox.set_additional_entries(self.additional_entries)

    def update_combobox_data(self, data):
        self.treeview_combobox.data = data
        self.treeview_combobox.refresh_data()

# Controller: cls_client_information_frame_controller
class cls_client_information_frame_controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

    def get_data(self):
        return self.model.get_data()

    def filter_data(self, query):
        filtered_data = self.model.filter_data(query)
        self.view.update_combobox_data(filtered_data)


# Combobox for Treeview (Remains the same)
class cls_TreeviewCombobox(ttk.Entry):
    def __init__(self, master, columns, data, dropdown_width=800, dropdown_height=600, **kwargs):
        super().__init__(master, **kwargs)
        self.columns = columns
        self.data = data
        self.dropdown_width = dropdown_width
        self.dropdown_height = dropdown_height
        self.dropdown = None

        # Bind events to show and interact with dropdown
        self.bind("<Button-1>", self.show_dropdown)
        self.bind("<KeyRelease>", self.filter_data)

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
        self.controller.filter_data(query)

    def refresh_data(self, query=""):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert filtered rows
        for row in self.data:
            if query in row[0].lower() or query in row[1].lower() or query in row[2].lower():  # Filter by the first, second, or third column
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


# Sample usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Treeview Combobox Example with Additional Entries")

    sample_columns = ["ID", "Name", "MST", "Địa chỉ"]

    # Model, View, Controller setup
    model = cls_client_information_frame_model()
    view = cls_client_information_frame_view(root, columns=sample_columns, controller=None)
    controller = cls_client_information_frame_controller(model, view)

    # Create and pack the client frame
    view.pack(padx=10, pady=10, fill="both", expand=True)

    root.mainloop()
