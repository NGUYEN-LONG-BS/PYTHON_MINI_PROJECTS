# view.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class CRUDTreeviewView:
    def __init__(self, master):
        self.master = master
        self.master.title("CRUD Treeview Example")
        self.master.geometry("1100x700")
        
        self.entries = []
        self.columns = [f"Column {i+1}" for i in range(10)]
        
        # Create the frame to hold the Treeview and scrollbar
        self.treeview_frame = tk.Frame(self.master)
        self.treeview_frame.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

        # Create the Treeview with 10 columns
        self.treeview = ttk.Treeview(self.treeview_frame, columns=self.columns, show="headings", height=10)
        self.treeview.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

        # Add a horizontal scrollbar
        self.h_scrollbar = tk.Scrollbar(self.treeview_frame, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.h_scrollbar.set)
        self.h_scrollbar.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        # Create headings for the Treeview columns
        self.treeview.heading(self.columns[0], text="STT")  # Set the first column header to "STT"
        for col in self.columns[1:]:
            self.treeview.heading(col, text=col)

        # Create headings for the Treeview columns
        for col in self.columns:
            self.treeview.heading(col, text=col)
            
        # Set column widths (optional)
        for i in range(10):
            self.treeview.column(self.columns[i], width=150)  # Adjust width as needed

        # Bind selection event to fill entries with the selected row's values
        self.treeview.bind("<ButtonRelease-1>", self.select_item)
        
        # Create 10 Entry fields for input
        self.create_entry_fields()

        # Create buttons for CRUD operations
        self.create_buttons()

    def create_entry_fields(self):      # Create 10 Entry fields for input
        for i in range(10):
            label = tk.Label(self.master, text=f"Field {i+1}:")
            label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self.master)
            entry.insert(0, f"Field {i+1}")  # Set the default value
            entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.entries.append(entry)
    
    def create_buttons(self):       # Create buttons for CRUD operations
        create_button = tk.Button(self.master, text="Create", command=self.create_entry)
        create_button.grid(row=11, column=0, padx=10, pady=10)

        update_button = tk.Button(self.master, text="Update", command=self.update_entry)
        update_button.grid(row=11, column=1, padx=10, pady=10)

        delete_button = tk.Button(self.master, text="Delete", command=self.delete_entry)
        delete_button.grid(row=11, column=2, padx=10, pady=10)

        refresh_button = tk.Button(self.master, text="Refresh", command=self.clear_entries)
        refresh_button.grid(row=11, column=3, padx=10, pady=10)
    
    # CRUD Functions to interact with the Treeview
    def create_entry(self):
        # Get the values from the entry fields
        values = [entry.get() for entry in self.entries]
        
        # Check if all fields are filled
        if all(values):
            # Insert a new row in the Treeview
            self.treeview.insert("", "end", values=values)
            
            # Clear entry fields
            self.clear_entries()

            # # Sort the Treeview after insertion (if needed)
            # self.sort_treeview()  # Sort after creating entry
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def update_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            # Get the values from the entry fields
            values = [entry.get() for entry in self.entries]
            if all(values):
                self.treeview.item(selected_item, values=values)
                self.clear_entries()
                # self.sort_treeview()  # Sort after deletion
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select an item to update")

    def delete_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            # self.sort_treeview()  # Sort after deletion
        else:
            # If no row is selected, delete the last row
            all_items = self.treeview.get_children()
            if all_items:
                last_item = all_items[-1]  # Get the last item
                self.treeview.delete(last_item)
            else:
                messagebox.showwarning("No Rows", "There are no rows to delete.")

    def select_item(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            for i in range(10):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, values[i])

    def clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
            entry.insert(0, f"Field {self.entries.index(entry)+1}")  # Set default value

    def sort_treeview(self):
        # Get all items in the Treeview
        items = self.treeview.get_children()

        # Filter out items where the first column is not a valid integer
        sorted_items = sorted(
            items, 
            key=lambda item: (
                int(self.treeview.item(item, "values")[0]) 
                if self.is_int(self.treeview.item(item, "values")[0]) 
                else float('inf')  # Assign a large number to non-numeric values
            )
        )
        
        # Clear all items in the Treeview
        for item in items:
            self.treeview.delete(item)

        # Insert the sorted items back into the Treeview
        for item in sorted_items:
            values = self.treeview.item(item, "values")
            self.treeview.insert("", "end", values=values)
    
    def is_int(self, value):
        try:
            int(value)  # Try to convert to an integer
            return True
        except ValueError:
            return False  # Return False if it fails

