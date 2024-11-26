# KD01QuanLyGoiThauView.py
from customtkinter import *
from PIL import Image
from datetime import datetime
from app.controllers.KD01QuanLyGoiThauController import KD01QuanLyGoiThauController


class KD01QuanLyGoiThauView(CTk):
    def __init__(self):
        super().__init__()
        # Initialize controller
        self.controller = KD01QuanLyGoiThauController()  # Assign the controller to an instance variable
        
        # Setup the main window
        self.geometry("900x800")
        self.title("QUẢN LÝ GÓI THẦU")
        
        # Setup the components
        self.setup_logo()
        self.setup_Employee_Info_Labels()
        self.setup_Title_H1()
        self.setup_labels()
        self.setup_LABEL_TenThuMucSeKhoiTao()
        self.setup_COMBOBOX_NamGoiThau()
        self.setup_COMBOBOX_ChangeTheme()
        self.setup_entries()
        self.setup_BTN_TaoThuMucMoi()
        self.setup_switches()
        self.setup_scrollable_frame()

    # ==================================================================================================
    # SETUP HEADER FRAME
    # ==================================================================================================
    def setup_logo(self):
        # Get the project root directory
        # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))   # Going two levels up
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Going two levels up
        
        # Load the logo images
        logo_path_light = os.path.join(project_root, "assets/img/logo-Light.jpg")
        logo_path_dark = os.path.join(project_root, "assets/img/logo-Dark.jpg")
        posX = 5
        posY = 5
        
        # Debugging print to check image paths
        print("Logo path (light mode):", logo_path_light)
        print("Logo path (dark mode):", logo_path_dark)
        
        try:
            # Try loading the light mode image first
            logo_image_light = Image.open(logo_path_light)
            logo_image_dark = Image.open(logo_path_dark)
            
            # Create the CTkImage for both light and dark modes
            self.logo_image = CTkImage(light_image=logo_image_light, dark_image=logo_image_dark, size=(100, 100))
            
            # Create the CTkLabel and display the image
            logo_label = CTkLabel(self, image=self.logo_image, text="")
            logo_label.place(x=posX, y=posY)
            
        except FileNotFoundError:
            print(f"Logo file not found at {logo_path_light} or {logo_path_dark}")
            error_label = CTkLabel(self, text="Logo not found", font=("", 16))
            error_label.place(x=posX, y=posY)


    def setup_Employee_Info_Labels(self):
        # Employee Info Labels
        LABEL_IDNhanVien = CTkLabel(master=self, text="ID: TBD001", font=("", 13))
        LABEL_IDNhanVien.place(x=115, y=10)

        LABEL_TenNhanVien = CTkLabel(master=self, text="Họ tên: Nguyễn Văn B", font=("", 13))
        LABEL_TenNhanVien.place(x=200, y=10)

        LABEL_TenBoPhan = CTkLabel(master=self, text="Bộ phận: Kinh doanh", font=("", 13))
        LABEL_TenBoPhan.place(x=370, y=10)

        LABEL_CapBac = CTkLabel(master=self, text="Cấp bậc: Nhân viên", font=("", 13))
        LABEL_CapBac.place(x=550, y=10)

        LABEL_TenCongTy = CTkLabel(master=self, text="Cty: Thiết bị điện", font=("", 13))
        LABEL_TenCongTy.place(x=750, y=10)

    # ==================================================================================================
    # SETUP HEADER H1
    # ==================================================================================================
    def setup_Title_H1(self):
        # Static Labels
        LABEL_TieuDe_H1 = CTkLabel(master=self, text="TẠO FOLDER QUẢN LÝ GÓI THẦU MỚI", font=("", 25))
        LABEL_TieuDe_H1.place(relx=0.2, rely=0.1)

    # ==================================================================================================
    # SETUP ALL LABELS
    # ==================================================================================================
    def setup_LABEL_TenThuMucSeKhoiTao(self):
        # Store the label in an instance variable to update it later
        self.LABEL_TenThuMucSeKhoiTao = CTkLabel(master=self, text="24_GOI_THAU_0000_0000", font=("", 18))
        self.LABEL_TenThuMucSeKhoiTao.place(x=390, y=230)

    def setup_labels(self):
        # Static Labels
        LABEL_SoThongBaoMoiThau = CTkLabel(master=self, text="Số thông báo mời thầu", font=("", 18))
        LABEL_SoThongBaoMoiThau.place(x=50, y=200)

        LABEL_NamGoiThau = CTkLabel(master=self, text="Năm gói thầu", font=("", 18))
        LABEL_NamGoiThau.place(x=50, y=130)

        LABEL_DanhSachGoiThau = CTkLabel(master=self, text="Danh sách gói thầu", font=("", 18))
        LABEL_DanhSachGoiThau.place(x=50, y=300)

    # ==================================================================================================
    # SETUP ALL COMBOBOXS
    # ==================================================================================================
    def setup_COMBOBOX_NamGoiThau(self):
        # Combobox for selecting year
        current_year = datetime.now().year
        year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

        def change_handler(value):
            print(f"Selected Value: {value}")
            self.update_folder_name()  # Call the method to update the folder name

        self.COMBOBOX_NamGoiThau = CTkComboBox(master=self, values=year_array, command=change_handler)
        self.COMBOBOX_NamGoiThau.set(str(current_year))  # Default to current year
        self.COMBOBOX_NamGoiThau.place(x=50, y=160)
        
    # ==================================================================================================
    # setup_COMBOBOX_ChangeTheme
    # ==================================================================================================
    def setup_COMBOBOX_ChangeTheme(self):
        # Combobox for theme selection
        themes = ["MoonlitSky", "NeonBanana", "DaynNight"]

        def change_theme(choice):
            print(f"Theme selected: {choice}")

        self.COMBOBOX_ChangeTheme = CTkComboBox(master=self, values=themes, command=change_theme)
        self.COMBOBOX_ChangeTheme.place(x=650, y=700)

    # ==================================================================================================
    # setup_entries
    # ==================================================================================================
    def setup_entries(self):
        # Entry for notification number
        self.ENTRY_SoThongBaoMoiThau = CTkEntry(master=self, placeholder_text="Start typing...", width=300)
        self.ENTRY_SoThongBaoMoiThau.place(x=50, y=230)
        self.ENTRY_SoThongBaoMoiThau.bind("<KeyRelease>", self.on_entry_change)

    # ==================================================================================================
    # setup_BTN_TaoThuMucMoi
    # ==================================================================================================
    def setup_BTN_TaoThuMucMoi(self):
        # Button to create folder
        def BTN_TaoThuMucMoi_Click():
            folder_name = self.LABEL_TenThuMucSeKhoiTao.cget("text")  # Get the current folder name
            self.controller.create_folder(folder_name)  # Pass folder name to controller

        BTN_TaoThuMucMoi = CTkButton(self, text="Tạo thư mục mới", command=BTN_TaoThuMucMoi_Click)
        BTN_TaoThuMucMoi.place(x=50, y=700)

    # ==================================================================================================
    # setup_switches
    # ==================================================================================================
    def setup_switches(self):
        # Switch for light/dark mode
        def SWITCH_DarkLightMode_Change():
            current_mode = get_appearance_mode()
            new_mode = "dark" if current_mode == "Light" else "light"
            set_appearance_mode(new_mode)
            print(f"Mode switched to {new_mode}")

        SWITCH_DarkLightMode = CTkSwitch(self, text="Dark Mode", command=SWITCH_DarkLightMode_Change)
        SWITCH_DarkLightMode.place(x=500, y=700)

    # ==================================================================================================
    # setup_scrollable_frame
    # ==================================================================================================
    def setup_scrollable_frame(self):
        # Scrollable frame for folder contents
        self.scrollable_frame = CTkScrollableFrame(self, width=800, height=200)
        self.scrollable_frame.place(x=50, y=330)

        def refresh_scrollable_frame():
            # Simulate directory contents
            directory_contents = [f"Folder {i}" for i in range(1, 21)]
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            for item in directory_contents:
                label = CTkLabel(self.scrollable_frame, text=item, font=("", 14))
                label.pack(anchor="w")

        refresh_scrollable_frame()
    
    # ==================================================================================================
    # on_entry_change
    # ==================================================================================================
    def on_COMBOBOX_NamGoiThau_change(self, event):
        self.update_folder_name()
    
    # ==================================================================================================
    # on_entry_change
    # ==================================================================================================
    def on_entry_change(self, event):
        self.update_folder_name()

    def update_folder_name(self):
        # Get the year from COMBOBOX
        selected_year = self.COMBOBOX_NamGoiThau.get()
        year_suffix = selected_year[-2:]  # Get last 2 digits of the selected year
        
        # Get the notification number from ENTRY_SoThongBaoMoiThau and pad to 4 digits
        notification_number = self.ENTRY_SoThongBaoMoiThau.get().zfill(4)
        
        # Construct the new folder name
        folder_name = f"{year_suffix}_GOI_THAU_0000_{notification_number}"
        
        # Update the LABEL_TenThuMucSeKhoiTao with the new folder name
        self.LABEL_TenThuMucSeKhoiTao.configure(text=folder_name)