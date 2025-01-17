import tkinter as tk
from Components_View import *
from Components_View.menu_top import cls_menu_top
from utils import *
from utils.define import *
from PIL import Image, ImageTk

class cls_base_form_number_05_DashBoard_init(tk.Tk):
    def __init__(self, title_of_form="Default Title", name_of_slip="TẬP ĐOÀN TUẤN ÂN"):
        super().__init__()  # Gọi phương thức __init__ của lớp cha
        
        # Set up window initial properties
        self.name_of_slip = name_of_slip
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
        f_utils_set_window_size_is_4_per_5_screen(self, 0, 0)
        f_utils_set_center_screen(self)
        try:
            f_utils_setup_fav_icon(self)
        except Exception as e:
            print(f"Error setting up favicon: {e}")
    
    def f_Goi_Cac_Thanh_Phan_Tai_Su_Dung(self):
        """Initializes reusable components."""
        try:
            # Add cls_menu_top
            cls_menu_top(self)

            # Add cls_Frame_Main
            self.frame_main = cls_Frame_Main(self)
            self.frame_main.grid(row=0, column=0, sticky="nsew")
            # Configure grid weights for resizing
            self._configure_grid_weights_of_self()
            
            # Add elements to frame_info_of_slip
            self.f_add_elements_to_frame_main()
            
        except Exception as e:
            print(f"Error initializing components: {e}")

    def _close_window_Click(self):
        self.destroy()
        from app.views.AD00_User_Management_View.AD0001_login_View import cls_Login_View
        # Gọi cửa sổ LoginView
        login_window = cls_Login_View()
        login_window.mainloop()
    
    def f_add_elements_to_frame_main(self):
        # Add elements to frame_main
        Frame_Header = cls_Frame_Header(self.frame_main, name_of_slip=self.name_of_slip)
        Frame_Header.grid(row=0, column=0, sticky="ew")
        
        self.Frame_Body = cls_Frame_Body(self.frame_main)
        self.Frame_Body.grid(row=1, column=0, sticky="nsew")
              
        self.Frame_Footer = cls_Frame_Footer(self.frame_main)
        self.Frame_Footer.grid(row=2, column=0, sticky="ew")
        
        # Add elements to frame_body
        self.f_add_elements_to_frame_body()
                    
    def f_add_elements_to_frame_body_02(self):
        # Cấu hình số dòng và cột
        rows = 2
        columns = 3

        # Đường dẫn đến ảnh mẫu (thay đổi thành đường dẫn ảnh của bạn)
        image_path = PATH_CARD_IMG  # Đặt ảnh của bạn tại đây

        # Mở và resize ảnh
        img = Image.open(image_path)
        img = img.resize((200, 140))  # Điều chỉnh kích thước ảnh phù hợp với card
        img_tk = ImageTk.PhotoImage(img)

        for row in range(rows):
            for col in range(columns):
                # Tạo một frame cho từng "card"
                card = tk.Frame(
                    self.Frame_Body,
                    bg="lightblue",
                    width=300,
                    height=240,
                    highlightbackground="gray",
                    highlightthickness=1,
                )
                card.grid(row=row, column=col, padx=10, pady=10)

                # Thêm label chứa hình ảnh vào card
                image_label = tk.Label(card, image=img_tk, bg="lightblue")
                image_label.image = img_tk  # Lưu tham chiếu để tránh ảnh bị thu hồi
                image_label.pack(pady=5)

                # Thêm label chứa text vào card
                text_label = tk.Label(card, text=f"Card {row * columns + col + 1}", bg="lightblue", font=("Arial", 12))
                text_label.pack()
        print("tạo dashboard xong")
        
    def f_add_elements_to_frame_body(self):
        # Số dòng và cột
        rows = 2
        columns = 3

        # Center-align the grid
        self.Frame_Body.grid_rowconfigure(tuple(range(rows)), weight=1)  # Center vertically
        self.Frame_Body.grid_columnconfigure(tuple(range(columns)), weight=1)  # Center horizontally

        # Danh sách hình ảnh và nội dung cho mỗi card
        cards_data = [
            {"image": PATH_CARD_IMG, "text": "KINH DOANH"},
            {"image": PATH_CARD_IMG, "text": "VẬT TƯ"},
            {"image": PATH_CARD_IMG, "text": "KỸ THUẬT"},
            {"image": PATH_CARD_IMG, "text": "KHO"},
            {"image": PATH_CARD_IMG, "text": "TÀI CHÍNH"},
            {"image": PATH_CARD_IMG, "text": "NHÂN SỰ"},
        ]

        # Load và resize ảnh
        images = []
        for card_data in cards_data:
            img = Image.open(card_data["image"])
            img = img.resize((100, 70))  # Điều chỉnh kích thước ảnh phù hợp với card
            img_tk = ImageTk.PhotoImage(img)
            images.append(img_tk)  # Lưu ảnh để tránh bị thu hồi

        # Thêm card vào frame_body
        for index, card_data in enumerate(cards_data):
            row = index // columns
            col = index % columns

            # Tạo một frame cho từng "card"
            card = tk.Frame(
                self.Frame_Body,
                bg=BG_COLOR_0_0,
                width=150,
                height=150,
                highlightbackground="gray",
                highlightthickness=1,
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Thêm label chứa hình ảnh vào card
            image_label = tk.Label(card, image=images[index], bg=BG_COLOR_0_0)
            image_label.image = images[index]  # Lưu tham chiếu để tránh ảnh bị thu hồi
            image_label.pack(pady=5)

            # Thêm label chứa text vào card
            text_label = tk.Label(card, text=card_data["text"], bg=BG_COLOR_0_0, font=("Arial", 12))
            text_label.pack()
        
    
    def _configure_grid_weights_of_self(self):
        """Configures grid weights for resizing."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Ensure proper layout for the main frame
        frame_main = self.children.get('!cls_frame_main', None)
        if frame_main:
            frame_main.rowconfigure(0, weight=0)  # Header
            frame_main.rowconfigure(1, weight=1)  # Body
            frame_main.rowconfigure(2, weight=0)  # Footer
            frame_main.columnconfigure(0, weight=1)
        

        