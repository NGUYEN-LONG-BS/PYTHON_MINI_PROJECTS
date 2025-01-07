import tkinter as tk
from tkinter import filedialog, messagebox
import os

def open_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select a File")
    
    if file_path:
        # Check if the file is an Excel file
        if file_path.endswith(('.xls', '.xlsx')):
            messagebox.showinfo("File Selected", f"Valid Excel file selected:\n{file_path}")
        else:
            print("Not valid")
            messagebox.showerror("Invalid File", "The selected file is not a valid Excel file!")

# Create the main application window
root = tk.Tk()
root.title("Excel File Checker")

# Add a button to open the file dialog
button = tk.Button(root, text="Select a File", command=open_file)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
