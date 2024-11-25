from customtkinter import *
from PIL import Image
from datetime import datetime
from app.controllers.KD01QuanLyGoiThauController import KD01QuanLyGoiThauController


# def create_KD01QuanLyGoiThauView():
#     app = CTk()
#     app.geometry("900x800")
#     app.title("QUẢN LÝ GÓI THẦU")

#     # Controller for managing app logic
#     controller = KD01QuanLyGoiThauController()
        
#     # ======================================================================================
#     # LABEL_SoThongBaoMoiThau
#     # ======================================================================================
#     LABEL_SoThongBaoMoiThau = CTkLabel(master=app, 
#                                     text="Số thông báo mời thầu"
#                                         ,font=("",18)
#                                     )
#     LABEL_SoThongBaoMoiThau.place(x=50, y=170)

#     # ======================================================================================
#     # LABEL_TenThuMucSeKhoiTao
#     # ======================================================================================
#     LABEL_TenThuMucSeKhoiTao = CTkLabel(master=app, 
#                                         text="24_GOI_THAU_0000_0000"
#                                         ,font=("",18)
#                                         )
#     LABEL_TenThuMucSeKhoiTao.place(x=390, y=200)

#     # ======================================================================================
#     # LABEL_NamGoiThau
#     # ======================================================================================
#     LABEL_NamGoiThau = CTkLabel(master=app
#                         ,text="Năm gói thầu"
#                         ,font=("",18)
#                         )
#     LABEL_NamGoiThau.place(x=50, y=70)

#     # ======================================================================================
#     # LABEL_DanhSachGoiThau
#     # ======================================================================================
#     LABEL_DanhSachGoiThau = CTkLabel(master=app
#                                         ,text="Danh sách gói thầu"
#                                         ,font=("",18)
#                                         )
#     LABEL_DanhSachGoiThau.place(x=50, y=270)

#     # ======================================================================================
#     # LABEL_IDNhanVien
#     # ======================================================================================
#     LABEL_IDNhanVien = CTkLabel(master=app
#                                 ,text="ID: TBD001"
#                                 ,font=("",13)
#                                 )
#     LABEL_IDNhanVien.place(x=50, y=10)

#     # ======================================================================================
#     # LABEL_TenNhanVien
#     # ======================================================================================
#     LABEL_TenNhanVien = CTkLabel(master=app
#                                 ,text="Họ tên: Nguyễn Văn B"
#                                 ,font=("",13)
#                                 )
#     LABEL_TenNhanVien.place(x=150, y=10)

#     # ======================================================================================
#     # LABEL_TenBoPhan
#     # ======================================================================================
#     LABEL_TenBoPhan = CTkLabel(master=app
#                             ,text="Bộ phận: Kinh doanh"
#                             ,font=("",13)
#                             )
#     LABEL_TenBoPhan.place(x=350, y=10)

#     # ======================================================================================
#     # LABEL_CapBac
#     # ======================================================================================
#     LABEL_CapBac = CTkLabel(master=app
#                             ,text="Cấp bậc: Nhân viên"
#                             ,font=("",13)
#                             )
#     LABEL_CapBac.place(x=550, y=10)

#     # ======================================================================================
#     # LABEL_TenCongTy
#     # ======================================================================================
#     LABEL_TenCongTy = CTkLabel(master=app
#                             ,text="Cty: Thiết bị điện"
#                             ,font=("",13)
#                             )
#     LABEL_TenCongTy.place(x=750, y=10)

#     # ======================================================================================
#     # ENTRY_SoThongBaoMoiThau
#     # ======================================================================================
#     ENTRY_SoThongBaoMoiThau = CTkEntry(master=app
#                                             ,placeholder_text="Start typing..."
#                                             ,width=300
#                                             # ,text_color="#FFCC70"
#                                             )
#     ENTRY_SoThongBaoMoiThau.place(x=50, y=200)
#     # ENTRY_SoThongBaoMoiThau.bind("<KeyRelease>", update_label)
#     ENTRY_SoThongBaoMoiThau.bind("<KeyRelease>")

