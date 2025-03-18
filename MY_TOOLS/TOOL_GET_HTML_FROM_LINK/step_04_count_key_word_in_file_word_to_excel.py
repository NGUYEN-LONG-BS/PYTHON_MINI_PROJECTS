import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
import pandas as pd
import os

# Hàm kiểm tra các từ khóa trong nội dung Word
def find_keywords_in_word(file_path, keywords):
    try:
        # Mở file Word
        doc = Document(file_path)
        
        # Lấy nội dung toàn bộ văn bản trong file
        full_text = ""
        for para in doc.paragraphs:
            full_text += para.text + "\n"
        
        # Tạo một từ điển để đếm số lần xuất hiện của từng từ khóa
        keyword_counts = {}
        
        # Kiểm tra các từ khóa trong nội dung văn bản
        for keyword in keywords:
            count = full_text.lower().count(keyword.lower())  # Đếm số lần từ khóa xuất hiện
            if count > 0:
                keyword_counts[keyword] = count
        
        return keyword_counts
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi đọc file: {e}")
        return {}

# Hàm để lưu kết quả vào file Excel
def save_to_excel(data, file_path):
    # Tạo DataFrame từ kết quả tìm kiếm
    df = pd.DataFrame(list(data.items()), columns=["Từ khóa", "Số lần xuất hiện"])
    
    # Kiểm tra xem file đã tồn tại chưa, nếu có thì tự động tăng số thứ tự
    if os.path.exists(file_path):
        base, ext = os.path.splitext(file_path)
        i = 1
        new_file_path = f"{base}_{i}{ext}"
        while os.path.exists(new_file_path):
            i += 1
            new_file_path = f"{base}_{i}{ext}"
        file_path = new_file_path

    # Lưu DataFrame thành file Excel
    df.to_excel(file_path, index=False, engine='openpyxl')
    messagebox.showinfo("Thành công", f"Kết quả đã được lưu vào file: {file_path}")

# Hàm để chọn file và tìm từ khóa
def select_file_and_check():
    # Chọn file Word
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx")])
    
    if not file_path:
        return  # Nếu người dùng hủy chọn file
    
    # Danh sách các từ khóa cần tìm kiếm
    keywords = ['python', 'data', 'machine learning', 'AI', 'word']
    
    # Tìm kiếm các từ khóa trong file Word
    keyword_counts = find_keywords_in_word(file_path, keywords)
    
    # Kiểm tra kết quả
    if not keyword_counts:
        messagebox.showinfo("Kết quả tìm kiếm", "Không tìm thấy từ khóa nào trong file.")
        return
    
    # Mở hộp thoại chọn nơi lưu file Excel
    file_path_to_save = filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="ket_qua_tu_khoa.xlsx", title="Chọn nơi lưu file Excel")
    
    if not file_path_to_save:
        return  # Nếu người dùng hủy thao tác lưu file
    
    # Lưu kết quả vào file Excel
    save_to_excel(keyword_counts, file_path_to_save)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Kiểm Từ Khóa trong File Word và Lưu Kết Quả Thành Excel")

# Tạo nút chọn file và kiểm tra từ khóa
button = tk.Button(root, text="Chọn File Word và Kiểm Từ Khóa", command=select_file_and_check)
button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
