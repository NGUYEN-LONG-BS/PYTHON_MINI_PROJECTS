import tkinter as tk
from tkinter import *
from tkinter import filedialog
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

collumn_margin = 5
Collum_01_left = 50
Collum_01_width = 100
Collum_02_width = 100
Collum_02_left = Collum_01_left + Collum_01_width + collumn_margin
Collum_03_left = Collum_02_left + Collum_02_width + collumn_margin

# Creating functions
def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)  # Update the label with the selected folder path
    path_length.set(len(folder_selected))  # Update the label with the length of the folder path


# Create StringVars to hold the folder path and its length
folder_path = StringVar()
path_length = StringVar()


# ============================================================================ Row_01
# # Adding a label at x=50, y=60 with border width 1
# new_label = Label(root, text="New Label_01", bd=1, relief="solid")
# new_label.place(x=50, y=60)

# Create a button and attach the select_folder function
button = Button(root, text="Select Folder", command=select_folder)
button.place(x=Row_01_top, y=Collum_01_left)


# ============================================================================ Row_02
# # Adding a label at x=50, y=60 with border width 2
# new_label_02 = Label(root, text="New Label_02", bd=border_size, relief="solid")
# new_label_02.place(x=50, y=120)

# Create a title label for the folder path
path_title_label = Label(root, text="The PATH", bd=border_size, relief="solid")
path_title_label.place(x=Collum_01_left, y=Row_02_top) 

# Create a label to display the selected folder path
path_label = Label(root, textvariable=folder_path, bd=border_size, relief="solid")
path_label.place(x=Collum_02_left, y=Row_02_top)

# ============================================================================ Row_03
# # Adding a label at x=50, y=60 with border width 3
# new_label_03 = Label(root, text="New Label_03", bd=1, relief="solid")
# new_label_03.place(x=50, y=180)

# Create a title label for the length of the folder path
length_title_label = Label(root, text="The LENGTH", bd=border_size, relief="solid")
length_title_label.place(x=Collum_01_left, y=Row_03_top)

# Create a label to display the length of the folder path
length_label = Label(root, textvariable=path_length, bd=border_size, relief="solid")
length_label.place(x=Collum_02_left, y=Row_03_top)

# Run the application
root.mainloop()