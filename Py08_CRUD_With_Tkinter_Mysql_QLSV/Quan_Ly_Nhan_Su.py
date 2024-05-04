# Lập trình ứng dụng Tkinter và Python
# https://www.youtube.com/playlist?list=PLUocOGc7RDEK4CzthbdqoJ5J7cDW4-hLw


from tkinter import *
from database import *

def add():
    line=id.get() + ' - '+name.get()+' '+year.get()
    save(line)
    show()

def show():
    sv=read()
    listbox.delete(0, END)
    for i in sv:
        listbox.insert(END,i)

def sort():
    sv=read
    for i in range(len(sv)):
        for j in range(len(sv)): 
            x, y=sv[1], sv[1]
            if x[2]>y[2]:
                sv[i], sv[j]=y,x
    listbox.delete(0, END)
    for i in sv:
        listbox.insert(END, 1)



root=Tk() 
#Var
id=StringVar()
name=StringVar()
year=StringVar()
root.title('Quản Lý Sinh Viên ')
root.minsize (height=580, width=500)
Label(root, text='ÚNG DỤNG QUẢN LÝ SINH VIÊN',fg='red', font=('cambria',16),width=25).grid(row=0) 
listbox = Listbox (root, width=80,height=20)
listbox.grid(row=1, columnspan=2)
show()
Label(root, text='Mã SV:').grid(row=2, column=0)
Entry(root, width=30, textvariable=id).grid(row=2, column=1)
Label(root, text='Tên SV:').grid(row=3, column=0)
Entry(root, width=38, textvariable=name).grid(row=3, column=1) 
Label(root, text='Năm sinh: ').grid(row=4, column=0)
Entry(root, width=30, textvariable=year).grid(row=4, column=1) 
button=Frame (root)
Button(button, text='Thêm', command=add).pack(side=LEFT) 
Button(button, text='Xem').pack(side=LEFT)
Button(button, text='Sắp xếp', command=sort).pack(side=LEFT) 
Button(button, text='Thoát ', command=root.quit).pack (side=LEFT) 
button.grid(row=5, column=1)
root.mainloop()

