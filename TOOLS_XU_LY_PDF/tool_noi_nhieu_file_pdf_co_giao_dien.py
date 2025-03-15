import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nối file PDF")
        self.root.geometry("400x300")

        # Biến lưu trữ đường dẫn các file PDF
        self.pdf_files = []

        # Tạo giao diện
        self.label_01 = tk.Label(root, text="Chọn các file PDF để nối:", font=("Arial", 12))
        self.label_01.pack(pady=10)
        
        self.label_02 = tk.Label(root, text="Lưu ý: nối theo thứ tự abc tên file", font=("Arial", 9))
        self.label_02.pack(pady=10)

        self.select_button = tk.Button(root, text="Chọn file PDF", command=self.select_pdf_files)
        self.select_button.pack(pady=5)

        self.merge_button = tk.Button(root, text="Nối file PDF", command=self.merge_pdfs, state=tk.DISABLED)
        self.merge_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

        # Listbox để hiển thị các file đã chọn
        self.file_listbox = tk.Listbox(root, width=50, height=10)
        self.file_listbox.pack(pady=10)

    def select_pdf_files(self):
        # Mở hộp thoại chọn file và cho phép chọn nhiều file PDF
        selected_files = filedialog.askopenfilenames(
            title="Chọn các file PDF",
            filetypes=[("PDF files", "*.pdf")]
        )

        if selected_files:
            for file in selected_files:
                # Thêm từng file vào listbox và danh sách pdf_files
                self.pdf_files.append(file)
                self.file_listbox.insert(tk.END, file)

            self.status_label.config(text=f"Đã chọn {len(self.pdf_files)} file PDF.")
            self.merge_button.config(state=tk.NORMAL)  # Kích hoạt nút "Nối file PDF"
        else:
            self.status_label.config(text="Không có file PDF nào được chọn.")
            self.merge_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút "Nối file PDF"

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một file PDF!")
            return

        # Chọn nơi lưu file PDF đã nối
        output_file = filedialog.asksaveasfilename(
            title="Lưu file PDF đã nối",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )

        if output_file:
            try:
                merger = PdfMerger()

                # Đang nối theo thứ tự tên file
                # Thêm từng file PDF vào merger
                for pdf in self.pdf_files:
                    merger.append(pdf)
                    
                # Lưu file PDF đã nối
                merger.write(output_file)
                merger.close()

                messagebox.showinfo("Thành công", f"Đã nối và lưu file PDF tại:\n{output_file}")
                self.status_label.config(text="Hoàn thành!")
                self.pdf_files = []  # Reset danh sách file
                self.file_listbox.delete(0, tk.END)  # Xóa tất cả các file trong listbox
                self.merge_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút sau khi hoàn thành
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi nối file PDF:\n{str(e)}")
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn nơi lưu file PDF!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
