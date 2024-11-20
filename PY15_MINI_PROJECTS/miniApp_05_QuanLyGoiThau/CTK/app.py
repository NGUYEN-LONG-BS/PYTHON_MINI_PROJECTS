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
script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current script
os.chdir(script_dir)

# ======================================================================================
# CREATE NEW FOLDER
# ======================================================================================
def Create_New_Folder():
    # Khai báo đường dẫn đến các gói thầu
    PathQuanLyThau = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"
    arr_DanhSachGoiThau = os.listdir(PathQuanLyThau)
    # print(arr_DanhSachGoiThau)
    
    # Tạo tên folder mới
    folder_name_01_year = COMBOBOX_NamGoiThau.get()[-2:]
    folder_name_02 = "GOI_THAU"
    folder_name_03_number = str(len(arr_DanhSachGoiThau) + 1).zfill(4)      # hiển thị 4 ký tự
    # folder_name_04 = "SoThongBaoMoiThau"
    folder_name_04 = ENTRY_01_SoThongBaoMoiThau.get().zfill(4)
    folder_name_completed = folder_name_01_year + "_" + folder_name_02 + "_" + folder_name_03_number + "_" + folder_name_04
    new_folder_path = os.path.join(PathQuanLyThau, folder_name_completed)
    sub_folder_01_path = os.path.join(PathQuanLyThau, folder_name_completed, "1.THONG_BAO_MOI_THAU")
    sub_folder_02_path = os.path.join(PathQuanLyThau, folder_name_completed, "2.DUYET_GIA")
    sub_folder_03_path = os.path.join(PathQuanLyThau, folder_name_completed, "3.MO_THAU")
    sub_folder_04_path = os.path.join(PathQuanLyThau, folder_name_completed, "4.TRUNG_THAU")
    
    # Kiểm tra nếu folder chưa tồn tại, thì tạo mới
    def check_variable_in_array(array, variable):
        if variable in array:
            return True
        else:
            return False
    result = check_variable_in_array(arr_DanhSachGoiThau, folder_name_completed)
    # Thực hiện tạo folder
    if result:
        print(f"The string '{folder_name_completed}' exists in the array.")
    else:
        print(f"The string '{folder_name_completed}' does not exist in the array.")
        os.makedirs(new_folder_path)
        os.makedirs(sub_folder_01_path)
        os.makedirs(sub_folder_02_path)
        os.makedirs(sub_folder_03_path)
        os.makedirs(sub_folder_04_path)
        print(f"Đã tạo folder: {new_folder_path}")


# ======================================================================================
# CREATE USER FORM
# ======================================================================================
app = CTk()
app.geometry("900x800")
# Create the main application window
app.title("QUẢN LÝ GÓI THẦU")

# Mode Dark or Light
# set_appearance_mode("dark")
set_appearance_mode("light")

# Change the color style
# set_default_color_theme(r"json\MoonlitSky.json")
# set_default_color_theme(r"json\NeonBanana.json")
set_default_color_theme(r"json\DaynNight.json")


# ======================================================================================
# BTN_TaoThuMucMoi
# ======================================================================================
def click_handler_BTN_TaoThuMucMoi():
    # print("Button Clicked")
    Create_New_Folder()
    reset_scrollable_frame()
    set_scrollable_frame()

img = Image.open(r"img\icons8-chat-message-50.png")

BTN_TaoThuMucMoi = CTkButton(master=app, 
                text="Tạo thư mục mới", 
                image=CTkImage(dark_image=img, light_image=img),
                command=click_handler_BTN_TaoThuMucMoi)
BTN_TaoThuMucMoi.place(x=50, y=700)

# ======================================================================================
# BTN_DenThuMucDaChon
# ======================================================================================
def click_handler_BTN_DenThuMucDaChon():
    print("Thư mục đã chọn là: ")

img = Image.open(r"img\icons8-chat-message-50.png")

