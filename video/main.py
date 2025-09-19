import streamlit as st
from scripts.script import *

st.title("Analisis Tren Berita dan Komentar")

st.markdown("""
Aplikasi ini melakukan pra-pemrosesan teks pada data berita dan komentar
untuk mengidentifikasi kata-kata yang paling sering muncul.
""")

# File uploader section
col1, col2 = st.columns(2)

with col1:
    comment_file = st.file_uploader("Unggah file comment_news.csv", type=['csv'])

with col2:
    news_file = st.file_uploader("Unggah file news_data.csv", type=['csv'])

# Processing logic
if comment_file and news_file:
    comment_news_data = read_comment(comment_file)
    news_data = read_news(news_file)

    if comment_news_data is not None and news_data is not None:
        st.success("File berhasil diunggah dan diproses!")

        # Display cleaned data in tabs
        tab1, tab2 = st.tabs(["Data Komentar Bersih", "Data Berita Bersih"])

        with tab1:
            st.subheader("Data Komentar Bersih")
            df_comment = pd.DataFrame(comment_news_data)
            st.dataframe(df_comment)
            
        with tab2:
            st.subheader("Data Berita Bersih")
            df_news = pd.DataFrame(news_data)
            st.dataframe(df_news)

else:
    st.info("Silakan unggah kedua file CSV untuk memulai analisis.")