import tkinter as tk

def create_notification(parent, message="This is a notification!"):
    notification_frame = tk.Frame(parent, bg="lightblue", padx=10, pady=5)
    notification_frame.pack(side=tk.TOP, fill=tk.X)
    
    notification_label = tk.Label(notification_frame, text=message, fg="black")
    notification_label.pack()
    
    return notification_frame
