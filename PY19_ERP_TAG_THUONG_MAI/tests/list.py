import tkinter as tk
from tkinter import ttk

# Function to add data to the Treeview
def add_to_treeview():
    ma_hh = entry_ma_hh.get()
    ten_hh = entry_ten_hh.get()
    so_luong = entry_so_luong.get()
    ghi_chu = entry_ghi_chu.get()

    if ma_hh and ten_hh and so_luong:
        tree.insert("", "end", values=(tree.get_children().__len__() + 1, ma_hh, ten_hh, so_luong, ghi_chu))
        entry_ma_hh.delete(0, tk.END)
        entry_ten_hh.delete(0, tk.END)
        entry_so_luong.delete(0, tk.END)
        entry_ghi_chu.delete(0, tk.END)

# Function to print data from the Treeview
def print_data():
    data = []
    for child in tree.get_children():
        row = tree.item(child, "values")
        data.append((
            entry_ma_kh.get(),
            entry_ten_kh.get(),
            entry_so_don_hang.get(),
            row[0],
            row[1],
            row[2],
            float(row[3]),
            row[4]
        ))
    print(data)

# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Customer Info Frame
frame_customer = tk.Frame(root)
frame_customer.pack(pady=10)

tk.Label(frame_customer, text="Mã KH:").grid(row=0, column=0, padx=5, pady=5)
entry_ma_kh = tk.Entry(frame_customer)
entry_ma_kh.grid(row=0, column=1, padx=5, pady=5)

entry_ma_kh.insert(0, "NV001")

tk.Label(frame_customer, text="Tên KH:").grid(row=1, column=0, padx=5, pady=5)
entry_ten_kh = tk.Entry(frame_customer)
entry_ten_kh.grid(row=1, column=1, padx=5, pady=5)

entry_ten_kh.insert(0, "Khách hàng 01")

tk.Label(frame_customer, text="Số đơn hàng:").grid(row=2, column=0, padx=5, pady=5)
entry_so_don_hang = tk.Entry(frame_customer)
entry_so_don_hang.grid(row=2, column=1, padx=5, pady=5)

entry_so_don_hang.insert(0, "DH03")

# Add Item Frame
frame_item = tk.Frame(root)
frame_item.pack(pady=10)

tk.Label(frame_item, text="Mã HH:").grid(row=0, column=0, padx=5, pady=5)
entry_ma_hh = tk.Entry(frame_item)
entry_ma_hh.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_item, text="Tên HH:").grid(row=1, column=0, padx=5, pady=5)
entry_ten_hh = tk.Entry(frame_item)
entry_ten_hh.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_item, text="Số lượng:").grid(row=2, column=0, padx=5, pady=5)
entry_so_luong = tk.Entry(frame_item)
entry_so_luong.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_item, text="Ghi chú HH:").grid(row=3, column=0, padx=5, pady=5)
entry_ghi_chu = tk.Entry(frame_item)
entry_ghi_chu.grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame_item, text="Add to Treeview", command=add_to_treeview).grid(row=4, columnspan=2, pady=10)

# Treeview Frame
frame_treeview = tk.Frame(root)
frame_treeview.pack(pady=10)

tree = ttk.Treeview(frame_treeview, columns=("STT", "Mã HH", "Tên HH", "Số lượng", "Ghi chú HH"), show="headings")
tree.heading("STT", text="STT")
tree.heading("Mã HH", text="Mã HH")
tree.heading("Tên HH", text="Tên HH")
tree.heading("Số lượng", text="Số lượng")
tree.heading("Ghi chú HH", text="Ghi chú HH")

tree.column("STT", width=50)
tree.column("Mã HH", width=100)
tree.column("Tên HH", width=150)
tree.column("Số lượng", width=100)
tree.column("Ghi chú HH", width=200)

tree.pack()

# Print Button
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Print Data", command=print_data).pack()

root.mainloop()
