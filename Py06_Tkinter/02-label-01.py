from tkinter import *
from define import *
import os

from app import App

window = Tk()

app = App(window)

# Label pack()-place()-grid()
label = Label( window, text="Hello").pack()

window.mainloop()
