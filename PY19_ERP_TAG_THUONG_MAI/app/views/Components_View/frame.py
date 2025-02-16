import tkinter as tk
from .label import *
from .entry import *
from utils import *
from utils.define import *
from PIL import Image, ImageTk  # For handling images

class cls_ToolTip:
    """Custom tooltip class."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None

    def show_tip(self):
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + cy + self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):   
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = None

class cls_frame_while_design(tk.Frame):
    def __init__(self, master=None, ControlTipText="", *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.f_set_style()
        self.tooltip = cls_ToolTip(self, ControlTipText)
        self.bind("<Enter>", self.show_tooltip)
        self.bind("<Leave>", self.hide_tooltip)
        
    def f_set_style(self):
        self.configure(bd=1, relief="solid")
        
    def show_tooltip(self, event):
        self.tooltip.show_tip()
    
    def hide_tooltip(self, event):
        self.tooltip.hide_tip()

# class cls_frame_normal(tk.Frame):
#     def __init__(self, master=None, *args, **kwargs):
#         super().__init__(master, *args, **kwargs)
#         self.f_set_style()
        
#     def f_set_style(self):
#         self.configure(bd=0, relief="flat")
#         # self.configure(bd=1, relief="solid")  # dùng khi phân tích khung

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
        Frame_logo = tk.Frame(self, width=240, height=100)
        Frame_logo.pack(side='left', padx=10, pady=5)
        f_utils_setup_logo(Frame_logo)
        
    def f_setup_Label_Name(self):
        # Create a frame for the name of the slip
        Name_Label_Frame = tk.Frame(self, width=100, height=100, bd=0, relief='flat')
        Name_Label_Frame.pack(fill='both', expand=True)
        # Create a label for the name of the slip
        Name_label = cls_my_label_num_02_title_H1(Name_Label_Frame, text=self.name_of_slip)
        Name_label.place(relx=0.5, rely=0.5, anchor="center")
        
class cls_Frame_Footer(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._f_setup_frame_style()
        self._f_create_footer_labels()
    
    def _f_setup_frame_style(self):
        super().f_setup_style_of_frame()
        self.configure(height=40, bd=0, relief='flat')
    
    def _f_create_footer_labels(self):
        # Label for "All Rights Reserved" message
        tk.Label(
            self,
            text="© 2025 Tuan An Group. All Rights Reserved."
        ).pack()
    
        # Label for notifications
        self.footer_notification = tk.Label(self, text="Notification")
        self.footer_notification.place(x=0, y=0)
        
    def f_update_notification(self, text="", fg="dark"):
        """Update the notification label with new text and foreground color."""
        self.footer_notification.config(text=text, fg=fg)
        
class cls_Frame_Body(cls_Frame_Main):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.f_setup_style_of_frame()
    
    def f_setup_style_of_frame(self):
        super().f_setup_style_of_frame()
        self.configure(bd=0, relief='flat')
        
class cls_Frame_date_and_number_of_slip(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0)

        # Create grid layout inside the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Add Row, Date, and Number of Slips
        self.create_widgets()

    def create_widgets(self):
        # Get today's date in dd/mm/yyyy format
        today = f_utils_get_formatted_today_YYYY_MM_DD("%d/%m/%Y")

        # Date Label and Entry
        tk.Label(self, text="Ngày:", bg=BG_COLOR_0_0).pack(side="left", padx=(0, 2))
        self.date_entry = cls_my_date_time_entry_num_01(self, name="date_entry")
        self.date_entry.config(state="normal")
        self.date_entry.insert(0, today)
        self.date_entry.config(state="readonly")
        self.date_entry.pack(side="left")

        # Number of Slips Label and Entry
        tk.Label(self, text="Số chứng từ:", bg=BG_COLOR_0_0).pack(side="left", padx=(5, 2))
        self.slips_entry = cls_my_text_entry_num_01(self, name="slips_entry")
        self.slips_entry.pack(side="left")
        
        # Load 48x48 icon
        icon_path = os.path.join(PATH_ASSETS_ICONS, "refresh_icon.png")
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((20, 20))  # change the size here
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.icon_photo = icon_photo
        
        # Small Refresh Button with Icon
        refresh_button = tk.Button(self,
                                   image=self.icon_photo, 
                                   borderwidth=0.5,
                                   name="refresh_number_of_slip_button")
        refresh_button.pack(side="left", padx=(5, 0))
        
class cls_Frame_client_information(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Configure initial appearance
        self.config(bg=BG_COLOR_0_0, width=200, height=200, bd=1, relief="groove")
        