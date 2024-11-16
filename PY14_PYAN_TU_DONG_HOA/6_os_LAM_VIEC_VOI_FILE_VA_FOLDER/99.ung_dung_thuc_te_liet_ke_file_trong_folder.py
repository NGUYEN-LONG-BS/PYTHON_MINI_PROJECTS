# Ứng dụng liệt kê tên folder và tep trong mot folder bất kỳ
# pip install tk
import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)  # Update the label with the selected folder path

# Create the main window
root = tk.Tk()
root.title("Folder Selector")

# Set the size of the window to 500x600
root.geometry("500x600")
root.resizable(False, False)

# Create a StringVar to hold the folder path
folder_path = tk.StringVar()

# Create a button and attach the select_folder function
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)

# Create a label to display the selected folder path
path_label = tk.Label(root, textvariable=folder_path)
path_label.pack(pady=20)

# Run the application
root.mainloop()
