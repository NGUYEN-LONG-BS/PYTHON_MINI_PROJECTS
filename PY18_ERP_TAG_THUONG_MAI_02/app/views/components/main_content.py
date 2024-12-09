# Project/views/components/main_content.py
import tkinter as tk

class cls_MainContainer:
    def __init__(self, parent, content_type="statistics"):
        """
        Constructor to initialize the main content area of the dashboard.
        It calculates the dynamic width and updates content based on the content_type.
        """
        self.parent = parent
        self.content_type = content_type

        # Create the main content frame
        self.container_frame = tk.Frame(self.parent, bg="white")
        
        self.left_menu_frame = tk.Frame(self.container_frame, bg="white")
        self.left_menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        self.main_content_frame = tk.Frame(self.container_frame, bg="white")
        self.main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        
        self.right_banner_frame = tk.Frame(self.container_frame, bg="white")
        self.right_banner_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

        # Update width on initialization
        self.update_main_content_width()

        # Bind the resizing event
        self.parent.bind("<Configure>", self.on_resize)

    def update_main_content_width(self):
        """
        Updates the width of the main content dynamically based on the parent window's width.
        """
        parent_width = self.parent.winfo_width()  # Get the parent window width
        left_menu_width = self.left_menu_frame.winfo_width()  # Get left menu width
        right_banner_width = self.right_banner_frame.winfo_width()  # Get right banner width

        # Calculate the available width for the main content
        available_width = parent_width - left_menu_width - right_banner_width

        # Update the width of the main content frame
        self.main_content_frame.config(width=available_width)

    def on_resize(self, event):
        """
        Event handler to handle window resizing. It updates the width when the window is resized.
        """
        self.update_main_content_width()

    def create_content(self):
        """
        Creates content dynamically based on the content_type.
        """
        if self.content_type == "default":
            main_content_label = tk.Label(self.main_content_frame, text="Welcome to the Dashboard!", font=("Arial", 16))
            main_content_label.pack(pady=20)
        elif self.content_type == "statistics":
            main_content_label = tk.Label(self.main_content_frame, text="Statistics Overview", font=("Arial", 16))
            main_content_label.pack(pady=20)
            # Add more widgets for statistics content here
        elif self.content_type == "settings":
            main_content_label = tk.Label(self.main_content_frame, text="Settings Page", font=("Arial", 16))
            main_content_label.pack(pady=20)
            # Add more widgets for settings content here
        else:
            main_content_label = tk.Label(self.main_content_frame, text="Default Content", font=("Arial", 16))
            main_content_label.pack(pady=20)

    def get_frame(self):
        """
        Returns the frame containing the main content.
        """
        return self.main_content_frame
