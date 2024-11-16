#===============================================================================================================
#========= Khai báo đường dẫn trực tiếp
#===============================================================================================================

# cách 1: sử dụng r
path_01 = r"C:\Users\ADMIN\Desktop"
# cách 2: sử dụng \\
path_02 = "C:\\Users\\ADMIN\\Desktop"

Excel_File_name = "Book1.xlsm"

Full_Name_01 = path_01 + "\\" + Excel_File_name
Full_Name_02 = path_02 + "\\" + Excel_File_name
print(Full_Name_01)
print(Full_Name_02)

import xlwings as xl

# Cách 1: Mở file Excel bằng biến
xl.Book(Full_Name_01)
xl.Book(Full_Name_02)
# Cách 2: Mở file Excel bằng đường dẫn tuyệt đối
xl.Book(r"C:\Users\ADMIN\Desktop\Book1.xlsm")

#===============================================================================================================
#========= Thao tác với tệp
#===============================================================================================================

# Kiểm tra sự tồn tại của Tệp
import os

file_path = r"C:\Users\ADMIN\Desktop\Book1.xlsm"

if os.path.exists(file_path):
    print(f'{file_path} tồn tại.')
else:
    print(f'{file_path} không tồn tại.')
    
#===============================================================================================================
#========= Thao tác với Thư mục
#===============================================================================================================

# Tạo Thư mục mới
new_directory = r"C:\Users\ADMIN\Desktop\Thư mục mới"
os.mkdir(new_directory)
print(f'{new_directory} đã được tạo.')

# Lấy thư mục làm việc hiện tại
current_directory = os.getcwd()
print(f'Thư mục làm việc hiện tại: {current_directory}')

# Di chuyển Thư mục
target_directory = r"C:\Users\ADMIN\Desktop"
os.chdir(target_directory)
print(f'Thư mục làm việc đã được chuyển đến {target_directory}.')

# Xóa Thư mục
os.rmdir(target_directory)
print(f'{target_directory} đã được xóa.')

#===============================================================================================================
#========= Thao tác với Đường dẫn
#===============================================================================================================

# Lấy Đường dẫn Tuyệt đối của file đang thực thi lệnh
script_path = os.path.abspath(__file__)
print(f'Đường dẫn tuyệt đối của script: {script_path}')

# Kết hợp Đường dẫn
new_path = os.path.join(r"C:\Users\ADMIN\Desktop", 'subfolder', 'file.txt')
print(f'Đường dẫn mới: {new_path}')