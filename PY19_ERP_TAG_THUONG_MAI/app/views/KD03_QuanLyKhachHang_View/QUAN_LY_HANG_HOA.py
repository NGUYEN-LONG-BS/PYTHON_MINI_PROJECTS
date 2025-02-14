import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Kết nối SQLite (thay bằng kết nối SQL Server nếu cần)
conn = sqlite3.connect("inventory.db")
cursor = conn.cursor()

# Tạo bảng mô phỏng dữ liệu hàng hoá
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ma_hang TEXT UNIQUE,
    ten_hang TEXT,
    dvt TEXT,
    so_luong INTEGER,
    don_gia REAL
)
''')
conn.commit()

# Hàm tải danh sách hàng hoá
def load_inventory():
    cursor.execute("SELECT ma_hang, ten_hang, dvt, so_luong, don_gia FROM inventory")
    rows = cursor.fetchall()
    for row in inventory_tree.get_children():
        inventory_tree.delete(row)
    for row in rows:
        inventory_tree.insert("", "end", values=row)

def add_item():
    ma_hang = entry_ma_hang.get()
    ten_hang = entry_ten_hang.get()
    dvt = entry_dvt.get()
    so_luong = entry_so_luong.get()
    don_gia = entry_don_gia.get()
    if not (ma_hang and ten_hang and dvt and so_luong and don_gia):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        cursor.execute("INSERT INTO inventory (ma_hang, ten_hang, dvt, so_luong, don_gia) VALUES (?, ?, ?, ?, ?)",
                       (ma_hang, ten_hang, dvt, int(so_luong), float(don_gia)))
        conn.commit()
        messagebox.showinfo("Thành công", "Thêm hàng hoá thành công!")
        load_inventory()
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Mã hàng đã tồn tại!")

def update_stock(is_import):
    ma_hang = entry_ma_hang_nhap_xuat.get()
    so_luong = entry_so_luong_nhap_xuat.get()
    if not (ma_hang and so_luong):
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        so_luong = int(so_luong)
        cursor.execute("SELECT so_luong FROM inventory WHERE ma_hang = ?", (ma_hang,))
        row = cursor.fetchone()
        if not row:
            messagebox.showerror("Lỗi", "Mã hàng không tồn tại!")
            return
        current_stock = row[0]
        new_stock = current_stock + so_luong if is_import else current_stock - so_luong
        if new_stock < 0:
            messagebox.showerror("Lỗi", "Không đủ hàng để xuất!")
            return
        cursor.execute("UPDATE inventory SET so_luong = ? WHERE ma_hang = ?", (new_stock, ma_hang))
        conn.commit()
        messagebox.showinfo("Thành công", "Cập nhật kho thành công!")
        load_inventory()
    except ValueError:
        messagebox.showerror("Lỗi", "Số lượng phải là số nguyên!")

# Giao diện chính
root = tk.Tk()
root.title("Quản lý kho hàng")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Tab 1: Danh sách hàng hoá
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text="Danh sách hàng hoá")

inventory_tree = ttk.Treeview(frame1, columns=("Mã hàng", "Tên hàng", "ĐVT", "Số lượng", "Đơn giá"), show="headings")
for col in ("Mã hàng", "Tên hàng", "ĐVT", "Số lượng", "Đơn giá"):
    inventory_tree.heading(col, text=col)
inventory_tree.pack(expand=True, fill="both")

btn_load = ttk.Button(frame1, text="Tải danh sách", command=load_inventory)
btn_load.pack(pady=5)

# Tab 2: Nhập kho
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text="Nhập kho")

entry_ma_hang_nhap_xuat = ttk.Entry(frame2)
entry_ma_hang_nhap_xuat.pack()
entry_ma_hang_nhap_xuat.insert(0, "Nhập mã hàng")
entry_so_luong_nhap_xuat = ttk.Entry(frame2)
entry_so_luong_nhap_xuat.pack()
entry_so_luong_nhap_xuat.insert(0, "Nhập số lượng")

btn_nhap = ttk.Button(frame2, text="Nhập kho", command=lambda: update_stock(True))
btn_nhap.pack()

# Tab 3: Xuất kho
frame3 = ttk.Frame(notebook)
notebook.add(frame3, text="Xuất kho")

btn_xuat = ttk.Button(frame3, text="Xuất kho", command=lambda: update_stock(False))
btn_xuat.pack()

# Tab 4: Thêm hàng hoá
frame4 = ttk.Frame(notebook)
notebook.add(frame4, text="Tạo mới hàng hoá")

entry_ma_hang = ttk.Entry(frame4)
entry_ma_hang.pack()
entry_ma_hang.insert(0, "Mã hàng")
entry_ten_hang = ttk.Entry(frame4)
entry_ten_hang.pack()
entry_ten_hang.insert(0, "Tên hàng")
entry_dvt = ttk.Entry(frame4)
entry_dvt.pack()
entry_dvt.insert(0, "Đơn vị tính")
entry_so_luong = ttk.Entry(frame4)
entry_so_luong.pack()
entry_so_luong.insert(0, "Số lượng")
entry_don_gia = ttk.Entry(frame4)
entry_don_gia.pack()
entry_don_gia.insert(0, "Đơn giá")

btn_add = ttk.Button(frame4, text="Thêm hàng hoá", command=add_item)
btn_add.pack()

root.mainloop()
