from customtkinter import *
from PIL import Image
from datetime import datetime
from app.controllers.KD01QuanLyGoiThauController import KD01QuanLyGoiThauController

class KD01QuanLyGoiThauView(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x800")
        self.title("QUẢN LÝ GÓI THẦU")
        self.setup_logo()
        self.setup_Employee_Info_Labels()
        self.setup_Title_H1()
        self.setup_labels()
        self.setup_comboboxes()
        self.setup_entries()
        self.setup_buttons()
        self.setup_switches()
        self.setup_scrollable_frame()

    def setup_logo(self):
        # Get the project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
        
        # Load the logo image
        # logo_path = os.path.join(os.path.dirname(__file__), "../assets/img/logo.png")
        logo_path = os.path.join(project_root, "assets/img/logo.png")
        print(f"Resolved logo path: {os.path.abspath(logo_path)}")
        posX = 5
        posY = 5
        try:
            logo_image = CTkImage(light_image=Image.open(logo_path), dark_image=Image.open(logo_path), size=(100, 100))
            logo_label = CTkLabel(self, image=logo_image, text="")  # Set text="" to show only the image
            logo_label.place(x=posX, y=posY)  # Position the logo
        except FileNotFoundError:
            print(f"Logo file not found at {logo_path}")
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
    
    def setup_Title_H1(self):
        # Static Labels
        LABEL_TieuDe_H1 = CTkLabel(master=self, text="TẠO FOLDER QUẢN LÝ GÓI THẦU MỚI", font=("", 25))
        LABEL_TieuDe_H1.place(relx=0.2, rely=0.1)
        
    def setup_labels(self):
        # Static Labels
        LABEL_SoThongBaoMoiThau = CTkLabel(master=self, text="Số thông báo mời thầu", font=("", 18))
        LABEL_SoThongBaoMoiThau.place(x=50, y=200)

        LABEL_TenThuMucSeKhoiTao = CTkLabel(master=self, text="24_GOI_THAU_0000_0000", font=("", 18))
        LABEL_TenThuMucSeKhoiTao.place(x=390, y=230)

        LABEL_NamGoiThau = CTkLabel(master=self, text="Năm gói thầu", font=("", 18))
        LABEL_NamGoiThau.place(x=50, y=130)

        LABEL_DanhSachGoiThau = CTkLabel(master=self, text="Danh sách gói thầu", font=("", 18))
        LABEL_DanhSachGoiThau.place(x=50, y=300)

    def setup_comboboxes(self):
        # Combobox for selecting year
        current_year = datetime.now().year
        year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

        def change_handler(value):
            print(f"Selected Value: {value}")

        self.COMBOBOX_NamGoiThau = CTkComboBox(master=self, values=year_array, command=change_handler)
        self.COMBOBOX_NamGoiThau.set(str(current_year))  # Default to current year
        self.COMBOBOX_NamGoiThau.place(x=50, y=160)

        # Combobox for theme selection
        themes = ["MoonlitSky", "NeonBanana", "DaynNight"]

        def change_theme(choice):
            print(f"Theme selected: {choice}")

        self.COMBOBOX_ChangeTheme = CTkComboBox(master=self, values=themes, command=change_theme)
        self.COMBOBOX_ChangeTheme.place(x=650, y=700)

    def setup_entries(self):
        # Entry for notification number
        self.ENTRY_SoThongBaoMoiThau = CTkEntry(master=self, placeholder_text="Start typing...", width=300)
        self.ENTRY_SoThongBaoMoiThau.place(x=50, y=230)

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