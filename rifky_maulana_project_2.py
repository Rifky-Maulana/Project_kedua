# -*- coding: utf-8 -*-
"""Rifky_Maulana_Project_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NySRNro5LEbEVXAk2z4BTn0OFad-3qbU

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

- Nama: Rifky Maulana Pasaribu
- Email: rifkymp0@gmail.com
- Id Dicoding:

#Import Library

Cell ini bertanggung jawab untuk mengimpor semua pustaka (libraries) Python yang akan digunakan di sepanjang notebook ini. Pustaka-pustaka ini menyediakan fungsionalitas esensial untuk berbagai tahapan dalam proyek, mulai dari manipulasi data, pemrosesan teks, hingga pembangunan model dan visualisasi
"""

import gdown
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import pandas as pd
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
import time
from sklearn.neighbors import NearestNeighbors

"""# Load Dataset

Cell ini bertanggung jawab untuk mengunduh dataset yang diperlukan untuk analisis dari Google Drive. Dataset ini diidentifikasi menggunakan ID uniknya, dan kemudian diunduh ke lingkungan runtime Google Colab atau lingkungan lokal sebagai file CSV dengan nama Dataset.csv.
"""

# Ganti dengan ID asli dari file kamu
dataset = '1zvE4-Y_CYMYANs1mqS6A1qawySsYODZd'

url_dataset = f'https://drive.google.com/uc?id={dataset}'

gdown.download(url_dataset, 'Dataset.csv', quiet=False)

"""# Data Understanding dan EDA

Cell ini adalah titik masuk ke dalam fase Data Understanding dan Exploratory Data Analysis (EDA). Tujuan utamanya adalah untuk memuat dataset yang telah diunduh (Dataset.csv) ke dalam struktur data yang dapat dioperasikan (Pandas DataFrame) dan selanjutnya melakukan inspeksi awal untuk memahami karakteristik dasar, struktur, dan potensi masalah pada data sebelum tahapan pra-pemrosesan lebih lanjut
"""

# menampilkan 5 data teratass
dataset= pd.read_csv('Dataset.csv')
dataset.head()

"""### Nenampilkan info data"""

dataset.info()

dataset.describe(include='all')

""" Berdasarkan grafik "10 Genre Terbanyak", dapat disimpulkan bahwa genre Drama merupakan genre yang paling sering muncul dengan jumlah yang sangat dominan dibandingkan genre lainnya. Di posisi berikutnya terdapat genre Comedy dan Horror, meskipun jumlahnya masih cukup jauh di bawah Drama. Sementara itu, genre seperti Adventure, Biography, Thriller, Romance, Fantasy, dan Crime memiliki frekuensi kemunculan yang jauh lebih rendah. Hal ini menunjukkan bahwa distribusi genre dalam dataset cenderung tidak merata, dengan hanya beberapa genre yang mendominasi dan sisanya memiliki representasi yang sangat kecil.


"""

# Genre paling sering muncul
plt.figure(figsize=(10, 5))
top_genres = dataset['genre'].value_counts().head(10)
sns.barplot(x=top_genres.index, y=top_genres.values)
plt.title("10 Genre Terbanyak")
plt.xticks(rotation=45)
plt.ylabel("Jumlah")
plt.show()

"""Berdasarkan grafik "Jumlah Film per Tahun", dapat disimpulkan bahwa produksi film mengalami peningkatan yang signifikan sejak awal tahun 2000-an, dengan puncaknya terjadi sekitar tahun 2019. Sebelumnya, jumlah film yang diproduksi per tahun cenderung rendah dan relatif stabil. Lonjakan tajam ini mencerminkan berkembangnya industri film modern, kemajuan teknologi, serta meningkatnya permintaan dan akses terhadap hiburan visual. Namun, terjadi penurunan drastis pada tahun 2020, yang kemungkinan besar disebabkan oleh dampak pandemi COVID-19 terhadap industri perfilman global."""

# Menalmpilkan jumplah film pertahun
plt.figure(figsize=(12, 6))
sns.countplot(x='year', data=dataset, order=dataset['year'].value_counts().index.sort_values())
plt.xticks(rotation=90)
plt.title('Jumlah Film per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Film')
plt.show()

