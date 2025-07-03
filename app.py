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
    hasil = None
    if request.method == "POST":
        usia = int(request.form["usia"])
        jk = request.form["jk"]
        tinggi = float(request.form["tinggi"])
        berat = float(request.form["berat"])

        berat_ideal = hitung_berat_ideal(jk, tinggi)
        saran = berikan_saran(berat, berat_ideal)

        hasil = {
            "usia": usia,
            "jenis_kelamin": "Laki-laki" if jk == 'L' else "Perempuan",
            "tinggi": tinggi,
            "berat": berat,
            "berat_ideal": round(berat_ideal, 2),
            "saran": saran
        }

    return render_template("index.html", hasil=hasil, username=session.get('username'))

if __name__ == "__main__":
    app.run(debug=True)
