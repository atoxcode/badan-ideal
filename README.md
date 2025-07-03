# Aplikasi Berat Badan Ideal

Disclaimer: Code ini di generate oleh generative AI.

Aplikasi web sederhana untuk menghitung berat badan ideal berdasarkan usia, jenis kelamin, dan tinggi badan dengan sistem login personal dan visualisasi grafik.

## Fitur

- ✅ Sistem login personal
- ✅ Perhitungan berat badan ideal
- ✅ Evaluasi berat badan (kurus, ideal, gemuk)
- ✅ Perhitungan BMI (Body Mass Index)
- ✅ Visualisasi grafik dengan Chart.js
- ✅ Halaman hasil terpisah dengan grafik interaktif
- ✅ Saran kesehatan berdasarkan hasil
- ✅ Interface yang responsif dan modern
- ✅ Session management
- ✅ Fitur cetak hasil

## Cara Menjalankan

1. **Install dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan aplikasi:**

   ```bash
   python app.py
   ```

3. **Buka browser dan akses:**
   ```
   http://localhost:5000
   ```

## Akun Demo

- **Username:** admin, **Password:** password123
- **Username:** user1, **Password:** password123
- **Username:** user2, **Password:** password123

## Struktur Aplikasi

```
weight_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styling
└── templates/
    ├── index.html     # Halaman input data
    ├── login.html     # Halaman login
    └── hasil.html     # Halaman hasil dengan grafik
```

## Fitur Grafik

### 1. Grafik Perbandingan Berat Badan

- Bar chart yang membandingkan berat badan saat ini vs berat ideal
- Visualisasi yang jelas untuk melihat perbedaan

### 2. Grafik BMI (Body Mass Index)

- Doughnut chart yang menampilkan nilai BMI
- Warna berbeda berdasarkan kategori BMI:
  - Kuning: Kurus (< 18.5)
  - Hijau: Normal (18.5 - 24.9)
  - Orange: Gemuk (25 - 29.9)
  - Merah: Obesitas (≥ 30)

## Rumus Berat Ideal

- **Laki-laki:** (Tinggi - 100) - (0.10 × (Tinggi - 100))
- **Perempuan:** (Tinggi - 100) - (0.15 × (Tinggi - 100))

## Keamanan

- Session-based authentication
- Login required untuk akses halaman utama dan hasil
- Flash messages untuk feedback user
- Logout functionality

## Teknologi

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Grafik:** Chart.js
- **Authentication:** Flask Session
- **Styling:** Custom CSS dengan responsive design

## Alur Aplikasi

1. **Login** → Masuk dengan akun demo
2. **Input Data** → Masukkan usia, jenis kelamin, tinggi, dan berat badan
3. **Hasil dengan Grafik** → Lihat hasil evaluasi dengan visualisasi grafik
4. **Cetak/Save** → Simpan atau cetak hasil evaluasi
