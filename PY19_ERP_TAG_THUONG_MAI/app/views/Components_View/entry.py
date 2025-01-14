import tkinter as tk
from utils import *
from utils.define import *

class cls_my_text_entry_num_01(tk.Entry):
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
        self.config(bg=BG_COLOR_0_0)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event):
        """Change appearance when the mouse leaves."""        
        # Configure appearance when selecting
        self.config(bg=BG_COLOR_0_0)
        
    def f_on_typing(self, event):
        """Change appearance when typing."""
        self.config(bg=HIGHLIGHT_COLOR)

class cls_my_number_entry_num_01(tk.Entry):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_set_style()
        self.bind("<FocusIn>", self.f_on_selecting)
        self.bind("<FocusOut>", self.f_on_not_selecting)
        self.bind("<Enter>", self.f_on_entering)
        self.bind("<Leave>", self.f_on_leaving)
        self.bind("<Button-1>", self.f_on_selecting)
        self.bind("<Key>", self.f_on_typing)
        self.bind("<KeyPress>", self.f_validate_input)
    
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
        self.f_format_text()
        self.config(bg=BG_COLOR_0_0)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event):
        """Change appearance when the mouse leaves."""        
        # Configure appearance when selecting
        self.config(bg=BG_COLOR_0_0)
        
    def f_on_typing(self, event):
        """Change appearance when typing."""
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_validate_input(self, event):
        """Validate input to ensure only numeric values are entered."""
        current_value = self.get()
        valid_chars = "0123456789.,"
        if not all(char in valid_chars for char in current_value):
            self.delete(0, tk.END)
            self.insert(0, ''.join(filter(lambda x: x in valid_chars, current_value)))

    def f_format_text(self):
        """Format the entry text as a number with commas and two decimal places."""
        try:
            current_text = self.get().replace(",", "")
            if current_text.strip():
                formatted_text = f"{float(current_text):,.2f}"
                self.delete(0, tk.END)
                self.insert(0, formatted_text)
        except ValueError:
            # Reset text if invalid
            self.delete(0, tk.END)