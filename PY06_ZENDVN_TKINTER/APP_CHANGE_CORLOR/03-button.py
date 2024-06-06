from tkinter import *
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

# function methode  font_title
# variable          fontTitle
# place pack grid

def show_hello():
    print("Xin chào")

def show_course_info(name):
    print("Xin chào" + name)

fontTitle  = font.Font(family="Stencil Std", size= 20, weight=font.BOLD)
fontText   = font.Font(family="Terminal", size= 12)

btnHello   = Button(window, text="Hello", font=fontText, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=show_hello)
btnHello.grid(row=0, column=0)  

btnPython   = Button(window, text="Python", font=fontText, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=lambda:show_course_info("Python"))
btnPython.grid(row=0, column=1) 

btnTkinter   = Button(window, text="Tkinter", font=fontText, padx=30, pady=20, bg=COLOR_YELLOW, activebackground=COLOR_GREEN, fg=COLOR_RED, command=lambda:show_course_info("Tkinter"))
btnTkinter.grid(row=0, column=2) 

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)


window.mainloop()


