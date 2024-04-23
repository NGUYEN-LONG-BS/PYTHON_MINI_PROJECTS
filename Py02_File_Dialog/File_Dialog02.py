# Source: https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
import sys
import ctypes
co_initialize = ctypes.windll.ole32.CoInitialize
#   Force STA mode
co_initialize(None)

import clr 

clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import OpenFileDialog

file_dialog = OpenFileDialog()
ret = file_dialog.ShowDialog()
if ret != 1:
    print("Cancelled")
    sys.exit()

print(file_dialog.FileName)