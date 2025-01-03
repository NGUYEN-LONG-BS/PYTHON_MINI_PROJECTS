import tkinter as tk
from tkinter import ttk
from utils import *
from utils.define import *

class cls_my_combobox_num_01(ttk.Combobox):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()
        self.bind("<FocusIn>", self.f_on_selecting)
        self.bind("<FocusOut>", self.f_on_not_selecting)
        self.bind("<Enter>", self.f_on_entering)
        self.bind("<Leave>", self.f_on_leaving)
        self.bind("<Button-1>", self.f_on_selecting)
        self.bind("<Key>", self.f_on_typing)
    
    def f_set_style(self):
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, fg="black", font=("Arial", 12))
    
    def f_on_selecting(self, event):
        """Change appearance when selecting."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_not_selecting(self, event):
        """Change appearance when not selecting."""        
        # Configure appearance when selecting
        self.config(bg=COLOR_WHITE)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event):
        """Change appearance when the mouse leaves."""        
        # Configure appearance when selecting
        self.config(bg=COLOR_WHITE)
        
    def f_on_typing(self, event):
        """Change appearance when typing."""
        self.config(bg=HIGHLIGHT_COLOR)
