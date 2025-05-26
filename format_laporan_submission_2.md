# Laporan Proyek Machine Learning - Rifky Maulana Pasaribu

## Project Overview

Dalam era digital saat ini, sistem rekomendasi telah menjadi komponen penting dalam berbagai layanan berbasis data, seperti e-commerce, platform streaming, dan media sosial. Salah satu implementasi yang paling umum dan berdampak luas adalah sistem rekomendasi film yang dapat mempersonalisasi pengalaman pengguna berdasarkan preferensi mereka. Sistem ini membantu pengguna menemukan film yang relevan, menghemat waktu pencarian, dan meningkatkan kepuasan pengguna terhadap platform.

Proyek ini bertujuan untuk membangun \*\*sistem rekomendasi film berbasis \*\****user-based collaborative filtering***. Pendekatan ini bekerja dengan cara mencari kemiripan antar pengguna berdasarkan histori penilaian film, kemudian merekomendasikan film yang disukai oleh pengguna lain yang memiliki selera serupa. Teknik ini tidak bergantung pada atribut konten film, melainkan sepenuhnya berdasarkan interaksi pengguna.

Dataset yang digunakan dalam proyek ini diperoleh dari Kaggle dengan judul [Movie Recommendation Dataset by dev0914sharma](https://www.kaggle.com/datasets/dev0914sharma/dataset), yang berisi informasi seperti ID pengguna, ID film, dan rating yang diberikan pengguna terhadap film tertentu. Dataset ini menyediakan data dasar yang dibutuhkan untuk membangun model collaborative filtering.

### Alasan dan Relevansi Permasalahan

Permasalahan utama yang diangkat adalah bagaimana memberikan rekomendasi yang relevan kepada pengguna dalam jumlah data yang besar dan bersifat subjektif. Pendekatan user-based filtering dipilih karena kesederhanaannya dan kemampuannya dalam menangkap pola preferensi pengguna berdasarkan komunitas pengguna lain.

Beberapa alasan mengapa masalah ini penting untuk diselesaikan:

* **Volume data yang besar**: Platform streaming memiliki ribuan film, membuat pencarian secara manual menjadi tidak efisien.
* **Pengalaman pengguna**: Rekomendasi yang relevan dapat meningkatkan kepuasan dan loyalitas pengguna.
* **Nilai bisnis**: Sistem rekomendasi yang efektif dapat meningkatkan waktu tayang pengguna dan konversi.

### Studi Literatur dan Referensi

Penelitian oleh Sarwar et al. (2001) menunjukkan bahwa collaborative filtering, khususnya pendekatan user-based, efektif dalam menghasilkan rekomendasi yang akurat dengan asumsi cukupnya jumlah pengguna dan rating yang tersedia \[1]. Selain itu, Ricci et al. (2011) dalam buku *Recommender Systems Handbook* menekankan pentingnya memilih algoritma yang sesuai dengan karakteristik data dan tujuan sistem \[2].

### Referensi

\[1] B. M. Sarwar, G. Karypis, J. A. Konstan, dan J. Riedl, “Item-based collaborative filtering recommendation algorithms,” in *Proceedings of the 10th international conference on World Wide Web*, 2001, pp. 285–295.

\[2] F. Ricci, L. Rokach, B. Shapira, dan P. B. Kantor, *Recommender Systems Handbook*. Springer, 2011.

## Business Understanding

### Problem Statements

1. Bagaimana cara merekomendasikan film yang relevan kepada pengguna berdasarkan preferensi pengguna lain yang memiliki pola penilaian serupa?
2. Bagaimana mengatasi keterbatasan data (sparse rating) yang umum terjadi dalam sistem rekomendasi berbasis pengguna?
3. Bagaimana memastikan sistem dapat memberikan rekomendasi yang cepat dan tetap akurat saat jumlah pengguna dan item meningkat?

### Goals

1. Membangun model user-based collaborative filtering untuk merekomendasikan film kepada pengguna.
2. Mengimplementasikan teknik pengolahan data yang dapat mengurangi dampak data sparsity.
3. Mengukur performa model rekomendasi dalam hal akurasi dan efisiensi.

### Solution Statements

Untuk mencapai goals di atas, pendekatan solusi yang digunakan antara lain:

* **User-Based Collaborative Filtering**: Mencari pengguna yang memiliki pola rating mirip, kemudian merekomendasikan item yang disukai oleh pengguna-pengguna tersebut.
* **Matrix Factorization (sebagai alternatif)**: Jika diperlukan, pendekatan seperti Singular Value Decomposition (SVD) dapat digunakan untuk mengatasi masalah sparsity dan meningkatkan efisiensi sistem.
* **Similarity Metrics**: Menggunakan cosine similarity atau Pearson correlation coefficient untuk mengukur kedekatan antar pengguna.
* **Top-N Recommendation**: Menyusun daftar film yang paling relevan berdasarkan skor prediksi tertinggi untuk setiap pengguna.

Pendekatan-pendekatan ini akan dibandingkan dan dianalisis berdasarkan keefektifan dan kemampuannya dalam menjawab pernyataan masal.

## Data Understanding

Dataset yang digunakan dalam proyek ini bersumber dari Kaggle, yaitu [Movie Recommendation Dataset by dev0914sharma](https://www.kaggle.com/datasets/dev0914sharma/dataset). Dataset ini terdiri dari dua file utama: `movies.csv` yang berisi informasi detail mengenai film, dan `ratings.csv` yang mencatat penilaian yang diberikan oleh pengguna terhadap film-film tersebut. Dataset ini mencakup **100.000 rating** dari **943 pengguna** untuk **1682 film**.

### Variabel pada Dataset

Berikut adalah penjelasan mengenai variabel-variabel yang terdapat dalam dataset:

**1. `ratings.csv`:**

* **`user_id`**: ID unik untuk setiap pengguna.
* **`item_id`**: ID unik untuk setiap film (merujuk pada ID film di `movies.csv`).
* **`rating`**: Penilaian (rating) yang diberikan oleh pengguna terhadap film, dengan skala 1 hingga 5.
* **`timestamp`**: Waktu saat rating diberikan (dalam format Unix timestamp).

**2. `movies.csv`:**

* **`item_id`**: ID unik untuk setiap film.
* **`title`**: Judul film beserta tahun rilisnya.
* **`release date`**: Tanggal rilis film.
* **`video release date`**: Tanggal rilis video (seringkali kosong).
* **`IMDb URL`**: Tautan ke halaman IMDb film tersebut.
* **Genre Columns (19 kolom)**: Kolom-kolom biner (`unknown`, `Action`, `Adventure`, `Animation`, `Children's`, `Comedy`, `Crime`, `Documentary`, `Drama`, `Fantasy`, `Film-Noir`, `Horror`, `Musical`, `Mystery`, `Romance`, `Sci-Fi`, `Thriller`, `War`, `Western`) yang menunjukkan genre dari film tersebut. Sebuah film bisa memiliki lebih dari satu genre.

### Exploratory Data Analysis (EDA)

Untuk mendapatkan pemahaman awal mengenai data, beberapa visualisasi telah dilakukan, seperti yang terlihat pada gambar di bawah:

![26dafe76-4d9d-476d-a490-039bf10acc3f](https://github.com/user-attachments/assets/4257760b-65c4-4a61-a653-690e83d0a4c1)


* **Distribusi Rating**: Seperti yang terlihat pada grafik batang pertama, distribusi rating menunjukkan bahwa pengguna cenderung memberikan rating yang tinggi. Rating **4** adalah yang paling banyak diberikan, diikuti oleh rating **3** dan **5**. Rating **1** dan **2** jauh lebih sedikit, mengindikasikan bahwa sebagian besar interaksi adalah positif atau netral.
* **Film Paling Banyak Dinilai**: Grafik batang horizontal kedua menunjukkan 10 film yang paling sering mendapatkan rating dari pengguna. **Star Wars (1977)** menempati posisi teratas dengan jumlah rating terbanyak, diikuti oleh **Contact (1997)** dan **Fargo (1996)**. Ini menunjukkan film-film mana yang paling populer atau paling banyak ditonton dalam dataset ini.

Dari pemahaman data awal ini, terlihat bahwa meskipun ada banyak rating, matriks interaksi pengguna-film kemungkinan besar akan bersifat *sparse* (jarang), karena tidak setiap pengguna menilai setiap film. Ini adalah tantangan umum dalam *collaborative filtering* yang perlu ditangani dalam tahap pemodelan.
## Data Preparation

Tahapan data preparation sangat penting untuk memastikan data siap digunakan untuk pemodelan dan dapat menghasilkan model yang andal. Pada proyek ini, beberapa langkah persiapan data dilakukan:

### 1. Menggabungkan Data (Merging DataFrames)

Langkah pertama adalah menggabungkan informasi rating pengguna dengan informasi detail film. Ini dilakukan dengan menggabungkan DataFrame `ratings` (yang berisi `user_id`, `item_id`, `rating`) dengan DataFrame `movies` (yang berisi `item_id`, `title`, dan genre) berdasarkan kolom kunci `item_id`.

![image](https://github.com/user-attachments/assets/df3bb472-ca44-4f49-96e1-a1c129e008a2)

Alasan: Penggabungan ini diperlukan agar kita memiliki DataFrame tunggal yang berisi informasi lengkap untuk setiap rating. Dengan adanya judul film (title) langsung dalam data rating, proses analisis dan nantinya penyajian rekomendasi menjadi lebih mudah dipahami daripada hanya menggunakan item_id.

### 2. Membagi Data (Splitting Data)
Setelah data digabungkan, langkah selanjutnya adalah membagi dataset menjadi dua bagian: data latih (training set) dan data uji (test set). Kami menggunakan pembagian 80% untuk data latih dan 20% untuk data uji. Penggunaan random_state memastikan bahwa pembagian data ini bersifat konsisten dan dapat direproduksi.

![image](https://github.com/user-attachments/assets/b07ab318-4ffb-4303-b99a-e6add60945c1)

Alasan: Pembagian data ini krusial dalam machine learning.

Data Latih (Train Set) digunakan untuk "mengajarkan" model bagaimana pola preferensi pengguna berdasarkan rating yang ada.
Data Uji (Test Set) digunakan untuk menguji seberapa baik model yang telah dilatih dapat membuat prediksi (atau rekomendasi) pada data yang belum pernah dilihat sebelumnya. Ini memberikan ukuran kinerja yang objektif dan membantu mendeteksi overfitting.

## Modeling

Pada tahap ini, penulis membangun model sistem rekomendasi menggunakan pendekatan **User-Based Collaborative Filtering (UBCF)**. Pendekatan ini dipilih karena kemampuannya untuk menemukan pola preferensi pengguna berdasarkan kesamaan perilaku dengan pengguna lain, tanpa memerlukan informasi detail tentang konten film itu sendiri.

---

### 1. Persiapan Matriks User-Movie

Sebelum membangun model, penulis melakukan beberapa langkah persiapan tambahan pada data latih:

* **Filter User & Movie Aktif**: Untuk mengurangi *sparsity* (ketersebaran data) dan fokus pada interaksi yang lebih signifikan, kami memfilter data untuk hanya menyertakan pengguna yang telah memberikan minimal 10 rating dan film yang telah menerima minimal 10 rating. Ini membantu memastikan bahwa perhitungan kemiripan didasarkan pada pengguna dan item dengan data yang cukup.

![image](https://github.com/user-attachments/assets/92304dd3-cb3b-4d97-916d-6f1d481ef5ba)


* **Pembuatan Matriks User-Movie**: Data latih yang telah difilter kemudian diubah menjadi sebuah matriks menggunakan `pivot_table`. Matriks ini memiliki `user_id` sebagai *index* (baris), `title` sebagai *kolom*, dan `rating` sebagai *nilai*. Nilai `NaN` (Not a Number) akan muncul di sel di mana seorang pengguna belum memberikan rating untuk sebuah film. Matriks ini adalah representasi inti yang akan digunakan untuk menghitung kemiripan antar pengguna.


![image](https://github.com/user-attachments/assets/97e02033-fb2b-4f33-9a71-a55b76f99a95)

---

### 2. Algoritma User-Based Collaborative Filtering

Inti dari model ini adalah fungsi rekomendasi yang mengimplementasikan UBCF. Prosesnya adalah sebagai berikut:

1.  **Penanganan *Cold-Start***: Sistem memeriksa apakah pengguna yang meminta rekomendasi ada dalam matriks. Jika tidak (pengguna baru atau tidak aktif), sistem tidak dapat memberikan rekomendasi dan akan mengembalikan hasil kosong.
2.  **Perhitungan Kemiripan (Similarity)**:
    * Sistem mengambil data rating milik pengguna target.
    * Kemudian, dihitung **Korelasi Pearson** antara rating pengguna target dengan *semua* pengguna lain dalam matriks. Korelasi Pearson dipilih karena mengukur kemiripan linear dan dapat menangani perbedaan skala rating antar pengguna.
    * Hasilnya adalah skor kemiripan untuk setiap pengguna lain terhadap pengguna target.
3.  **Normalisasi & Perhitungan Skor Awal**: Skor kemiripan dinormalisasi (disesuaikan berdasarkan rata-rata rating pengguna) dan digunakan untuk menghitung skor rekomendasi awal untuk setiap film. Film yang dirating tinggi oleh pengguna yang *mirip* akan mendapatkan skor tinggi.
4.  **Penambahan Bobot Popularitas**: Skor ditingkatkan dengan memperhitungkan jumlah rating (`rating_count`) yang dimiliki setiap film. Ini dilakukan untuk memberikan bobot lebih pada film yang populer dan banyak dinilai.
5.  **Filter Film yang Sudah Ditonton**: Film yang sudah pernah ditonton oleh pengguna target dihapus dari daftar calon rekomendasi.
6.  **Filter Rating Minimum**: Film dengan jumlah rating sangat sedikit (kurang dari 2) juga dihapus untuk menjaga kualitas rekomendasi.
7.  **Skor Akhir Berbobot**: Skor akhir dihitung dengan menggabungkan skor kemiripan dengan logaritma dari jumlah rating. Penggunaan logaritma membantu menyeimbangkan pengaruh film yang sangat populer agar tidak mendominasi sepenuhnya.
8.  **Pengurutan & Top-N Output**: Rekomendasi diurutkan berdasarkan skor akhir tertinggi, dan **N** film teratas (biasanya 10) dikembalikan sebagai hasil rekomendasi (Top-N Recommendation).


![image](https://github.com/user-attachments/assets/3ba14bce-d556-4129-b5f3-9d3a106ce7ed)

---

### 3. Kelebihan dan Kekurangan UBCF

**Kelebihan:**

* **Tidak Memerlukan Konten**: Tidak butuh analisis fitur item (genre, aktor, dll.), hanya mengandalkan interaksi pengguna.
* **Serendipity**: Mampu merekomendasikan item yang *cross-genre* atau tidak terduga, selama pengguna yang mirip menyukainya.
* **Interpretasi**: Relatif mudah dijelaskan ("Direkomendasikan karena orang yang seleranya mirip dengan Anda menyukainya").

**Kekurangan:**

* **Sparsity Data**: Kinerja menurun drastis jika matriks user-item sangat jarang. Langkah filtering kami mencoba mengurangi ini, tetapi tetap menjadi tantangan.
* **Skalabilitas**: Perhitungan kemiripan menjadi sangat mahal secara komputasi saat jumlah pengguna dan item meningkat.
* ***Cold Start***: Sulit memberikan rekomendasi untuk pengguna baru atau item baru.
* **Popularity Bias**: Cenderung merekomendasikan item populer, yang bisa mengurangi *novelty* atau penemuan film baru bagi pengguna.

## Evaluation
## Evaluasi

Untuk mengukur performa model User-Based Collaborative Filtering yang telah dibangun, kami menggunakan metrik evaluasi yang umum digunakan dalam sistem rekomendasi, yaitu Precision@k, Recall@k, dan F1-Score@k. Metrik-metrik ini membantu kita memahami seberapa relevan dan komprehensif rekomendasi yang diberikan oleh sistem.

---

### 1. Metrik Evaluasi

Dalam konteks sistem rekomendasi, kita ingin tahu:
* Dari film yang direkomendasikan, berapa banyak yang benar-benar disukai pengguna? (Precision)
* Dari semua film yang disukai pengguna, berapa banyak yang berhasil kita rekomendasikan? (Recall)

Untuk evaluasi ini, kami menetapkan **k = 20**, artinya mengevaluasi **20 rekomendasi teratas** yang diberikan untuk setiap pengguna. Penulis juga mendefinisikan film yang "relevan" atau "disukai" sebagai film yang diberi rating **minimal 3.5** oleh pengguna di dalam set pengujian.

* **Precision@k**:
    Mengukur proporsi item yang direkomendasikan dalam daftar Top-k yang benar-benar relevan bagi pengguna.
    Precision@k menunjukkan seberapa "tepat" rekomendasi kita. Nilai tinggi berarti sebagian besar dari 20 film yang direkomendasikan memang disukai pengguna.

* **Recall@k**:
    Mengukur proporsi item relevan yang berhasil ditemukan dan masuk ke dalam daftar rekomendasi Top-k.
    Recall@k menunjukkan seberapa "lengkap" rekomendasi kita dalam menemukan semua film yang mungkin disukai pengguna.

* **F1-Score@k**:
    Merupakan rata-rata harmonik dari Precision@k dan Recall@k. Metrik ini memberikan gambaran tunggal yang menyeimbangkan antara ketepatan dan kelengkapan.
    F1-Score berguna ketika kita ingin memastikan bahwa model tidak hanya akurat tetapi juga mampu mencakup sebagian besar item yang relevan.

---

### 2. Proses Evaluasi

Evaluasi dilakukan dengan mengikuti langkah-langkah berikut, seperti yang diimplementasikan dalam kode:

1.  **Sampling**: Untuk efisiensi, kami mengambil sampel acak **100 pengguna** dari *test set*.
2.  **Identifikasi Item Relevan**: Untuk setiap pengguna dalam sampel, mengidentifikasi daftar film yang mereka sukai (rating >= 3.5) di *test set*. Ini menjadi *ground truth*.
3.  **Generasi Rekomendasi**: Untuk setiap pengguna, memanggil fungsi `recommend_movies_for_user` untuk mendapatkan 20 (k=20) rekomendasi teratas.
4.  **Perhitungan Metrik**: membandingkan daftar rekomendasi dengan daftar film relevan untuk menghitung jumlah *True Positives* (film yang direkomendasikan DAN relevan). Berdasarkan ini, kami menghitung Precision@20, Recall@20, dan F1-Score@20 untuk setiap pengguna.
5.  **Rata-Rata Metrik**: Nilai Precision, Recall, dan F1 dari semua pengguna sampel kemudian dirata-ratakan untuk mendapatkan gambaran kinerja sistem secara keseluruhan.

---

### 3. Hasil Evaluasi

Proses evaluasi pada 100 pengguna sampel menghasilkan metrik sebagai berikut:

* **Precision@20 : 0.0281**
* **Recall@20 : 0.0270**
* **F1-Score@20 : 0.0245**

Meskipun angka-angka ini terlihat rendah, hal ini cukup umum terjadi pada sistem rekomendasi, terutama dengan pendekatan *collaborative filtering* pada dataset yang *sparse* dan evaluasi Top-N yang ketat. Beberapa faktor penyebabnya:
1.  **Sparsity Data**: Tidak semua film yang *mungkin* disukai pengguna ada di *test set*. Evaluasi hanya bisa membandingkan dengan *rating yang ada*.
2.  **Katalog Besar**: Dengan 1682 film, merekomendasikan 20 film yang tepat adalah tugas yang sulit.
3.  ***Cold Start* & Pengguna Tidak Aktif**: Pengguna dengan sedikit rating menyulitkan perhitungan kemiripan yang akurat.
4.  **Kesederhanaan Model**: UBCF dasar memiliki keterbatasan dibandingkan algoritma yang lebih kompleks (misalnya, Matrix Factorization).

Hasil ini memberikan **baseline** untuk kinerja sistem. Meskipun ada ruang besar untuk peningkatan (misalnya, dengan *tuning*, algoritma berbeda, atau data tambahan), model ini telah berhasil mengimplementasikan logika dasar sistem rekomendasi berbasis pengguna.
**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
