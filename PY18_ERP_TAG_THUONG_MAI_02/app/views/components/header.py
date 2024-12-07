# Project/views/components/header.py
import tkinter as tk

# def create_header(parent, title="TUẤN ÂN GROUP"):
#     header_frame = tk.Frame(parent)
#     header_frame.pack(side=tk.TOP, fill=tk.X)
    
#     header_label = tk.Label(header_frame, text=title, font=("Arial", 20))
#     header_label.pack()
    
#     return header_frame


class cls_Header:
    def __init__(self, master):
        self.master = master
        self.header_frame = tk.Frame(self.master, bg="lightblue", height=50)
        self.header_frame.pack(fill=tk.X)

        self.create_header()


    def create_header(self):
        header_frame = tk.Frame(self)
        header_frame.pack(side=tk.TOP, fill=tk.X)
        
        header_label = tk.Label(header_frame, text="title", font=("Arial", 20), bg="lightblue")
        header_label.pack()
        
        # Example header with a title and placeholder buttons
        title = tk.Label(header_frame, text="My Application", font=("Arial", 18), bg="lightblue")
        title.pack(side=tk.LEFT, padx=10)

        logout_button = tk.Button(header_frame, text="Logout", command=self.logout)
        logout_button.pack(side=tk.RIGHT, padx=10)
        
        return header_frame

    def logout(self):
        print("Logging out...")
