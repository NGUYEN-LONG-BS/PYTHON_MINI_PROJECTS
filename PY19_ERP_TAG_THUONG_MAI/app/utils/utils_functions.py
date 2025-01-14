import os
import sys
import time
import inspect

import tkinter as tk
from tkinter import font
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl import load_workbook

import xlwings as xw

from define import *


def f_utils_setup_logo(parent_frame):
    # Define function when click
    def on_logo_click(event):
        # Get the top-level window containing the parent_frame
        parent_window = parent_frame.winfo_toplevel()
        parent_window.destroy()  # Close the parent window
        # Open Dashboard
        from views.AD01_Dashboard_View.Dashboard_View import cls_Dashboard_View
        cls_Dashboard_View()
        
    try:
        # Try loading the light mode image first
        logo_image_light = Image.open(PATH_LOGO_LIGHT)
        logo_image_dark = Image.open(PATH_LOGO_DARK)
        
        # Convert the PIL image to a Tkinter-compatible photo image
        logo_image_light_tk = ImageTk.PhotoImage(logo_image_light)
        logo_image_dark_tk = ImageTk.PhotoImage(logo_image_dark)
        
        # Store the image as an attribute of the parent_frame (to prevent it from being garbage collected)
        parent_frame.logo_image_light = logo_image_light_tk
        parent_frame.logo_image_dark = logo_image_dark_tk
        
        # Create the tk.Label and display the image
        logo_label = tk.Label(parent_frame, image=logo_image_light_tk)
        logo_label.pack(fill="both", expand=True) # Using pack to add it to the parent_frame
        logo_label.bind("<Button-1>", on_logo_click)  # Button-1 is left mouse click
    except FileNotFoundError:
        print(f"Logo file not found at {logo_image_light} or {logo_image_dark}")
        error_label = tk.Label(parent_frame, text="Logo not found", font=("", 16))
        error_label.pack(fill="both", expand=True)
        error_label.bind("<Button-1>", on_logo_click)  # Button-1 is left mouse click

def f_utils_setup_fav_icon(window):
        # Get the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Going 2 levels up
        
        # Load the logo images
        fav_icon = os.path.join(project_root, "assets/icons/favicon.png")
        
        img = Image.open(fav_icon)  # Replace with the path to your image file
        logo = ImageTk.PhotoImage(img)
        # Set the window icon
        window.iconphoto(False, logo)

def f_utils_find_my_function_path(function_name):
    source_file = inspect.getfile(function_name)
    print(f"Function is defined in: {source_file}")

def set_window_size(root, width=1600, height=900):
    # Thiết lập kích thước cửa sổ
    root.geometry(f"{width}x{height}")
    
    # Đảm bảo cửa sổ không thể thay đổi kích thước
    root.resizable(False, False)
    
    # Nếu bạn muốn căn giữa cửa sổ, bạn có thể tính toán vị trí và đặt lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)
    print(f"Position Right: {position_right}, Position Top: {position_top}")
    
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

def f_utils_set_window_size_is_4_per_5_screen(root, width=0, height=0):
    """Set the window size to 4/5 of the screen size."""
    if width == 0 or height == 0:
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Calculate 4/5 of screen dimensions
        height = int(screen_height * 4 / 5)
        width = int(screen_width * 4 / 5)
    
    # Set the window size
    root.geometry(f"{width}x{height}")

def f_utils_set_center_screen(root):
    # Lấy kích thước của cửa sổ
    root.update_idletasks()  # Cập nhật các thay đổi về kích thước
    width = root.winfo_width()
    height = root.winfo_height()
    
    # lấy thông tin kích thước màn hình và tinh toán lại
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Tính toán vị trí để căn giữa cửa sổ
    position_top = int(screen_height / 2 - height / 2) - 50
    position_right = int(screen_width / 2 - width / 2)

    # Đặt lại vị trí của cửa sổ
    root.geometry(f'{width}x{height}+{position_right}+{position_top}')

# Reusable function to set font for menu items
def f_utils_set_menu_font(widget, size=14, font_is="Arial"):
    """Set the font for menu items to a specified size."""
    custom_font = font.Font(family=font_is, size=size)  # Create a new Font object with the desired size
    widget.config(font=custom_font)  # Apply the font to the menu

def f_utils_open_dashboard():
    from views.AD01_Dashboard_View.Dashboard_View import cls_Dashboard_View
    new_view = cls_Dashboard_View()
    f_utils_set_window_size_is_4_per_5_screen(new_view)
    f_utils_set_center_screen(new_view)
    new_view.focus_force()
    
