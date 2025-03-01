import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pdfplumber
import pandas as pd
import os
from tabula import read_pdf

class PDFToExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chuyển đổi PDF sang Excel")
        self.root.geometry("600x400")

        # Tạo Notebook (Tab Control)
        self.tabControl = ttk.Notebook(root)
        
        # Tab 1 - PDFPlumber
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="PDFPlumber")
        self.create_pdfplumber_tab()

        # Tab 2 - Tabula
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="Tabula-Py")
        self.create_tabula_tab()

        self.tabControl.pack(expand=1, fill="both")

    def create_pdfplumber_tab(self):
        """Tạo giao diện cho tab PDFPlumber"""
        label = tk.Label(self.tab1, text="Chọn file PDF để chuyển sang Excel (PDFPlumber)", font=("Arial", 12))
        label.pack(pady=10)

        self.btn_choose1 = tk.Button(self.tab1, text="Chọn PDF", command=self.choose_pdf_plumber, font=("Arial", 10))
        self.btn_choose1.pack(pady=5)

        self.file_label1 = tk.Label(self.tab1, text="Chưa chọn file", font=("Arial", 10))
        self.file_label1.pack(pady=5)

        self.btn_convert1 = tk.Button(self.tab1, text="Chuyển đổi", command=self.convert_pdf_to_excel_plumber, font=("Arial", 10), state=tk.DISABLED)
        self.btn_convert1.pack(pady=10)

    def create_tabula_tab(self):
        """Tạo giao diện cho tab Tabula-Py"""
        label = tk.Label(self.tab2, text="Chọn file PDF để chuyển sang Excel (Tabula-Py)", font=("Arial", 12))
        label.pack(pady=10)

        self.btn_choose2 = tk.Button(self.tab2, text="Chọn PDF", command=self.choose_pdf_tabula, font=("Arial", 10))
        self.btn_choose2.pack(pady=5)

        self.file_label2 = tk.Label(self.tab2, text="Chưa chọn file", font=("Arial", 10))
        self.file_label2.pack(pady=5)

        self.btn_convert2 = tk.Button(self.tab2, text="Chuyển đổi", command=self.convert_pdf_to_excel_tabula, font=("Arial", 10), state=tk.DISABLED)
        self.btn_convert2.pack(pady=10)

    def choose_pdf_plumber(self):
        """Chọn file PDF cho phương pháp PDFPlumber"""
        self.pdf_path1 = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if self.pdf_path1:
            self.file_label1.config(text=f"File: {os.path.basename(self.pdf_path1)}")
            self.btn_convert1.config(state=tk.NORMAL)

    def choose_pdf_tabula(self):
        """Chọn file PDF cho phương pháp Tabula-Py"""
        self.pdf_path2 = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if self.pdf_path2:
            self.file_label2.config(text=f"File: {os.path.basename(self.pdf_path2)}")
            self.btn_convert2.config(state=tk.NORMAL)

    def convert_pdf_to_excel_plumber(self):
        """Chuyển đổi PDF sang Excel bằng PDFPlumber"""
        if not self.pdf_path1:
            messagebox.showerror("Lỗi", "Vui lòng chọn file PDF trước!")
            return

        try:
            data = self.extract_table_from_pdf(self.pdf_path1)
            if not data:
                messagebox.showerror("Lỗi", "Không tìm thấy bảng trong PDF!")
                return

            output_path = self.pdf_path1.replace(".pdf", "_plumber.xlsx")
            df = pd.DataFrame(data[1:], columns=data[0])  # Dòng đầu tiên làm tiêu đề
            df.to_excel(output_path, index=False)

            messagebox.showinfo("Thành công", f"Chuyển đổi hoàn tất!\nFile Excel: {output_path}")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def convert_pdf_to_excel_tabula(self):
        """Chuyển đổi PDF sang Excel bằng Tabula-Py"""
        if not self.pdf_path2:
            messagebox.showerror("Lỗi", "Vui lòng chọn file PDF trước!")
            return

        try:
            tables = read_pdf(self.pdf_path2, pages="all", multiple_tables=True)
            if not tables:
                messagebox.showerror("Lỗi", "Không tìm thấy bảng trong PDF!")
                return

            output_path = self.pdf_path2.replace(".pdf", "_tabula.xlsx")
            with pd.ExcelWriter(output_path) as writer:
                for i, table in enumerate(tables):
                    table.to_excel(writer, sheet_name=f"Trang_{i+1}", index=False)

            messagebox.showinfo("Thành công", f"Chuyển đổi hoàn tất!\nFile Excel: {output_path}")

        except Exception as e:
            messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

    def extract_table_from_pdf(self, pdf_path):
        """Hàm trích xuất bảng từ PDF bằng PDFPlumber"""
        data = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        cleaned_row = [cell.replace("\n", " ") if cell else "" for cell in row]
                        data.append(cleaned_row)
        return data

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToExcelApp(root)
    root.mainloop()
