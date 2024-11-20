import os
import sys
from customtkinter import *
from PIL import Image
from datetime import datetime

# ======================================================================================
# Mục đích
# Tạo mới folder cho gói thầu mới, số thông báo mời thầu: ABC1728
# Cấu trúc tên của folder: 24_GOI_THAU_0001_15234685
# ======================================================================================


# ======================================================================================
# Change the current working directory to the script's directory
# ======================================================================================
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory to the script's directory
os.chdir(script_dir)



# ======================================================================================
# Tạo tên thư mục
# ======================================================================================

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




# ======================================================================================
# Tạo giao diện
# ======================================================================================
app = CTk()
app.geometry("900x800")

set_appearance_mode("dark")
# set_appearance_mode("light")

# ======================================================================================
# BUTTON
# ======================================================================================
def click_handler():
    print("Button Clicked")

img = Image.open(r"img\icons8-chat-message-50.png")

btn = CTkButton(master=app, 
                text="Tạo thư mục mới", 
                corner_radius=32, 
                fg_color="#4158D0",
                hover_color="#C850C0", 
                border_color="#FFCC70",
                border_width=2, 
                image=CTkImage(dark_image=img, light_image=img),
                command=click_handler)
btn.place(x=50, y=700)

# ======================================================================================
# COMBOBOX
# ======================================================================================
def change_handler(value):
    print(f"Selected Value {value}")
    
# Get the current year
current_year = str(datetime.now().year)

combobox = CTkComboBox(master=app, 
                       values=["2022","2023","2024","2025","2026","2027","2028"], 
                       fg_color="#0093E9",
                       border_color="#FBAB7E", 
                       dropdown_fg_color="#0093E9",
                       command=change_handler)

# Set the default value to the current year
combobox.set(current_year)

# Place the combobox in the window
combobox.place(x=50, y=100)

# ======================================================================================
# LABEL_01_SoThongBaoMoiThau
# ======================================================================================
LABEL_01_SoThongBaoMoiThau = CTkLabel(master=app, text="Số thông báo mời thầu", font=("Arial", 14), text_color="#FFCC70")
LABEL_01_SoThongBaoMoiThau.place(x=50, y=170)

# ======================================================================================
# LABEL_02_TenThuMucSeKhoiTao
# ======================================================================================
LABEL_02_TenThuMucSeKhoiTao = CTkLabel(master=app, text="24_GOI_THAU_0001_15234685", font=("Arial", 14), text_color="#FFCC70")
LABEL_02_TenThuMucSeKhoiTao.place(x=50, y=660)

# ======================================================================================
# ENTRY_01_SoThongBaoMoiThau
# ======================================================================================
ENTRY_01_SoThongBaoMoiThau = CTkEntry(master=app, 
                                        placeholder_text="Start typing...", 
                                        width=300,
                                        text_color="#FFCC70")
ENTRY_01_SoThongBaoMoiThau.place(x=50, y=200)


app.mainloop()