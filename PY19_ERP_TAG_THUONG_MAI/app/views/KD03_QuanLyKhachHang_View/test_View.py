import tkinter as tk
from tkinter import ttk

# Function to add a row to the table
def add_row():
    id_value = id_entry.get()
    name_value = name_entry.get()
    age_value = age_entry.get()

    if not id_value or not name_value or not age_value:
        result_label.config(text="All fields are required!", fg="red")
        return

    try:
        int(id_value)  # Validate ID is an integer
        int(age_value)  # Validate Age is an integer
    except ValueError:
        result_label.config(text="ID and Age must be numbers!", fg="red")
        return

    # Add row to the treeview
    table.insert("", "end", values=(id_value, name_value, age_value))
    result_label.config(text="Row added successfully!", fg="green")

    # Clear input fields
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)


# Function to get all data from the table
def get_data():
    rows = []
    for child in table.get_children():
        rows.append(table.item(child)["values"])
    print("Current data array:", rows)
    result_label.config(text="Data printed to console!", fg="blue")


# Create main window
root = tk.Tk()
root.title("Data Entry Table")
root.geometry("500x500")

# Input fields
tk.Label(root, text="ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Add button
add_button = tk.Button(root, text="Add Row", command=add_row)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# # Add button
# print_button = tk.Button(root, text="Print data", command=add_row)
# print_button.grid(row=3, column=1, columnspan=2, pady=10)

# Table (Treeview)
columns = ("ID", "Name", "Age")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)
table.grid(row=4, column=0, columnspan=2, pady=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

# Get Data button
get_button = tk.Button(root, text="Print Data Array", command=get_data)
get_button.grid(row=5, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=2)

# Run the application
root.mainloop()
