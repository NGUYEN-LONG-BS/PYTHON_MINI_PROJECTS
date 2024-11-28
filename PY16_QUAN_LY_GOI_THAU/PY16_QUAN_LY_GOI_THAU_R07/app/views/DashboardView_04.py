# Project/Views/DashboardView_04.py
import tkinter as tk

def create_layout():
    # Create the main window
    root = tk.Tk()
    root.title("3 Frame Layout with Top and Bottom")

    # Set the size of the window
    root.geometry("800x600")

    # Create Top Frame
    top_frame = tk.Frame(root, bg="lightgray", height=100)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    # Add a label to Top Frame
    top_label = tk.Label(top_frame, text="Top Frame", bg="lightgray", font=("Arial", 14))
    top_label.pack(padx=20, pady=20)

    # Create Bottom Frame
    bottom_frame = tk.Frame(root, bg="lightgray", height=100)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    # Add a label to Bottom Frame
    bottom_label = tk.Label(bottom_frame, text="Bottom Frame", bg="lightgray", font=("Arial", 14))
    bottom_label.pack(padx=20, pady=20)

    # Create a container frame to hold the 3 middle frames
    middle_frame_container = tk.Frame(root)
    middle_frame_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create Left Frame
    left_frame = tk.Frame(middle_frame_container, bg="lightblue")
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a label to Left Frame
    left_label = tk.Label(left_frame, text="Left Frame", bg="lightblue", font=("Arial", 14))
    left_label.pack(padx=20, pady=20)

    # Create Middle Frame
    middle_frame = tk.Frame(middle_frame_container, bg="lightgreen")
    middle_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a label to Middle Frame
    middle_label = tk.Label(middle_frame, text="Middle Frame", bg="lightgreen", font=("Arial", 14))
    middle_label.pack(padx=20, pady=20)

    # Create Right Frame
    right_frame = tk.Frame(middle_frame_container, bg="lightcoral")
    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a label to Right Frame
    right_label = tk.Label(right_frame, text="Right Frame", bg="lightcoral", font=("Arial", 14))
    right_label.pack(padx=20, pady=20)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_layout()
