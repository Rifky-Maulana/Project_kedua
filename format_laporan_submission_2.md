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

Pada tahapan ini, dilakukan pembangunan model sistem rekomendasi untuk memberikan rekomendasi film berdasarkan kemiripan konten. Model yang digunakan adalah *Content-Based Filtering*, dan untuk memperkaya hasil, ditambahkan juga alternatif model menggunakan *K-Nearest Neighbors (KNN)* sebagai pembanding.

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

Pada tahap evaluasi ini, sistem rekomendasi diuji menggunakan metode **rating prediction**, yaitu dengan memprediksi rating suatu film berdasarkan rating dari film-film yang direkomendasikan.

### Metode Evaluasi:

* **Mean Squared Error (MSE)**: Rata-rata kuadrat dari selisih antara nilai aktual dan prediksi. Semakin kecil nilainya, semakin baik model.

  * Formula: $MSE = \frac{1}{n} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$
* **Mean Absolute Error (MAE)**: Rata-rata dari nilai absolut selisih antara nilai aktual dan prediksi.

  * Formula: $MAE = \frac{1}{n} \sum_{i=1}^{n}|y_i - \hat{y}_i|$
* **Root Mean Squared Error (RMSE)**: Akar dari MSE, memberikan interpretasi dalam satuan yang sama dengan rating.

  * Formula: $RMSE = \sqrt{MSE}$
* **Accuracy (\u00b10.5)**: Persentase prediksi yang berada dalam rentang \u00b10.5 dari rating aktual.

### Hasil Evaluasi:

* Jumlah film yang dievaluasi: **100 film**
* MSE: **2.0669**
* MAE: **1.0944**
* RMSE: **1.4377**
* Accuracy (\u00b10.5): **35.0%**

### Interpretasi:

* Model memiliki **akurasi 35%**, artinya hanya 35 dari 100 prediksi yang memiliki selisih tidak lebih dari 0.5 dari rating asli. Ini menunjukkan bahwa model masih dapat dikembangkan lebih lanjut untuk meningkatkan performa.
* **MAE dan RMSE** yang cukup besar menandakan bahwa prediksi rating rata-rata masih memiliki selisih lebih dari 1 poin terhadap rating aktual, yang bisa berdampak pada kepuasan pengguna terhadap sistem rekomendasi.

### Visualisasi:

* **Scatter plot** menunjukkan sebaran nilai aktual vs prediksi.
* **Histogram residuals** menggambarkan distribusi kesalahan.
* **Bar chart evaluasi** menyajikan perbandingan nilai MSE, MAE, dan RMSE.

---

**Kesimpulan**:
Dari hasil evaluasi yang dilakukan menggunakan metrik MSE, MAE, RMSE, dan akurasi dengan toleransi ±0.5, diperoleh gambaran umum tentang performa sistem rekomendasi dalam memprediksi rating film. Nilai-nilai metrik tersebut memberikan informasi kuantitatif mengenai sejauh mana prediksi model mendekati nilai rating sebenarnya.

Evaluasi ini menunjukkan bahwa sistem mampu menghasilkan prediksi rating berdasarkan data yang diberikan dan memberikan rekomendasi film yang sesuai dalam beberapa kasus. Visualisasi hasil seperti grafik actual vs predicted dan distribusi error juga membantu dalam memahami pola dan persebaran prediksi yang dilakukan oleh sistem.

Secara umum, proses evaluasi ini memberikan gambaran menyeluruh mengenai kinerja model yang dibangun serta menjadi dasar dalam menentukan langkah selanjutnya, baik untuk pengembangan lebih lanjut maupun penerapan sistem dalam konteks nyata.

**--- Ini adalah bagian akhir laporan ---**
