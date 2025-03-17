import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document

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
    
    # Hiển thị kết quả
    if keyword_counts:
        result_text = "Từ khóa tìm thấy trong file Word:\n"
        for keyword, count in keyword_counts.items():
            result_text += f"Từ khóa: '{keyword}' xuất hiện {count} lần\n"
    else:
        result_text = "Không tìm thấy từ khóa nào trong file."
    
    # Hiển thị kết quả trong hộp thông báo
    messagebox.showinfo("Kết quả tìm kiếm", result_text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Kiểm Từ Khóa trong File Word")

# Tạo nút chọn file và kiểm tra từ khóa
button = tk.Button(root, text="Chọn File Word và Kiểm Từ Khóa", command=select_file_and_check)
button.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
