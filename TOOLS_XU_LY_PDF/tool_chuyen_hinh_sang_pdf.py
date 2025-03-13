import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Chuyển ảnh sang PDF")
        self.root.geometry("400x200")

        # Biến lưu trữ đường dẫn file ảnh
        self.image_files = []

        # Tạo giao diện
        self.label = tk.Label(root, text="Chọn file ảnh để chuyển sang PDF:", font=("Arial", 12))
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Chọn ảnh", command=self.select_images)
        self.select_button.pack(pady=5)

        self.convert_button = tk.Button(root, text="Chuyển sang PDF", command=self.convert_to_pdf, state=tk.DISABLED)
        self.convert_button.pack(pady=5)

        self.status_label = tk.Label(root, text="", fg="blue")
        self.status_label.pack(pady=10)

    def select_images(self):
        # Mở hộp thoại chọn file và cho phép chọn nhiều file ảnh
        self.image_files = filedialog.askopenfilenames(
            title="Chọn file ảnh",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

        if self.image_files:
            self.status_label.config(text=f"Đã chọn {len(self.image_files)} file ảnh.")
            self.convert_button.config(state=tk.NORMAL)  # Kích hoạt nút "Chuyển sang PDF"
        else:
            self.status_label.config(text="Không có file ảnh nào được chọn.")
            self.convert_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút "Chuyển sang PDF"

    def convert_to_pdf(self):
        if not self.image_files:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn ít nhất một file ảnh!")
            return

        # Chọn nơi lưu file PDF
        output_file = filedialog.asksaveasfilename(
            title="Lưu file PDF",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")]
        )

        if output_file:
            try:
                # Tạo một đối tượng PDF
                pdf = FPDF()

                # Thêm từng ảnh vào PDF
                for image_file in self.image_files:
                    # Mở ảnh bằng Pillow
                    img = Image.open(image_file)

                    # Chuyển đổi ảnh sang PDF
                    pdf.add_page()
                    pdf.image(image_file, x=10, y=10, w=190)  # Điều chỉnh kích thước và vị trí

                # Lưu file PDF
                pdf.output(output_file)

                messagebox.showinfo("Thành công", f"Đã chuyển đổi và lưu file PDF tại:\n{output_file}")
                self.status_label.config(text="Hoàn thành!")
                self.image_files = []  # Reset danh sách file
                self.convert_button.config(state=tk.DISABLED)  # Vô hiệu hóa nút sau khi hoàn thành
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi khi chuyển đổi:\n{str(e)}")
        else:
            messagebox.showwarning("Cảnh báo", "Bạn chưa chọn nơi lưu file PDF!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()