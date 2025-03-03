import tkinter as tk

def create_main_content(parent, left_menu_frame, right_banner_frame, content_type="statistics"):
    """
    Function to create the main content area of the dashboard.
    The main content width will be calculated dynamically based on the parent width.
    """
    # Create the main content frame
    main_content_frame = tk.Frame(parent, bg="white")
    main_content_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

    # Function to update the width of the main content dynamically
    def update_main_content_width():
        parent_width = parent.winfo_width()  # Get the parent window width
        left_menu_width = left_menu_frame.winfo_width()  # Get left menu width
        right_banner_width = right_banner_frame.winfo_width()  # Get right banner width

        # Calculate the available width for the main content
        available_width = parent_width - left_menu_width - right_banner_width
        
        # Update the width of the main content frame
        main_content_frame.config(width=available_width)

    # Call the function to adjust the width initially
    update_main_content_width()

    # Dynamically adjust the main content width when the parent window is resized
    parent.bind("<Configure>", lambda event: update_main_content_width())

    # Different content based on the content_type parameter
    if content_type == "default":
        main_content_label = tk.Label(main_content_frame, text="Welcome to the Dashboard!", font=("Arial", 16))
        main_content_label.pack(pady=20)
    elif content_type == "statistics":
        main_content_label = tk.Label(main_content_frame, text="Statistics Overview", font=("Arial", 16))
        main_content_label.pack(pady=20)
        # Add more widgets for statistics content here
    elif content_type == "settings":
        main_content_label = tk.Label(main_content_frame, text="Settings Page", font=("Arial", 16))
        main_content_label.pack(pady=20)
        # Add more widgets for settings content here
    else:
        main_content_label = tk.Label(main_content_frame, text="Default Content", font=("Arial", 16))
        main_content_label.pack(pady=20)

    return main_content_frame
