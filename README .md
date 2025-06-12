# 🤖 Diablyze – Early Detection of Diabetes with Artificial Neural Network (ANN)

**Diablyze** adalah proyek capstone machine learning yang bertujuan untuk membangun sistem deteksi dini penyakit **diabetes** menggunakan **Artificial Neural Network (ANN)**. Model ini dilatih dengan data medis yang relevan untuk memprediksi kemungkinan seseorang terkena diabetes, sebagai upaya preventif dalam bidang kesehatan.

---

## 📂 Struktur Proyek

- **Capstone Diabetes.ipynb** → Notebook utama yang berisi preprocessing data, training model ANN, evaluasi metrik, serta visualisasi hasil.
- **model_diabetes.h5** → Model ANN hasil training dalam format HDF5.
- **app.py** → REST API berbasis Flask untuk melayani prediksi.
- **ROC_curve.png**, **confusion_matrix.png** → Visualisasi evaluasi model.
- **diabetes_prediction_data.csv** → Dataset yang digunakan dalam pelatihan dan pengujian model.

---

## 🚀 Setup Environment

Untuk menjalankan proyek ini, kamu bisa memilih salah satu dari dua cara berikut:

### 🧪 Menggunakan Anaconda
```bash
conda create --name .env python=3.9  
conda activate .env  
pip install scikit-learn tensorflow tensorflow-lite tensorflowjs matplotlib keras numpy flask
```

### 🐍 Menggunakan Pipenv
```bash
pipenv install  
pipenv install scikit-learn tensorflow tensorflow-lite tensorflowjs matplotlib keras numpy flask  
pipenv shell
```

---

## 🎯 Tujuan Proyek

1. Mengembangkan model klasifikasi berbasis ANN untuk prediksi awal diabetes.
2. Menganalisis performa model dengan metrik seperti akurasi, precision, recall, F1-score, dan ROC AUC.
3. Membangun antarmuka API menggunakan Flask untuk mendistribusikan model prediktif.
4. Memberikan insight yang dapat membantu tenaga medis atau sistem kesehatan dalam deteksi dini.

---

## 📈 Evaluasi Model

Model ANN menunjukkan performa sangat baik:

- **Akurasi:** 92.91%
- **Precision:** 59.80%
- **Recall:** 89.98%
- **F1 Score:** 71.85%
- **ROC AUC:** 98.03%

Visualisasi evaluasi seperti *confusion matrix* dan *ROC curve* tersedia dalam folder gambar.

---

## 🌐 API Prediksi

Endpoint prediksi tersedia dalam `app.py`:

- **GET /** → Cek status API
- **POST /predict** → Kirim data numerik JSON untuk mendapatkan hasil prediksi

Contoh input JSON:
```json
{
  "input": [45, 25.3, 6.8, 140, 1, 0]
}
```

Untuk mengujinya, bisa gunakan perintah `curl`:
```bash
curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"input": [45, 25.3, 6.8, 140, 1, 0]}'
```

---

## 📌 Catatan Tambahan

- Model ini belum diuji secara klinis, hanya ditujukan sebagai studi kasus edukatif.
- Untuk produksi, disarankan menambahkan validasi input, sistem autentikasi, dan deployment ke cloud.
---
