from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
import sqlite3
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key untuk session

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert default admin user if not exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        hashed_password = hashlib.sha256('password123'.encode()).hexdigest()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                      ('admin', hashed_password, 'admin@example.com'))
    
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed):
    return hash_password(password) == hashed

def get_user_by_username(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def create_user(username, password, email=None):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                      (username, hashed_password, email))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Initialize database
init_db()

# Decorator untuk mengecek login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def hitung_berat_ideal(jk, tinggi):
    if jk == 'L':
        return (tinggi - 100) - (0.10 * (tinggi - 100))
    elif jk == 'P':
        return (tinggi - 100) - (0.15 * (tinggi - 100))
    return None

def berikan_saran(berat_sekarang, berat_ideal):
    selisih = berat_sekarang - berat_ideal
    if abs(selisih) < 2:
        return "Berat badan Anda ideal. Pertahankan pola hidup sehat!"
    elif selisih > 2:
        return "Anda kelebihan berat badan. Disarankan untuk mengurangi berat badan."
    else:
        return "Anda kekurangan berat badan. Disarankan untuk menambah berat badan."

def tentukan_kategori_bmi(berat, tinggi):
    # Konversi tinggi dari cm ke meter
    tinggi_m = tinggi / 100
    bmi = berat / (tinggi_m ** 2)
    
    if bmi < 18.5:
        return "Kurus", bmi, "rgba(255, 206, 86, 0.8)", "rgba(255, 206, 86, 1)"
    elif 18.5 <= bmi < 25:
        return "Normal", bmi, "rgba(75, 192, 192, 0.8)", "rgba(75, 192, 192, 1)"
    elif 25 <= bmi < 30:
        return "Gemuk", bmi, "rgba(255, 159, 64, 0.8)", "rgba(255, 159, 64, 1)"
    else:
        return "Obesitas", bmi, "rgba(255, 99, 132, 0.8)", "rgba(255, 99, 132, 1)"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        email = request.form.get("email", "")
        
        # Validasi input
        if not username or not password:
            flash('Username dan password harus diisi!', 'error')
            return render_template("register.html")
        
        if password != confirm_password:
            flash('Password tidak cocok!', 'error')
            return render_template("register.html")
        
        if len(password) < 6:
            flash('Password minimal 6 karakter!', 'error')
            return render_template("register.html")
        
        # Cek apakah username sudah ada
        if get_user_by_username(username):
            flash('Username sudah digunakan!', 'error')
            return render_template("register.html")
        
        # Buat user baru
        if create_user(username, password, email):
            flash('Registrasi berhasil! Silakan login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Terjadi kesalahan saat registrasi!', 'error')
    
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        user = get_user_by_username(username)
        
        if user and verify_password(password, user[2]):  # user[2] adalah password
            session['username'] = username
            session['user_id'] = user[0]
            flash('Login berhasil! Selamat datang, ' + username, 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah!', 'error')
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('user_id', None)
    flash('Anda telah logout.', 'info')
    return redirect(url_for('login'))

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        usia = int(request.form["usia"])
        jk = request.form["jk"]
        tinggi = float(request.form["tinggi"])
        berat = float(request.form["berat"])

        berat_ideal = hitung_berat_ideal(jk, tinggi)
        saran = berikan_saran(berat, berat_ideal)
        kategori_bmi, nilai_bmi, bmi_color, bmi_border_color = tentukan_kategori_bmi(berat, tinggi)

        hasil = {
            "usia": usia,
            "jenis_kelamin": "Laki-laki" if jk == 'L' else "Perempuan",
            "tinggi": tinggi,
            "berat": berat,
            "berat_ideal": round(berat_ideal, 2),
            "saran": saran,
            "kategori_bmi": kategori_bmi,
            "nilai_bmi": round(nilai_bmi, 2),
            "bmi_color": bmi_color,
            "bmi_border_color": bmi_border_color
        }
        
        # Simpan hasil ke session untuk digunakan di halaman hasil
        session['hasil'] = hasil
        return redirect(url_for('hasil'))

    return render_template("index.html", username=session.get('username'))

@app.route("/hasil")
@login_required
def hasil():
    hasil = session.get('hasil')
    if not hasil:
        flash('Tidak ada data hasil. Silakan cek berat badan ideal terlebih dahulu.', 'error')
        return redirect(url_for('index'))
    
    return render_template("hasil.html", hasil=hasil, username=session.get('username'))

if __name__ == "__main__":
    app.run(debug=True)
