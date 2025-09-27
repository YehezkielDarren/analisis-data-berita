import streamlit as st
from script import read_comment, read_news, extract_text, find_top_words

def app():
   st.title("Analisa Kata Sering Muncul di Sebuah Berita dalam Satu Hari")
   st.write("Menampilkan 10 kata yang paling sering muncul dari gabungan komentar dan isi berita")
   
   load_comment = read_comment('comment_news.csv')
   load_news = read_news('news_data.csv')
   
   extract = extract_text(load_comment, load_news)
   
   res = find_top_words(extract)
   st.table(res)

if __name__ == "__main__":
    app()