import tkinter as tk
from app.utils import *
from . import menu_top
from . import frame

class cls_base_form_number_03_DashBoard(tk.Tk):
    def __init__(self, title_of_form="Default Title"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        self.title_of_form = title_of_form
        self.title(self.title_of_form)
        
        # Set up favicon and window configuration
        f_utils_setup_fav_icon(self)
        self.f_Thiet_lap_Kich_thuoc_Cua_So()
        
        # Set up reusable components
        self.f_Goi_Cac_Thanh_Phan_Tai_Su_Dung()
        
        # Bind close event
        parent_window = self.winfo_toplevel()
        parent_window.protocol("WM_DELETE_WINDOW", self._close_window_Click)
        
        # Store a reference to scheduled animations so they can be cancelled if needed
        self.animations = []
    
    def f_Thiet_lap_Kich_thuoc_Cua_So(self):
        """Configures window size and position."""
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(self, maximize=True)
        f_utils_set_center_screen(self)
        try:
            f_utils_setup_fav_icon(self)
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
    
    def f_Goi_Cac_Thanh_Phan_Tai_Su_Dung(self):
        """Initializes reusable components."""
        try:
            # Add cls_menu_top
            menu_top.cls_menu_top(self)

            self.frame_main = frame.cls_Frame_Main(self)
            self.frame_main.grid(row=0, column=0, sticky="nsew")
            
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()
            
            # Add elements to frame_info_of_slip
            self.f_add_elements_to_frame_main()
            
        except Exception as e:
            print(f"Error: {e}")
            print("Error at function: ", f_utils_get_current_function_name())
    
    def _configure_grid_weights_of_self(self):
        """Configures grid weights for resizing."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Ensure proper layout for the main frame
        frame_main = self.children.get('!cls_frame_main', None)
        if frame_main:
            frame_main.rowconfigure(0, weight=1)
            frame_main.columnconfigure(0, weight=1)
        
            
    def _close_window_Click(self):
        self.destroy()
        from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View
        # Gọi cửa sổ LoginView
        login_window = cls_Login_View()
        login_window.mainloop()
    
    def f_add_elements_to_frame_main(self):
        # Create 3 Frame
        self.frame_left_body = tk.Frame(self.frame_main, bg=COLOR_HIGHLIGHT_LIGHT_ORANGE, width=10)
        self.frame_right_body = tk.Frame(self.frame_main, bg=COLOR_HIGHLIGHT_LIGHT_GREEN, width=10)

        left_width = 200
        right_width = 200
        middle_width = self.frame_main.winfo_width() - 10 - 10

        # Initially, we set their width to 10
        self.frame_left_body.grid_propagate(False)  # Disable automatic resizing
        self.frame_right_body.grid_propagate(False)  # Disable automatic resizing

        # Initially, the middle frame will take the remaining width
        self.frame_middle_body = tk.Frame(self.frame_main, bg=COLOR_BACKGROUND, width=middle_width)
        
         # Use the 'place' geometry manager to have more control over the position
        self.frame_left_body.place(x=10-left_width, y=0, width=left_width, height=self.frame_main.winfo_height())  # Initial position
        self.frame_middle_body.place(x=10, y=0, width=middle_width, height=self.frame_main.winfo_height())
        self.frame_right_body.place(x=self.frame_main.winfo_width() - 10, y=0, width=right_width, height=self.frame_main.winfo_height())

        # Pack frames
        self.frame_left_body.pack(side="left", fill="both", expand=False)
        self.frame_middle_body.pack(side="left", fill="both", expand=True)
        self.frame_right_body.pack(side="left", fill="both", expand=False)

        # Bind hover events
        # self.frame_left_body.bind("<Enter>", lambda event: self._frame_left_body_Hover())
        # self.frame_middle_body.bind("<Enter>", lambda event: self._frame_middle_body_Hover())
        # self.frame_right_body.bind("<Enter>", lambda event: self._frame_right_body_Hover())
        
    def _frame_left_body_Hover(self):
        # # unpack all elements in right body
        # self.f_unpack_all_elements_in_right_body()
        
        total_width = self.frame_main.winfo_width()
        left_width = 200
        right_width = 200
        middle_width = total_width - left_width - right_width + 190
        # self._animate_frame_width(self.frame_left_body, left_width)
        # self._animate_frame_width(self.frame_middle_body, middle_width)
        # self._animate_frame_width(self.frame_right_body, right_width)
        
        # Animation step for left body movement
        self._animate_frame_left_position(self.frame_left_body, -190)  # Move left by 190 pixels
        self._animate_frame_width(self.frame_middle_body, middle_width)
        self._animate_frame_width(self.frame_right_body, right_width)
        
        # self.f_re_pack_all_elements_in_left_body()

    def _frame_middle_body_Hover(self):
        # # unpack all elements in right and left body
        # self.f_unpack_all_elements_in_left_body()
        # self.f_unpack_all_elements_in_right_body()
        
        total_width = self.frame_main.winfo_width()
        left_width = 200
        right_width = 200
        middle_width = total_width - left_width - right_width + 190 + 190
        # self._animate_frame_width(self.frame_left_body, left_width)
        # self._animate_frame_width(self.frame_middle_body, middle_width)
        # self._animate_frame_width(self.frame_right_body, right_width)
        
        # Animation step for left body movement
        self._animate_frame_left_position(self.frame_left_body, -190)  # Move left by 190 pixels
        self._animate_frame_right_position(self.frame_right_body, 190)  # Move left by 190 pixels
        self._animate_frame_width(self.frame_middle_body, middle_width)

    def _frame_right_body_Hover(self):
        # # unpack all elements in left body
        # self.f_unpack_all_elements_in_left_body()
        
        total_width = self.frame_main.winfo_width()
        left_width = 200
        right_width = 200
        middle_width = total_width - left_width - right_width + 190
        # self._animate_frame_width(self.frame_left_body, left_width)
        # self._animate_frame_width(self.frame_middle_body, middle_width)
        # self._animate_frame_width(self.frame_right_body, right_width)
        
        # Animation step for left body movement
        self._animate_frame_right_position(self.frame_right_body, 190)  # Move left by 190 pixels
        self._animate_frame_width(self.frame_middle_body, middle_width)
        self._animate_frame_width(self.frame_right_body, right_width)
        
        # self.f_re_pack_all_elements_in_right_body()

    def _animate_frame_width(self, frame, target_width, step=2):
        current_width = frame.winfo_width()
        if current_width < target_width:
            new_width = min(current_width + step, target_width)
        elif current_width > target_width:
            new_width = max(current_width - step, target_width)
        else:
            return  # Animation complete

        frame.config(width=new_width)
        self.after(2, self._animate_frame_width, frame, target_width, step)
        
        
    def _animate_frame_left_position(self, frame, target_x, step=2):
        """Animate the position of the left frame to the target_x position."""
        current_x = frame.winfo_x()

        if current_x < target_x:
            new_x = min(current_x + step, target_x)
        elif current_x > target_x:
            new_x = max(current_x - step, target_x)
        else:
            return  # Animation complete

        frame.place(x=new_x)  # Update position

        self.after(2, self._animate_frame_left_position, frame, target_x, step)
        
    def _animate_frame_right_position(self, frame, target_x, step=2):
        """Animate the position of the left frame to the target_x position."""
        current_x = frame.winfo_x()

        if current_x < target_x:
            new_x = min(current_x + step, target_x)
        elif current_x > target_x:
            new_x = max(current_x - step, target_x)
        else:
            return  # Animation complete

        frame.place(x=new_x)  # Update position

        self.after(2, self._animate_frame_left_position, frame, target_x, step)
        
