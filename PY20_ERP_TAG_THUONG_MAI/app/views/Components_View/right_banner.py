# Project/views/components/right_banner.py
import tkinter as tk

def create_right_banner(parent):
    # Create a frame for the right banner
    right_banner_frame = tk.Frame(parent, bg="lightgray", width=200, height=500)
    right_banner_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Label for the banner
    right_banner_label = tk.Label(right_banner_frame, text="Ad Banner Here", bg="lightgray")
    right_banner_label.pack(fill=tk.Y, padx=10)

    # Function to display the right banner if the mouse is within 10px of the right edge
    def show_right_banner(event):
        mouse_x = event.x
        # Check if the mouse is within 10px of the right edge of the window
        if mouse_x >= parent.winfo_width() - 10:  # 10px from the right edge
            right_banner_frame.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Function to hide the right banner when the mouse leaves the banner area
    def hide_right_banner(event):
        mouse_x = event.x
        # Hide the banner if the mouse is outside the right banner (banner width is 200px)
        if mouse_x < parent.winfo_width() - 200:  # Mouse is outside the right banner
            right_banner_frame.pack_forget()
            # print("Right banner hidden")

    # Function to keep the right banner visible when hovering over it
    def keep_banner_visible(event):
        mouse_x = event.x
        if mouse_x >= parent.winfo_width() - 200:  # While the mouse is inside the right banner (banner width is 200px)
            right_banner_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Bind the mouse motion on the parent window to show the right banner when hovering near the right edge
    parent.bind("<Motion>", show_right_banner)

    # Bind the mouse leave event on the right banner itself to hide it
    right_banner_frame.bind("<Leave>", hide_right_banner)

    # Bind mouse motion inside the banner to keep it visible
    right_banner_frame.bind("<Motion>", keep_banner_visible)

    # Initially hide the banner
    right_banner_frame.pack_forget()  # Banner is hidden at the start

    return right_banner_frame
