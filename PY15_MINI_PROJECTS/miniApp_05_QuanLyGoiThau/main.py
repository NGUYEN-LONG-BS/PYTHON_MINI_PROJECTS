import os

# Tạo mới folder cho gói thầu mới, số thông báo mời thầu: ABC1728
# Cấu trúc tên của folder: 24_GOI_THAU_0001_15234685

# Khai báo đường dẫn đến các gói thầu
PathQuanLyThau = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"
arr_DanhSachGoiThau = os.listdir(PathQuanLyThau)

print(arr_DanhSachGoiThau)

# Tạo mới folder theo tên có sẵn

# Tạo mới folder có tên "hhhhhhhh"
folder_name_01_year = "24"
folder_name_02 = "GOI_THAU"
folder_name_03_number = str(len(arr_DanhSachGoiThau) + 1).zfill(4)      # hiển thị 4 ký tự
folder_name_04 = "SoThongBaoMoiThau"
folder_name_completed = folder_name_01_year + "_" + folder_name_02 + "_" + folder_name_03_number + "_" + folder_name_04

new_folder_path = os.path.join(PathQuanLyThau, folder_name_completed)

# Kiểm tra nếu folder chưa tồn tại, thì tạo mới
def check_variable_in_array(array, variable):
    if variable in array:
        return True
    else:
        return False

result = check_variable_in_array(arr_DanhSachGoiThau, folder_name_completed)

if result:
    print(f"The string '{folder_name_completed}' exists in the array.")
else:
    print(f"The string '{folder_name_completed}' does not exist in the array.")
    os.makedirs(new_folder_path)
    print(f"Đã tạo folder: {new_folder_path}")