BTN_DenThuMucDaChon = CTkButton(master=app, 
                text="Mở thư mục", 
                # corner_radius=32, 
                # border_width=2, 
                image=CTkImage(dark_image=img, light_image=img),
                command=click_handler_BTN_DenThuMucDaChon)
BTN_DenThuMucDaChon.place(x=250, y=700)

# ======================================================================================
# COMBOBOX_NamGoiThau
# ======================================================================================
def change_handler(value):
    last_02_chars = value[-2:]
    print(f"Selected Value {value}, Last Two Characters: {last_02_chars}")
    
# Get the current year
current_year = datetime.now().year
# Create the array with the specified years
year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

COMBOBOX_NamGoiThau = CTkComboBox(master=app, 
                       values=year_array,
                    #    fg_color="#0093E9",
                    #    border_color="#FBAB7E", 
                    #    dropdown_fg_color="#0093E9",
                       command=change_handler)

# Set the default value to the current year
COMBOBOX_NamGoiThau.set(current_year)
# Place the combobox in the window
COMBOBOX_NamGoiThau.place(x=50, y=100)

# ======================================================================================
# LABEL_SoThongBaoMoiThau
# ======================================================================================
LABEL_SoThongBaoMoiThau = CTkLabel(master=app, 
                                   text="Số thông báo mời thầu"
                                    ,font=("",18)
                                    # ,text_color="#FFCC70"
                                   )
LABEL_SoThongBaoMoiThau.place(x=50, y=170)

# ======================================================================================
# LABEL_TenThuMucSeKhoiTao
# ======================================================================================
LABEL_TenThuMucSeKhoiTao = CTkLabel(master=app, 
                                    text="24_GOI_THAU_0000_0000"
                                    ,font=("",18)
                                    )
LABEL_TenThuMucSeKhoiTao.place(x=390, y=200)

# ======================================================================================
# LABEL_NamGoiThau
# ======================================================================================
LABEL_NamGoiThau = CTkLabel(master=app
                    ,text="Năm gói thầu"
                    ,font=("",18)
                    # ,text_color="#FFCC70"
                    )
LABEL_NamGoiThau.place(x=50, y=70)

# ======================================================================================
# LABEL_DanhSachGoiThau
# ======================================================================================
LABEL_DanhSachGoiThau = CTkLabel(master=app
                                    ,text="Danh sách gói thầu"
                                    ,font=("",18)
                                    # ,text_color="#FFCC70"
                                    )
LABEL_DanhSachGoiThau.place(x=50, y=270)

# ======================================================================================
# LABEL_IDNhanVien
# ======================================================================================
LABEL_IDNhanVien = CTkLabel(master=app
                            ,text="ID: TBD001"
                            ,font=("",13)
                            # ,text_color="#FFCC70"
                            )
LABEL_IDNhanVien.place(x=50, y=10)

# ======================================================================================
# LABEL_TenNhanVien
# ======================================================================================
LABEL_TenNhanVien = CTkLabel(master=app
                            ,text="Họ tên: Nguyễn Văn B"
                            ,font=("",13)
                            # ,text_color="#FFCC70"
                             )
LABEL_TenNhanVien.place(x=150, y=10)

# ======================================================================================
# LABEL_TenBoPhan
# ======================================================================================
LABEL_TenBoPhan = CTkLabel(master=app
                           ,text="Bộ phận: Kinh doanh"
                           ,font=("",13)
                        #    ,text_color="#FFCC70"
                           )
LABEL_TenBoPhan.place(x=350, y=10)

# ======================================================================================
# LABEL_CapBac
# ======================================================================================
LABEL_CapBac = CTkLabel(master=app
                        ,text="Cấp bậc: Nhân viên"
                        ,font=("",13)
                        # ,text_color="#FFCC70"
                        )
LABEL_CapBac.place(x=550, y=10)

# ======================================================================================
# LABEL_TenCongTy
# ======================================================================================
LABEL_TenCongTy = CTkLabel(master=app
                           ,text="Cty: Thiết bị điện"
                           ,font=("",13)
                        #    ,text_color="#FFCC70"
                           )
