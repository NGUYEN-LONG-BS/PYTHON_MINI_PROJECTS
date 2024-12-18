import tkinter as tk
from utils import *
from utils.define import *

class cls_Frame_Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
    
    def f_setup_style_of_frame(self):
        self.configure(bg=BG_COLOR_0_0)

class cls_Frame_Header(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
        self.f_setup_Logo()
        self.f_setup_Label_Name()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(height=100)
        self.configure(bd=1, relief='solid')
        
    def f_setup_Logo(self):
        Frame_logo = tk.Frame(self, width=100, height=100)
        Frame_logo.pack(side='left', padx=10, pady=5)
        f_utils_setup_logo(Frame_logo)
        
    def f_setup_Label_Name(self):
        Name_Label_Frame = tk.Frame(self, width=100, height=100, bd=1, relief='solid')
        Name_Label_Frame.pack(fill='both', expand=True)
                
        Name_label = tk.Label(Name_Label_Frame, text="TÊN CỬA SỔ")
        f_utils_set_menu_font(Name_label, 25, "Arial")
        Name_label.pack()
        
class cls_Frame_Footer(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
        self.f_create_footer_label()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(height=40)
        self.configure(bd=1, relief='solid')
    
    def f_create_footer_label(self):
        footer_label = tk.Label(self, text="© 2025 Tuan An Group. All Rights Reserved.")
        footer_label.pack()
        
class cls_Frame_Body(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(bd=2, relief='sunken')
