# Source: https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
# Ẩn cửa sổ đi
root.withdraw()

file_path = filedialog.askopenfilename()

