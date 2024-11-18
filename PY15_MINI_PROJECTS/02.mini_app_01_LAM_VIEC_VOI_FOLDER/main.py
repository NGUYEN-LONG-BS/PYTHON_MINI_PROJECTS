import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from My_SIZE import *
from My_SIZE import size

# Create the main window
root = tk.Tk()
root.title("PY - TƯƠNG TÁC TỚI TỆP VÀ THƯ MỤC")

# Set the size of the window to 500x600 and make it non-resizable
root.geometry("900x600")
root.resizable(False, False)

# Force the window to update its size
root.update_idletasks()

# Set the geometry of TILTE
border_size = 0
Title_width_01 = 450      
Title_height = 0
Title_top = 10
Title_margin_bot = 5

# Estimate the pixel width of the label (assuming average character width of 8 pixels)
# label_pixel_width = Title_width * 8
Title_left = (root.winfo_width() - Title_width_01) // 2

# Creating a the title label
FORM_TITLE = Label(root, text = "THAO TÁC VỚI FOLDER VÀ TỆP", bd=size.border_size, relief="solid", font=("Arial", 20))
FORM_TITLE.place(x=Title_left,y = Title_top, width=Title_width_01)

# Set the geometry of rows and collumns
Row_height = 20
Row_margin = 50
# Row_01_top = Title_top + Title_height + Title_margin_bot
Row_01_top = 50
Row_02_top = Row_01_top + Row_height + Row_margin
Row_03_top = Row_02_top + Row_height + Row_margin
Row_04_top = Row_03_top + Row_height + Row_margin
Row_05_top = Row_04_top + Row_height + Row_margin

# print(Row_01_top)
# print(Row_02_top)
# print(Row_03_top)
# print(Row_04_top)
# print(Row_05_top)

collumn_margin = 5
Collum_01_left = 50
Collum_01_width = 100
Collum_02_width = 100
Collum_02_left = Collum_01_left + Collum_01_width + collumn_margin
Collum_03_left = Collum_02_left + Collum_02_width + collumn_margin

# print(Collum_01_left)
# print(Collum_02_left)
# print(Collum_03_left)

# Creating functions
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)                # Update the label with the selected folder path
    path_length.set(len(folder_selected))           # Update the label with the length of the folder path


# Create StringVars to hold the folder path and its length
folder_path = StringVar()
path_length = StringVar()

# ============================================================================ Row_01
# Create a button and attach the select_folder function
button_01 = Button(root, text="Select Folder NGUỒN", command=select_folder)
button_01.place(x=50, y=80, width=200)

# Create a button and attach the select_folder function
button_02 = Button(root, text="Select Folder ĐÍCH", command=select_folder)
button_02.place(x=50+200+20, y=80, width=200)

# ============================================================================ Row_02
# Create a title label for the folder path
path_title_label = Label(root, text="The PATH_01", bd=border_size, relief="solid")
path_title_label.place(x=Collum_01_left, y=Row_02_top) 

# Create a label to display the selected folder path
path_label = Label(root, textvariable=folder_path, bd=border_size, relief="solid")
path_label.place(x=Collum_02_left, y=Row_02_top)

# ============================================================================ Row_03
# Create a title label for the length of the folder path
length_title_label = Label(root, text="The LENGTH_01", bd=border_size, relief="solid")
length_title_label.place(x=Collum_01_left, y=Row_03_top)

# Create a label to display the length of the folder path
length_label = Label(root, textvariable=path_length, bd=border_size, relief="solid")
length_label.place(x=Collum_02_left, y=Row_03_top)

# ============================================================================ Row_04
# Create a title label for the folder path
path_title_label_02 = Label(root, text="The PATH_02", bd=border_size, relief="solid")
path_title_label_02.place(x=Collum_01_left, y=Row_04_top) 

# Create a label to display the selected folder path
path_label_02 = Label(root, textvariable=folder_path, bd=border_size, relief="solid")
path_label_02.place(x=Collum_02_left, y=Row_04_top)

# ============================================================================ Row_05
# Create a title label for the length of the folder path
length_title_label_02 = Label(root, text="The LENGTH_02", bd=border_size, relief="solid")
length_title_label_02.place(x=Collum_01_left, y=Row_05_top)

# Create a label to display the length of the folder path
length_label_02 = Label(root, textvariable=path_length, bd=border_size, relief="solid")
length_label_02.place(x=Collum_02_left, y=Row_05_top)

# ============================================================================ Add a Table
# Create a Treeview widget
columns = ("#1", "#2", "#3")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("#1", text="Column 1")
tree.heading("#2", text="Column 2")
tree.heading("#3", text="Column 3")

# Add some sample data
tree.insert("", "end", values=("Item 1", "Value 1", "Description 1"))
tree.insert("", "end", values=("Item 2", "Value 2", "Description 2"))
tree.insert("", "end", values=("Item 3", "Value 3", "Description 3"))

# Place the Treeview widget
tree.place(x=50, y=300, width=800, height=200)

# ============================================================================ Row_06
# Create a button and attach the select_folder function
button_03 = Button(root, text="Select Folder NGUỒN", command=select_folder)
button_03.place(x=50, y=550, width=200)

# Create a button and attach the select_folder function
button_04 = Button(root, text="Select Folder ĐÍCH", command=select_folder, bg="green")
button_04.place(x=50+200+20, y=550, width=200)

# Run the application
root.mainloop()