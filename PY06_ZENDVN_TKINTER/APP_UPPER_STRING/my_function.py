from tkinter  import NORMAL, DISABLED, END, messagebox
from notify import *

def convert(entryOutput, entryInput):
    entryOutput.config(state=NORMAL)
    input = entryInput.get()
    if input == "":
        messagebox.showwarning(NAME_WARNING_BOX, MESSAGE_WARNING_BOX)
    entryOutput.insert(0, str(input.upper()))
    entryOutput.config(state=DISABLED) 

def clear(entryInput, entryOutput):
    MsgBox = messagebox.askquestion(NAME_CONFIRM_BOX, MESSAGE_CONFIRM_BOX, icon='warning')
    if MsgBox == 'yes':
        entryInput.delete(0, END)
        entryOutput.config(state=NORMAL)
        entryOutput.delete(0, END)
        entryOutput.config(state=DISABLED)