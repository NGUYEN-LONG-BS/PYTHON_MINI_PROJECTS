import tkinter as tk
from tkinter import ttk
from Components_View import *
from utils import *
from utils.define import *


class cls_KD0301_CRUDP_KhachHang_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD0301 | THÔNG TIN KHÁCH HÀNG"
        name = "THÔNG TIN KHÁCH HÀNG"
        super().__init__(title_of_form=title, name_of_slip=name)

        # # Initialize controller
        # # self.controller = cls_KD01QuanLyGoiThauController()
        # # self.controller_02 = cls_Controller_config_treeview()
        
        # Gọi các thành phần tái sử dụng
        self.f_create_widgets()
        
    def f_create_widgets(self):
        # Create tabs
        self.f_create_widgets_of_tab_01()
        self.f_create_widgets_of_tab_02()
        self.f_create_widgets_of_tab_03()
        
    def f_create_widgets_of_tab_01(self):
        # Create form fields
        form_fields = ttk.Frame(self.tab1, padding="20")
        form_fields.pack(fill="both", expand=True)
        
        tk.Label(form_fields, text="Thông tin khách hàng", font=("Arial", 18)).grid(column=0, row=0, columnspan=2)

        tk.Label(form_fields, text="Name:", font=("Arial", 12)).grid(column=0, row=1)
        self.name_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
        self.name_entry.grid(column=1, row=1)

        tk.Label(form_fields, text="Email:", font=("Arial", 12)).grid(column=0, row=2)
        self.email_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
        self.email_entry.grid(column=1, row=2)

        tk.Label(form_fields, text="Phone:", font=("Arial", 12)).grid(column=0, row=3)
        self.phone_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
        self.phone_entry.grid(column=1, row=3)

        tk.Label(form_fields, text="Address:", font=("Arial", 12)).grid(column=0, row=4)
        self.address_entry = tk.Text(form_fields, font=("Arial", 12), height=5, width=30)
        self.address_entry.grid(column=1, row=4)

        submit_button = tk.Button(form_fields, text="Register", command=self.f_submit_button_click, bg="#007bff", fg="white", font=("Arial", 12))
        submit_button.grid(column=1, row=5, pady=10)
        
    def f_submit_button_click(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get("1.0", "end-1c")
        self.f_submit_form(name, email, phone, address)
        
    def f_submit_form(self, name, email, phone, address):
        # Save data (e.g., database, file)
        print("Customer registered successfully!")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Address: {address}")    
