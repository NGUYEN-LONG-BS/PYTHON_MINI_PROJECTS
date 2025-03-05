import tkinter as tk

def create_left_menu(parent):
    # Create a frame for the left menu
    left_menu_frame = tk.Frame(parent, bg="#d3d3d3", width=200, height=500)
    left_menu_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    # Function to display the left menu if the mouse is within 10px from the left edge
    def show_left_menu(event):
        # Get the x-coordinate of the mouse
        mouse_x = event.x
        # Check if the mouse is within 10px of the left edge of the window
        if mouse_x <= 10:
            left_menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Function to hide the left menu when the mouse leaves the menu area
    def hide_left_menu(event):
        # Get the x-coordinate of the mouse
        mouse_x = event.x
        # Hide the menu if the mouse is outside the left menu area (menu width is 200px)
        if mouse_x > 200:  # Mouse is outside the left menu
            left_menu_frame.pack_forget()

    # Bind the events to show/hide the menu based on mouse position
    parent.bind("<Enter>", show_left_menu)  # Show the left menu when entering the window
    parent.bind("<Leave>", hide_left_menu)  # Hide the menu when the mouse leaves the window

    # Define the action functions for each menu item
    def function_home_main():
        print("Function_Home_Main selected")

    def function_qlgt_taomoi():
        print("Function_QLGT_TaoMoi selected")

    def function_qlgt_goithau_dalap():
        print("Function_QLGT_GoiThauDaLap selected")

    def function_qlycdh_tala():
        print("Function_QLYCDH_TALA selected")

    def function_qlycdh_tm():
        print("Function_QLYCDH_TM selected")

    def function_help_about():
        print("Function_Help_About selected")

    def function_help_userinfo():
        print("Function_Help_UserInfo selected")

    # Create menu buttons inside the left frame
    home_button = tk.Button(left_menu_frame, text="Home", bg="#828d8b", fg="#262544", command=function_home_main)
    home_button.pack(fill=tk.X, padx=10, pady=5)

    qlgt_button = tk.Button(left_menu_frame, text="Quản lý gói thầu", bg="#828d8b", fg="#262544")
    qlgt_button.pack(fill=tk.X, padx=10, pady=5)

    qlgt_taomoi_button = tk.Button(left_menu_frame, text="Tạo mới gói thầu", bg="#f0f0f0", fg="#262544", command=function_qlgt_taomoi)
    qlgt_taomoi_button.pack(fill=tk.X, padx=10, pady=5)

    qlgt_goithau_button = tk.Button(left_menu_frame, text="Các gói thầu đã lập", bg="#f0f0f0", fg="#262544", command=function_qlgt_goithau_dalap)
    qlgt_goithau_button.pack(fill=tk.X, padx=10, pady=5)

    qlycdh_button = tk.Button(left_menu_frame, text="Quản lý yêu cầu đặt hàng", bg="#828d8b", fg="#262544")
    qlycdh_button.pack(fill=tk.X, padx=10, pady=5)

    qlycdh_tala_button = tk.Button(left_menu_frame, text="Yêu cầu TALA", bg="#f0f0f0", fg="#262544", command=function_qlycdh_tala)
    qlycdh_tala_button.pack(fill=tk.X, padx=10, pady=5)

    qlycdh_tm_button = tk.Button(left_menu_frame, text="Yêu cầu TM", bg="#f0f0f0", fg="#262544", command=function_qlycdh_tm)
    qlycdh_tm_button.pack(fill=tk.X, padx=10, pady=5)

    help_button = tk.Button(left_menu_frame, text="Help", bg="#828d8b", fg="#262544")
    help_button.pack(fill=tk.X, padx=10, pady=5)

    about_button = tk.Button(left_menu_frame, text="About", bg="#828d8b", fg="#f0f0f0", command=function_help_about)
    about_button.pack(fill=tk.X, padx=10, pady=5)

    userinfo_button = tk.Button(left_menu_frame, text="User Info", bg="#828d8b", fg="#f0f0f0", command=function_help_userinfo)
    userinfo_button.pack(fill=tk.X, padx=10, pady=5)

    # Initially hide the menu
    left_menu_frame.pack_forget()  # Menu is hidden at the start

    return left_menu_frame
