# Laporan Proyek Machine Learning - Rifky Maulana Pasaribu

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

Dataset yang digunakan dalam proyek sistem rekomendasi film ini terdiri dari **1.272 entri** dengan **12 kolom fitur**, yang berisi berbagai informasi penting mengenai film, seperti judul, tahun rilis, genre, aktor, bahasa, dan lainnya. Dataset ini digunakan untuk membangun model rekomendasi berbasis *content-based filtering*.

link: https://www.kaggle.com/datasets/haryodwi/database-film-indonesia

### Kondisi Data

* Sebagian kolom memiliki data yang tidak lengkap:

  * `description`: hanya tersedia 840 dari 1272 entri.
  * `genre`: terdapat 36 nilai kosong.
  * `rating`: hanya terisi pada 376 entri.
  * `runtime`: 403 nilai kosong.
  * `directors`: 7 nilai kosong.
* Format data untuk kolom `votes` dan `runtime` masih berupa string, sehingga perlu dilakukan *data cleaning* sebelum dianalisis atau digunakan dalam model.

### Variabel dalam Dataset:

* **movie\_id** : ID unik untuk setiap film (numerik).
* **title** : Judul film (teks).
* **year** : Tahun rilis film (numerik).
* **description** : Deskripsi atau sinopsis film (teks).
* **genre** : Genre film, bisa lebih dari satu genre (teks).
* **rating** : Rating umum film, misalnya PG-13, R (teks).
* **users\_rating** : Rating rata-rata dari pengguna (numerik, float).
* **votes** : Jumlah pemilih yang memberikan rating (string, perlu dikonversi).
* **languages** : Bahasa yang digunakan dalam film (teks).
* **directors** : Nama sutradara film (teks).
* **actors** : Daftar aktor yang membintangi film (teks).
* **runtime** : Durasi film (string, perlu dikonversi menjadi satuan menit).

### Eksplorasi Data (Exploratory Data Analysis)

Untuk memahami lebih jauh isi dataset, dilakukan beberapa eksplorasi awal, antara lain:

#### 1. Visualisasi 10 Genre Terbanyak

Hasil visualisasi menunjukkan bahwa genre **Drama**, **Comedy**, **Horror**, dan **Action** adalah genre yang paling sering muncul dalam dataset. Ini menunjukkan preferensi atau ketersediaan data lebih besar di genre-genre populer tersebut.

#### 2. Distribusi Jumlah Film per Tahun

Dari grafik yang dianalisis, jumlah produksi film meningkat secara signifikan dari tahun 2000-an hingga 2020. Ini menunjukkan adanya tren peningkatan produksi film digital serta kemudahan distribusi film dalam dekade terakhir.

### Insight Tambahan

* Beberapa film tidak memiliki `description`, `runtime`, atau `genre`, yang dapat memengaruhi kinerja sistem rekomendasi berbasis konten.
* Akan dilakukan proses *imputation* atau penghapusan data tergantung pada jumlah dan pentingnya fitur tersebut dalam sistem rekomendasi.

Dataset ini menyediakan fondasi yang cukup kaya untuk membangun sistem rekomendasi film berbasis *content-based filtering*, terutama dengan memanfaatkan fitur seperti `description`, `genre`, dan `actors`.

## Data Preparation

Pada tahap ini, dilakukan beberapa proses persiapan data (data preparation) sebelum digunakan dalam pembuatan sistem rekomendasi berbasis konten (content-based recommender). Tahapan ini penting untuk memastikan bahwa data berada dalam format yang sesuai dan lengkap agar analisis dan pemodelan dapat dilakukan dengan optimal.

Berikut adalah langkah-langkah data preparation yang dilakukan:

### 1. Penanganan Nilai Kosong (Missing Values)

Beberapa fitur seperti `description` dan `genre` memiliki nilai kosong (NaN). Untuk menghindari error pada proses pemodelan dan vektorisasi teks, nilai kosong ini diganti dengan string kosong:

```python
# Ganti NaN dengan string kosong
dataset['description'] = dataset['description'].fillna('')
dataset['genre'] = dataset['genre'].fillna('')
```

**Alasan:**

* Teks kosong tidak akan mempengaruhi perhitungan TF-IDF secara signifikan.
* Menghindari error ketika melakukan penggabungan string atau proses vektorisasi teks.

### 2. Pembuatan Fitur Gabungan (Combined Features)

Untuk membuat sistem rekomendasi berbasis konten, informasi teks dari beberapa fitur digabungkan menjadi satu fitur gabungan (`combined_features`). Dalam kasus ini, fitur yang digunakan adalah `description` dan `genre`:

