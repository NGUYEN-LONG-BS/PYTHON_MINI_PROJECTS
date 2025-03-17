import tkinter as tk
import qrcode
from PIL import ImageTk, Image

# Hàm tạo QR code
def generate_qr():
    # Lấy text từ entry
    text = entry.get()
    
    if text:
        # Tạo QR code
        qr = qrcode.QRCode(version=5,  # Phiên bản 5 (kích thước lớn hơn)
                            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Mức độ sửa lỗi cao
                            box_size=10,
                            border=5,
                           )
        qr.add_data(text)
        qr.make(fit=True)
        
        # Tạo hình ảnh QR code
        img = qr.make_image(fill="black", back_color="white")
        
        # Hiển thị QR code lên giao diện
        img = img.resize((200, 200))  # Resize cho phù hợp với kích thước giao diện
        img_tk = ImageTk.PhotoImage(img)
        
        label_img.config(image=img_tk)
        label_img.image = img_tk  # Giữ ảnh trong bộ nhớ để tránh bị mất khi thay đổi
    else:
        label_img.config(image='', text="Vui lòng nhập văn bản!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi văn bản thành QR Code")

# Tạo Entry để người dùng nhập văn bản
entry_label = tk.Label(root, text="Nhập văn bản:")
entry_label.pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Tạo nút để tạo QR code
generate_button = tk.Button(root, text="Tạo QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Label để hiển thị QR code
label_img = tk.Label(root)
label_img.pack(pady=10)

# Khởi chạy giao diện
root.mainloop()
