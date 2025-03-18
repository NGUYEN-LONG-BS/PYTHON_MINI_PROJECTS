import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

from app.views.Components_View import *
from app.utils import *

class cls_Dashboard_kinhdoanh_View(cls_base_form_number_02_ManyTabs):
    def __init__(self):
        title = "KD00 - DashboardKinhDoanhView"
        name_of_slip = "BỘ PHẬN KINH DOANH"
        super().__init__(title_of_form=title, name_of_slip=name_of_slip)
        # call reuse components
        self._f_view_thay_doi_gia_tri_cua_base_form()
        self._f_view_create_all_container_frames_of_window()
    
    def _f_view_thay_doi_gia_tri_cua_base_form(self):
        # Thay đổi thông tin các tab
        notebook = None
        def find_notebook(widget):
            nonlocal notebook
            for child in widget.winfo_children():
                if isinstance(child, ttk.Notebook):
                    notebook = child
                    return True
                if find_notebook(child):
                    return True
            return False

        find_notebook(self) 

        if not notebook:
            print("Error: notebook not found!")
            return

        # Change the text of the second tabs
        notebook.tab(0, text="DANH SÁCH NGHIÊP VỤ")
        notebook.tab(1, text="TỔNG QUAN CÔNG VIỆC")
        
        # Delete the third tab
        notebook.forget(2)
        
        # Change the title of TieuDeTab_01
        for child in self.tab1.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-01":
                        grandchild.destroy()
                        break
        # Change the title of TieuDeTab_01
        for child in self.tab2.winfo_children():
            if isinstance(child, ttk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, tk.Label) and grandchild.cget("text") == "Tiêu đề tab-02":
                        grandchild.destroy()
                        break
        return notebook
   
    def _f_view_create_all_container_frames_of_window(self):
        # Create tabs
        self.tab_01 = self.tab1
        self.tab_02 = self.tab2
        # Settings tab content
        self._f_view_create_in_tab_01_all_container_frames()
        self._f_add_elements_to_card_QL_KHACHANG()
        self._f_view_create_in_tab_02_all_container_frames()
    
    def _f_view_create_in_tab_01_all_container_frames(self):
        parent_frame = self.tab_01
        # parent_frame = tk.Frame(self.tab_01)
        # parent_frame.pack(fill="both", expand=True)
        # parent_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        rows = 2
        columns = 3

        # Center-align the grid
        parent_frame.grid_rowconfigure(tuple(range(rows)), weight=1)  # Center vertically
        parent_frame.grid_columnconfigure(tuple(range(columns)), weight=1)  # Center horizontally

        # Danh sách hình ảnh và nội dung cho mỗi card
        cards_data = [
            {"image": PATH_CARD_KD_QUAN_LY_KE_HOACH_DAT_HANG,"text": "QUẢN LÝ KẾ HOẠCH ĐẶT HÀNG", "click_event": self.f_card_04_ke_hoach_dat_hang_click,"name_of_card": "card_frame_ke_hoach_dat_hang", "visitable": True},
            {"image": PATH_CARD_KD_05,"text": "QUẢN LÝ YÊU CẦU ĐẶT HÀNG", "click_event": self.f_card_06_yeu_cau_dat_hang_click,"name_of_card": "card_frame_yeu_cau_dat_hang", "visitable": True},
            {"image": PATH_CARD_KD_QUAN_LY_DE_NGHI_XUAT_KHO,"text": "ĐỀ NGHỊ XUẤT KHO", "click_event": self.f_card_DE_NGHI_XUAT_KHO_click,"name_of_card": "card_frame_de_nghi_xuat_kho", "visitable": True},
            
            {"image": PATH_CARD_KD_QUAN_LY_KHACH_HANG,"text": "DANH SÁCH KHÁCH HÀNG", "click_event": self.f_card_01_click,"name_of_card": "card_frame_danh_sach_khach_hang", "visitable": False},
            {"image": PATH_CARD_KD_02,"text": "DANH SÁCH HÀNG HOÁ", "click_event": self.f_card_02_danh_sach_hang_hoa_click,"name_of_card": "card_frame_2", "visitable": True},
            {"image": PATH_CARD_KD_03,"text": "QUẢN LÝ GÓI THẦU", "click_event": self.f_card_03_click,"name_of_card": "card_frame_3", "visitable": False},
            {"image": PATH_CARD_KD_04,"text": "QUẢN LÝ CÔNG NỢ", "click_event": self.f_card_05_click,"name_of_card": "card_frame_4", "visitable": False},
            {"image": PATH_CARD_KD_06,"text": "BÁO CÁO", "click_event": self.f_card_07_click,"name_of_card": "card_frame_6", "visitable": True},
            
        ]

        # Kích thước card và padding
        card_width = 300
        card_height = 300
        image_padding = 10  # Padding xung quanh hình ảnh

        # Load và resize ảnh
        images = []
        for card_data in cards_data:
            img = Image.open(card_data["image"])
            img = img.resize((card_width - 2 * image_padding, card_height - 2 * image_padding))  # Điều chỉnh kích thước ảnh phù hợp với card
            img_tk = ImageTk.PhotoImage(img)
            images.append(img_tk)  # Lưu ảnh để tránh bị thu hồi

        # Thêm card vào parent_frame nếu visitable là True
        visible_index = 0
        for index, card_data in enumerate(cards_data):
            if not card_data["visitable"]:
                continue  # Skip if visitable is False
            
            row = visible_index // columns
            col = visible_index % columns
            visible_index += 1

            # Tạo một frame cho từng "card"
            card = tk.Frame(
                parent_frame,
                bg=BG_COLOR_0_0,
                width=card_width,
                height=card_height,
                highlightbackground="gray",
                highlightthickness=1,
                name=card_data["name_of_card"],
                cursor="hand2"
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Thêm label chứa text vào card
            text_label = tk.Label(card, text=card_data["text"], bg=BG_COLOR_0_0, font=("Arial", 12))
            text_label.pack()

            # Thêm label chứa hình ảnh vào card
            image_label = tk.Label(
                card, 
                image=images[index], 
                bg=BG_COLOR_0_0, 
                # bg=COLOR_GREEN, 
                cursor="hand2" 
                )
            image_label.image = images[index]  # Lưu tham chiếu để tránh ảnh bị thu hồi
            image_label.pack(fill=tk.BOTH, expand=True)

            # Bind click event to print card name
            text_label.bind("<Button-1>", card_data["click_event"])
            image_label.bind("<Button-1>", card_data["click_event"])
            card.bind("<Button-1>", card_data["click_event"])
    
    def f_card_01_click(self, event):
        print("f_card_01_click")
    def f_card_02_danh_sach_hang_hoa_click(self, event):
        from app.views.VT00_QuanLyHangHoa_View.QUAN_LY_HANG_HOA_view import cls_test_View
        self.destroy()
        new_view = cls_test_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
        
    def f_card_03_click(self, event):
        print("f_card_03_click")
        
    def f_card_04_ke_hoach_dat_hang_click(self, event):
        # from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
        from app.views.KD0201_QuanLyKeHoachDatHang_View_250225_11h40.KE_HOACH_DAT_HANG_View import cls_KE_HOACH_DAT_HANG_View
        self.destroy()
        new_view = cls_KE_HOACH_DAT_HANG_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()
    
    def f_card_05_click(self, event):
        print("f_card_05_click")
    
    def f_card_06_yeu_cau_dat_hang_click(self, event):
        # from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
        from app.views.KD0202_QuanLyYeuCauDatHang_View_250217_09h01.YEU_CAU_DAT_HANG_View import cls_YEU_CAU_DAT_HANG_View
        self.destroy()
        new_view = cls_YEU_CAU_DAT_HANG_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()

    def f_card_07_click(self, event):
        print("f_card_07_click")
        
    def f_card_DE_NGHI_XUAT_KHO_click(self, event):
        # from app.views.KD03_QuanLyKhachHang_View.test_View import cls_test_View
        from app.views.KD0301_QuanLyDeNghiXuatKho_View_250225_10h00.DE_NGHI_XUAT_KHO_View import cls_DE_NGHI_XUAT_KHO_View
        self.destroy()
        new_view = cls_DE_NGHI_XUAT_KHO_View()
        # new_view.dashboard = self.parent
        utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(new_view, maximize=True)
        f_utils_set_center_screen(new_view)
        new_view.focus_force()

    def _f_add_elements_to_card_QL_KHACHANG(self):
        try:
            parent_frame = self.tab_01.nametowidget("card_frame_yeu_cau_dat_hang")
        except KeyError:
            print("Error: Frame 'card_frame_yeu_cau_dat_hang' not found!")
            return

        # frame_01 = tk.Frame(parent_frame)
        # frame_01.pack(fill="x", expand=True, padx=10, pady=10)

        # BTN_01 = tk.Button(frame_01, text="Nhật ký yêu cầu đặt hàng", font=("Arial", 12), command=self.f_view_tab_01_button_NhatKyYeuCauDatHang_click)
        # BTN_01.pack(side="left", padx=10, pady=5)
    
    def _f_view_create_in_tab_02_all_container_frames(self):
        parent_frame = self.tab_02
        self.Frame_Body.configure(bg=BG_COLOR_0_0)

        # Create a frame to hold the chart
        chart_frame_01 = ttk.Frame(parent_frame, padding="10", borderwidth=2, relief="solid")
        chart_frame_01.pack(side="top", fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create a Matplotlib figure and plot
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Line")
        ax.set_title("Sample Chart")
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")
        ax.legend()

        # Embed the Matplotlib figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame_01)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        # Create a frame to hold the chart
        chart_frame_02 = ttk.Frame(parent_frame, padding="10", borderwidth=2, relief="solid")
        chart_frame_02.pack(side="top", fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create a Matplotlib figure and plot
        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Line")
        ax.set_title("Sample Chart")
        ax.set_xlabel("X-Axis")
        ax.set_ylabel("Y-Axis")
        ax.legend()

        # Embed the Matplotlib figure into the Tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame_02)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)

        
    