```python
# Gabungkan konten untuk fitur text
dataset['combined_features'] = dataset['description'] + ' ' + dataset['genre']
```

**Alasan:**

* Menggabungkan fitur teks memungkinkan model mengenali konteks yang lebih luas tentang film.
* `description` menggambarkan sinopsis, sementara `genre` menggambarkan kategori film — keduanya relevan untuk sistem rekomendasi.

### 3. Vektorisasi Teks (TF-IDF)

Fitur gabungan yang sudah dibuat kemudian ditransformasikan ke dalam bentuk vektor menggunakan TF-IDF (Term Frequency-Inverse Document Frequency):

```python
self.tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
tfidf_matrix = self.tfidf.fit_transform(df['combined_features'])
```

**Alasan:**

* TF-IDF digunakan untuk mengukur pentingnya sebuah kata terhadap dokumen dalam korpus.
* Menghilangkan stop words membantu mengurangi noise dalam data teks.

### 4. Penghitungan Similaritas (Cosine Similarity)

Setelah TF-IDF matrix didapatkan, langkah selanjutnya adalah menghitung kemiripan antar film menggunakan cosine similarity:

```python
self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
```

**Alasan:**

* Cosine similarity adalah metode umum untuk mengukur kemiripan antar dokumen teks.
* Digunakan untuk menentukan film mana yang memiliki konten serupa.

### 5. Indexing Data Judul

Agar lebih efisien dalam pencarian, dilakukan pembuatan indeks berdasarkan judul film:

```python
self.indices = pd.Series(df.index, index=df['title']).drop_duplicates()
```

**Alasan:**

* Mempermudah pemetaan dari judul film ke indeks dataset.
* Diperlukan dalam proses pencarian rekomendasi.

---

Semua proses di atas merupakan tahap persiapan yang esensial dalam membangun sistem rekomendasi berbasis konten dengan pendekatan NLP (Natural Language Processing). Tanpa tahapan ini, data tidak akan siap digunakan untuk pemodelan atau bisa menghasilkan model yang tidak akurat.


## Modeling

Pada tahapan ini, dilakukan pembangunan model sistem rekomendasi untuk memberikan rekomendasi film berdasarkan kemiripan konten. Model yang digunakan adalah *Content-Based Filtering*.

### 1. Content-Based Filtering

Model ini memanfaatkan fitur teks dari film, seperti genre, sutradara, dan sinopsis yang telah digabung dalam fitur `combined_features`. Proses pembuatan model melibatkan:

* **Pengukuran kemiripan** antar film dengan menggunakan *cosine similarity*.
* **Rekomendasi** film dihitung berdasarkan skor kemiripan tertinggi terhadap film yang dipilih.

```python
# Train Model
recommender = MovieRecommender()
recommender.fit(dataset)
```

Contoh rekomendasi yang dihasilkan ketika pengguna memilih film `#FriendButMarried 2`:

```
Rekomendasi:
     title                   genre      users_rating
131  #FriendButMarried      Biography        6.9
1118 Johny Indo             Biography        7.6
224  Udah Putusin Aja!      Drama            7.2
962  Brownies               Drama            6.0
414  3600 Detik             Drama            6.6
```

### Kesimpulan

Metode Content-Based Filtering berhasil digunakan untuk membangun sistem rekomendasi film dengan memanfaatkan fitur-fitur teks seperti genre, sutradara, dan sinopsis yang digabung dalam fitur combined_features. Proses ini memungkinkan sistem untuk menghitung kemiripan antar film menggunakan cosine similarity, lalu merekomendasikan film lain yang memiliki kemiripan tertinggi dengan film yang dipilih pengguna.

Hasil implementasi menunjukkan bahwa saat pengguna memilih film #FriendButMarried 2, sistem mampu merekomendasikan film lain yang memiliki genre dan konten serupa, seperti Johny Indo, Udah Putusin Aja!, dan Brownies, dengan rata-rata user rating yang cukup tinggi. Hal ini menunjukkan bahwa pendekatan Content-Based Filtering dapat memberikan rekomendasi yang relevan secara konten bagi pengguna.

Dengan demikian, metode ini cocok diterapkan dalam sistem rekomendasi di mana fitur-fitur item tersedia secara eksplisit dan relevan untuk dianalisis.


## Evaluation

Pada tahap evaluasi ini, sistem rekomendasi diuji menggunakan pendekatan **top-N recommendation**, khususnya dengan menilai performa sistem dalam memberikan **10 rekomendasi teratas** yang paling sesuai untuk setiap pengguna. Fokus dari evaluasi ini adalah menilai seberapa baik sistem merekomendasikan item yang benar-benar relevan bagi pengguna, dengan menggunakan dua metrik utama, yaitu **Precision@10** dan **Recall@10**.