def f_utils_show_fading_popup(message):
    # Tạo cửa sổ popup
    popup = tk.Toplevel()
    popup.title("Thông báo")
    # Set background color of popup window
    popup.config(bg=BG_COLOR_0_0)
    # Ẩn thanh tiêu đề (title bar)
    popup.overrideredirect(True)
    # Căn giữa màn hình
    f_utils_set_window_size_is_4_per_5_screen(popup, 150, 50)
    f_utils_set_center_screen(popup)
    
    # Add frame
    main_frame = tk.Frame(popup, width=popup.winfo_width(), height=popup.winfo_height(), bd=1, relief="solid")
    # main_frame.grid(row=0, column=0)
    main_frame.pack()

    # Tạo nhãn để hiển thị thông báo
    label = tk.Label(main_frame, text=message, font=("Helvetica", 12))
    label.pack(pady=10, padx=10)

    # Đặt thời gian để tự động đóng cửa sổ sau 3 giây (3000 milliseconds)
    popup.after(1000, popup.destroy)

def f_utils_tim_component_label_with_text(root=None, text_to_find=""):
    if root is None:  # Start from self if root is not provided
        # root = self
        return
    
    # Loop through all children of the current root
    for widget in root.winfo_children():
        # Check if widget is a Label and its text matches
        if isinstance(widget, tk.Label) and widget.cget("text") == text_to_find:
            return widget  # Found the Label, return it

        # If widget has children, recursively search in its children
        result = f_utils_tim_component_label_with_text(widget, text_to_find)
        if result:
            return result
    return None  # No matching Label found

def f_utils_open_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select a File")
    file_name = os.path.basename(file_path)
    if file_path:
        # Check if the file is an Excel file
        if file_path.endswith(('.xls', '.xlsx')):
            return file_name
        else:
            return file_name

def f_utils_create_template_excel_file(file_name="template_wb.xlsx",sheet_name="template_sh",column_names=["Col1", "Col2", "Col3"]):
    # Open a file dialog to select the save location
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        initialdir=desktop_path,
        initialfile=file_name,
        filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
        title="Save Excel File"
    )
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Create a new Excel workbook and sheet
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = sheet_name

    # Write column names to the first row
    for col_num, column_name in enumerate(column_names, start=1):
        cell = sheet.cell(row=1, column=col_num, value=column_name)
        # Apply formatting to the header row
        cell.font = Font(bold=True, color="FFFFFF")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        sheet.column_dimensions[cell.column_letter].width = 15  # Adjust column width

    # Set background color for the header row
    for cell in sheet[1]:
        cell.fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")

    # Save the workbook
    workbook.save(file_path)
    return f"Excel file created and saved to: {file_path}"

def f_utils_find_string_in_row_of_excel(file_path, sheet_name, target_string, row_number=1, case_sensitive=True, return_as_index=True):
    """
    Find a string in a specified row of an Excel sheet.
    
    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to search.
        target_string (str): String to search for.
        row_number (int): Row number to search in (default is 1).
        case_sensitive (bool): Whether the search should be case-sensitive (default is True).
        return_as_index (bool): Whether to return the column index (True) or column name (False).
    
    Returns:
        int or str: Column index or name where the string is found. Returns None if not found.
    """
    try:
        # Load the workbook and sheet
        workbook = openpyxl.load_workbook(file_path)
        if sheet_name not in workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' does not exist in the workbook.")
        sheet = workbook[sheet_name]

        # Check for valid row number
        if row_number < 1 or row_number > sheet.max_row:
            raise ValueError(f"Invalid row number: {row_number}. It must be between 1 and {sheet.max_row}.")

        # Iterate through columns in the specified row
        for col in sheet.iter_cols(1, sheet.max_column):
            cell = col[row_number - 1]  # Row numbers are 1-based
            if cell.value is not None:
                cell_value = str(cell.value)
                if not case_sensitive:
                    if cell_value.lower() == target_string.lower():
                        return cell.column if return_as_index else cell.column_letter
                else:
                    if cell_value == target_string:
                        return cell.column if return_as_index else cell.column_letter
        
        return None  # String not found
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def f_utils_find_string_in_column_of_excel(file_path, sheet_name, target_string, column_number=1, case_sensitive=True, return_as_index=True):
    """
    Find a string in a specified column of an Excel sheet.
    
    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to search.
        target_string (str): String to search for.
        column_number (int): Column number to search in (default is 1).
        case_sensitive (bool): Whether the search should be case-sensitive (default is True).
        return_as_index (bool): Whether to return the row index (True) or cell reference (False).
    
    Returns:
        int or str: Row index or cell reference where the string is found. Returns None if not found.
    """
    try:
        # Load the workbook and sheet
        workbook = openpyxl.load_workbook(file_path)
        if sheet_name not in workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' does not exist in the workbook.")
        sheet = workbook[sheet_name]

        # Check for valid column number
        if column_number < 1 or column_number > sheet.max_column:
            raise ValueError(f"Invalid column number: {column_number}. It must be between 1 and {sheet.max_column}.")

        # Iterate through rows in the specified column
        for row in sheet.iter_rows(1, sheet.max_row):
            cell = row[column_number - 1]  # Column numbers are 1-based
            if cell.value is not None:
                cell_value = str(cell.value)
                if not case_sensitive:
                    if cell_value.lower() == target_string.lower():
                        return cell.row if return_as_index else f"{cell.column_letter}{cell.row}"
                else:
                    if cell_value == target_string:
                        return cell.row if return_as_index else f"{cell.column_letter}{cell.row}"
        
        return None  # String not found
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def f_utils_copy_sheet_to_new_workbook(file_path, sheet_name):
    try:
        # Start a new Excel instance
        app = xw.App(visible=False, add_book=False)  # Start a new Excel process
        app.display_alerts = False  # Suppress Excel alerts
        # app.screen_updating = False  # Speed up operations

        # Open the workbook
        wb = app.books.open(file_path)

        # Check if the "PRINT" sheet exists
        if sheet_name in [sheet.name for sheet in wb.sheets]:
            print_sheet = wb.sheets[sheet_name]

            # Create a new workbook
            new_wb = xw.Book()

            # Copy the "PRINT" sheet to the new workbook
            print_sheet.api.Copy(Before=new_wb.sheets[0].api)
            print("Sheet {sheet_name} copied successfully.")
            
            # Make the new workbook visible to the user
            new_wb.app.visible = True
            print("New workbook opened for user.")

            # Maximize the new workbook window
            new_wb.app.api.WindowState = -4137  # -4137 corresponds to the "maximized" state
            print("New workbook maximized and opened for user.")
        else:
            print("Sheet 'PRINT' does not exist in the workbook.")

        # Close the original workbook
        wb.close()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Ensure the Excel application started by this code is closed
        if not app.books:  # If no books are left open, quit the app
            app.quit()

