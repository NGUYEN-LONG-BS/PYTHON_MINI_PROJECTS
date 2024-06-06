from tkinter import *
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

font_title  = font.Font(family="Stencil Std", size= 12, weight=font.BOLD)
font_text   = font.Font(family="Terminal", size= 20)

# Label pack() place() grid()
label_python = Label( window, text="Python", font=font_title, bg=COLOR_RED, fg=COLOR_YELLOW,  padx=10, pady=5)
label_python.grid(row=0, column=0, sticky=NW)

label_tkinter = Label( window, text="Tkinter", font=font_title, bg=COLOR_YELLOW, fg=COLOR_RED,  padx=10, pady=5)
label_tkinter.grid(row=0, column=1, sticky=S)

label_pygame = Label( window, text="Pygame", font=font_title, bg=COLOR_BLACK, fg=COLOR_YELLOW,  padx=10, pady=5)
label_pygame.grid(row=0, column=2, sticky=NE)


window.columnconfigure(0, weight= 1)
window.columnconfigure(1, weight= 1)
window.columnconfigure(2, weight= 1)

window.rowconfigure(0, weight= 1)


window.mainloop()


