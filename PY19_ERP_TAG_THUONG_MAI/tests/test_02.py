import tkinter as tk
from tkinter import StringVar

def update_entries(*args):
    try:
        # Retrieve and convert the input values
        num01 = float(entry_num01_var.get()) if entry_num01_var.get() else 0
        num02 = float(entry_num02_var.get()) if entry_num02_var.get() else 0

        # Calculate the values for the dependent entries
        min_value = min(num01, num02)
        difference = max((num02 - num01), 0)

        # Update the dependent entries
        entry_num03_var.set(f"{min_value}")
        entry_num04_var.set(f"{difference}")
    except ValueError:
        # Handle invalid input gracefully
        entry_num03_var.set("Error")
        entry_num04_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Dynamic Entry Example")

# Variables to store the values of the entries
entry_num01_var = StringVar()
entry_num02_var = StringVar()
entry_num03_var = StringVar()
entry_num04_var = StringVar()

# Link updates to changes in the first two entries
entry_num01_var.trace("w", update_entries)
entry_num02_var.trace("w", update_entries)

# Create and place the labels and entries
labels = ["Tồn kho khả dụng", "Nhu cầu", "Sl giữ chỗ", "Sl YCDH"]

entry_num01 = tk.Entry(root, textvariable=entry_num01_var)
entry_num02 = tk.Entry(root, textvariable=entry_num02_var)
entry_num03 = tk.Entry(root, textvariable=entry_num03_var, state="readonly")
entry_num04 = tk.Entry(root, textvariable=entry_num04_var, state="readonly")

entries = [entry_num01, entry_num02, entry_num03, entry_num04]

for i, (label_text, entry) in enumerate(zip(labels, entries)):
    tk.Label(root, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry.grid(row=i, column=1, padx=10, pady=5)

# Run the main loop
root.mainloop()
