import tkinter as tk
from utils import *
from utils.define import *

class cls_Frame_Element_number_01(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0)
        
        # Create a shadow frame as a child of the parent
        self.shadow = tk.Frame(parent, bg=BG_COLOR_0_0, bd=0)
        self.shadow.lower()  # Ensure shadow is below the main frame

        # Bind mouse events to the frame
        self.bind("<Enter>", self.f_on_enter_02)
        self.bind("<Leave>", self.f_on_leave_02)
        
    def f_on_enter_02(self, event):
        """Change appearance when the mouse enters the frame."""
        # self.shadow.place(in_=self, x=-5, y=-5, relwidth=1.1, relheight=1.1)
        self.shadow.place(in_=self, x=-0.5, y=-0.5, relwidth=1.01, relheight=1.02)
        self.shadow.config(bg=HIGHLIGHT_COLOR)

    def f_on_leave_02(self, event):
        """Revert appearance when the mouse leaves the frame."""
        self.shadow.place_forget()
        self.shadow.config(bg=BG_COLOR_0_0)

class cls_Frame_Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
    
    def f_setup_style_of_frame(self):
        self.configure(bg=BG_COLOR_0_0)

class cls_Frame_Header(cls_Frame_Main):
    def __init__(self, parent, name_of_slip="Default Name", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.name_of_slip = name_of_slip
        self.f_setup_style_of_frame()
        self.f_setup_Logo()
        self.f_setup_Label_Name()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(height=100)
        self.configure(bd=0, relief='flat')
        
    def f_setup_Logo(self):
        Frame_logo = cls_Frame_Element_number_01(self, width=240, height=100)
        Frame_logo.pack(side='left', padx=10, pady=5)
        f_utils_setup_logo(Frame_logo)
        
    def f_setup_Label_Name(self):
        Name_Label_Frame = tk.Frame(self, width=100, height=100, bd=0, relief='flat')
        Name_Label_Frame.pack(fill='both', expand=True)
                
        Name_label = tk.Label(Name_Label_Frame, text=self.name_of_slip)
        f_utils_set_menu_font(Name_label, 25, "Arial")
        Name_label.place(relx=0.5, rely=0.5, anchor="center")
        
class cls_Frame_Footer(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
        self.f_create_footer_label()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(height=40)
        self.configure(bd=0, relief='flat')
    
    def f_create_footer_label(self):
        footer_label = tk.Label(self, text="© 2025 Tuan An Group. All Rights Reserved.")
        footer_label.pack()
        
class cls_Frame_Body(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(bd=0, relief='flat')
        