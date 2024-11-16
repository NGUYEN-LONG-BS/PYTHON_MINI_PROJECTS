import os
import shutil

# # Sử dụng hàm unlink xoá file delete.txt trong folder02
os.unlink(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder02\delete.txt")

# # Sử dụng hàm unlink xoá file delete.txt trong folder02
os.remove(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder02\delete.txt")

# # Xoá nhiều file trong folder folder03_delete
folder = r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete"
for fileName in os.listdir(folder):
    filePath = os.path.join(folder, fileName)
    os.unlink(filePath)

# # Xoá tất cả các file có đuôi là .xlsx
folder = r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete"
for fileName in os.listdir(folder):
    filePath = os.path.join(folder, fileName)
    fileName, fileExtention = os.path.splitext(filePath)
    if fileExtention == ".xlsx":
        os.unlink(filePath)

# # Tạo một folder mới có tên folder_bi_xoa
os.mkdir(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete\folder_bi_xoa")
        
# # Xoá folder (folder bắt buộc phải trống)
os.rmdir(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete\folder_bi_xoa")

# # Xoá folder bất kỳ (Xoá luôn, không vào thùng rác)
shutil.rmtree(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete\folder_bi_xoa")

# Xoá folder bất kỳ (xoá an toàn - cho vào thùng rác)
# pip install send2trash
import send2trash
send2trash.send2trash(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\Folder03_delete\folder_bi_xoa")