# Project/Views/components/user_Info.py
import tkinter as tk

# Project/Views/components/user_Info.py
import tkinter as tk

def setup_employee_info_labels(parent):
    """
    This function creates and places the employee info labels horizontally in the given parent widget
    using the .pack() method with side='left'.
    """
    # Create a frame to hold the labels horizontally
    frame = tk.Frame(parent, bd=2, relief='solid', padx=10, pady=10)  # Border with 2px width
    frame.pack(side='top', padx=10, pady=10, fill='x')  # Adjust padding and fill as needed

    # ID label
    id_label = tk.Label(frame, text="ID: TBD001", font=("Arial", 13))
    id_label.pack(side='left', padx=10)  # Place horizontally side by side

    # Name label
    name_label = tk.Label(frame, text="Họ tên: Nguyễn Văn B", font=("Arial", 13))
    name_label.pack(side='left', padx=10)

    # Department label
    department_label = tk.Label(frame, text="Bộ phận: Kinh doanh", font=("Arial", 13))
    department_label.pack(side='left', padx=10)

    # Rank label
    rank_label = tk.Label(frame, text="Cấp bậc: Nhân viên", font=("Arial", 13))
    rank_label.pack(side='left', padx=10)

    # Company label
    company_label = tk.Label(frame, text="Cty: Thiết bị điện", font=("Arial", 13))
    company_label.pack(side='left', padx=10)
