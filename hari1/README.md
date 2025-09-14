# Analisa Kata Sering Muncul di Sebuah Berita dalam Satu Hari

## Latar Belakang

Sebuah lembaga riset politik ingin mendapatkan gambaran yang lebih mendalam mengenai narasi berita dan respons publik terhadapnya. Mereka memiliki dua set data:

1. Data Berita: Berisi judul dan isi artikel berita.

2. Data Komentar: Berisi komentar-komentar yang diberikan oleh pembaca terhadap artikel berita.

**Tugas Anda** adalah membuat program yang dapat memproses kedua file tersebut dan mencari kata yang sering muncul dalam Berita tersebut yang sedang terjadi dalam satu hari ini.

## Deskripsi Soal

Fokus dari bagian ini adalah mencari kata yang paling sering muncul di berbagai artikel.

- Pemuatan Data Berita: Baca seluruh data dari `news_data.csv`. Simpan data ini ke dalam dictionary di mana idBerita menjadi kunci dan data berita (Headline, Content) menjadi nilai.

- Pra-pemrosesan Teks: Lakukan langkah-langkah pembersihan kolom Content:

  1. Konversi ke huruf kecil.

  2. Penghapusan tanda baca dan angka.

- Analisis Frekuensi: Gunakan dictionary lain untuk menghitung frekuensi kemunculan setiap kata dari semua konten berita.

- Penyajian Hasil: Tampilkan semua kata yang paling sering muncul dari semua berita di dataset `news_data.csv` beserta frekuensinya.

## Struktur Data File

Ada dua file CSV yang akan Anda gunakan:

1. `news_data.csv`

   - Berisi data berita.

   - Kolom: `idBerita`, `Headline`, `Content`.

   - idBerita berfungsi sebagai Primary Key.

2. `comment_news.csv`

   - Berisi data komentar.

   - Kolom: `idKomentar`, `idBerita`, `Komentar`, `Rating`.

   - `idBerita` di sini berfungsi sebagai Foreign Key, yang menghubungkan setiap komentar ke berita yang relevan.

## Output/Hasil

## Catatan

1. File `comment_news.csv`, dan `news_data.csv` sudah disediakan, tidak usah membuat lagi

2. **Kerjakan mandiri dan jangan bertanya kepada teman lainnya**

3. Plagiasi akan di kurangi nilainya

4. Output harus sesuai dengan ketentuan soal

5. Gunakan tipe data `dictionary` untuk menyimpan data secara temporary

6. Usahakan menggunakan fungsi untuk penyelesaian soal


## Penilaian

1. Kemampuan Membuat Fungsi (35%)

2. Output sesuai dengan ketentuan soal (35%)

3. Orisinalitas (30%)