"""#Data Preparation

Cell ini adalah bagian awal dari tahapan Data Preparation, berfokus pada penanganan nilai-nilai yang hilang (NaN) pada kolom teks kunci dan rekayasa fitur dengan menggabungkan beberapa kolom teks menjadi satu fitur gabungan. Langkah-langkah ini penting untuk memastikan data siap untuk pemrosesan teks lebih lanjut (misalnya, vectorization) dan model tidak mengalami error karena nilai kosong atau format data yang terpisah.

 Langkah pertama adalah mengganti nilai NaN pada kolom description dan genre dengan string kosong untuk menghindari error saat pemrosesan. Kemudian, kedua kolom tersebut digabung menjadi satu fitur teks baru bernama combined_features. Fitur gabungan ini selanjutnya diubah menjadi representasi numerik menggunakan metode TF-IDF (Term Frequency-Inverse Document Frequency), yang hanya mempertahankan 1000 fitur paling informatif dan menghilangkan kata-kata umum dalam bahasa Inggris. Setelah itu, dihitung jarak kemiripan antar film menggunakan cosine similarity, yang menghasilkan matriks kemiripan antar semua film. Akhirnya, dilakukan pemetaan indeks terhadap judul film agar sistem dapat dengan mudah mengambil data film berdasarkan judul sebagai referensi untuk rekomendasi.
"""

# Ganti NaN dengan string kosong
dataset['description'] = dataset['description'].fillna('')
dataset['genre'] = dataset['genre'].fillna('')

# Gabungkan konten untuk fitur text
dataset['combined_features'] = dataset['description'] + ' ' + dataset['genre']

# Buat TF-IDF matrix di Data Preparation
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
tfidf_matrix = tfidf.fit_transform(dataset['combined_features'])

# Hitung cosine similarity
from sklearn.metrics.pairwise import cosine_similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Buat mapping indices untuk judul film
indices = pd.Series(dataset.index, index=dataset['title']).drop_duplicates()

dataset.info()

"""# Build Model dan Algoritma

Cell ini mendefinisikan dan mengimplementasikan kelas MovieRecommender yang merupakan inti dari sistem rekomendasi berbasis konten. Kelas ini menggunakan fitur teks gabungan (combined_features) untuk membangun representasi TF-IDF dari film dan kemudian menghitung kesamaan kosinus antar film. Selanjutnya, kelas ini menyediakan metode untuk menghasilkan rekomendasi berdasarkan judul film yang diberikan. Di bagian bawah cell, kelas ini diinisialisasi, dan dilatih.

Kode ini membangun sebuah kelas bernama MovieRecommender yang berfungsi untuk merekomendasikan film berdasarkan kemiripan konten. Konstruktor __init__ menginisialisasi atribut seperti cosine_sim, df, dan indices sebagai None. Fungsi fit() digunakan untuk melatih model dengan data yang telah diproses sebelumnya, termasuk matriks TF-IDF dan matriks kemiripan cosine yang sudah dibuat. Metode get_recommendations() menerima judul film dan jumlah rekomendasi yang diinginkan. Pertama, ia mencari indeks dari film yang diberikan, lalu menghitung skor kemiripan dengan semua film lain, mengurutkannya berdasarkan skor tertinggi, dan mengambil film-film dengan skor tertinggi (kecuali film itu sendiri). Terakhir, ia mengembalikan judul, genre, dan rating pengguna dari film yang direkomendasikan. Jika judul tidak ditemukan, maka akan mengembalikan pesan error.

## Content Based filtering
"""

class MovieRecommender:
    def __init__(self):
        """
        Initialize recommender
        """
        self.cosine_sim = None
        self.indices = None
        self.df = None

    def fit(self, df):
        """
        Fit model dengan dataset yang sudah dipreprocess
        """
        self.df = df
        # Menggunakan TF-IDF matrix dan cosine similarity yang sudah dibuat di Data Preparation
        self.cosine_sim = cosine_sim
        self.indices = indices

    def get_recommendations(self, title, n_recommendations=10):
        """
        Dapatkan rekomendasi berdasarkan judul film
        """
        try:
            # Dapatkan index dari judul film
            idx = self.indices[title]

            # Dapatkan similarity scores
            sim_scores = list(enumerate(self.cosine_sim[idx]))

            # Sort berdasarkan similarity score
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Ambil top n recommendations (skip index 0 karena itu film itu sendiri)
            sim_scores = sim_scores[1:n_recommendations+1]

            # Dapatkan movie indices
            movie_indices = [i[0] for i in sim_scores]

            # Return judul, genre, dan rating film yang direkomendasikan
            return self.df.iloc[movie_indices][['title', 'genre', 'users_rating']]

        except KeyError:
            return f"Film '{title}' tidak ditemukan dalam dataset"

"""Di akhir, kelas diinstansiasi, data dilatih, dan sistem diuji dengan mengambil film pertama sebagai contoh dan menampilkan hasil rekomendasinya."""

