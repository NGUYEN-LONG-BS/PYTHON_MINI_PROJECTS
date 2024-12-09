# Project/views/components/header.py
import tkinter as tk

class cls_Header:
    def __init__(self, master):
        self.master = master
        self.header_frame = tk.Frame(self.master, bg="lightblue", height=50)
        self.header_frame.pack(fill=tk.X)

        self.create_header()

    def create_header(self):
        header_frame = tk.Frame(
            self.master
            # ,bd=2
            # ,relief="solid"
            )
        header_frame.pack(side=tk.TOP, fill=tk.X)
        
        header_label = tk.Label(
            header_frame, 
            text="TUẤN ÂN GROUP", 
            font=("Arial", 20), 
            bg="lightblue")
        header_label.pack()

        logout_button = tk.Button(header_frame, text="Logout", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10)
        
        return header_frame

    def logout(self):
        print("Logging out...")
