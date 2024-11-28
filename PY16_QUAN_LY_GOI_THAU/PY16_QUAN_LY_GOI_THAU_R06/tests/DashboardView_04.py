# Project/Views/DashboardView_04.py
import tkinter as tk

def create_layout():
    # Create the main window
    root = tk.Tk()
    root.title("Responsive Frame Layout")
    
    # Set the size of the window
    root.geometry("800x600")

    # Create Top Frame
    top_frame = tk.Frame(root, bg="lightgray", height=100)
    top_frame.grid(row=0, column=0, sticky="ew")

    # Add a label to Top Frame
    top_label = tk.Label(top_frame, text="Top Frame", bg="lightgray", font=("Arial", 14))
    top_label.pack(padx=20, pady=20)

    # Create Bottom Frame
    bottom_frame = tk.Frame(root, bg="lightgray", height=100)
    bottom_frame.grid(row=2, column=0, sticky="ew")

    # Add a label to Bottom Frame
    bottom_label = tk.Label(bottom_frame, text="Bottom Frame", bg="lightgray", font=("Arial", 14))
    bottom_label.pack(padx=20, pady=20)

    # Create a container frame to hold the 3 middle frames
    middle_frame_container = tk.Frame(root)
    middle_frame_container.grid(row=1, column=0, sticky="nsew")

    # Configure grid weights so the middle section expands correctly
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create Left Frame
    left_frame = tk.Frame(middle_frame_container, bg="lightblue")
    left_frame.grid(row=0, column=0, sticky="nsew")

    # Add a label to Left Frame
    left_label = tk.Label(left_frame, text="Left Frame", bg="lightblue", font=("Arial", 14))
    left_label.pack(padx=20, pady=20)

    # Create Middle Frame
    middle_frame = tk.Frame(middle_frame_container, bg="lightgreen")
    middle_frame.grid(row=0, column=1, sticky="nsew")

    # Add a label to Middle Frame
    middle_label = tk.Label(middle_frame, text="Middle Frame", bg="lightgreen", font=("Arial", 14))
    middle_label.pack(padx=20, pady=20)

    # Create Right Frame
    right_frame = tk.Frame(middle_frame_container, bg="lightcoral")
    right_frame.grid(row=0, column=2, sticky="nsew")

    # Add a label to Right Frame
    right_label = tk.Label(right_frame, text="Right Frame", bg="lightcoral", font=("Arial", 14))
    right_label.pack(padx=20, pady=20)

    # Function to resize frames based on hover
    def resize_frames_on_hover(frame_hovered):
        total_width = root.winfo_width()  # Get the width of the main window
        if frame_hovered == "left":
            left_frame.grid_configure(weight=9)   # 90% of the width
            middle_frame.grid_configure(weight=0.5)  # 5% of the width
            right_frame.grid_configure(weight=0.5)  # 5% of the width
        elif frame_hovered == "middle":
            left_frame.grid_configure(weight=0.5)   # 5% of the width
            middle_frame.grid_configure(weight=9)   # 90% of the width
            right_frame.grid_configure(weight=0.5)  # 5% of the width
        elif frame_hovered == "right":
            left_frame.grid_configure(weight=0.5)   # 5% of the width
            middle_frame.grid_configure(weight=0.5)  # 5% of the width
            right_frame.grid_configure(weight=9)    # 90% of the width
        else:
            left_frame.grid_configure(weight=3)  # Reset to normal proportions
            middle_frame.grid_configure(weight=3)
            right_frame.grid_configure(weight=3)

        # Force the window to update its layout after changes
        root.update_idletasks()

    # Bind mouse enter and leave events to the frames
    left_frame.bind("<Enter>", lambda event: resize_frames_on_hover("left"))
    middle_frame.bind("<Enter>", lambda event: resize_frames_on_hover("middle"))
    right_frame.bind("<Enter>", lambda event: resize_frames_on_hover("right"))

    # Bind mouse leave events to reset the frame sizes
    left_frame.bind("<Leave>", lambda event: resize_frames_on_hover(None))
    middle_frame.bind("<Leave>", lambda event: resize_frames_on_hover(None))
    right_frame.bind("<Leave>", lambda event: resize_frames_on_hover(None))

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_layout()
