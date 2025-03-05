import os
import sys

# Lấy thư mục chứa main.exe hoặc script đang chạy
if getattr(sys, 'frozen', False):
    # Khi chạy từ file .exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # Khi chạy từ file .py
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths
PATH_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../.."))
PATH_PARENT_OF_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../.."))

# # Định nghĩa thư mục `assets` nằm cùng cấp với `main.exe`
# PATH_ASSETS = os.path.join(BASE_DIR, "assets")



# Define paths
# PATH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
# PATH_PARENT_OF_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
PATH_ASSETS_ICONS = os.path.join(PATH_PARENT_OF_ROOT, "assets/icons")
PATH_ASSETS_TEMPLATES = os.path.join(PATH_PARENT_OF_ROOT, "assets/templates")

PATH_LOGO_LIGHT = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/logo-Light.jpg")
PATH_LOGO_DARK = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/logo-Dark.jpg")

PATH_CARD_IMG = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/teamwork.jpg")
PATH_CARD_BAN_KINH_DOANH = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/BanKinhDoanh.png")
PATH_CARD_BAN_VAT_TU = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/VAT_TU.png")
PATH_CARD_KHO = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KHO.png")
PATH_CARD_BAN_TAI_CHINH = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/TAI_CHINH.png")
PATH_CARD_BAN_KY_THUAT = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KY_THUAT.png")
PATH_CARD_BAN_NHAN_SU = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/NHAN_SU.png")

PATH_CARD_KD_QUAN_LY_KHACH_HANG = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_DS_KHACH_HANG.png")
PATH_CARD_KD_02 = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_DS_HANG_HOA.png")
PATH_CARD_KD_03 = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_QUAN_LY_GOI_THAU.png")
PATH_CARD_KD_04 = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_QUAN_LY_CONG_NO.png")
PATH_CARD_KD_QUAN_LY_KE_HOACH_DAT_HANG = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_QUAN_LY_KE_HOACH_DAT_HANG.png")
PATH_CARD_KD_05 = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_YEU_CAU_DAT_HANG.png")
PATH_CARD_KD_06 = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_REPORT.png")
PATH_CARD_KD_QUAN_LY_DE_NGHI_XUAT_KHO = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/KD_QUAN_LY_DE_NGHI_XUAT_KHO.png")

PATH_CARD_ADMIN_QUAN_LY_DATABASE = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/ADMIN_QUAN_LY_DATABASE.png")
PATH_CARD_ADMIN_CAI_DAT_CHUNG = os.path.join(PATH_PARENT_OF_ROOT, "assets/img/ADMIN_CAI_DAT_CHUNG.png")

PATH_FAV_ICON = os.path.join(PATH_PARENT_OF_ROOT, "assets/icons/favicon.png")

PATH_ICON_HIDE = os.path.join(PATH_ASSETS_ICONS, "icon-closed-eye-50.png")
PATH_ICON_UNHIDE = os.path.join(PATH_ASSETS_ICONS, "icon-opening-eye-26.png")

PATH_ASSETS_TEMPLATES_EXCEL = os.path.join(PATH_ASSETS_TEMPLATES, "excel")
PATH_PRINT_TEMPLATES = os.path.join(PATH_ASSETS_TEMPLATES, "print_templates.xlsx")

PATH_ASSETS_TEMPLATES_JSON = os.path.join(PATH_ASSETS_TEMPLATES, "json")

PATH_CONFIG_JSON = os.path.join(PATH_ROOT, "config/config.json")
PATH_CONFIG_KEY = os.path.join(PATH_ROOT, "config/encryption_key.key")

PATH_JSON_LOGIN_CREDENTIALS = os.path.join(PATH_ASSETS_TEMPLATES_JSON, "AD_LOGIN/login_credentials.json")

def f_define_PATH_DEFAUL():
    paths_to_check = [
        r"C:\\Users\\ADMIN\\Desktop",
        r"C:\\",
        r"D:\\",
        r"E:\\"
    ]

    for path in paths_to_check:
        if os.path.exists(path):
            return path

    return None  # Return None if no path exists

PATH_DEFAUL = f_define_PATH_DEFAUL()


# Window dimensions and positions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
WINDOW_POSITION_RIGHT = 400
WINDOW_POSITION_DOWN = 200

# Color
COLOR_BACKGROUND = "#f0f0f5"
COLOR_BG_0_1 = "#f0f0f9"
COLOR_BACKGROUND_NUM_02_DARK_GRAY = "#A9A9A9"
COLOR_HIGHLIGHT_LIGHT_ORANGE = "#ffeecc"
COLOR_HIGHLIGHT_LIGHT_GREEN = "#e6ffe6"
COLOR_HIGHLIGHT_BORDER_OF_LOGO = "#F0E0D3"


HIGHLIGHT_COLOR_LIGHT_ORANGE = "#EFC2A4"
HIGHLIGHT_COLOR_TEA_GREEN = "#BCD2A2"
HIGHLIGHT_COLOR = HIGHLIGHT_COLOR_TEA_GREEN


BG_COLOR_0_0 = "#f0f0f0"
BG_COLOR_0_1 = "#f0f0f5"
BG_COLOR_0_2 = "#f0f0f9"
BG_COLOR_0_3 = "#e0e0e0"
BG_COLOR_0_4 = "#e57a17"
BG_COLOR_1 = "#f0f0f0"

FG_COLOR_01 = "#000000"
FG_COLOR_02 = "#ffffff"
FG_COLOR_03 = "#bdbdbf"

COLOR_TEST = "#a64dff"


COLOR_GRAY = "#f0f0f0"
COLOR_BLACK = "#726461"
COLOR_RED = "#ff3333"
COLOR_BLUE = "#53D4F7"
COLOR_GREEN = "#00b359"
COLOR_WHITE = "#ffffff"
COLOR_PURPLE = "#a64dff"
COLOR_YELLOW = "#ffff00"
COLOR_PINK = "#f7b5e2"

# Font
FONT_DEFAULT_NUM_01 = ("Arial", 10)

# Border size
BORDER_SIZE_0 = 0
BORDER_SIZE_1 = 0

