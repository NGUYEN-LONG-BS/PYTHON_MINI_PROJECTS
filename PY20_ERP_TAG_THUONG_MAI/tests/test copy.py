import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create the main Tkinter window
root = tk.Tk()
root.title("Chart in a Frame")
root.geometry("800x600")

# Create a frame to hold the chart
chart_frame = ttk.Frame(root, padding="10", borderwidth=2, relief="solid")
chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create a Matplotlib figure and plot
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Line")
ax.set_title("Sample Chart")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()

# Embed the Matplotlib figure into the Tkinter frame
canvas = FigureCanvasTkAgg(fig, master=chart_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

# Add a button to refresh the chart
def refresh_chart():
    ax.clear()
    ax.plot([1, 2, 3, 4], [30, 20, 15, 10], label="Updated Line", color="red")
    ax.set_title("Updated Chart")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.legend()
    canvas.draw()

refresh_button = ttk.Button(root, text="Refresh Chart", command=refresh_chart)
refresh_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
