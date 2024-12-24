import tkinter as tk
from tkinter import ttk
from Components_View import *
from utils import *
from utils.define import *


class cls_KD0301_CRUDP_KhachHang_View(tk.Tk):

    def __init__(self):
        super().__init__()  # Gọi phương thức __init__ của lớp cha

        # Initialize controller
        # self.controller = cls_KD01QuanLyGoiThauController()
        # self.controller_02 = cls_Controller_config_treeview()

        # Setup window
        self.title("KD0301 | THÔNG TIN KHÁCH HÀNG")
        
        # Thiết lập kích thước cửa sổ
        f_utils_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_utils_set_center_screen(self)
        f_utils_setup_fav_icon(self)
        
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self)
        self.f_create_widgets()
        
    # Employee Info Labels
    def f_create_widgets(self):
        # Create a notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Add tabs to notebook
        self.notebook.add(self.tab1, text="Thông tin")
        self.notebook.add(self.tab2, text="Phân loại")
        self.notebook.add(self.tab3, text="About")

        # Settings tab content
        tk.Label(self.tab2, text="Settings", font=("Arial", 24)).pack(pady=20)
        tk.Checkbutton(self.tab2, text="Option 1").pack()
        tk.Checkbutton(self.tab2, text="Option 2").pack()

        # About tab content
        tk.Label(self.tab3, text="About us", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.tab3, text="This is a beautiful dashboard made with Tkinter.").pack(pady=10)
        
        self.f_create_widgets_of_tab_01()
        
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
        
    def f_create_widgets_of_tab_02(self):
        # Create form fields
        form_fields = ttk.Frame(self.tab2, padding="20")
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
