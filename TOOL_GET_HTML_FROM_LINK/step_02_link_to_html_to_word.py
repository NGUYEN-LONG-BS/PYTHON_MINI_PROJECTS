import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import os
from docx import Document
import html2text

# Hàm lấy mã HTML từ URL và lưu vào file Word
def get_html():
    url = entry_url.get()  # Lấy đường link từ ô nhập liệu
    if not url:
        messagebox.showerror("Lỗi", "Vui lòng nhập URL.")
        return
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kiểm tra xem yêu cầu có thành công không
        
        # Mở hộp thoại cho phép người dùng chọn đường dẫn và tên file Word
        file_path = filedialog.asksaveasfilename(defaultextension=".docx", initialfile="html_from_link.docx", title="Chọn nơi lưu file")
        
        if not file_path:
            return  # Nếu người dùng hủy thao tác chọn file
        
        # Kiểm tra xem file có tồn tại không, nếu có thì thêm số thứ tự vào tên file
        if os.path.exists(file_path):
            base, ext = os.path.splitext(file_path)
            i = 1
            new_file_path = f"{base}_{i}{ext}"
            while os.path.exists(new_file_path):
                i += 1
                new_file_path = f"{base}_{i}{ext}"
            file_path = new_file_path
        
        # Chuyển đổi HTML thành text (nội dung)
        html_content = response.text
        h = html2text.HTML2Text()
        h.ignore_links = False  # Có thể giữ liên kết trong HTML
        text_content = h.handle(html_content)
        
        # Tạo tài liệu Word và chèn nội dung
        doc = Document()
        doc.add_paragraph(text_content)
        
        # Lưu tài liệu Word
        doc.save(file_path)
        
        messagebox.showinfo("Thành công", f"Đã lưu mã HTML vào file Word: {file_path}")
    
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Lỗi", f"Không thể tải trang web: {e}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lấy Mã HTML Từ URL và Chuyển Thành Word")

# Tạo nhãn hướng dẫn
label = tk.Label(root, text="Nhập URL:")
label.pack(pady=5)

# Tạo ô nhập URL
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=5)

# Tạo nút lấy mã HTML và lưu vào file Word
button = tk.Button(root, text="Lấy Mã HTML và Lưu Thành Word", command=get_html)
button.pack(pady=5)

# Chạy ứng dụng
root.mainloop()
