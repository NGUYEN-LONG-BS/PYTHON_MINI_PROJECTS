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
        self._f_thay_doi_gia_tri_cua_base_form()
        self.f_create_widgets()
        
    def f_create_widgets(self):
        # Create tabs
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
        
        tk.Label(form_fields, text="Mst:", font=("Arial", 12)).grid(column=0, row=5)
        self.mst_entry = tk.Entry(form_fields, font=("Arial", 12), width=30)
        self.mst_entry.grid(column=1, row=5)

        submit_button = tk.Button(form_fields, text="Register", command=self.f_submit_button_click, bg="#007bff", fg="white", font=("Arial", 12))
        submit_button.grid(column=1, row=6, pady=10)
        
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

    def _f_thay_doi_gia_tri_cua_base_form(self):
        # Thay đổi thông tin các tab
        notebook = None
        def find_notebook(widget):
            nonlocal notebook
            for child in widget.winfo_children():
                if isinstance(child, ttk.Notebook):
                    notebook = child
                    return True
                if find_notebook(child):
                    return True
            return False

        find_notebook(self) 

        if not notebook:
            print("Error: notebook not found!")
            return

        # Change the text of the second tab
        notebook.tab(0, text="Thông tin khách hàng")
        notebook.tab(1, text="Danh sách khách hàng")
        # Delete the third tab
        notebook.forget(2)

        # Create new tabs
        tab3 = ttk.Frame(notebook)
        tab4 = ttk.Frame(notebook)

        notebook.add(tab3, text="Tab mới thêm số 3")
        notebook.add(tab4, text="Tab mới thêm số 4")
        
        # Change the title of TieuDeTab_01
        for child in self.tab1.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-01":
                        grandchild.config(text="Thông tin khách hàng")
                        break
        
        return notebook


