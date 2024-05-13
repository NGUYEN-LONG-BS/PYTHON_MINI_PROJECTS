# How To Create a Search-able tkinter Combo Box | Tkinter and Python | How To Create ComboBox
# https://www.youtube.com/watch?v=-OAxe5LvtuM&list=PLvjjT-9qIs3h04pPU6XlrjVX5YX9nOQmf&index=8

from tkinter import *
from tkinter import ttk

lst = ['C','C++', 'Java', 
        'Python', 'Perl'
        'PHP', 'ASP', 'JS', 'HTML',
        'Ruby', 'Machine Learning']

def search(event):
    value = event.widget.get()

    if value == '':
        combo_box['values'] = lst
    else:
        data = []
        for item in list:
            if value.lower() in item.lower():
                data.append(item)
        combo_box['values'] = data

root = Tk()
root.title("Combobox")
root.geometry("300x200")
Label = Label(root,text='Search your favourite language')
Label.pack()
# Creating Combobox
combo_box = ttk.Combobox(root, values=lst)

combo_box.set('Search')
combo_box.pack()

combo_box.bind('<KeyRelease>',search)

root.mainloop()