def f_utils_delete_extend_row_and_column(file_path, sheet_name, start_column, end_column, start_row, last_row):
    """
    Delete rows and columns in an Excel sheet based on specified ranges.

    Parameters:
        file_path (str): Path to the Excel file.
        sheet_name (str): Name of the sheet to modify.
        start_column (int): Start column index to delete before.
        end_column (int): End column index to delete after.
        start_row (int): Start row index to delete before.
        last_row (int): Last row index to delete after.

    Returns:
        None: The function modifies the Excel file in place.
    """
    try:
        # Load the workbook and sheet
        workbook = openpyxl.load_workbook(file_path)
        if sheet_name not in workbook.sheetnames:
            raise ValueError(f"Sheet '{sheet_name}' does not exist in the workbook.")
        sheet = workbook[sheet_name]

        # Delete rows above start_row (if applicable)
        if start_row > 1:
            sheet.delete_rows(1, start_row - 1)

        # Delete rows below last_row (if applicable)
        if last_row < sheet.max_row:
            sheet.delete_rows(last_row + 1, sheet.max_row - last_row)

        # Delete columns to the left of start_column (if applicable)
        if start_column > 1:
            sheet.delete_cols(1, start_column - 1)

        # Delete columns to the right of end_column (if applicable)
        if end_column < sheet.max_column:
            sheet.delete_cols(end_column + 1, sheet.max_column - end_column)

        # Save the modified workbook
        workbook.save(file_path)
        print(f"Modifications completed successfully for '{sheet_name}' in file '{file_path}'.")

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

def f_utils_open_print_template(file_path, sheet_name):
    start_column = f_utils_find_string_in_row_of_excel(file_path, sheet_name, "FIRST_COLUMN", row_number=1, case_sensitive=True, return_as_index=True)
    end_column = f_utils_find_string_in_row_of_excel(file_path, sheet_name, "LAST_COLUMN", row_number=1, case_sensitive=True, return_as_index=True)
    value_column = f_utils_find_string_in_row_of_excel(file_path, sheet_name, "VALUE_COLUMN", row_number=1, case_sensitive=True, return_as_index=True)
    start_row = f_utils_find_string_in_column_of_excel(file_path, sheet_name, "FIRST_ROW", column_number=1, case_sensitive=True, return_as_index=True)
    last_row = f_utils_find_string_in_column_of_excel(file_path, sheet_name, "LAST_ROW", column_number=1, case_sensitive=True, return_as_index=True)
    
    f_utils_copy_sheet_to_new_workbook(file_path, sheet_name)
    f_utils_delete_extend_row_and_column(file_path, sheet_name, start_column, end_column, start_row, last_row)
    
    