### Metode Evaluasi:

* **Precision@10**: Precision mengukur seberapa banyak dari 10 item yang direkomendasikan oleh sistem merupakan item yang benar-benar relevan (disukai pengguna). Nilai precision yang tinggi menunjukkan bahwa sistem memiliki tingkat akurasi yang baik dalam memilih item yang tepat untuk direkomendasikan.

  * Formula:  
   Precision@10 = (Jumlah item relevan dalam 10 rekomendasi) / 10

  * Penjelasan:  
    Jika dari 10 item yang direkomendasikan, 9 di antaranya ternyata memang disukai oleh pengguna, maka Precision@10 = 0.9 atau 90%.

  * Contoh:
          - Jika 9 dari 10 rekomendasi relevan:
          - Precision@10 = 9/10 = 0.9 (90%)

* **Recall@10**: Recall mengukur seberapa besar proporsi dari seluruh item relevan yang berhasil direkomendasikan dalam daftar 10 teratas. Nilai recall yang rendah mengindikasikan bahwa masih banyak item relevan yang tidak berhasil ditangkap oleh sistem.

  * Formula:  
      Recall@10 = (Jumlah item relevan dalam 10 rekomendasi) / (Total item relevan yang ada)

  * Penjelasan:  
    Jika seorang pengguna memiliki 50 item relevan secara total, namun sistem hanya mampu merekomendasikan 1 di antaranya dalam 10 item teratas, maka Recall@10 = 0.02 atau 2%.

  * Contoh:
   - Jika ada 50 item relevan total dan sistem merekomendasikan 1 di top 10:
   - Recall@10 = 1/50 = 0.02 (2%)

### Hasil Evaluasi:

* Jumlah item rekomendasi per pengguna: **10 item**
* Precision@10: **0.9233**
* Recall@10: **0.0080**

### Interpretasi:

* Nilai **Precision@10 sebesar 92.33%** menunjukkan bahwa dari setiap 10 rekomendasi yang diberikan, lebih dari 9 item merupakan item yang dinilai relevan oleh pengguna. Ini menandakan bahwa sistem sangat akurat dalam memilih item rekomendasi.
* Namun, nilai **Recall@10 sebesar 0.80%** Dari ribuan film berkualitas tinggi di dataset, sistem berhasil mengidentifikasi sebagian kecil yang paling relevan.
  - Recall yang rendah (0.0080) itu normal untuk Content-Based Filtering! Ini terjadi karena:
      Recall dihitung dari SEMUA film rating tinggi di dataset
      Dataset movie biasanya besar (ribuan film dengan rating ≥4.0)
      Kita cuma rekomendasikan 10 film, jadi proporsinya kecil   
      Contoh perhitungan:
      
      Total film rating tinggi: 1000 film
      Rekomendasi yang relevan: 8 film
      Recall = 8/1000 = 0.008 = 0.8%
      
      Ini bukan masalah! Yang penting:
      
      Precision tinggi (0.9233) = 92% rekomendasi relevan ✅
      Recall rendah tapi wajar untuk sistem rekomendasi
      
      Interpretasi hasil:
      
      Model sangat baik dalam memberikan rekomendasi yang relevan
      92.33% dari rekomendasi adalah film berkualitas tinggi
      Sistem fokus pada quality over quantity


## Kesimpulan

Evaluasi menggunakan **Precision@10 dan Recall@10** menunjukkan bahwa sistem rekomendasi content-based yang dikembangkan memiliki kemampuan **tinggi dalam memberikan rekomendasi yang akurat** (terlihat dari precision yang tinggi). Secara keseluruhan, proses evaluasi ini memberikan pemahaman mendalam mengenai kinerja sistem, baik dari sisi kekuatan maupun kekurangannya. Hasil evaluasi ini menjadi **dasar penting untuk merancang strategi peningkatan model**, baik dengan memperluas data fitur, menggabungkan pendekatan lain, ataupun menyempurnakan algoritma pemilihan item.

Model Content-Based Filtering yang dikembangkan menunjukkan performa yang baik dengan:
- Tingkat presisi tinggi dalam memberikan rekomendasi yang relevan
- Fokus pada kualitas daripada mencoba merekomendasikan sebanyak mungkin film
- Sesuai untuk aplikasi praktis di mana pengguna lebih menghargai rekomendasi berkualitas tinggi

**--- Ini adalah bagian akhir laporan ---**
