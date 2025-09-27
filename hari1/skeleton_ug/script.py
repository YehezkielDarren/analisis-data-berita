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

def find_top_words(data, n=10): # parameter jangan diubah
    # isi dengan memproses data
    # hitung kemunculan tiap kata pada key 'teks'
    # kembalikan n kata yang paling sering muncul dalam bentuk dictionary
    
    # Hint : boleh gunakan ini untuk sorting
    # sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    # top_n_ascending = sorted_words[:n]
    pass