LABEL_TenCongTy.place(x=750, y=10)

# ======================================================================================
# ENTRY_01_SoThongBaoMoiThau
# ======================================================================================
def update_label(*args):
    # Khai báo đường dẫn đến các gói thầu
    PathQuanLyThau = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"
    arr_DanhSachGoiThau = os.listdir(PathQuanLyThau)
    # print(arr_DanhSachGoiThau)
    
    # Tạo tên folder mới
    folder_name_01_year = COMBOBOX_NamGoiThau.get()[-2:]
    folder_name_02 = "GOI_THAU"
    folder_name_03_number = str(len(arr_DanhSachGoiThau) + 1).zfill(4)      # hiển thị 4 ký tự
    # folder_name_04 = "SoThongBaoMoiThau"
    folder_name_04 = ENTRY_01_SoThongBaoMoiThau.get().zfill(4)
    folder_name_completed = folder_name_01_year + "_" + folder_name_02 + "_" + folder_name_03_number + "_" + folder_name_04
    # new_folder_path = os.path.join(PathQuanLyThau, folder_name_completed)
    
    LABEL_TenThuMucSeKhoiTao.configure(text=folder_name_completed)
    
ENTRY_01_SoThongBaoMoiThau = CTkEntry(master=app
                                        ,placeholder_text="Start typing..."
                                        ,width=300
                                        # ,text_color="#FFCC70"
                                        )
ENTRY_01_SoThongBaoMoiThau.place(x=50, y=200)
ENTRY_01_SoThongBaoMoiThau.bind("<KeyRelease>", update_label)

# ======================================================================================
# LISTBOX
# ======================================================================================
# Function to list all files and folders in the directory
def list_directory_contents(directory):
    try:
        contents = os.listdir(directory)
        return contents
    except Exception as e:
        print(f"Error: {e}")
        return []
        
# Global variable to keep track of the currently highlighted label
highlighted_label_now = None
# Function to handle click event on labels
def on_label_click(event):
    global highlighted_label_now
    label = event.widget
    print(f"Clicked on: {label.cget('text')}")
    # Reset the background color of the previously highlighted label
    for child in label.master.winfo_children():
        child.configure(bg="#333333")
    if highlighted_label_now:
        highlighted_label_now.configure(bg="#333333")
        # Highlight the clicked label
        label.configure(bg="#FFCC70")
        # Update the highlighted label
        highlighted_label_now = label

# Function to populate the Frame with directory contents
def populate_frame(frame, contents):
    for item in contents:
        label = CTkLabel(master=frame
                         ,text=item
                         ,font=("", 14)
                         )
        label.pack(anchor="w")
        label.bind("<Button-1>", on_label_click)

def reset_scrollable_frame():
    # Clear existing contents
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

def set_scrollable_frame():
    # Get the current directory (or specify a different directory)
    # current_directory = os.getcwd()
    current_directory = r"\\172.16.0.191\2.0 ksnb\TUAN_AN_GROUP\BAN_KINH_DOANH\QUAN_LY_THAU"

    # List the contents of the directory
    directory_contents = list_directory_contents(current_directory)

    # Sort the contents in descending order
    directory_contents.sort(reverse=True)

    # Populate the Frame with the directory contents
    populate_frame(scrollable_frame, directory_contents)

    # Scroll to the end by default
    scrollable_frame.update_idletasks()
    # scrollable_frame._parent_canvas.yview_moveto(1.0)       # Scroll to the end
    scrollable_frame._parent_canvas.yview_moveto(0.0)

scrollable_frame = CTkScrollableFrame(master=app
                                        ,width=800
                                        ,height=200
                                        )
scrollable_frame.place(x=50, y=300)

set_scrollable_frame()
# ======================================================================================
# MAINLOOP
# ======================================================================================
app.mainloop()