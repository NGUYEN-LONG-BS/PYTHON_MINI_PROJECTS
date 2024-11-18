import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)  # Update the label with the selected folder path
    path_length.set(len(folder_selected))  # Update the label with the length of the folder path

# Create the main window
root = tk.Tk()
root.title("Folder Selector")

# Set the size of the window to 500x600 and make it non-resizable
root.geometry("900x600")
root.resizable(False, False)

# Create StringVars to hold the folder path and its length
folder_path = tk.StringVar()
path_length = tk.StringVar()

# Create a button and attach the select_folder function
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.grid(row=0, column=0, columnspan=2, pady=20)

# Create a title label for the folder path
path_title_label = tk.Label(root, text="The PATH")
path_title_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Create a label to display the selected folder path
path_label = tk.Label(root, textvariable=folder_path)
path_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Create a title label for the length of the folder path
length_title_label = tk.Label(root, text="The LENGTH")
length_title_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Create a label to display the length of the folder path
length_label = tk.Label(root, textvariable=path_length)
length_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Run the application
root.mainloop()