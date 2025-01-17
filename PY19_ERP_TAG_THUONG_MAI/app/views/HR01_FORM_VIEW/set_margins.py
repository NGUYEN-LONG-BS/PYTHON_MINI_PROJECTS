import tkinter as tk
from tkinter import messagebox
import tempfile
from docx import Document
from docx.shared import Cm
from Components_View import *

class cls_hr01_view(cls_base_form_number_04_dashboard):
    def __init__(self):
        
        title = "HR00 | HÀNH CHÍNH - NHÂN SỰ"
        name = "HÀNH CHÍNH NHÂN SỰ"
        super().__init__(title_of_form=title, name_of_slip=name)
        self.f_create_widgets()
        # Set up all global variants
        self._f_setup_all_global_variants()
    
    def f_create_widgets(self):
        # Add a label
        label = tk.Label(self.Frame_Body, text="Set Default Word Margins", font=("Arial", 14))
        label.pack(pady=20)

        # Add a button to set margins
        set_margins_button = tk.Button(self.Frame_Body, text="Get Margins file", command=self.set_default_margins, font=("Arial", 12))
        set_margins_button.pack(pady=20)

    def _f_setup_all_global_variants(self):    
        # Timer interval (in milliseconds)
        self.last_click_time = 0
        self.double_click_interval = 0.3  # 300 ms
        self.label_footer = f_utils_tim_component_label_with_text(self, "Notification")
    
    def _f_config_notification(self, text="", fg="black"):
        self.label_footer.config(text=text, fg=fg)
    
    def set_default_margins(self):
        # Create a new Word document
        doc = Document()

        # Set the margins in centimeters
        section = doc.sections[0]
        section.left_margin = Cm(1)
        section.right_margin = Cm(1.5)
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)
        
        # Save the document
        file_name = "default_margins.docx"
        file_path = os.path.join(PATH_DEFAUL, file_name)
        doc.save(file_path)

        # Open the document without saving
        try:
            os.startfile(file_path)  # Opens the document with its associated application
            text = f"Document opened: {file_path}"
            self._f_config_notification(text=text, fg="blue")
        except Exception as e:
            text = f"Error opening document: {e}"
            self._f_config_notification(text=text, fg="red")