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
    
class cls_my_label_num_02_title_H1(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()

    def f_set_style(self):
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, fg="black", font=("Arial", 25, "bold"))

class cls_my_label_num_03_title_H2(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()

    def f_set_style(self):
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, fg="black", font=("Arial", 15, "bold"))