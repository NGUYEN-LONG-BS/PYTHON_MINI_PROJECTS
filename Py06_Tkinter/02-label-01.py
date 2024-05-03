# from tkinter import *
# from define import *
# import os

# from app import App

# window = Tk()

# app = App(window)

# # Label pack()-place()-grid()
# label = Label( window, text="Hello").pack()

# window.mainloop()



from tkinter import *
from tkinter import font 
from define import *

from app import App

window = Tk()

app = App(window)

font_title = font. Font(family="Stencil Std", size= 44, weight-font.BOLD)
font_text = font.Font (family="Terminal", size= 20)

# Label pack() place() grid()
print(font.families())
labelTitle Label( window, text="Hello", font-font_title, bg=COLOR_RED, fg=COLOR_YELLOW, width=10, padx=40, pady=20).pack() labelText = Label( window, text="Hello", font-font_text, bg=COLOR_RED, fg=COLOR_YELLOW, width=10, padx=40, pady=20).pack()
window.mainloop()
