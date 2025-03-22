import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def load_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if not file_path:
        return
    
    df = pd.read_excel(file_path)
    
    if len(df.columns) < 2:
        return
    
    display_data(df)
    plot_line_chart(df)

def display_data(df):
    for widget in table_frame.winfo_children():
        widget.destroy()
    
    tree = ttk.Treeview(table_frame, columns=list(df.columns), show="headings")
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    
    for _, row in df.iterrows():
        tree.insert("", tk.END, values=list(row))
    
    tree.pack(fill=tk.BOTH, expand=True)

def plot_line_chart(df):
    x_values = df.iloc[:, 0]  # Cột đầu tiên làm trục X
    y_values = df.iloc[:, 1]  # Cột thứ hai làm trục Y
    
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    ax.set_xlabel("Danh mục")
    ax.set_ylabel("Giá trị")
    ax.set_title("Biểu đồ đường từ Excel")
    
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Excel to Line Chart")
root.geometry("800x600")

btn_load = tk.Button(root, text="Chọn file Excel", command=load_excel)
btn_load.pack(pady=10)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
