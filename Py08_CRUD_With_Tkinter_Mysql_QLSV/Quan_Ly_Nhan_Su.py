# Lập trình ứng dụng Tkinter và Python
# https://www.youtube.com/playlist?list=PLUocOGc7RDEK4CzthbdqoJ5J7cDW4-hLw


from tkinter import *
root=Tk()
root.title('Quản Lý Sinh Viên')
root.minsize (height=500, width=500)
Label(root,text='ÚNG DỤNG QUẢN LÝ SINH VIÊN',fg='red',font=('cambria',16),width=25).grid(row=0)
Listbox(root, width=80,height=20).grid(row=1,columnspan=2)
Label(root, text='Mã SV:').grid(row=2, column=0)
Entry(root, width=30).grid(row=2, column=1)
Label(root, text='Tên SV:').grid(row=3, column=0)
Entry(root, width=30).grid(row=3, column=1)
Label(root, text='Năm sinh: ').grid(row=4, column=0) 
Entry(root, width=30).grid(row=4, column=1)
button=Frame(root)
Button (button, text='Thêm').pack(side=LEFT)
Button (button, text='Xem').pack (side=LEFT)
Button(button, text='Sắp xếp').pack(side=LEFT)
Button(button, text='Thoát ', command=root.quit).pack(side=LEFT)
button.grid(row=5, column=1)
root.mainloop()
