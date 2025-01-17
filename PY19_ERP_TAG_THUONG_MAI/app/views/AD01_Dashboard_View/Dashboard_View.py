import tkinter as tk
from Components_View import *
from utils import *
# cls_base_form_number_05_DashBoard_init
# class cls_Dashboard_View(cls_base_form_number_03_DashBoard):
class cls_Dashboard_View(cls_base_form_number_05_DashBoard_init):
    def __init__(self):
        title = "AD0101 - DashboardView"
        super().__init__(title_of_form=title)
        # self.f_add_content_to_left_frame()
        # self.f_add_content_to_right_frame()
    
    def f_add_content_to_left_frame(self):
        # Example content for left frame
        tk.Label(self.frame_left_body, text="Navigation Menu", bg="yellow", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_left_body, text="Home", width=20).pack(pady=5)
        tk.Button(self.frame_left_body, text="Profile", width=20).pack(pady=5)
        tk.Button(self.frame_left_body, text="Settings", width=20).pack(pady=5)
        
    def f_add_content_to_right_frame(self):
        # Example content for right frame
        tk.Label(self.frame_right_body, text="Notifications", bg="green", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.frame_right_body, text="You have 3 new messages", bg="green").pack(pady=5)
        tk.Label(self.frame_right_body, text="Your profile was viewed 5 times", bg="green").pack(pady=5)