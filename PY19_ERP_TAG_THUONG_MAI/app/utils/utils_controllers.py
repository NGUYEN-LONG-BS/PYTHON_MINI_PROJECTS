
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
            root.is_maximized = True  # Set the flag to track maximized state
            root.bind("<Configure>", utils_controller_set_size_of_windown_250215_10h24.on_resize)  # Bind the resize event
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

    def on_resize(event):
        """Called when the window is resized, adjusts the window to 75% of the screen if maximized."""
        if isinstance(event.widget, tk.Tk):  # Ensure we're working with the root window
            root = event.widget
            
            # Only apply the resizing logic if the window was maximized
            if getattr(root, 'is_maximized', False):  # Check if window was maximized
                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()

                # Calculate 75% of screen dimensions
                ratio = 0.75
                new_width = int(screen_width * ratio)
                new_height = int(screen_height * ratio)

                current_width = root.winfo_width()
                current_height = root.winfo_height()

                # Only update the window size if it's different from the current size
                if current_width != new_width or current_height != new_height:
                    root.geometry(f"{new_width}x{new_height}")
                    root.is_maximized = False
            else:
                # If the window is not maximized, do nothing
                pass
            
            if root.winfo_width() < 900 or root.winfo_height() < 500:
                root.geometry("900x500")
            