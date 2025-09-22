import csv
import streamlit as st

# load data 
def load_news(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def load_comments(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)


def process_data(news_list, comments_list):
    # Buat dictionary untuk kumpulkan komentar per idBerita
    comments_per_news = {}
    for c in comments_list:
        idb = c['idBerita']
        rating = float(c['Rating'])
        if idb not in comments_per_news:
            comments_per_news[idb] = {'ratings': [], 'count': 0}
        comments_per_news[idb]['ratings'].append(rating)
        comments_per_news[idb]['count'] += 1

    # Buat list hasil gabungan
    result = []
    for n in news_list:
        idb = n['idBerita']
        headline = n['Headline']
        # hitung rata-rata rating
        if idb in comments_per_news:
            jumlah = comments_per_news[idb]['count']
            rata = sum(comments_per_news[idb]['ratings']) / jumlah
        else:
            jumlah = 0
            rata = 0
        result.append({
            'ID Berita': idb,
            'Headline': headline,
            'Rata-rata Rating': round(rata, 2),
            'Jumlah Komentar': jumlah
        })

    #Urutkan berdasarkan rating
    def ambil_rating(item):
        return item['Rata-rata Rating']

    result.sort(key=ambil_rating, reverse=True)

    return result

# --- Fungsi untuk tampilkan di Streamlit ---
def main():
    st.title("Analisis Sentimen & Popularitas Berita")
    st.write("Menampilkan ID, Headline, Rata-rata Rating, dan Jumlah Komentar, diurutkan dari rating tertinggi.")

    # Baca data CSV
    news_data = load_news('news_data.csv')
    comment_data = load_comments('comment_news.csv')

 
    hasil = process_data(news_data, comment_data)

    
    st.table(hasil) 

if __name__ == '__main__':
    main()
