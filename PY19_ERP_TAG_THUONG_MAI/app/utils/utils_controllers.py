
from .utils_models import *
from utils import *
import traceback
from datetime import datetime

import os
import sys
import time
import inspect
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import filedialog, messagebox
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl import load_workbook
import xlwings as xw
from define import *
import pyodbc
import json
from cryptography.fernet import Fernet
# import datetime
from datetime import datetime
from decimal import Decimal
from PIL import Image, ImageTk
import pandas as pd
import re

class utils_controller_action_after_event_250216_14h57:
    
    def f_get_the_latest_number_of_slip(entry_so_phieu, ma_thanh_vien, loai_phieu):
        # Get the latest number of slip
        so_phieu = utils_controller_get_the_latest_number_of_slip.handle_button_get_number_of_slip_click()
        
        # Create the connection string
        connection_number_of_slip = f"{ma_thanh_vien}-{loai_phieu}-{so_phieu + 1}"
        
        # Config the entry_so_phieu
        entry_so_phieu.config(state="normal")
        entry_so_phieu.delete(0, tk.END)
        entry_so_phieu.insert(0, connection_number_of_slip)
        entry_so_phieu.config(state="readonly")

    def update_entry_id_after_adding_new_row(tree, entry_id):
        row_count = 1 + len(tree.get_children())    
        entry_id.config(state="normal")  # Enable the Entry widget to update the value
        entry_id.delete(0, tk.END)  # Clear the existing value
        entry_id.insert(0, row_count)  # Insert the new value (ID)
        entry_id.config(state="disabled")  # Disable the Entry widget again

class utils_controller_config_notification_250220_10h05:
    def f_config_notification(element_label, text="...", fg="blue"):
            element_label.config(text=text, fg=fg)

class utils_controller_get_the_latest_number_of_slip:
    
    def get_list_number_of_slip(database_name, table_name, slip_column_name):
        # Tạo câu query SQL với danh sách số phiếu
        query = f"""
        SELECT DISTINCT
            {slip_column_name}
        FROM [{database_name}].[dbo].[{table_name}]
        WHERE [XOA_SUA] = ''
        """
        # print("query", query)
        
        # lấy danh sách số phiếu từ SQL
        danh_sach_so_phieu = utils_model_get_data_from_SQL.get_data_with_query(query)
        # print("danh_sach_so_phieu", danh_sach_so_phieu)
        
        return danh_sach_so_phieu
        
    def extract_numbers_from_data_SQL_num_01(data):
        data_01 = data
        data_02 = tuple(int(item[0].split('-')[-1]) for item in data_01)
        if not data_02:
            current_year = str(datetime.now().year)[-2:]  # Lấy 2 số cuối của năm hiện tại
            data_final = int(f'{current_year}0000')
        else:
            data_final = max(data_02)
        return data_final
        
    def handle_button_get_number_of_slip_click(database_name, table_name):
        # Lấy danh sách số phiếu từ SQL
        data_01 = utils_controller_get_the_latest_number_of_slip.get_list_number_of_slip(database_name, table_name)
        # Lấy số phiếu cuối cùng
        data_02 = utils_controller_get_the_latest_number_of_slip.extract_numbers_from_data_SQL_num_01(data_01)
        
        return data_02
                
class utils_controller_set_size_of_windown_250215_10h24:    
    def f_utils_set_window_size_of_new_view(root, width=0, height=0, maximize=False):
        """Set the window size to 4/5 of the screen size or maximize it."""
        if maximize:
            root.state('zoomed')  # Maximizes the window (Windows)
            # root.is_maximized = True  # Set the flag to track maximized state
            # root.bind("<Configure>", utils_controller_set_size_of_windown_250215_10h24.on_resize)  # Bind the resize event
            return

        if width == 0 or height == 0:
            # Get screen dimensions
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            
            # Calculate 4/5 of screen dimensions
            ratio = 0.75
            height = int(screen_height * ratio)
            width = int(screen_width * ratio)
        
        # Set the window size
        root.geometry(f"{width}x{height}")

    # def on_resize(event):
    #     """Called when the window is resized, adjusts the window to 75% of the screen if maximized."""
    #     if isinstance(event.widget, tk.Tk):  # Ensure we're working with the root window
    #         root = event.widget
            
    #         # # Only apply the resizing logic if the window was maximized
    #         # if getattr(root, 'is_maximized', False):  # Check if window was maximized
    #         #     screen_width = root.winfo_screenwidth()
    #         #     screen_height = root.winfo_screenheight()

    #         #     # Calculate 75% of screen dimensions
    #         #     ratio = 0.75
    #         #     new_width = int(screen_width * ratio)
    #         #     new_height = int(screen_height * ratio)

    #         #     current_width = root.winfo_width()
    #         #     current_height = root.winfo_height()

    #         #     # Only update the window size if it's different from the current size
    #         #     if current_width != new_width or current_height != new_height:
    #         #         root.geometry(f"{new_width}x{new_height}")
    #         #         root.is_maximized = False
    #         # else:
    #         #     # If the window is not maximized, do nothing
    #         #     pass
            
    #         if root.winfo_width() < 1000 or root.winfo_height() < 750:
    #             root.geometry("1000x750")
            
class utils_controller_TreeviewConfigurator_250217_13h20:
    """Class để áp dụng cấu hình cho Treeview"""

    @staticmethod
    def apply_treeview_config(my_treeview, config_json_path):
        """Cấu hình Treeview dựa trên JSON"""
        
        # Xóa các cột hiện tại
        my_treeview.delete(*my_treeview.get_children())
        for col in my_treeview["columns"]:
            my_treeview.heading(col, text="")  # Xóa tiêu đề

        # Load dữ liệu từ JSON
        data = utils_model_TreeviewConfigLoader_250217_13h20.load_json(config_json_path)
        if not data:
            return
        
        columns_config, column_names = utils_model_TreeviewConfigLoader_250217_13h20.get_column_config(data)
        my_treeview["columns"] = column_names

        # Lấy cấu hình font header
        header_font = utils_model_TreeviewConfigLoader_250217_13h20.get_header_font(data)

        # Cấu hình cột
        for config, col in zip(columns_config, column_names):
            my_treeview.heading(col, text=col)
            my_treeview.column(
                col,
                width=config.get("width", 100),
                minwidth=config.get("min_width", 50),
                anchor=config.get("anchor", "w"),
                stretch=config.get("stretch", True)
            )

        # Cấu hình font tiêu đề
        style = ttk.Style()
        style.configure("Treeview.Heading", font=header_font)

        # print("Treeview đã được cấu hình thành công từ JSON.")

class utils_controller_TreeviewHandler_click_250217_22h34:

    def treeview_single_click(my_Treeview):
        selected_item = my_Treeview.selection()
        if selected_item:
            row_values = my_Treeview.item(selected_item[0], "values")
            result_tuple = tuple(row_values) if row_values else None
            # print(result_tuple)
            return result_tuple
        return None

    def treeview_double_click(my_Treeview, column_return):
        selected_item = my_Treeview.selection()
        if selected_item:
            row_values = my_Treeview.item(selected_item[0], "values")
            return row_values[column_return] if len(row_values) > column_return else None
        return None