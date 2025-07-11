# 📌 Lưu file này tên app.py, rồi chạy: streamlit run app.py

import streamlit as st
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

st.title("📊 Dashboard Phân Tích Văn Bản")

uploaded_file = st.file_uploader("Tải file .txt lên", type="txt")
if uploaded_file:
    text = uploaded_file.read().decode("utf-8").lower()
    
    # Làm sạch
    words = re.findall(r'\b\w+\b', text)
    stopwords = set(['là', 'và', 'của', 'trong', 'một', 'có', 'với', 'cho', 'được', 'đến', 'từ'])
    words_filtered = [w for w in words if w not in stopwords and len(w) > 2]

    st.markdown(f"**Tổng số từ:** {len(words)}")
    st.markdown(f"**Số từ sau khi lọc:** {len(words_filtered)}")
    
    # Từ khóa phổ biến
    counter = Counter(words_filtered)
    common = counter.most_common(10)
    st.markdown("### 🔑 Top 10 từ khóa:")
    st.table(common)

    # Word Cloud
    st.markdown("### ☁️ Word Cloud")
    wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(words_filtered))
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
