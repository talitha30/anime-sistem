# Anime Search Engine Dalam Mengambil Keputusan Berdasarkan Synopsis dan Popularity

### SISTEM TEMU KEMBALI INFORMASI - TALITHA SAFA NABILA - A11.2022.14809

---

## - Dataset
Dataset yang digunakan adalah dataset publik dari &#8594; [![Kaggle Badge](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/marlesson/myanimelist-dataset-animes-profiles-reviews/data)

Dataset anime memiliki 12 kolom. Pada sistem ini digunakan beberapa kolom seperti : kolom title, synopsis, popularity. dan genre

---

## - Tujuan
Sistem ini bertujuan untuk dapat membantu penonton dalam mengambil keputusan lebih tepat tentang anime yang akan jadi pilihan untuk ditonton yang sesuai dengan minat mereka sesuai dengan judul yang mereka berikan dan menghasilkan beberapa daftar judul, synopsis, dan genre.

---

## - Model dan Tahapan
* Data Collection : pada tahapan ini bertujuan untuk pengumpulan data dari sumber kaggle
* Preprocessing : pada tahapan ini bertujuan untuk merubah teks yang tidak terstruktur menjadi lebih terstruktur.
* Metode yang digunakan :
  - Untuk melakukan vektorisasi TF-IDF menggunakan SKLearn
  - Untuk menghitung similaritas (cosine similarity) berdasarkan matrix TF-IDF dari vektorisasi menggunakan SKLearn
  - Output yang diberikan 5 judul anime, synopsis, dan genre yang memiliki synopsis yang serupa dari input judul anime yang dimasukkan pengguna

 ---

 ## - Performa Uji
 Performa Uji dilakukan menggunakan K-Fold Cross-Validation yang sebelumnya penulis perlu membuat beberapa sampel rekomendasi pada judul anime tertentu untuk mendapatkan hasil dari pengujian ini. Setelah dilakukan pengujian hasil Average Hit Ratio yang didapat: 0.224.

 ---

 ## - Deployment
 Sistem Rekomendasi Anime dapat digunakan pada link &#8594; [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://macam-anime.streamlit.app/)
