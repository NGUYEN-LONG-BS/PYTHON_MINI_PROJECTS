# https://quantrimang.com/hoc/lam-viec-voi-file-trong-python-160073

# # Kiểm tra thư mục hiện hành đang làm việc là thư mục nào
# import os
# # Lấy thư mục làm việc hiện tại
# current_directory = os.getcwd()
# print(f'Thư mục làm việc hiện tại: {current_directory}')

# # Cú pháp mở và đóng file
# f = open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\test.txt", encoding='utf-8')
# f.close()

# # Mở file test.txt và ghi đè nội dung lên
# with open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\test.txt",'w',encoding = 'utf-8') as f:
#     f.write("Quantrimang\n") 
#     f.write("Kiến thức - Kinh nghiệm - Hỏi đáp\n\n") 
#     f.write("Quantrimang.com\n")

# # Đọc file test.txt
# f = open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\test.txt",'r',encoding = 'utf-8')
# a = f.read(12) # đọc 12 kí tự đầu tiên
# print('Nội dung 11 kí tự đầu là:\n', (a))
# b = f.read(35) # đọc 35 kí tự tiếp theo
# print('Nội dung 35 kí tự tiếp theo là:\n', (b))
# c = f.read() # đọc phần còn lại
# print('Nội dung phần còn lại là:\n', (c))

# Dùng tell() và seek()
f = open(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\test.txt",'r',encoding = 'utf-8')
a = f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung là: \n', (a))
b = f.tell() # Kiểm tra vị trí hiện tại
print ('Vị trí hiện tại: ', (b))
f.seek(0) # Đặt lại vị trí con trỏ tại vị trí đầu file
c = f.read()
print('Nội dung mới là: \n', (c))
f.close()