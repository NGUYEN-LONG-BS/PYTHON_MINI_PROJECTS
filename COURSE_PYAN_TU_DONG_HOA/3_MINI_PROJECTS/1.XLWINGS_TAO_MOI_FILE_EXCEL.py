import xlwings as xw

# Create workbook
wb = xw.Book()

# Save workbook
wb.save(r"C:\Users\QuanN\OneDrive\Desktop\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\3_MINI_PROJECTS\sample.xlsx")

# close workbook
wb.close()