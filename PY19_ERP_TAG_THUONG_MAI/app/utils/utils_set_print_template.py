import os
import xlsxwriter

def calculate_start_column(start_column: str, left_shape_width: int) -> str:
    """
    Calculate the column where the right shape should start based on the width of the left shape.

    :param start_column: The starting column of the left shape (e.g., 'A').
    :param left_shape_width: The width of the left shape in pixels.
    :return: The column where the right shape should start (e.g., 'G').
    """
    import string

    # Approximate width of one Excel column in pixels (default scaling)
    pixels_per_column = 64

    # Convert the starting column letter to a number (e.g., 'A' -> 1, 'B' -> 2)
    start_column_index = string.ascii_uppercase.index(start_column.upper()) + 1

    # Calculate the number of columns covered by the left shape
    columns_covered = left_shape_width / pixels_per_column

    # Determine the starting column for the right shape
    right_shape_start_index = int(start_column_index + columns_covered)

    # Convert the column number back to a letter
    column_letter = ""
    while right_shape_start_index > 0:
        right_shape_start_index, remainder = divmod(right_shape_start_index - 1, 26)
        column_letter = string.ascii_uppercase[remainder] + column_letter

    return column_letter

def set_print_area_width(workbook, worksheet, header_shape_width: int):
    """
    Set the print area width to match the width of the first header shape.

    :param workbook: The xlsxwriter Workbook object.
    :param worksheet: The xlsxwriter Worksheet object.
    :param header_shape_width: The width of the header shape in pixels.
    """
    # Approximate width of one Excel column in pixels (default scaling)
    pixels_per_column = 64

    # Calculate the number of columns covered by the header shape
    columns_covered = header_shape_width / pixels_per_column

    # Convert to the nearest whole column count
    total_columns = int(columns_covered)

    # Define the print area from A1 to the calculated column
    end_column = ""
    while total_columns > 0:
        total_columns, remainder = divmod(total_columns - 1, 26)
        end_column = chr(65 + remainder) + end_column

    # Set the print area
    worksheet.print_area(0, 0, 0, ord(end_column.upper()) - 65)
    
def create_workbook_with_unique_name(base_name="Print_Template.xlsx"):
    """
    Creates a new Excel workbook with a unique name if a file with the base name already exists.

    Parameters:
    base_name (str): The desired base name for the file.

    Returns:
    str: The name of the created workbook file.
    """
    file_name = base_name
    base_name_no_ext = os.path.splitext(base_name)[0]
    extension = os.path.splitext(base_name)[1]
    counter = 1

    # Check if file already exists, generate a new name if necessary
    while os.path.exists(file_name):
        file_name = f"{base_name_no_ext}_{counter}{extension}"
        counter += 1

    # Create the workbook
    workbook = xlsxwriter.Workbook(file_name)
    # worksheet = workbook.add_worksheet("Template")
    
    # Add content or configurations here as needed
    # worksheet.write("A1", "This is a new workbook.")
    
    # # Close workbook
    # workbook.close()

    return workbook, file_name

# Example usage:
left_shape_width = 64 * 5  # Width in pixels
start_column = "A"      # Left shape starts at column A
right_shape_start_column = calculate_start_column(start_column, left_shape_width)
print(f"Right shape should start at column: {right_shape_start_column}")


# Create a new workbook and add a worksheet
workbook, file_name = create_workbook_with_unique_name()
# workbook = xlsxwriter.Workbook("Excel_Template_with_Shapes.xlsx")
worksheet = workbook.add_worksheet("Print_sh")

# Set height of Row 1
row_1_height_in_points = 100
header_shape_height_in_pixels = int(row_1_height_in_points * 1.33)
worksheet.set_row(0, row_1_height_in_points)

# Set height of Row 2
row_2_height_in_points = 200
second_row_shape_height_in_pixels = int(row_2_height_in_points * 1.33)
worksheet.set_row(1, row_2_height_in_points)

# Set height of Row 16
row_16_height_in_points = 100
third_row_shape_height_in_pixels = int(row_16_height_in_points * 1.33)
worksheet.set_row(15, row_16_height_in_points)

# Add first shape (A1:F1)
worksheet.insert_textbox('A1', 'First Shape', {
    'width': 64*10,
    'height': header_shape_height_in_pixels,
    'align': {'vertical': 'middle', 'horizontal': 'center'},
    'font': {'bold': True, 'size': 14},
    'fill': {'color': '#FFFFFF'},
    'line': {'color': '#000000'}
})

# Second shape on the left (A2:C2)
second_shape_on_the_left = """
Mã khách hàng: [__________]
Tên khách hàng: [__________]
Địa chỉ: [__________]
Số điện thoại: [__________]
"""
worksheet.insert_textbox('A2', second_shape_on_the_left, {
    'width': 400,  # Half of 800
    'height': second_row_shape_height_in_pixels,  # Same height for both shapes
    'align': {'vertical': 'middle', 'horizontal': 'left'},
    'font': {'size': 12},
    'fill': {'color': '#FFFFFF'},
    'line': {'color': '#000000'}
})

# Second shape on the right (D2:F2)
second_shape_on_the_right = """
Số phiếu: [__________]
Số hợp đồng: [__________]
"""
column_start_right_shape = calculate_start_column("A",400)
worksheet.insert_textbox(column_start_right_shape + '2', second_shape_on_the_right, {
    'width': 64*3,
    'height': second_row_shape_height_in_pixels,  # Same height for both shapes
    'align': {'vertical': 'middle', 'horizontal': 'left'},
    'font': {'size': 12},
    'fill': {'color': '#FFFFFF'},
    'line': {'color': '#000000'}
})

# Add a table from A3:F15
columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5', 'Column 6']
data = [
    ['Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5', 'Data 6'] for _ in range(13)
]

worksheet.add_table('A3:F15', {
    'columns': [{'header': col} for col in columns],
    'data': data,
    'style': 'Table Style Medium 9'
})

# Add third shape (A16:F16)
worksheet.insert_textbox('A16', 'Third Shape', {
    'width': 64*8,
    'height': third_row_shape_height_in_pixels,
    'align': {'vertical': 'middle', 'horizontal': 'center'},
    'font': {'bold': True, 'size': 14},
    'fill': {'color': '#FFFFFF'},
    'line': {'color': '#000000'}
})

# Example usage
margins = {
    'top': 1.0,    # 1 inch
    'left': 0.5,   # 0.5 inch
    'right': 0.5,  # 0.5 inch
    'bottom': 1.0  # 1 inch
}

# Set the print margins
worksheet.set_margins(
    left=margins.get('left', 0.7),     # Default left margin is 0.7 inches
    right=margins.get('right', 0.7),  # Default right margin is 0.7 inches
    top=margins.get('top', 0.75),     # Default top margin is 0.75 inches
    bottom=margins.get('bottom', 0.75)  # Default bottom margin is 0.75 inches
)

# Close the workbook
workbook.close()

print("Excel file created: Excel_Template_with_Shapes.xlsx")
