from tkinter import *
from define import *
import os

root = Tk()

def setup_window():
    # Thiết lập Width Height Position
    # .geometry("window width x window height + position right + position down")

    root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))

    # Title
    root.title("Change Color")

    # Icon
    root.iconbitmap(os.path.join(PATH_IMAGES, 'icon.ico') )

    # Background
    root['background']=COLOR_BACKGROUND

    root.resizable(False, False) 

setup_window()

root.mainloop()