# Inisialisasi recommender
recommender = MovieRecommender()
recommender.fit(dataset)
print("✅ Model berhasil dilatih!")

# ========================================
# Test Recommendation

# Ambil film pertama sebagai contoh
sample_movie = dataset['title'].iloc[0]
print(f"Film: {sample_movie}")
print("\nRekomendasi:")
recommendations = recommender.get_recommendations(sample_movie, 5)
print(recommendations)

"""# Evaluation Model

Cell ini mendefinisikan fungsi evaluate_model(df) yang bertujuan untuk mengevaluasi kinerja sistem rekomendasi dari perspektif "prediksi rating". Meskipun sistem rekomendasi berbasis konten biasanya tidak secara eksplisit "memprediksi" rating, pendekatan ini mencoba mengukur seberapa baik rekomendasi yang diberikan memiliki rating pengguna yang tinggi, mengindikasikan kualitas rekomendasi. Fungsi ini mengambil sampel film secara acak, mendapatkan rekomendasi untuk setiap film tersebut, dan kemudian menghitung Mean Squared Error (MSE), Mean Absolute Error (MAE), dan Root Mean Squared Error (RMSE) antara rata-rata rating dari rekomendasi dan rating asli film yang menjadi dasar rekomendasi.
"""

def evaluate_content_based(recommender, k=10):
    """
    Simple evaluation dengan Precision@K dan Recall@K
    """
    # Ambil film dengan rating tinggi sebagai ground truth
    high_rated = set(dataset[dataset['users_rating'] >= 4.0]['title'].values)

    # Sample 30 film untuk test
    sample_movies = dataset['title'].sample(30, random_state=42).values

    precision_scores = []
    recall_scores = []

    for movie_title in sample_movies:
        try:
            recs = recommender.get_recommendations(movie_title, k)

            if len(recs) == 0:
                continue

            recommended = set(recs['title'].values)
            relevant = recommended.intersection(high_rated)

            # Precision@K dan Recall@K
            precision = len(relevant) / len(recommended) if len(recommended) > 0 else 0
            recall = len(relevant) / len(high_rated) if len(high_rated) > 0 else 0

            precision_scores.append(precision)
            recall_scores.append(recall)

        except:
            continue

    return {
        f'Precision@{k}': np.mean(precision_scores) if precision_scores else 0,
        f'Recall@{k}': np.mean(recall_scores) if recall_scores else 0
    }

# Jalankan evaluasi
print("🎬 Content-Based Filtering Evaluation...")
results = evaluate_content_based(recommender, k=10)

print("📊 Hasil Evaluasi:")
print(f"Precision@10: {results['Precision@10']:.4f}")
print(f"Recall@10: {results['Recall@10']:.4f}")

"""# Test Sistem

## Deskripsi:
Cell ini memiliki dua tujuan utama:

1. Membangun Fungsi Rekomendasi Interaktif: Mendefinisikan fungsi recommend_movie yang memungkinkan pengguna mendapatkan rekomendasi film dengan mudah hanya dengan memberikan judul film dan jumlah rekomendasi yang diinginkan. Fungsi ini juga menangani kasus di mana film tidak ditemukan.

2. Menguji Fungsi Interaktif & Memberikan Ringkasan Model: Menguji fungsi recommend_movie dengan contoh konkret dan kemudian menyajikan ringkasan singkat tentang sistem rekomendasi, termasuk ukuran dataset, metode yang digunakan, dan metrik evaluasi yang telah dihitung sebelumnya.
"""

# Interactive Recommendation Function
def recommend_movie(title, n=5):
    try:
        recs = recommender.get_recommendations(title, n)
        print(f"📽️ Rekomendasi untuk '{title}':")
        for i, (_, row) in enumerate(recs.iterrows(), 1):
            print(f"{i}. {row['title']} - {row['genre']} - Rating: {row['users_rating']}")
    except:
        print("❌ Film tidak ditemukan")

# Test Interactive Function
# Contoh penggunaan
print("Contoh rekomendasi:")
recommend_movie(dataset['title'].iloc[10], 5)

# Summary
print("\n📊 RINGKASAN SISTEM REKOMENDASI")
print(f"• Dataset: {len(dataset)} film")
print(f"• Metode: Content-Based Filtering")
# Update the evaluation results to show Precision@10 and Recall@10
print(f"• Hasil Evaluasi: Precision@10={results['Precision@10']:.4f}, Recall@10={results['Recall@10']:.4f}")
print(f"• Status: ✅ Siap digunakan")