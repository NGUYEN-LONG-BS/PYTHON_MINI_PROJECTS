import tkinter as tk
from tkinter import filedialog
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
    
    plot_chart(df)

def plot_chart(df):
    x_values = df.iloc[:, 0]  # Cột đầu tiên làm trục X
    y_values = df.iloc[:, 1]  # Cột thứ hai làm trục Y
    
    fig, ax = plt.subplots()
    ax.bar(x_values, y_values, color='skyblue')
    ax.set_xlabel("Danh mục")
    ax.set_ylabel("Giá trị")
    ax.set_title("Biểu đồ cột từ Excel")
    
    for widget in frame.winfo_children():
        widget.destroy()
    
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Excel to Bar Chart")
root.geometry("600x500")

btn_load = tk.Button(root, text="Chọn file Excel", command=load_excel)
btn_load.pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
