import os
import tkinter as tk
from PIL import Image, ImageTk  # Import Image and ImageTk for Tkinter compatibility

def setup_logo(parent_frame):
    # Get the project root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Going two levels up
    
    # Load the logo images
    logo_path_light = os.path.join(project_root, "assets/img/logo-Light.jpg")
    logo_path_dark = os.path.join(project_root, "assets/img/logo-Dark.jpg")
    
    try:
        # Try loading the light mode image first
        logo_image_light = Image.open(logo_path_light)
        logo_image_dark = Image.open(logo_path_dark)
        
        # Convert the PIL image to a Tkinter-compatible photo image
        logo_image_light_tk = ImageTk.PhotoImage(logo_image_light)
        logo_image_dark_tk = ImageTk.PhotoImage(logo_image_dark)
        
        # Store the image as an attribute of the parent_frame (to prevent it from being garbage collected)
        parent_frame.logo_image_light = logo_image_light_tk
        parent_frame.logo_image_dark = logo_image_dark_tk
        
        # Create the tk.Label and display the image
        logo_label = tk.Label(parent_frame, image=logo_image_light_tk)
        logo_label.pack()  # Using pack to add it to the parent_frame

    except FileNotFoundError:
        print(f"Logo file not found at {logo_path_light} or {logo_path_dark}")
        error_label = tk.Label(parent_frame, text="Logo not found", font=("", 16))
        error_label.pack()
