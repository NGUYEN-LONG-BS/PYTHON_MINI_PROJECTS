# setupWindowSize.py
import tkinter as tk

def set_window_size(root):      #, window_width=1600, window_height=900
    # =======================================================================================================================
    # Get the screen height and width
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Set the window height to 4/5 of the screen height
    window_height = int(4 * screen_height / 5)
    # Set the window width (you can adjust as needed)
    window_width = window_height // 9 * 16
    # Calculate the position to center the window
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)
    # Set the window geometry (centered window)
    # print(window_width)
    # print(window_height)
    # print(x_position)
    # print(y_position)
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")