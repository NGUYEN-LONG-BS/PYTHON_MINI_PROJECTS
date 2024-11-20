import os

# in hàm walk ra để kiểm tra
print(os.walk(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER"))

# ép hàm walk về kiểu list
print(list(os.walk(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER")))

# [('C:\\Users\\ADMIN\\Desktop\\ICONS\\GITHUB\\PYTHON_MINI_PROJECTS\\PY14_PYAN_TU_DONG_HOA\\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER', ['Folder01', 'Folder02', 'folder03_delete', 'Ham_walk'], ['1.thuvien_OS.py', '2.lam_viec_voi_file_txt.py', '3.copy_va_duy_chuyen_file.py', '4.xoa_File.py', '5.ham_walk.py', 'test.txt']),
# ('C:\\Users\\ADMIN\\Desktop\\ICONS\\GITHUB\\PYTHON_MINI_PROJECTS\\PY14_PYAN_TU_DONG_HOA\\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\\Folder01', [], ['a.txt', 'c.txt']), 
# ('C:\\Users\\ADMIN\\Desktop\\ICONS\\GITHUB\\PYTHON_MINI_PROJECTS\\PY14_PYAN_TU_DONG_HOA\\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\\Folder02', [], ['b.txt']), 
# ('C:\\Users\\ADMIN\\Desktop\\ICONS\\GITHUB\\PYTHON_MINI_PROJECTS\\PY14_PYAN_TU_DONG_HOA\\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\\folder03_delete', [], ['b copy 2.txt', 'b copy 3.txt', 'b copy.txt', 'b.txt']), 
# ('C:\\Users\\ADMIN\\Desktop\\ICONS\\GITHUB\\PYTHON_MINI_PROJECTS\\PY14_PYAN_TU_DONG_HOA\\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER\\Ham_walk', [], [])]

for FolderName, SubFolderNames, FileNames in os.walk(r"C:\Users\ADMIN\Desktop\ICONS\GITHUB\PYTHON_MINI_PROJECTS\PY14_PYAN_TU_DONG_HOA\6_os_LAM_VIEC_VOI_FILE_VA_FOLDER"):
    print("============================")
    print("Folder cha tên là " + FolderName)
    print("Các folder con nằm trong folder cha " + FolderName + " là " + str(SubFolderNames))
    print("Các file nằm trong folder cha " + FolderName + " là " + str(FileNames))
    print("============================")