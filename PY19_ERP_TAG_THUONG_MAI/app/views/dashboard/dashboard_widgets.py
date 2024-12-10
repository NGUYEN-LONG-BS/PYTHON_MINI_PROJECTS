import tkinter as tk

class DashboardWidgets:
    def __init__(self, master):
        self.master = master

    def create_widgets(self):
        # Example widget: a simple button
        self.button = tk.Button(self.master, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        print("Button clicked!")
