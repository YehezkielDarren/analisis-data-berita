import streamlit as st
from scripts.script import *

st.title("Analisis Tren Berita dan Komentar")

st.markdown("""
Aplikasi ini melakukan pra-pemrosesan teks pada data berita dan komentar
untuk mengidentifikasi kata-kata yang paling sering muncul.
""")
# Processing logic
try:
    comment_news_data = read_comment("comment_news.csv")
    news_data = read_news("news_data.csv")
except Exception as e:
    st.error(f"Terjadi kesalahan saat membaca file: {e}")
    comment_news_data = None
    news_data = None

if comment_news_data is not None and news_data is not None:
    st.success("File berhasil diunggah dan diproses!")

    # Display cleaned data in tabs
    tab1, tab2 = st.tabs(["Data Komentar Bersih", "Data Berita Bersih"])

    with tab1:
        st.subheader("Data Komentar Bersih")
        st.table(comment_news_data)
        
    with tab2:
        st.subheader("Data Berita Bersih")
        st.table(news_data)
else:
    st.warning("Pastikan file 'comment_news.csv' dan 'news_data.csv' tersedia dan formatnya benar.")
