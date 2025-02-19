import tkinter as tk
from tkinter import filedialog
import openai
from utils import *
import traceback

class AIChatApp(tk.Tk):
    def __init__(self, root):
        self.root = root
        self.root.title("AI00 |TRỢ LÝ AI-CHATBOT")
        self.root.geometry("500x700")
        self.f_thiet_lap_fav_icon()
        # Cấu hình OpenAI API
        openai.api_key = "YOUR_OPENAI_API_KEY"

        # Khung chat
        self.chat_history = tk.Text(self.root, wrap=tk.WORD, bg="white", font=("Arial", 12))
        self.chat_history.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.chat_history.tag_configure("user", foreground="blue")
        self.chat_history.tag_configure("ai", foreground="green")
        self.chat_history.tag_configure("file", foreground="purple")
        
        # Nội dung mặc định
        default_message = """Tôi có thể giúp:
        - Tự động hoá nhập liệu từ file Excel, pdf, hình ảnh
        - Tự động gửi mail xác nhận, ...
        - Tra cứu quy định của công ty"""
        self.chat_history.insert(tk.END, default_message, "ai")

        # Ô nhập liệu
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=5, padx=10, fill=tk.X)

        # Frame chứa nút
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=5, padx=10, fill=tk.X)

        # Nút đính kèm tệp
        self.attach_button = tk.Button(self.button_frame, text="Đính kèm tệp", command=self.attach_file, font=("Arial", 12))
        self.attach_button.pack(side=tk.LEFT)

        # Nút gửi
        self.send_button = tk.Button(self.button_frame, text="Gửi", command=self.chat_with_ai, font=("Arial", 14), bg="lightblue")
        self.send_button.pack(side=tk.RIGHT)
    
    def f_thiet_lap_fav_icon(self):
        """Configures window size and position."""
        # utils_controller_set_size_of_windown_250215_10h24.f_utils_set_window_size_of_new_view(self, maximize=False)
        # f_utils_set_center_screen(self)
        try:
            f_utils_setup_fav_icon(self.root)
        except RecursionError:
            print("Error: Maximum recursion depth exceeded! Check if `f_utils_setup_fav_icon` calls itself.")
        except Exception as e:
            print(f"Error setting up favicon: {e}")
            traceback.print_exc()
    
    def chat_with_ai(self):
        user_input = self.entry.get()
        self.chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
        self.entry.delete(0, tk.END)
        
        # Gửi yêu cầu đến OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        
        ai_response = response["choices"][0]["message"]["content"]
        self.chat_history.insert(tk.END, "AI: " + ai_response + "\n", "ai")
    
    def attach_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.chat_history.insert(tk.END, f"[File attached: {file_path}]\n", "file")
