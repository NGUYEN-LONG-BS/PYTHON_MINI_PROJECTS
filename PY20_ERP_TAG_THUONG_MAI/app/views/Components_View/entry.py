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
        
    def f_on_not_selecting(self, event=None, color=None):
        """Change appearance when not selecting."""        
        # Configure appearance when selecting
        default_color = BG_COLOR_0_0
        if color is not None:
            self.config(bg=color)
        else:
            self.config(bg=default_color)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when selecting
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event=None, color=None):
        """Change appearance when the mouse leaves."""        
        # Use default background color if no color is provided
        default_color = BG_COLOR_0_0
        self.config(bg=color if color is not None else default_color)
        
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
        
    def f_on_not_selecting(self, event=None, color=None):
        """Change appearance when not selecting."""        
        # Configure appearance when not selecting
        self.f_format_text()
        default_color = BG_COLOR_0_0
        if color is not None:
            self.config(bg=color)
        else:
            self.config(bg=default_color)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when entering
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event=None, color=None):
        """Change appearance when the mouse leaves."""        
        # Use default background color if no color is provided
        default_color = BG_COLOR_0_0
        if color is not None:
            self.config(bg=color)
        else:
            self.config(bg=default_color)
        
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
        """Format the entry text as a number with commas.
        Show two decimal places only if necessary."""
        try:
            current_text = self.get().replace(",", "")
            if current_text.strip():  # Kiểm tra nếu không phải chuỗi rỗng
                number = float(current_text)
                if number.is_integer():  # Nếu là số nguyên
                    formatted_text = f"{int(number):,}"
                else:  # Nếu là số thập phân
                    formatted_text = f"{number:,.2f}"
                self.delete(0, tk.END)
                self.insert(0, formatted_text)
        except ValueError:
            # Reset text nếu nhập không hợp lệ
            self.delete(0, tk.END)
            
class cls_my_date_time_entry_num_01(tk.Entry):
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
        
    def f_on_not_selecting(self, event=None, color=None):
        """Change appearance when not selecting."""        
        # Configure appearance when not selecting
        default_color = BG_COLOR_0_0
        if color is not None:
            self.config(bg=color)
        else:
            self.config(bg=default_color)
        
    def f_on_entering(self, event):
        """Change appearance when the mouse enters."""        
        # Configure appearance when entering
        self.config(bg=HIGHLIGHT_COLOR)
        
    def f_on_leaving(self, event=None, color=None):
        """Change appearance when the mouse leaves."""        
        # Use default background color if no color is provided
        default_color = BG_COLOR_0_0
        if color is not None:
            self.config(bg=color)
        else:
            self.config(bg=default_color)
        
    def f_on_typing(self, event):
        """Change appearance when typing."""
        self.config(bg=HIGHLIGHT_COLOR)
            
    