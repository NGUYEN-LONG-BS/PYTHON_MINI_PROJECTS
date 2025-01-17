import os

# Define paths
PATH_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
PATH_ASSETS_ICONS = os.path.join(PATH_ROOT, "assets/icons")
PATH_ASSETS_TEMPLATES = os.path.join(PATH_ROOT, "assets/templates")

PATH_LOGO_LIGHT = os.path.join(PATH_ROOT, "assets/img/logo-Light.jpg")
PATH_LOGO_DARK = os.path.join(PATH_ROOT, "assets/img/logo-Dark.jpg")

PATH_CARD_IMG = os.path.join(PATH_ROOT, "assets/img/teamwork.jpg")

PATH_ICON_HIDE = os.path.join(PATH_ASSETS_ICONS, "icon-closed-eye-50.png")
PATH_ICON_UNHIDE = os.path.join(PATH_ASSETS_ICONS, "icon-opening-eye-26.png")

PATH_ASSETS_TEMPLATES_EXCEL = os.path.join(PATH_ASSETS_TEMPLATES, "excel")
PATH_PRINT_TEMPLATES = os.path.join(PATH_ASSETS_TEMPLATES, "print_templates.xlsx")

PATH_ASSETS_TEMPLATES_JSON = os.path.join(PATH_ASSETS_TEMPLATES, "json")

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
COLOR_HIGHLIGHT_LIGHT_ORANGE = "#ffeecc"
COLOR_HIGHLIGHT_LIGHT_GREEN = "#e6ffe6"
COLOR_HIGHLIGHT_BORDER_OF_LOGO = "#F0E0D3"
HIGHLIGHT_COLOR = "#f0c6a3"


BG_COLOR_0_0 = "#f0f0f0"
BG_COLOR_0_1 = "#f0f0f5"
BG_COLOR_0_2 = "#f0f0f9"

BG_COLOR_1 = "#f0f0f0"


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

