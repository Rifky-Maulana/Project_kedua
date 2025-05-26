# Laporan Proyek Machine Learning - Nama Anda

## Project Overview

Dalam era digital saat ini, sistem rekomendasi telah menjadi salah satu komponen penting dalam membantu pengguna menavigasi informasi yang berlimpah, terutama dalam industri hiburan seperti film. Dengan semakin meningkatnya jumlah film yang dirilis setiap tahun, pengguna seringkali kesulitan untuk menemukan film yang sesuai dengan preferensi pribadi mereka. Untuk mengatasi masalah ini, sistem rekomendasi digunakan untuk memberikan saran yang relevan kepada pengguna berdasarkan berbagai pendekatan.

Proyek ini bertujuan untuk membangun **sistem rekomendasi film berbasis _content-based filtering_** dengan menggunakan dataset film Indonesia dari Kaggle. Pendekatan content-based filtering bekerja dengan menganalisis karakteristik konten dari film, seperti genre, sinopsis, sutradara, dan pemeran utama, kemudian merekomendasikan film lain yang memiliki kemiripan konten. Berbeda dengan _collaborative filtering_ yang mengandalkan interaksi pengguna lain, pendekatan ini lebih cocok digunakan pada skenario cold-start, ketika data interaksi pengguna masih minim atau belum tersedia.

Masalah ini penting untuk diselesaikan karena:
- **Relevansi personalisasi**: Pengguna memiliki preferensi yang unik, dan sistem berbasis konten memungkinkan sistem untuk menyarankan film secara personal tanpa bergantung pada data pengguna lain.
- **Masalah cold-start**: Pada sistem baru atau dataset terbatas, _content-based filtering_ dapat memberikan hasil yang lebih baik dibanding collaborative filtering.
- **Meningkatkan konsumsi konten lokal**: Dengan rekomendasi yang relevan, penonton akan lebih mudah menemukan film Indonesia yang sesuai dengan minat mereka, sehingga berpotensi meningkatkan ketertarikan terhadap karya dalam negeri.

Studi oleh Lops et al. (2011) menunjukkan bahwa content-based filtering sangat cocok untuk domain seperti film karena kaya akan fitur deskriptif yang bisa diekstrak, seperti teks sinopsis atau metadata film. Selain itu, Ricci et al. (2011) menekankan bahwa sistem rekomendasi berbasis konten dapat berfungsi lebih baik dalam kondisi data pengguna yang terbatas, terutama di fase awal pengembangan sistem (_cold-start problem_). Hal ini membuat pendekatan ini sangat relevan untuk digunakan dalam konteks film lokal yang belum banyak mendapat rating atau ulasan dari pengguna.

Dataset yang digunakan dalam proyek ini adalah "Database Film Indonesia" yang dirilis di platform Kaggle oleh Haryo Dwi, yang memuat data deskriptif seperti judul film, sinopsis, genre, sutradara, produser, pemeran utama, dan tahun rilis. Dataset ini sangat cocok untuk membangun sistem rekomendasi berbasis konten karena mengandung informasi konten yang lengkap dan bervariasi.

### Referensi

- Lops, P., De Gemmis, M., & Semeraro, G. (2011). Content-based Recommender Systems: State of the Art and Trends. In F. Ricci, L. Rokach, B. Shapira, & P.B. Kantor (Eds.), *Recommender Systems Handbook* (pp. 73–105). Springer. https://doi.org/10.1007/978-0-387-85820-3_3  
- Ricci, F., Rokach, L., & Shapira, B. (2011). *Introduction to Recommender Systems Handbook*. Springer.  
- Adomavicius, G., & Tuzhilin, A. (2005). Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. *IEEE Transactions on Knowledge and Data Engineering*, 17(6), 734–749. https://doi.org/10.1109/TKDE.2005.99  
- Haryo Dwi. (2022). *Database Film Indonesia* [Data set]. Kaggle. https://www.kaggle.com/datasets/haryodwi/database-film-indonesia  


