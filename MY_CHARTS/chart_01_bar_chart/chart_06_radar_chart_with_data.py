import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import numpy as np
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
    plot_radar_chart(df)

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

def plot_radar_chart(df):
    labels = df.iloc[:, 0]
    values = df.iloc[:, 1].astype(float)
    
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values = values.tolist()
    values += values[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='b', alpha=0.3)
    ax.plot(angles, values, color='b', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title("Biểu đồ mạng nhện từ Excel")
    
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Excel to Radar Chart")
root.geometry("800x600")

btn_load = tk.Button(root, text="Chọn file Excel", command=load_excel)
btn_load.pack(pady=10)

table_frame = tk.Frame(root)
table_frame.pack(fill=tk.BOTH, expand=True)

chart_frame = tk.Frame(root)
chart_frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
