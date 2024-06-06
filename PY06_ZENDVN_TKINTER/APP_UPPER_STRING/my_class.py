from tkinter import Frame, Label, W, Entry, Button
from define import *

class MyFrame(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self['bg']      = COLOR_GRAY
        self['pady']    = 10

        self.grid(row=0)

class MyLabel(Label):

    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)
        self['bg']      = COLOR_GRAY
        self['padx']    = 10
        self['fg']      = COLOR_BLACK
        self['font']    = FONT_DEFAULT


        self.grid(row=0, sticky=W)

class MyEntry(Entry):

    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self['width']      = 40
        self['bg']      = COLOR_WHITE
        self['font']    = FONT_DEFAULT


        self.grid(row=1, padx=10)

class MyButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['padx']    = 15
        self['pady']    = 5
        self['fg']      = COLOR_WHITE
        self['font']    = 13


        self.grid(padx=10, pady=12, row=2)