## Business Understanding

Dalam proyek ini, sistem rekomendasi dirancang menggunakan pendekatan **content-based filtering** yang memanfaatkan informasi atau deskripsi konten dari masing-masing film untuk memberikan rekomendasi yang relevan bagi pengguna. Pendekatan ini tidak memerlukan data interaksi antar pengguna, melainkan hanya mengandalkan metadata dari film seperti genre dan sinopsis.

### Problem Statements

1. **Bagaimana cara membantu pengguna menemukan film Indonesia yang sesuai dengan preferensi mereka secara otomatis tanpa harus menelusuri satu per satu?**  
   Banyaknya jumlah film yang tersedia dapat membuat pengguna kesulitan memilih film yang sesuai dengan selera mereka.

2. **Bagaimana memanfaatkan metadata film seperti genre dan sinopsis untuk mengukur kemiripan antar film?**  
   Data film umumnya dilengkapi dengan deskripsi dan genre, namun belum banyak sistem yang mampu memanfaatkan informasi ini untuk memberikan rekomendasi personal.

3. **Bagaimana membangun sistem rekomendasi yang dapat memberikan daftar film yang mirip dengan film yang disukai pengguna?**  
   Dengan pendekatan berbasis konten, sistem dapat menyarankan film yang memiliki karakteristik mirip dengan film yang sudah dipilih oleh pengguna.

### Goals

1. **Mengembangkan sistem rekomendasi berbasis content-based filtering yang dapat menyarankan film Indonesia serupa berdasarkan konten.**  
   Sistem akan menganalisis atribut film seperti genre dan sinopsis untuk menemukan film-film yang mirip satu sama lain.

2. **Mengolah dan mengekstraksi fitur penting dari data film seperti sinopsis dan genre, kemudian mengukurnya menggunakan teknik seperti TF-IDF dan cosine similarity.**  
   Proyek akan menerapkan teknik NLP sederhana untuk mengubah deskripsi film menjadi vektor numerik sehingga bisa dibandingkan kemiripannya.

3. **Meningkatkan pengalaman pengguna dalam menemukan film lokal Indonesia yang sesuai dengan minat mereka.**  
   Sistem ini bertujuan mempercepat proses pencarian film yang relevan dan meningkatkan kepuasan pengguna terhadap layanan.

---

### Solution Approach

Untuk mencapai tujuan-tujuan di atas, digunakan beberapa pendekatan solusi sebagai berikut:

#### Solution 1: TF-IDF Vectorizer + Cosine Similarity  
Pendekatan utama dalam proyek ini menggunakan **TF-IDF (Term Frequency–Inverse Document Frequency)** untuk mengubah teks sinopsis film menjadi representasi vektor. Kemudian, digunakan **cosine similarity** untuk mengukur seberapa mirip dua buah film berdasarkan kemiripan vektor sinopsis mereka.

- Kelebihan: Sederhana, cepat, dan efektif untuk teks pendek seperti sinopsis.
- Kekurangan: Tidak memahami konteks atau makna kata secara mendalam.

#### Solution 2: Genre-based Filtering (One-Hot Encoding + Cosine Similarity)  
Selain sinopsis, sistem juga mempertimbangkan **genre** film. Genre diubah menjadi format vektor dengan **one-hot encoding**, kemudian dihitung kemiripan antar film berdasarkan genre-nya.

- Kelebihan: Membantu merekomendasikan film dengan tema serupa walaupun sinopsis berbeda jauh.
- Kekurangan: Genre bisa terlalu umum dan tidak cukup untuk merepresentasikan keseluruhan isi film.

> Kombinasi kedua pendekatan ini membantu menghasilkan rekomendasi yang lebih akurat dan personal karena mempertimbangkan deskripsi dan genre secara bersamaan.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai jumlah data, kondisi data, dan informasi mengenai data yang digunakan. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya, uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
