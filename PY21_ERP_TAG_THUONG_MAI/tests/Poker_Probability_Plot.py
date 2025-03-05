import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

ctrl_pressed = False  # Global variable to track if Ctrl is pressed

def on_key_press(event):
    global ctrl_pressed
    if event.keysym == 'Control_L' or event.keysym == 'Control_R':
        ctrl_pressed = True

def on_key_release(event):
    global ctrl_pressed
    if event.keysym == 'Control_L' or event.keysym == 'Control_R':
        ctrl_pressed = False

def update_chips_won(*args):
    try:
        chips_won_input.configure(state='normal')  # Unlock Chips Won for updates
        chips_lost = float(chips_lost_input.get())
        num_members = int(row1_input.get())

        if num_members < 2:
            result_label.config(text="Error: Number of players must be at least 2.")
            return

        chips_won = chips_lost * (num_members - 1)
        chips_won_input.delete(0, tk.END)
        chips_won_input.insert(0, f"{chips_won:.2f}")
        chips_won_input.configure(state='readonly')  # Lock Chips Won after update
    except ValueError:
        result_label.config(text="Error: Invalid input for Chips Lost or Number of Players.")
        chips_won_input.configure(state='readonly')  # Ensure it remains readonly

def calculate_ev():
    try:
        win_rate_percentage = float(win_rate_input.get())
        chips_lost = float(chips_lost_input.get())
        chips_won = float(chips_won_input.get())

        # Validate win_rate_percentage
        if not (1 <= win_rate_percentage <= 100):
            result_label.config(text="Error: Win rate must be between 1 and 100.")
            return

        win_rate = win_rate_percentage / 100  # Convert to 0-1 scale
        lose_rate = 1 - win_rate

        ev = chips_won * win_rate - chips_lost * lose_rate
        ev_label.config(text=f"Expected Value (EV): {ev:.2f} chips")
    except ValueError:
        result_label.config(text="Error: Invalid input for EV calculation. Please enter valid numbers.")

def plot_data():
    try:
        # Get user input for the number of elements in row 1
        num_elements = int(row1_input.get())
        win_rate_percentage = float(win_rate_input.get())

        # Validate win_rate_percentage
        if not (1 <= win_rate_percentage <= 100):
            result_label.config(text="Error: Win rate must be between 1 and 100.")
            return

        win_rate = win_rate_percentage / 100  # Convert to 0-1 scale

        # Calculate the maximum number of players
        max_players = (52 - 5) // 2  # Total cards minus community cards divided by 2 per player

        if num_elements < 2 or num_elements > max_players:
            result_label.config(text=f"Error: Enter a value between 2 and {max_players}.")
            return

        # Generate row 1 and row 2 values
        row1 = list(range(2, num_elements + 1))  # Ensure num_elements points are generated
        row2 = [100 / r for r in row1]

        # Clear previous plot
        for widget in plot_frame.winfo_children():
            widget.destroy()

        # Create a new figure for the plot
        fig, ax = plt.subplots(figsize=(6, 4))
        scatter = ax.plot(row1, row2, marker='o', linestyle='-', color='blue', picker=True, pickradius=5)[0]

        # Add percentage labels for each point with offset
        texts = []
        for x, y in zip(row1, row2):
            text = ax.text(x, y + 5, f"{y:.2f}%", fontsize=9, ha='center', va='bottom', alpha=1.0)  # Initially visible
            texts.append(text)

        # Add horizontal line for win rate
        # ax.axhline(y=win_rate * 100, color='red', linestyle='--', label=f'Your Win Rate: {win_rate_percentage:.2f}%')
        ax.axhline(y=win_rate * 100, color='red', linestyle='--', label=f'Tỷ lệ thắng sau khi chia bài: {win_rate_percentage:.2f}%')
        ax.legend()

        ax.set_xlabel("Số người chơi")
        # ax.set_ylabel("Probability (%) (Row 2)")
        ax.set_ylabel("Xác suất thắng")
        # ax.set_title("Probability vs Number of Players")
        ax.set_title("Xác suất thắng theo số người chơi")
        ax.grid(True, linestyle='--', alpha=0.7)

        selected_points = set()  # To track selected points

        # Function to highlight points on click
        def on_pick(event):
            global ctrl_pressed

            if not ctrl_pressed:  # Clear all selections if Ctrl is not held
                selected_points.clear()

            ind = event.ind[0]  # Get the index of the clicked point
            if ind in selected_points:
                selected_points.remove(ind)  # Deselect if already selected
            else:
                selected_points.add(ind)

            for i, text in enumerate(texts):
                text.set_alpha(1.0 if i in selected_points else 0.0)  # Show selected, hide others

            canvas.draw()

        # Connect the pick event
        fig.canvas.mpl_connect('pick_event', on_pick)

        # Embed the plot in the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        result_label.config(text="Plot generated successfully.")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please enter valid numbers.")

# Tkinter GUI setup
root = tk.Tk()
root.title("Probability Plotter")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input: Number of elements in row 1
row1_label = ttk.Label(frame, text="Number of Players (Row 1 Count, 2-22):")
row1_label.grid(row=0, column=0, sticky=tk.W, pady=5)

row1_input = ttk.Entry(frame, width=50)
row1_input.insert(0, "9")
row1_input.grid(row=0, column=1, pady=5)
row1_input.bind("<KeyRelease>", update_chips_won)

# Input: Win rate
win_rate_label = ttk.Label(frame, text="Your Win Rate (1-100):")
win_rate_label.grid(row=1, column=0, sticky=tk.W, pady=5)

win_rate_input = ttk.Entry(frame, width=50)
win_rate_input.insert(0, "50")
win_rate_input.grid(row=1, column=1, pady=5)

# Input: Chips lost
chips_lost_label = ttk.Label(frame, text="Chips Lost:")
chips_lost_label.grid(row=2, column=0, sticky=tk.W, pady=5)

chips_lost_input = ttk.Entry(frame, width=50)
chips_lost_input.insert(0, "100")
chips_lost_input.grid(row=2, column=1, pady=5)
chips_lost_input.bind("<KeyRelease>", update_chips_won)

# Input: Chips won
chips_won_label = ttk.Label(frame, text="Chips Won:")
chips_won_label.grid(row=3, column=0, sticky=tk.W, pady=5)

chips_won_input = ttk.Entry(frame, width=50)
chips_won_input.insert(0, "800")
chips_won_input.grid(row=3, column=1, pady=5)
chips_won_input.configure(state='readonly')

# EV label
ev_label = ttk.Label(frame, text="Expected Value (EV):", foreground="green")
ev_label.grid(row=4, column=0, columnspan=2, pady=5)

# Plot button
plot_button = ttk.Button(frame, text="Generate Plot", command=plot_data)
plot_button.grid(row=5, column=0, columnspan=2, pady=10)

# EV button
ev_button = ttk.Button(frame, text="Calculate EV", command=calculate_ev)
ev_button.grid(row=6, column=0, columnspan=2, pady=10)

# Result label
result_label = ttk.Label(frame, text="", foreground="blue")
result_label.grid(row=7, column=0, columnspan=2, pady=5)

# Frame for the plot
plot_frame = ttk.Frame(root, padding=10, relief=tk.SUNKEN)
plot_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Bind key press and release events
root.bind('<KeyPress>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

root.mainloop()
