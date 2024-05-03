from define import * 

class App():
    def __init__(self, window) -> None:
        # Thiết lập Width Height Position
        # .geometry("window width x window height + position right + position down")
        window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))

        # Title
        window.title("Change Color")

        # Icon
        window.iconbitmap(os.path.join(PATH_IMAGES, 'icon.ico'))

        # Background
        # root.configure(bg='blue')
        # root['bg']='green'
        # root['background']='yellow'
        window['background']=COLOR_BACKGROUND