#     # ======================================================================================
#     # COMBOBOX_NamGoiThau
#     # ======================================================================================
#     def change_handler(value):
#         last_02_chars = value[-2:]
#         print(f"Selected Value {value}, Last Two Characters: {last_02_chars}")
        
#     # Get the current year
#     current_year = datetime.now().year
#     # Create the array with the specified years
#     year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

#     COMBOBOX_NamGoiThau = CTkComboBox(master=app, 
#                         values=year_array,
#                         command=change_handler)

#     COMBOBOX_NamGoiThau.set(current_year)       # Set the default value to the current year
#     COMBOBOX_NamGoiThau.place(x=50, y=100)      # Place the combobox in the window
    
#     # ======================================================================================
#     # SWITCH_DarkLightMode
#     # ======================================================================================
    
#     # Switch for dark/light mode
#     def switch_mode():
#         current_mode = get_appearance_mode()
#         new_mode = "dark" if current_mode == "Light" else "light"
#         set_appearance_mode(new_mode)
#         controller.save_default_settings(new_mode, "theme_01")

#     SWITCH_DarkLightMode = CTkSwitch(app, text="Dark Mode", command=switch_mode)
#     SWITCH_DarkLightMode.place(x=500, y=700)

#     # ======================================================================================
#     # COMBOBOX_ChangeTheme
#     # ======================================================================================
#     # Combobox for theme selection
#     themes = ["MoonlitSky", "NeonBanana", "DaynNight"]
#     COMBOBOX_ChangeTheme = CTkComboBox(app, values=themes, command=controller.change_theme)
#     COMBOBOX_ChangeTheme.place(x=650, y=700)

#     # ======================================================================================
#     # BTN_TaoThuMucMoi
#     # ======================================================================================
#     # Button to create a new folder
#     def on_create_folder():
#         controller.create_folder()
#     BTN_TaoThuMucMoi = CTkButton(app, text="Tạo thư mục mới", command=on_create_folder)
#     BTN_TaoThuMucMoi.place(x=50, y=700)

#     # ======================================================================================
#     # scrollable_frame_01
#     # ======================================================================================
#     # Scrollable frame for displaying folder contents
#     scrollable_frame_01 = CTkScrollableFrame(app, width=800, height=200)
#     scrollable_frame_01.place(x=50, y=300)

#     def refresh_scrollable_frame():
#         contents = controller.get_directory_contents()
#         for widget in scrollable_frame_01.winfo_children():
#             widget.destroy()
#         for item in contents:
#             label = CTkLabel(scrollable_frame_01, text=item, font=("", 14))
#             label.pack(anchor="w")

#     refresh_scrollable_frame()
    
#     # ======================================================================================
#     # LOGO
#     # ======================================================================================
#     def setup_ui(self):
#         # Load the logo image
#         logo_path = os.path.join(os.path.dirname(__file__), "../assets/img/logo.png")
#         try:
#             logo_image = CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(100, 100))
#             # Display the logo
#             logo_label = CTkLabel(self, image=logo_image, text="")  # Set text="" to show only the image
#             logo_label.place(x=350, y=50)  # Position the logo in the center (adjust as needed)
#         except FileNotFoundError:
#             print(f"Logo file not found at {logo_path}")
#             error_label = CTkLabel(self, text="Logo not found", font=("", 16))
#             error_label.place(x=350, y=50)
    
#     setup_ui()

#     return app



