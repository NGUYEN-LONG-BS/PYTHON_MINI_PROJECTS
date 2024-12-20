import tkinter as tk
from utils import *
from utils.define import *

class cls_my_button_num_01(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()
        self.bind("<Enter>", self.f_on_entering)
        self.bind("<Leave>", self.f_on_leaving)
        self.bind("<ButtonPress-1>", self.on_pressing)
        self.bind("<ButtonRelease-1>", self.on_releasing)
    
    def f_set_style(self):
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, fg="black", font=("Arial", 12))
    
    def f_on_entering(self, event):
        """Change appearance when the mouse enters the frame."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event):
        """Change appearance when the mouse enters the frame."""        
        # Configure appearance when selecting
        self.config(bg=BG_COLOR_0_0)
        
    def on_pressing(self, event):
        """Change appearance when the left mouse button is pressed."""        
        self.config(bg=COLOR_HIGHLIGHT_LIGHT_GREEN)
    
    def on_releasing(self, event):
        """Change appearance when the left mouse button is released."""        
        self.config(bg=BG_COLOR_0_0)