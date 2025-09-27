import streamlit as st
from script import *

def app():
   st.title("Analisa Kata Sering Muncul di Sebuah Berita dalam Satu Hari")
   st.write("Menampilkan 10 kata yang paling sering muncul dari gabungan komentar dan isi berita")
   
   load_news = read_news('news_data.csv')
   
   res = find_top_words(load_news)
   st.table(res)

if __name__ == "__main__":
    app()