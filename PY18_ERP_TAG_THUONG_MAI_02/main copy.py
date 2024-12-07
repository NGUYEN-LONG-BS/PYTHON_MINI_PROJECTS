import tkinter as tk
from PY18_ERP_TAG_THUONG_MAI_02.app.views.components.header import Header
from PY18_ERP_TAG_THUONG_MAI_02.app.views.components.footer import Footer
from PY18_ERP_TAG_THUONG_MAI_02.app.views.components.left_menu import LeftMenu
from PY18_ERP_TAG_THUONG_MAI_02.app.views.components.right_banner import RightBanner
from app.views.dashboard.dashboard_view import DashboardView

def main():
    root = tk.Tk()
    root.geometry("1024x768")
    root.title("Modular Application")

    # Create Layout Components
    header = Header(root)
    footer = Footer(root)
    left_menu = LeftMenu(root)
    right_banner = RightBanner(root)

    # Create Main Content Area
    main_frame = tk.Frame(root, bg="lightgray")
    main_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    # Load Dashboard View into the main content area
    dashboard_view = DashboardView(main_frame)

    root.mainloop()

if __name__ == "__main__":
    main()
