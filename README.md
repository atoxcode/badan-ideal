# Aplikasi Berat Badan Ideal

Aplikasi web sederhana untuk menghitung berat badan ideal berdasarkan usia, jenis kelamin, dan tinggi badan dengan sistem login personal, database SQLite, dan visualisasi grafik.

## Fitur

- ✅ Sistem login personal dengan database SQLite
- ✅ Registrasi user baru
- ✅ Password hashing untuk keamanan
- ✅ Perhitungan berat badan ideal
- ✅ Evaluasi berat badan (kurus, ideal, gemuk)
- ✅ Perhitungan BMI (Body Mass Index)
- ✅ Visualisasi grafik dengan Chart.js
- ✅ Halaman hasil terpisah dengan grafik interaktif
- ✅ Saran kesehatan berdasarkan hasil
- ✅ Interface yang responsif dan modern untuk mobile
- ✅ Session management
- ✅ Fitur cetak hasil
- ✅ Script manajemen database

## Cara Menjalankan

1. **Install dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Inisialisasi database (opsional - akan otomatis dibuat):**

   ```bash
   python manage_db.py init
   ```

3. **Jalankan aplikasi:**

   ```bash
   python app.py
   ```

4. **Buka browser dan akses:**
   ```
   http://localhost:5000
   ```

## Akun Demo

- **Username:** admin, **Password:** password123

## Registrasi User Baru

1. Klik "Register di sini" di halaman login
2. Isi form registrasi dengan:
   - Username (wajib)
   - Email (opsional)
   - Password (minimal 6 karakter)
   - Konfirmasi password
3. Klik "Register"
4. Login dengan akun baru

## Manajemen Database

Gunakan script `manage_db.py` untuk mengelola user:

```bash
# Inisialisasi database
python manage_db.py init

# Tambah user baru
python manage_db.py add username password email@example.com

# Lihat semua user
python manage_db.py list

# Hapus user
python manage_db.py delete username

# Ubah password user
python manage_db.py change-password username newpassword

# Bantuan
python manage_db.py help
```

## Struktur Aplikasi

```
weight_app/
├── app.py              # Main Flask application
├── manage_db.py        # Database management script
├── users.db            # SQLite database (auto-generated)
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styling
└── templates/
    ├── index.html     # Halaman input data
    ├── login.html     # Halaman login
    ├── register.html  # Halaman registrasi
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

## Keamanan

- **Password Hashing**: Password di-hash menggunakan SHA-256
- **SQL Injection Protection**: Menggunakan parameterized queries
- **Session-based authentication**
- **Login required** untuk akses halaman utama dan hasil
- **Flash messages** untuk feedback user
- **Logout functionality**
- **Input validation** pada registrasi

## Database Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Rumus Perhitungan

### Berat Ideal

- **Laki-laki:** (Tinggi - 100) - (0.10 × (Tinggi - 100))
- **Perempuan:** (Tinggi - 100) - (0.15 × (Tinggi - 100))

### BMI (Body Mass Index)

- **Rumus:** Berat (kg) / (Tinggi (m))²
- **Kategori:**
  - Kurus: < 18.5
  - Normal: 18.5 - 24.9
  - Gemuk: 25 - 29.9
  - Obesitas: ≥ 30

## Teknologi

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Grafik:** Chart.js
- **Authentication:** Flask Session + Password Hashing
- **Styling:** Custom CSS dengan responsive design

## Alur Aplikasi

1. **Register/Login** → Buat akun baru atau login dengan akun existing
2. **Input Data** → Masukkan usia, jenis kelamin, tinggi, dan berat badan
3. **Hasil dengan Grafik** → Lihat hasil evaluasi dengan visualisasi grafik
4. **Cetak/Save** → Simpan atau cetak hasil evaluasi

## Mobile Responsive

Aplikasi sudah dioptimalkan untuk mobile dengan:

- Responsive design untuk semua ukuran layar
- Touch-friendly interface
- Optimized layout untuk mobile
- Proper viewport meta tags
