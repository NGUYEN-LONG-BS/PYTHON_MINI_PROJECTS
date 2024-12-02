import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# CRUD Functions to interact with the Treeview
def create_entry():
    # Get the values from the entry fields
    values = [entry.get() for entry in entries]
    
    if all(values):  # Check if all fields are filled
        # Insert a new row in the Treeview
        treeview.insert("", "end", values=values)
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

def update_entry():
    selected_item = treeview.selection()
    if selected_item:
        # Get the values from the entry fields
        values = [entry.get() for entry in entries]
        if all(values):
            treeview.item(selected_item, values=values)
            clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")
    else:
        messagebox.showwarning("Selection Error", "Please select an item to update")

def delete_entry():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
    else:
        messagebox.showwarning("Selection Error", "Please select an item to delete")

def select_item(event):
    selected_item = treeview.selection()
    if selected_item:
        values = treeview.item(selected_item, "values")
        for i in range(10):
            entries[i].delete(0, tk.END)
            entries[i].insert(0, values[i])

def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)
        entry.insert(0, f"Field {entries.index(entry)+1}")  # Set default value

# Create the main window
root = tk.Tk()
root.title("CRUD Treeview Example")
root.geometry("1100x700")

# Create the frame to hold the Treeview and scrollbar
treeview_frame = tk.Frame(root)
treeview_frame.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# Create the Treeview with 10 columns
columns = [f"Column {i+1}" for i in range(10)]
treeview = ttk.Treeview(treeview_frame, columns=columns, show="headings", height=10)
treeview.grid(row=0, column=0, columnspan=10, padx=10, pady=10)

# Add a horizontal scrollbar
h_scrollbar = tk.Scrollbar(treeview_frame, orient="horizontal", command=treeview.xview)
treeview.configure(xscrollcommand=h_scrollbar.set)
h_scrollbar.grid(row=1, column=0, sticky="ew", padx=10, pady=5)

# Create headings for the Treeview columns
for col in columns:
    treeview.heading(col, text=col)
    
# Set column widths (optional)
for i in range(10):
    treeview.column(columns[i], width=100)  # Adjust width as needed

# Bind selection event to fill entries with the selected row's values
treeview.bind("<ButtonRelease-1>", select_item)

# Create 10 Entry fields for input
entries = []
for i in range(10):
    label = tk.Label(root, text=f"Field {i+1}:")
    label.grid(row=i+1, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.insert(0, f"Field {i+1}")  # Set the default value
    entry.grid(row=i+1, column=1, padx=10, pady=5)
    entries.append(entry)

# Create buttons for CRUD operations
create_button = tk.Button(root, text="Create", command=create_entry)
create_button.grid(row=11, column=0, padx=10, pady=10)

update_button = tk.Button(root, text="Update", command=update_entry)
update_button.grid(row=11, column=1, padx=10, pady=10)

delete_button = tk.Button(root, text="Delete", command=delete_entry)
delete_button.grid(row=11, column=2, padx=10, pady=10)

Refresh_button = tk.Button(root, text="Refresh", command=clear_entries)
Refresh_button.grid(row=11, column=3, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
