import tkinter as tk
from utils import *
from utils.define import *

class cls_my_label_num_01(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()

    
    def f_set_style(self):
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, fg="black", font=("Arial", 12))
    
