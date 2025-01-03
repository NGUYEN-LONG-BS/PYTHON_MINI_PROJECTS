import tkinter as tk
from Tktable import Table

root = tk.Tk()
root.title("Editable Table with Tktable")

# Create table
table = Table(root)
table.pack()

# Insert data
table.insert("end", ("ID", "Name", "Age"))
table.insert("end", (1, "John Doe", 25))
table.insert("end", (2, "Jane Smith", 30))

root.mainloop()
