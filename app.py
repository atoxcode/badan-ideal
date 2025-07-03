from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key untuk session

# Database sederhana untuk user (dalam praktik nyata gunakan database yang proper)
users = {
    "admin": "password123",
    "user1": "password123",
    "user2": "password123"
}

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

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login berhasil! Selamat datang, ' + username, 'success')
            return redirect(url_for('index'))
        else:
            flash('Username atau password salah!', 'error')
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
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
