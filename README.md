# Analisa Tren Sebuah Berita dalam Satu Hari

## Latar Belakang

Sebuah lembaga riset politik ingin mendapatkan gambaran yang lebih mendalam mengenai narasi berita dan respons publik terhadapnya. Mereka memiliki dua set data:

1. Data Berita: Berisi judul dan isi artikel berita.
2. Data Komentar: Berisi komentar-komentar yang diberikan oleh pembaca terhadap artikel berita.

**Tugas Anda** adalah membuat program yang dapat melakukan proses pembersihan data di tiap kolom pada kedua file csv.

## Deskripsi Soal

Fokus dari bagian ini adalah melakukan pra-pemrosesan teks untuk mendapatkan teks bersih tanpa tanda baca dan angka di setiap kolom pada kedua file CSV.

- Pemuatan Data Berita: Baca seluruh data dari news_data.csv. Simpan data ini ke dalam dictionary di mana idBerita menjadi kunci dan data berita (Headline, Content) menjadi nilai.

- Pra-pemrosesan Teks: Lakukan langkah-langkah pembersihan kolom Content:

  1. Konversi ke huruf kecil.

  2. Penghapusan tanda baca dan angka.

  3. Penghapusan stop words (gunakan file stopwords.txt).

## Struktur Data File

Ada dua file CSV yang akan Anda gunakan:

1. `news_data.csv`

   - Berisi data berita.

   - Kolom: `idBerita`, `Headline`, `Content`.

   - idBerita berfungsi sebagai Primary Key.

2. `comment_news.csv`

   - Berisi data komentar.

   - Kolom: `idKomentar`, `idBerita`, `Komentar`.

   - `idBerita` di sini berfungsi sebagai Foreign Key, yang menghubungkan setiap komentar ke berita yang relevan.
