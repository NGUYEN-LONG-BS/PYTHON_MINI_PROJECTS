import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import pytesseract

# Cấu hình đường dẫn đến Tesseract nếu cần
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Hàm để chọn hình ảnh và nhận diện văn bản
def open_image():
    file_path = filedialog.askopenfilename(title="Chọn một hình ảnh", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        # Mở hình ảnh
        img = Image.open(file_path)
        img = img.resize((400, 400))  # Resize ảnh cho phù hợp với giao diện
        img_tk = ImageTk.PhotoImage(img)
        
        # Hiển thị hình ảnh lên giao diện
        image_label.config(image=img_tk)
        image_label.image = img_tk
        
        # Nhận diện văn bản từ hình ảnh
        text = pytesseract.image_to_string(img)
        
        # Hiển thị kết quả nhận diện
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, text)

# Tạo cửa sổ chính của ứng dụng
root = tk.Tk()
root.title("Ứng Dụng OCR với Tkinter")

# Tạo giao diện
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Nút chọn hình ảnh
open_button = tk.Button(frame, text="Chọn Hình Ảnh", command=open_image)
open_button.pack()

# Label để hiển thị hình ảnh
image_label = tk.Label(frame)
image_label.pack(pady=10)

# Text box để hiển thị văn bản nhận diện
result_text = tk.Text(frame, width=50, height=10)
result_text.pack()

# Chạy ứng dụng
root.mainloop()
