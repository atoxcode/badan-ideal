# Aplikasi Berat Badan Ideal

Disclaimer: Code ini di generate oleh generative AI. 

Aplikasi web sederhana untuk menghitung berat badan ideal berdasarkan usia, jenis kelamin, dan tinggi badan dengan sistem login personal.

## Fitur

- ✅ Sistem login personal
- ✅ Perhitungan berat badan ideal
- ✅ Evaluasi berat badan (kurus, ideal, gemuk)
- ✅ Saran kesehatan berdasarkan hasil
- ✅ Interface yang responsif dan modern
- ✅ Session management

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
    ├── index.html     # Halaman utama (setelah login)
    └── login.html     # Halaman login
```

## Rumus Berat Ideal

- **Laki-laki:** (Tinggi - 100) - (0.10 × (Tinggi - 100))
- **Perempuan:** (Tinggi - 100) - (0.15 × (Tinggi - 100))

## Keamanan

- Session-based authentication
- Login required untuk akses halaman utama
- Flash messages untuk feedback user
- Logout functionality

## Teknologi

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Authentication:** Flask Session
- **Styling:** Custom CSS dengan responsive design
# badan-ideal