class KD01QuanLyGoiThauView(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800")
        self.title("QUẢN LÝ GÓI THẦU")
        self.setup_ui()
        self.setup_labels()
        self.setup_comboboxes()
        self.setup_entries()
        self.setup_buttons()
        self.setup_switches()
        self.setup_scrollable_frame()

    def setup_ui(self):
        # Load the logo image
        logo_path = os.path.join(os.path.dirname(__file__), "../assets/img/logo.png")
        try:
            logo_image = CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(100, 100))
            logo_label = CTkLabel(self, image=logo_image, text="")  # Set text="" to show only the image
            logo_label.place(x=350, y=50)  # Position the logo
        except FileNotFoundError:
            print(f"Logo file not found at {logo_path}")
            error_label = CTkLabel(self, text="Logo not found", font=("", 16))
            error_label.place(x=350, y=50)

    def setup_labels(self):
        # Static Labels
        LABEL_SoThongBaoMoiThau = CTkLabel(master=self, text="Số thông báo mời thầu", font=("", 18))
        LABEL_SoThongBaoMoiThau.place(x=50, y=170)

        LABEL_TenThuMucSeKhoiTao = CTkLabel(master=self, text="24_GOI_THAU_0000_0000", font=("", 18))
        LABEL_TenThuMucSeKhoiTao.place(x=390, y=200)

        LABEL_NamGoiThau = CTkLabel(master=self, text="Năm gói thầu", font=("", 18))
        LABEL_NamGoiThau.place(x=50, y=70)

        LABEL_DanhSachGoiThau = CTkLabel(master=self, text="Danh sách gói thầu", font=("", 18))
        LABEL_DanhSachGoiThau.place(x=50, y=270)

        # Employee Info Labels
        LABEL_IDNhanVien = CTkLabel(master=self, text="ID: TBD001", font=("", 13))
        LABEL_IDNhanVien.place(x=50, y=10)

        LABEL_TenNhanVien = CTkLabel(master=self, text="Họ tên: Nguyễn Văn B", font=("", 13))
        LABEL_TenNhanVien.place(x=150, y=10)

        LABEL_TenBoPhan = CTkLabel(master=self, text="Bộ phận: Kinh doanh", font=("", 13))
        LABEL_TenBoPhan.place(x=350, y=10)

        LABEL_CapBac = CTkLabel(master=self, text="Cấp bậc: Nhân viên", font=("", 13))
        LABEL_CapBac.place(x=550, y=10)

        LABEL_TenCongTy = CTkLabel(master=self, text="Cty: Thiết bị điện", font=("", 13))
        LABEL_TenCongTy.place(x=750, y=10)

    def setup_comboboxes(self):
        # Combobox for selecting year
        current_year = datetime.now().year
        year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

        def change_handler(value):
            print(f"Selected Value: {value}")

        self.COMBOBOX_NamGoiThau = CTkComboBox(master=self, values=year_array, command=change_handler)
        self.COMBOBOX_NamGoiThau.set(str(current_year))  # Default to current year
        self.COMBOBOX_NamGoiThau.place(x=50, y=100)

        # Combobox for theme selection
        themes = ["MoonlitSky", "NeonBanana", "DaynNight"]

        def change_theme(choice):
            print(f"Theme selected: {choice}")

        self.COMBOBOX_ChangeTheme = CTkComboBox(master=self, values=themes, command=change_theme)
        self.COMBOBOX_ChangeTheme.place(x=650, y=700)

    def setup_entries(self):
        # Entry for notification number
        self.ENTRY_SoThongBaoMoiThau = CTkEntry(master=self, placeholder_text="Start typing...", width=300)
        self.ENTRY_SoThongBaoMoiThau.place(x=50, y=200)

    def setup_buttons(self):
        # Button to create folder
        def on_create_folder():
            print("Folder creation triggered!")

        BTN_TaoThuMucMoi = CTkButton(self, text="Tạo thư mục mới", command=on_create_folder)
        BTN_TaoThuMucMoi.place(x=50, y=700)

    def setup_switches(self):
        # Switch for light/dark mode
        def switch_mode():
            current_mode = get_appearance_mode()
            new_mode = "dark" if current_mode == "Light" else "light"
            set_appearance_mode(new_mode)
            print(f"Mode switched to {new_mode}")

        SWITCH_DarkLightMode = CTkSwitch(self, text="Dark Mode", command=switch_mode)
        SWITCH_DarkLightMode.place(x=500, y=700)

    def setup_scrollable_frame(self):
        # Scrollable frame for folder contents
        self.scrollable_frame = CTkScrollableFrame(self, width=800, height=200)
        self.scrollable_frame.place(x=50, y=300)

        def refresh_scrollable_frame():
            # Simulate directory contents
            directory_contents = [f"Folder {i}" for i in range(1, 21)]
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            for item in directory_contents:
                label = CTkLabel(self.scrollable_frame, text=item, font=("", 14))
                label.pack(anchor="w")

        refresh_scrollable_frame()