import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def chon_thu_muc():
    thu_muc = filedialog.askdirectory()
    entry_thu_muc.delete(0, tk.END)
    entry_thu_muc.insert(0, thu_muc)

def nhan_ban_hinh():
    thu_muc = entry_thu_muc.get()
    if not thu_muc:
        return

    hinh_goc = 'product-{}.jpg'
    so_luong = 200

    for i in range(1, so_luong + 1):
        so_hinh_goc = (i - 1) % 8 + 1
        ten_hinh_goc = hinh_goc.format(so_hinh_goc)
        duong_dan_hinh_goc = os.path.join(thu_muc, ten_hinh_goc)

        if not os.path.exists(duong_dan_hinh_goc):
            print(f"Hình ảnh {duong_dan_hinh_goc} không tồn tại. Bỏ qua...")
            continue

        ten_hinh_moi = 'product-{}.jpg'.format(i)
        duong_dan_hinh_moi = os.path.join(thu_muc, ten_hinh_moi)

        try:
            img = Image.open(duong_dan_hinh_goc)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            img.save(duong_dan_hinh_moi)
        except Exception as e:
            print(f"Lỗi khi xử lý hình ảnh {duong_dan_hinh_goc}: {str(e)}")

root = tk.Tk()
root.title('Ứng dụng nhân bản hình ảnh')

label_thu_muc = tk.Label(root, text='Thư mục:')
label_thu_muc.grid(row=0, column=0, padx=5, pady=5)

entry_thu_muc = tk.Entry(root, width=50)
entry_thu_muc.grid(row=0, column=1, padx=5, pady=5)

button_chon_thu_muc = tk.Button(root, text='Chọn thư mục', command=chon_thu_muc)
button_chon_thu_muc.grid(row=0, column=2, padx=5, pady=5)

button_nhan_ban = tk.Button(root, text='Nhân bản hình ảnh', command=nhan_ban_hinh)
button_nhan_ban.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()