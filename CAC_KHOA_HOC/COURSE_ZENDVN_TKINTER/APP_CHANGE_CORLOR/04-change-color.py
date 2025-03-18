from tkinter import *
from tkinter import font
from define import *
import random

from app import App



window = Tk()
app = App(window)

fontTitle  = font.Font(family="Stencil Std", size= 20, weight=font.BOLD)
fontText   = font.Font(family="Terminal", size= 12)

def random_color():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

def change_label_color(background):
    label['background']=background

def create_button(name, background, index ):
    Button(window, text=name, font=fontText, padx=30, pady=20, width=8, bg=background, fg=COLOR_BLACK, command=lambda:change_label_color(background)).grid(row=1, column=index, sticky=W+E, padx=30)

label = Label(window, text = "Hello", bg=random_color(), font = fontTitle, padx=30, pady=20)
label.grid(row=0, column=0, columnspan=4, sticky=W+S+E, padx=30)

create_button("Green", COLOR_GREEN, 0)
create_button("Blue", COLOR_BLUE, 1)
create_button("Red", COLOR_RED, 2)
create_button("Yellow", COLOR_YELLOW, 3)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.mainloop()


