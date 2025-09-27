import csv

def clean_text(data):
    # isi dengan membersihkan text
    # Hint : gunakan str.lower(), str.rstrip(), str.translate(), str.maketrans(), string.punctuation, string.digits, str.split()
    # split kata berdasarkan spasi
    pass

def read_news(filename):
    # isi dengan membaca file csv
    # Hint : gunakan csv.DictReader
    # gunakan fungsi clean_text untuk membersihkan text pada kolom 'Content'
    # kembalikan dalam bentuk list of dictionary
    pass

def read_comment(filename):
    # isi dengan membaca file csv
    # Hint : gunakan csv.DictReader
    # gunakan fungsi clean_text untuk membersihkan text pada kolom 'Komentar'
    # kembalikan dalam bentuk list of dictionary
    pass

def find_top_words(data, n=10): # parameter jangan diubah
    # isi dengan memproses data
    # hitung kemunculan tiap kata pada key 'teks'
    # kembalikan n kata yang paling sering muncul dalam bentuk dictionary
    pass

def extract_text(comments,news):
    # isi dengan mengekstrak text dari komentar dan berita
    # ambil data dari key 'komentar' pada comments
    # ambil data dari key 'content' pada news
    # gabungkan kedua list tersebut
    # kembalikan dalam bentuk list of dictionary dengan key 'teks'
    pass