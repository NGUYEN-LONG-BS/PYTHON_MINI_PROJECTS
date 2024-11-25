from customtkinter import *
from PIL import Image
from datetime import datetime
from app.controllers.main_controller import MainController


def create_app():
    app = CTk()
    app.geometry("900x800")
    app.title("QUẢN LÝ GÓI THẦU")

    # Controller for managing app logic
    controller = MainController()
        
    # ======================================================================================
    # LABEL_SoThongBaoMoiThau
    # ======================================================================================
    LABEL_SoThongBaoMoiThau = CTkLabel(master=app, 
                                    text="Số thông báo mời thầu"
                                        ,font=("",18)
                                    )
    LABEL_SoThongBaoMoiThau.place(x=50, y=170)

    # ======================================================================================
    # LABEL_TenThuMucSeKhoiTao
    # ======================================================================================
    LABEL_TenThuMucSeKhoiTao = CTkLabel(master=app, 
                                        text="24_GOI_THAU_0000_0000"
                                        ,font=("",18)
                                        )
    LABEL_TenThuMucSeKhoiTao.place(x=390, y=200)

    # ======================================================================================
    # LABEL_NamGoiThau
    # ======================================================================================
    LABEL_NamGoiThau = CTkLabel(master=app
                        ,text="Năm gói thầu"
                        ,font=("",18)
                        )
    LABEL_NamGoiThau.place(x=50, y=70)

    # ======================================================================================
    # LABEL_DanhSachGoiThau
    # ======================================================================================
    LABEL_DanhSachGoiThau = CTkLabel(master=app
                                        ,text="Danh sách gói thầu"
                                        ,font=("",18)
                                        )
    LABEL_DanhSachGoiThau.place(x=50, y=270)

    # ======================================================================================
    # LABEL_IDNhanVien
    # ======================================================================================
    LABEL_IDNhanVien = CTkLabel(master=app
                                ,text="ID: TBD001"
                                ,font=("",13)
                                )
    LABEL_IDNhanVien.place(x=50, y=10)

    # ======================================================================================
    # LABEL_TenNhanVien
    # ======================================================================================
    LABEL_TenNhanVien = CTkLabel(master=app
                                ,text="Họ tên: Nguyễn Văn B"
                                ,font=("",13)
                                )
    LABEL_TenNhanVien.place(x=150, y=10)

    # ======================================================================================
    # LABEL_TenBoPhan
    # ======================================================================================
    LABEL_TenBoPhan = CTkLabel(master=app
                            ,text="Bộ phận: Kinh doanh"
                            ,font=("",13)
                            )
    LABEL_TenBoPhan.place(x=350, y=10)

    # ======================================================================================
    # LABEL_CapBac
    # ======================================================================================
    LABEL_CapBac = CTkLabel(master=app
                            ,text="Cấp bậc: Nhân viên"
                            ,font=("",13)
                            )
    LABEL_CapBac.place(x=550, y=10)

    # ======================================================================================
    # LABEL_TenCongTy
    # ======================================================================================
    LABEL_TenCongTy = CTkLabel(master=app
                            ,text="Cty: Thiết bị điện"
                            ,font=("",13)
                            )
    LABEL_TenCongTy.place(x=750, y=10)

    # ======================================================================================
    # ENTRY_SoThongBaoMoiThau
    # ======================================================================================
    ENTRY_SoThongBaoMoiThau = CTkEntry(master=app
                                            ,placeholder_text="Start typing..."
                                            ,width=300
                                            # ,text_color="#FFCC70"
                                            )
    ENTRY_SoThongBaoMoiThau.place(x=50, y=200)
    # ENTRY_SoThongBaoMoiThau.bind("<KeyRelease>", update_label)
    ENTRY_SoThongBaoMoiThau.bind("<KeyRelease>")

    # ======================================================================================
    # COMBOBOX_NamGoiThau
    # ======================================================================================
    def change_handler(value):
        last_02_chars = value[-2:]
        print(f"Selected Value {value}, Last Two Characters: {last_02_chars}")
        
    # Get the current year
    current_year = datetime.now().year
    # Create the array with the specified years
    year_array = [str(current_year - 2), str(current_year - 1), str(current_year), str(current_year + 1)]

    COMBOBOX_NamGoiThau = CTkComboBox(master=app, 
                        values=year_array,
                        command=change_handler)

    COMBOBOX_NamGoiThau.set(current_year)       # Set the default value to the current year
    COMBOBOX_NamGoiThau.place(x=50, y=100)      # Place the combobox in the window
    
    # Switch for dark/light mode
    def switch_mode():
        current_mode = get_appearance_mode()
        new_mode = "dark" if current_mode == "Light" else "light"
        set_appearance_mode(new_mode)
        controller.save_default_settings(new_mode, "theme_01")

    switch = CTkSwitch(app, text="Dark Mode", command=switch_mode)
    switch.place(x=500, y=700)

    # Combobox for theme selection
    themes = ["MoonlitSky", "NeonBanana", "DaynNight"]
    combobox = CTkComboBox(app, values=themes, command=controller.change_theme)
    combobox.place(x=650, y=700)

    # Button to create a new folder
    def on_create_folder():
        controller.create_folder()
    BTN_TaoThuMucMoi = CTkButton(app, text="Tạo thư mục mới", command=on_create_folder)
    BTN_TaoThuMucMoi.place(x=50, y=700)

    # Scrollable frame for displaying folder contents
    scrollable_frame = CTkScrollableFrame(app, width=800, height=200)
    scrollable_frame.place(x=50, y=300)

    def refresh_scrollable_frame():
        contents = controller.get_directory_contents()
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        for item in contents:
            label = CTkLabel(scrollable_frame, text=item, font=("", 14))
            label.pack(anchor="w")

    refresh_scrollable_frame()

    return app
