# Lưu file này là app.py
import streamlit as st

st.title("Chào bạn 👋")
st.write("Đây là ứng dụng đầu tiên dùng Streamlit!")

name = st.text_input("Nhập tên của bạn:")
if name:
    st.success(f"Xin chào, {name}!")