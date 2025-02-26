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
        """Configure initial appearance using ttk.Style."""
        style = ttk.Style()

        # Base style for the combobox
        style.configure("TCombobox",
                        background=BG_COLOR_0_0,  # Default background color
                        foreground="black",       # Text color
                        font=FONT_DEFAULT_NUM_01,         # Font
                        borderwidth=0,             # Remove the border width
                        relief="flat",
                        fieldbackground=BG_COLOR_0_0, # Same as background color to hide internal border
                        lightcolor=BG_COLOR_0_0,      # Set the light shadow to the same color as background
                        darkcolor=BG_COLOR_0_0)       # Set the dark shadow to the same color as background
        
        # Apply the default style to the combobox
        self.configure(style="TCombobox")

    def f_on_selecting(self, event):
        """Change appearance when selecting (focus in)."""
        # Configure appearance when selecting (focus in)
        self.config(background=HIGHLIGHT_COLOR)
        
    def f_on_not_selecting(self, event):
        """Change appearance when not selecting (focus out)."""
        # Configure appearance when not selecting (focus out)
        self.config(background=BG_COLOR_0_0)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""
        # Configure appearance when mouse enters
        if not self.focus_get():  # Only apply if not focused
            self.config(background=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event):
        """Change appearance when the mouse leaves."""
        # Configure appearance when mouse leaves
        if not self.focus_get():  # Only apply if not focused
            self.config(background=BG_COLOR_0_0)
        
    def f_on_typing(self, event):
        """Change appearance when typing."""
        # Configure appearance when typing
        self.config(background=HIGHLIGHT_COLOR)
