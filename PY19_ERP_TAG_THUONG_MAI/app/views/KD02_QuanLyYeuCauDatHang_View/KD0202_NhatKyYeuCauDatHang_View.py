# view.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import json
import os
import unicodedata  # This will help normalize Vietnamese characters
from controllers.KD02QuanLyYeuCauDatHangController import cls_controller
from Components_View import *
from utils import *

class cls_KD0201_NhatKyYeuCauDatHang_View(tk.Tk):
    def __init__(self):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        self.title("KD0201 - PHIẾU YÊU CẦU ĐẶT HÀNG")
        # Gọi các thành phần tái sử dụng
        cls_menu_top(self)
        # =======================================================================================================================
        # Thiết lập kích thước cửa sổ
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(self, maximize=True)
        f_utils_set_center_screen(self)
        
        # Lấy kích thước của cửa sổ
        self.update_idletasks()  # Cập nhật các thay đổi về kích thước
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        # =======================================================================================================================
        # Theme
        BORDER_SIZE_0 = 0
        BORDER_SIZE_1 = 0
        BG_COLOR_0_0 = "#f0f0f0"
        BG_COLOR_1 = "#f0f0f0"
        
        # =======================================================================================================================
        # Create a canvas and a vertical scrollbar
        self.canvas = tk.Canvas(self.master, width=window_width, bg=BG_COLOR_0_0)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        
        # self.v_scrollbar_of_frame_inside_canvas = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview, bg=BG_COLOR_1)
        self.v_scrollbar_of_frame_inside_canvas = tk.Scrollbar(self.master, orient="vertical", command=self.canvas.yview, bg=BG_COLOR_1)
        self.v_scrollbar_of_frame_inside_canvas.pack(side="right", fill="y")
        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.v_scrollbar_of_frame_inside_canvas.set)

        # =======================================================================================================================
        # Create a frame to hold the widgets (this frame will be inside the canvas)
        frame_inside_canvas = tk.Frame(self.canvas, bd=BORDER_SIZE_0, relief="solid", bg=BG_COLOR_1)
        frame_inside_canvas.pack(fill="x", side="top", padx=10, pady=10)

        # Create a window on the canvas to add the frame
        self.canvas_window = self.canvas.create_window(0, 0, window=frame_inside_canvas, anchor="nw")

        # =======================================================================================================================
        # Create the frame to hold the entry fields
        self.frame_header_container = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid")
        self.frame_header_container.pack(fill="both", expand=True, padx=10, pady=10)

        # =======================================================================================================================
        # Create the frame to hold the entries of treeview
        self.H1_frame = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid")
        self.H1_frame.pack(fill="both", expand=True, padx=10, pady=10)
        # Create 10 Entry fields for input
        self.f_add_elements_to_frame_of_H1()

        # =======================================================================================================================
        # Create the frame to hold the entries of treeview
        self.frame_entries_of_form = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid")
        self.frame_entries_of_form.pack(fill="both", expand=True, padx=10, pady=10)
        # Create 10 Entry fields for input
        self.f_add_elements_to_frame_entries_of_form()
        
        # =======================================================================================================================
        # Create the frame to hold the entries of treeview
        self.frame_entries_of_treeview = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid")
        self.frame_entries_of_treeview.pack(fill="both", expand=True, padx=10, pady=10)
        # Create 10 Entry fields for input
        self.f_add_elements_to_frame_entries_of_treeview()
        
        # =======================================================================================================================
        # Create the frame to hold the entries of treeview
        self.frame_test = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid")
        self.frame_test.pack(fill="both", expand=True, padx=10, pady=10)
        # Create 10 Entry fields for input
        self.f_add_elements_to_frame_test()
        
        # =======================================================================================================================
        # Create the frame to hold the Treeview and scrollbar
        self.treeview_frame = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid", bg=BG_COLOR_1)
        self.treeview_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.f_add_elements_to_treeview_frame()
        
        # Bind mouse wheel events to both treeview and canvas
        self.treeview_frame.bind("<Enter>", self.f_enable_treeview_scroll)
        self.treeview_frame.bind("<Leave>", self.f_enable_canvas_scroll)

        # =======================================================================================================================
        # Create a frame for the top-right button (Refresh Button)
        self.frame_header_top_right = tk.Frame(self.frame_header_container, bd=BORDER_SIZE_0, relief="solid")
        self.frame_header_top_right.grid(row=0, column=10, padx=10, pady=10, sticky="ne")
        self.f_add_elements_to_frame_header_top_right()

        # =======================================================================================================================
        # Create the frame to hold the buttons
        self.buttons_frame = tk.Frame(frame_inside_canvas, bd=BORDER_SIZE_0, relief="solid", bg=BG_COLOR_1, height=150, width=500)
        self.buttons_frame.pack(fill="both", side="bottom", expand=True, padx=10, pady=10)
        self.f_add_elements_to_buttons_frame()
        
        # =======================================================================================================================
        # Update the scroll region of the canvas
        self.f_update_scroll_region()
        
        # Update the scrollregion of the canvas to match the size of the frame
        frame_inside_canvas.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
        # Default: scroll the canvas
        self.is_scrolling_canvas = True
        
        # Bind the mouse wheel event to the canvas (works anywhere on the window)
        self.canvas.bind_all("<MouseWheel>", self.f_on_mouse_wheel)
        
        # Monitor window size changes to toggle the scrollbar visibility
        self.bind("<Configure>", self.f_adjust_the_sizes_dynamically)
        
        # After everything is initialized, update scroll regions
        self.after(100, self.f_update_scroll_region)

    def f_adjust_the_sizes_dynamically(self, event):
        # =======================================================================================================================
        # Step: toggle_scrollbar_visibility
        # Check if the content of the canvas exceeds the window height
        bbox = self.canvas.bbox("all")
        if bbox:
            canvas_height = bbox[3]  # The bottommost coordinate of the content
            if canvas_height > self.winfo_height():
                # Show the scrollbar if content height is greater than window height
                self.v_scrollbar_of_frame_inside_canvas.pack(side="right", fill="y")
            else:
                # Hide the scrollbar if content height is less than window height
                self.v_scrollbar_of_frame_inside_canvas.pack_forget()
        # =======================================================================================================================
        # Step: Adjust the width of the frame inside the canvas dynamically.
        # Get the current width of the window and subtract 20
        new_width = self.winfo_width() - 0

        # Update the width of the frame_inside_canvas
        self.canvas.itemconfig(self.canvas_window, width=new_width)
        
        # =======================================================================================================================
        # Step: Move frame_inside_canvas to the top after resizing
        # Reset the position of frame_inside_canvas to top-left corner (only when resizing, not on scroll)
        if not self.is_scrolling_canvas:
            self.canvas.coords(self.canvas_window, 0, 0)
        
        # =======================================================================================================================
        # Step: toggle_scrollbar_visibility
        # Check the width of the Treeview content against the available width
        treeview_width = sum(self.treeview.column(col, "width") for col in self.columns)  # Get the width of the Treeview content
        
        # Compare the total width of the Treeview with the width of the treeview_frame
        if treeview_width > self.treeview_frame.winfo_width():
            # Show the horizontal scrollbar if the Treeview content is wider than the frame
            self.h_scrollbar.pack(side="bottom", fill="x", padx=10, pady=5)
        else:
            # Hide the horizontal scrollbar if the Treeview content fits within the frame
            self.h_scrollbar.pack_forget()
            
        # After resizing, update the scroll region of the canvas to include the new content
        self.f_update_scroll_region()
        

    # =======================================================================================================================
    def f_enable_treeview_scroll(self, event):
        # Enable scrolling for the Treeview when the cursor enters the Treeview frame
        self.is_scrolling_canvas = False

    def f_enable_canvas_scroll(self, event):
        # Enable scrolling for the Canvas when the cursor leaves the Treeview frame
        self.is_scrolling_canvas = True

    def f_on_mouse_wheel(self, event):
        if self.is_scrolling_canvas:
            # Scroll the canvas depending on the wheel movement (event.delta)
            if event.delta > 0:  # Scroll up
                self.canvas.yview_scroll(-1, "units")
            else:  # Scroll down
                self.canvas.yview_scroll(1, "units")
                
            # Trì hoãn việc cập nhật lại vị trí hoặc cuộn
            self.after(100, self.f_update_scroll_region)
        else:
            # Scroll the Treeview (vertical scroll) when the cursor is over it
            if event.delta > 0:  # Scroll up
                self.treeview.yview_scroll(-1, "units")
            else:  # Scroll down
                self.treeview.yview_scroll(1, "units")

    def f_add_elements_to_frame_header_top_right(self):      # Create 10 Entry fields for input
        # Create the refresh button in the top-right frame
        self.refresh_button = tk.Button(self.frame_header_top_right, text="Refresh", command=self.f_refresh_window)
        self.refresh_button.grid(row=0, column=0)

    def f_add_elements_to_frame_of_H1(self):
        label = tk.Label(self.H1_frame, text=f"PHIẾU YÊU CẦU ĐẶT HÀNG", font=("Arial", 20))
        label.pack(anchor="center")

    def f_add_elements_to_frame_entries_of_form(self):
        # Get today's date in the format dd/mm/yyyy
        today = datetime.datetime.today().strftime('%d/%m/%Y')
        
        # Row 0: Date
        label_date_on_slip = tk.Label(self.frame_entries_of_form, text=f"Ngày:")
        label_date_on_slip.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        entry_date_on_slip = tk.Entry(self.frame_entries_of_form)
        entry_date_on_slip.insert(0, today)  # Set the default value
        entry_date_on_slip.grid(row=0, column=1, padx=10, pady=5)
        
        # Row 0: Slip Number
        label_number_of_slip = tk.Label(self.frame_entries_of_form, text=f"Số phiếu:")
        label_number_of_slip.grid(row=0, column=2, padx=10, pady=5, sticky="w")
        
        entry_number_of_slip = tk.Entry(self.frame_entries_of_form)
        entry_number_of_slip.insert(0, "")  # Set the default value
        entry_number_of_slip.grid(row=0, column=3, padx=10, pady=5, sticky="w")
        
        # Row 1: Customer ID
        label_ma_doi_tuong = tk.Label(self.frame_entries_of_form, text=f"Mã KH:")
        label_ma_doi_tuong.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        entry_ma_doi_tuong = tk.Entry(self.frame_entries_of_form)
        entry_ma_doi_tuong.insert(0, "")  # Set the default value
        entry_ma_doi_tuong.grid(row=1, column=1, padx=10, pady=5)
        
        # Row 1: Customer Name - Span to the end of the frame
        label_ten_doi_tuong = tk.Label(self.frame_entries_of_form, text=f"Tên KH:")
        label_ten_doi_tuong.grid(row=1, column=2, padx=10, pady=5, sticky="w")
        
        entry_ten_doi_tuong = tk.Entry(self.frame_entries_of_form)
        entry_ten_doi_tuong.insert(0, "")  # Set the default value
        entry_ten_doi_tuong.grid(row=1, column=3, columnspan=2, padx=10, pady=5, sticky="ew")
        
        # Configure grid to stretch properly
        self.frame_entries_of_form.grid_columnconfigure(3, weight=2)  # Allow column 3 to expand to fill the space
            
    def f_add_elements_to_frame_entries_of_treeview(self):
        # Load product data from JSON file
        self.products = self.load_products_data()

        # Extract product details for comboboxes
        self.product_ids = [product["product_ID"] for product in self.products]
        self.product_names = [product["product_name"] for product in self.products]

        # Row 0: inventory ID
        # Create combobox for product_ID
        self.product_id_label = tk.Label(self.frame_entries_of_treeview, text=f"Mã HH:")
        self.product_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.product_id_combobox = ttk.Combobox(self.frame_entries_of_treeview, values=self.product_ids, state="normal")
        self.product_id_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.product_id_combobox.bind("<<ComboboxSelected>>", self.on_product_id_selected)
        self.product_id_combobox.bind("<KeyRelease>", self.filter_product_ids)

        # Row 0: inventory Name - Span to the end of the frame
        # Create combobox for product_name
        self.product_name_label = tk.Label(self.frame_entries_of_treeview, text="Tên HH:")
        self.product_name_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        
        self.product_name_combobox = ttk.Combobox(self.frame_entries_of_treeview, values=self.product_names, state="normal")
        self.product_name_combobox.grid(row=0, column=3, columnspan=9 ,padx=5, pady=5, sticky="ew")
        self.product_name_combobox.bind("<<ComboboxSelected>>", self.on_product_name_selected)
        self.product_name_combobox.bind("<KeyRelease>", self.filter_product_names)

        # Row 1: unit
        # Create text widget for unit
        self.product_unit_label = tk.Label(self.frame_entries_of_treeview, text="Đvt:")
        self.product_unit_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.unit_text = tk.Text(self.frame_entries_of_treeview, height=1, width=20)
        self.unit_text.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Row 1: quantity
        # Create text widget for quantity - 01
        self.product_quantity_label = tk.Label(self.frame_entries_of_treeview, text="SL tồn:")
        self.product_quantity_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.quantity_text = tk.Text(self.frame_entries_of_treeview, height=1, width=20)
        self.quantity_text.grid(row=1, column=3, padx=5, pady=5, sticky="w")

        # Create text widget for quantity - 02
        self.product_quantity_reserved_label = tk.Label(self.frame_entries_of_treeview, text="SL giữ chỗ:")
        self.product_quantity_reserved_label.grid(row=1, column=4, padx=5, pady=5, sticky="w")

        self.quantity_reserved_text = tk.Text(self.frame_entries_of_treeview, height=1, width=20)
        self.quantity_reserved_text.grid(row=1, column=5, padx=5, pady=5, sticky="w")

        # Create text widget for quantity - 03
        self.product_available_reserved_label = tk.Label(self.frame_entries_of_treeview, text="SL khả dụng:")
        self.product_available_reserved_label.grid(row=1, column=6, padx=5, pady=5, sticky="w")

        self.quantity_available_text = tk.Text(self.frame_entries_of_treeview, height=1, width=20)
        self.quantity_available_text.grid(row=1, column=7, padx=5, pady=5, sticky="w")

        # Create text widget for quantity - 04
        self.product_required_label = tk.Label(self.frame_entries_of_treeview, text="SL yêu cầu:")
        self.product_required_label.grid(row=1, column=8, padx=5, pady=5, sticky="w")

        self.quantity_required_text = tk.Text(self.frame_entries_of_treeview, height=1, width=20)
        self.quantity_required_text.grid(row=1, column=9, padx=5, pady=5, sticky="w")

        # Row 2: note
        label_note = tk.Label(self.frame_entries_of_treeview, text=f"Ghi chú:")
        label_note.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        entry_note = tk.Text(self.frame_entries_of_treeview, height=4, wrap="word")
        entry_note.insert(tk.END, "")  # Set the default value
        entry_note.grid(row=2, column=1, rowspan=3, columnspan=9, padx=5, pady=5, sticky="ew")
        
        # Configure grid to stretch properly
        # Allow column to expand to fill the space
        self.frame_entries_of_treeview.grid_columnconfigure(3, weight=2)
        self.frame_entries_of_treeview.grid_columnconfigure(4, weight=2)
        self.frame_entries_of_treeview.grid_columnconfigure(5, weight=2)
        
    def f_add_elements_to_frame_test(self):
        # Load product data from JSON file
        self.products = self.load_products_data()
        
        """Add a button to toggle the height of frame_test"""
        toggle_button = tk.Button(self.frame_test, text="Toggle Height", command=self.toggle_height)
        toggle_button.place(relx=1.0, rely=0, anchor="ne", x=-10, y=10)

        # Extract product details for comboboxes
        self.product_ids_1 = [product["product_ID"] for product in self.products]
        self.product_names_1 = [product["product_name"] for product in self.products]

        # Create combobox for product_ID
        self.product_id_label_1 = tk.Label(self.frame_test, text="Product ID:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.product_id_combobox_1 = ttk.Combobox(self.frame_test, values=self.product_ids, state="normal")
        self.product_id_combobox_1.grid(row=0, column=1, padx=10, pady=5)
        self.product_id_combobox_1.bind("<<ComboboxSelected>>", self.on_product_id_selected)
        self.product_id_combobox_1.bind("<KeyRelease>", self.filter_product_ids)

        # Create combobox for product_name
        self.product_name_label_1 = tk.Label(self.frame_test, text="Product Name:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.product_name_combobox_1 = ttk.Combobox(self.frame_test, values=self.product_names, state="normal")
        self.product_name_combobox_1.grid(row=1, column=1, padx=10, pady=5)
        self.product_name_combobox_1.bind("<<ComboboxSelected>>", self.on_product_name_selected)
        self.product_name_combobox_1.bind("<KeyRelease>", self.filter_product_names)

        # Create text widget for unit
        self.product_unit_label_1 = tk.Label(self.frame_test, text="Unit:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.unit_text_1 = tk.Text(self.frame_test, height=1, width=20)
        self.unit_text_1.grid(row=2, column=1, padx=10, pady=5)

        # Create text widget for quantity
        self.product_quantity_label_1 = tk.Label(self.frame_test, text="Quantity:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.quantity_text_1 = tk.Text(self.frame_test, height=1, width=20)
        self.quantity_text_1.grid(row=3, column=1, padx=10, pady=5)
        
        # Store the widgets for later use (needed for toggling visibility)
        self.widgets = [
            self.product_id_combobox,
            self.product_name_combobox,
            self.unit_text,
            self.quantity_text,
            self.product_id_label,
            self.product_name_label,
            self.product_unit_label,
            self.product_quantity_label
        ]   
        
    def load_products_data(self):
        """Load product data from a JSON file."""
        file_path = os.path.join(os.path.dirname(__file__), "products.json")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data["products"]
        except Exception as e:
            print(f"Error loading products data: {e}")
            return []
        
    def filter_product_ids(self, event):
        """Filter the product IDs as you type, handling Vietnamese diacritics."""
        search_term = self.product_id_combobox.get().lower()
        filtered_ids = [product_id for product_id in self.product_ids if self.normalize(search_term) in self.normalize(product_id.lower())]
        self.product_id_combobox['values'] = filtered_ids
        self.product_id_combobox.set(search_term)  # Keep the current input

    def filter_product_names(self, event):
        """Filter the product names as you type, handling Vietnamese diacritics."""
        search_term = self.product_name_combobox.get().lower()
        filtered_names = [product_name for product_name in self.product_names if self.normalize(search_term) in self.normalize(product_name.lower())]
        self.product_name_combobox['values'] = filtered_names
        self.product_name_combobox.set(search_term)  # Keep the current input
        
    def normalize(self, text):
        """Normalize the text by removing diacritics to handle search without worrying about accents."""
        # Normalize the text to NFD (decomposed form), then remove diacritics (accents)
        return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    
    def on_product_id_selected(self, event):
        """Update product name, unit, and quantity when product ID is selected."""
        selected_id = self.product_id_combobox.get()
        for product in self.products:
            if product["product_ID"] == selected_id:
                # Update product_name, unit, and quantity
                self.product_name_combobox.set(product["product_name"])
                self.unit_text.delete(1.0, tk.END)
                self.unit_text.insert(tk.END, product["unit"])
                self.quantity_text.delete(1.0, tk.END)
                self.quantity_text.insert(tk.END, product["quantity"])
                break

    def on_product_name_selected(self, event):
        """Update product ID, unit, and quantity when product name is selected."""
        selected_name = self.product_name_combobox.get()
        for product in self.products:
            if product["product_name"] == selected_name:
                # Update product_ID, unit, and quantity
                self.product_id_combobox.set(product["product_ID"])
                self.unit_text.delete(1.0, tk.END)
                self.unit_text.insert(tk.END, product["unit"])
                self.quantity_text.delete(1.0, tk.END)
                self.quantity_text.insert(tk.END, product["quantity"])
                break
    
    def f_add_elements_to_buttons_frame(self):       # Create buttons for CRUD operations
        create_button = tk.Button(self.buttons_frame, text="Create", command=self.f_create_entry)
        create_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        update_button = tk.Button(self.buttons_frame, text="Update", command=self.f_update_entry)
        update_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        delete_button = tk.Button(self.buttons_frame, text="Delete", command=self.f_delete_entry)
        delete_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        refresh_button = tk.Button(self.buttons_frame, text="Refresh", command=self.f_clear_entries)
        refresh_button.pack(side="left", fill="both", expand=True, padx=10, pady=10)
    
    # =======================================================================================================================
    # CRUD Functions to interact with the Treeview
    def f_create_entry(self):
        # Get the values from the entry fields within frame_entries_of_treeview
        values = []
        for entry in self.frame_entries_of_treeview.winfo_children():
            if isinstance(entry, tk.Entry):  # Only get values from Entry widgets
                values.append(entry.get())
        
        # Check if all fields are filled
        if all(values):
            # Insert the values as a new row into the Treeview
            self.treeview.insert("", "end", values=values)
            
            # Clear the entry fields
            self.f_clear_entries()

            # Optional: Sort the Treeview after insertion (uncomment if needed)
            # self.f_sort_treeview()

        else:
            # Show a warning if any field is empty
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def f_update_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            # Get the values from the entry fields
            values = [entry.get() for entry in self.entries]
            if all(values):
                self.treeview.item(selected_item, values=values)
                self.f_clear_entries()
                # self.f_sort_treeview()  # Sort after deletion
            else:
                messagebox.showwarning("Input Error", "Please fill in all fields")
        else:
            messagebox.showwarning("Selection Error", "Please select an item to update")

    def f_delete_entry(self):
        selected_item = self.treeview.selection()
        if selected_item:
            self.treeview.delete(selected_item)
            # self.f_sort_treeview()  # Sort after deletion
        else:
            # If no row is selected, delete the last row
            all_items = self.treeview.get_children()
            if all_items:
                last_item = all_items[-1]  # Get the last item
                self.treeview.delete(last_item)
            else:
                messagebox.showwarning("No Rows", "There are no rows to delete.")

    def f_select_item(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            for i in range(10):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, values[i])
                
            # Update the label with the selected row's index
            row_index = self.treeview.index(selected_item)
            self.selected_row_label.config(text=f"Selected Row: {row_index + 1}")

    def f_clear_entries(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
            entry.insert(0, f"Field {self.entries.index(entry)+1}")  # Set default value

    def f_sort_treeview(self):
        # Get all items in the Treeview
        items = self.treeview.get_children()

        # Filter out items where the first column is not a valid integer
        sorted_items = sorted(
            items, 
            key=lambda item: (
                int(self.treeview.item(item, "values")[0]) 
                if self.f_is_int(self.treeview.item(item, "values")[0]) 
                else float('inf')  # Assign a large number to non-numeric values
            )
        )
        
        # Clear all items in the Treeview
        for item in items:
            self.treeview.delete(item)

        # Insert the sorted items back into the Treeview
        for item in sorted_items:
            values = self.treeview.item(item, "values")
            self.treeview.insert("", "end", values=values)
    
    def f_is_int(self, value):
        try:
            int(value)  # Try to convert to an integer
            return True
        except ValueError:
            return False  # Return False if it fails
        
    def f_refresh_window(self):
        """Refresh the window by clearing the Treeview and entry fields"""
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        self.f_clear_entries()
        self.selected_row_label.config(text="Selected Row: 0")
        
    def f_add_elements_to_treeview_frame(self):
        self.columns = [f"Column {i+1}" for i in range(10)]
        print(self.columns)
        
        # # Load table configuration from JSON
        # # columns, scrollbars, general_settings = self.controller.get_table_config()
        # columns, scrollbars, general_settings = controller.get_table_config()
        # print(columns)
        
        # Create the Treeview
        self.treeview = ttk.Treeview(self.treeview_frame, columns=self.columns, show="headings", height=10)
        self.treeview.pack(fill="x", padx=10, pady=5)

        # Create headings for the Treeview columns
        self.treeview.heading(self.columns[0], text="STT")  # Set the first column header to "STT"
        for col in self.columns[1:]:
            self.treeview.heading(col, text=col)

        # Create headings for the Treeview columns
        for col in self.columns:
            self.treeview.heading(col, text=col)
            
        # Set column widths (optional)
        for i in range(10):
            self.treeview.column(self.columns[i], width=150)  # Adjust width as needed

        # Bind selection event to fill entries with the selected row's values
        self.treeview.bind("<ButtonRelease-1>", self.f_select_item)

        # Add a horizontal scrollbar
        self.h_scrollbar = tk.Scrollbar(self.treeview_frame, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=self.h_scrollbar.set)
        self.h_scrollbar.pack(fill="x", side="bottom", padx=10, pady=5)
        
        # Add a label to display selected row information
        self.selected_row_label = tk.Label(self.treeview_frame, text="Selected Row: 0", width=100)
        self.selected_row_label.pack(fill="x", side="bottom", padx=10, pady=5)

    def f_update_scroll_region(self):
        """Update the scroll region of the canvas to match the size of its content"""
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        # Ensure frame is at the top-left corner
        self.canvas.coords(self.canvas_window, 0, 0)
        
    def toggle_height(self):
        # Check current height of the frame
        current_height = self.frame_test.winfo_height()
        
        # If the height is collapsed (10px), expand it to the original height
        if current_height == 10:
            self.frame_test.config(height=200)  # You can adjust this height as needed
            # Show the widgets
            for widget in self.widgets:
                widget.grid()
        else:
            # Collapse the frame to 10px height
            self.frame_test.config(height=10)
            # Hide the widgets by calling grid_forget
            for widget in self.widgets:
                widget.grid_forget()
                
        print(self.frame_test.winfo_height())