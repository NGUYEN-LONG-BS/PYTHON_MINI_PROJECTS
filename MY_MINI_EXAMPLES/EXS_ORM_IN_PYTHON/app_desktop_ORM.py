import os
import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Lấy thư mục hiện tại nơi tệp Python đang chạy
current_dir = os.path.dirname(os.path.abspath(__file__))

# Tạo đường dẫn tuyệt đối tới tệp customers.db
db_path = os.path.join(current_dir, 'customers.db')

# Khởi tạo cơ sở dữ liệu và ORM
Base = declarative_base()
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Định nghĩa bảng Customer
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(engine)

# Tạo phiên làm việc với cơ sở dữ liệu
Session = sessionmaker(bind=engine)
session = Session()

# Hàm thêm khách hàng mới
def add_customer():
    name = name_entry.get()
    email = email_entry.get()
    
    if name and email:
        new_customer = Customer(name=name, email=email)
        session.add(new_customer)
        session.commit()
        messagebox.showinfo("Thành công", "Khách hàng đã được thêm!")
        load_customers()
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin.")

# Hàm tải danh sách khách hàng
def load_customers():
    for widget in customer_list_frame.winfo_children():
        widget.destroy()

    customers = session.query(Customer).all()
    for customer in customers:
        customer_label = tk.Label(customer_list_frame, text=f"{customer.name} - {customer.email}")
        customer_label.pack()

# Giao diện Tkinter
root = tk.Tk()
root.title("Ứng dụng Quản lý Khách Hàng")

# Entry và Button để thêm khách hàng
name_label = tk.Label(root, text="Tên khách hàng:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email khách hàng:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

add_button = tk.Button(root, text="Thêm khách hàng", command=add_customer)
add_button.pack()

# Frame để hiển thị danh sách khách hàng
customer_list_frame = tk.Frame(root)
customer_list_frame.pack()

# Tải danh sách khách hàng ban đầu
load_customers()

# Chạy ứng dụng Tkinter
root.mainloop()
