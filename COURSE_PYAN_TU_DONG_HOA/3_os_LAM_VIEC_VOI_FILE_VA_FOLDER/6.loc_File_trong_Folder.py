import os

# liệt kê tất cả các folder và tệp trong đường link hiện hành
arr_01 = os.listdir()
arr_02 = os.listdir(r"D:\TUAN_AN_GROUP")
arr_03 = os.listdir(r"D:\TUAN_AN_GROUP\BAN_TAI_CHINH")

# print(arr_01)
# print(arr_02)
print(arr_03)

# lọc qua từng tên, in ra độ dài của tên
for index in arr_03:
    file_name, file_extention = os.path.splitext(index)
    if len(index) > 0 and file_extention == ".pdf":
        print(index)
        old_path = os.path.join(r"D:\TUAN_AN_GROUP\BAN_TAI_CHINH",index)
        File_name_order = 1
        new_path = os.path.join(r"D:\TUAN_AN_GROUP\BAN_TAI_CHINH",file_name + str(File_name_order) + file_extention)
        # os.remove(os.path.join(r"D:\TUAN_AN_GROUP\BAN_TAI_CHINH",index))          # Xoá các file được chọn
        os.rename(old_path, new_path)                                               # Đổi tên các file được chọn
        File_name_order += 1