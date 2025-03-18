from tkinter import *
from define import *
from app import App
from my_function import *
from my_class import *

window = Tk()
app = App(window)

frameLeft = MyFrame(window)
frameLeft.grid(column=0)
frameRight = MyFrame(window)
frameRight.grid(column=1)

#Input
labelInput = MyLabel(frameLeft, text="Input")
labelInput.grid(column=0)

entryInput = MyEntry(frameLeft)
entryInput.grid(column=0)
entryInput.focus()

btnConvert = MyButton(frameLeft, text="Convert", bg=COLOR_GREEN, command=lambda:convert(entryOutput, entryInput))
btnConvert.grid(column=0, sticky=E)

# Output
labelOutput = MyLabel(frameRight, text="Output")
labelOutput.grid(column=1)

entryOutput = MyEntry(frameRight, state=DISABLED)
entryOutput.grid(column=1)

btnClear = MyButton(frameRight, text="Clear", bg=COLOR_BLUE, command=lambda:clear(entryInput, entryOutput))
btnClear.grid(column=1, sticky=W)

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


window.mainloop()


