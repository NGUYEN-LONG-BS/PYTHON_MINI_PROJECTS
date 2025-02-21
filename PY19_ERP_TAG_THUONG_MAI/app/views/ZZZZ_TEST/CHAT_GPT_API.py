import openai
import tkinter as tk
from tkinter import scrolledtext
from utils import *

# Đặt khóa API OpenAI của bạn tại đây
openai.api_key = 'YOUR_API_KEY'

def chatgpt_response(query):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Hoặc sử dụng "gpt-4" nếu có
            prompt=query,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error: {e}")
        print("Error at function: ", f_utils_get_current_function_name())
        return f"Error: {str(e)}"

def send_query():
    user_input = user_input_box.get("1.0", "end-1c")  # Lấy văn bản từ hộp nhập liệu
    if user_input.strip():
        chat_area.insert(tk.END, f"You: {user_input}\n")
        response = chatgpt_response(user_input)
        chat_area.insert(tk.END, f"ChatGPT: {response}\n")
        user_input_box.delete("1.0", "end")  # Xóa ô nhập liệu

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("ChatGPT Tkinter Interface")

# Tạo cửa sổ cuộn để hiển thị cuộc trò chuyện
chat_area = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
chat_area.grid(row=0, column=0, padx=10, pady=10)
chat_area.config(state=tk.DISABLED)

# Tạo ô nhập liệu
user_input_box = tk.Text(root, height=5, width=40)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Tạo nút gửi
send_button = tk.Button(root, text="Send", width=10, command=send_query)
send_button.grid(row=2, column=0, padx=10, pady=10)

# Chạy giao diện
root.mainloop()
