#!/usr/bin/env python3
"""
Script untuk mengelola database user
"""

import sqlite3
import hashlib
import sys

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_db():
    """Inisialisasi database"""
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
    
    conn.commit()
    conn.close()
    print("Database berhasil diinisialisasi!")

def add_user(username, password, email=None):
    """Menambah user baru"""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        hashed_password = hash_password(password)
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", 
                      (username, hashed_password, email))
        
        conn.commit()
        conn.close()
        print(f"User '{username}' berhasil ditambahkan!")
        return True
    except sqlite3.IntegrityError:
        print(f"Error: Username '{username}' sudah ada!")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def list_users():
    """Menampilkan semua user"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, username, email, created_at FROM users ORDER BY id")
    users = cursor.fetchall()
    
    conn.close()
    
    if not users:
        print("Tidak ada user dalam database.")
        return
    
    print("\nDaftar User:")
    print("-" * 60)
    print(f"{'ID':<5} {'Username':<15} {'Email':<20} {'Created At'}")
    print("-" * 60)
    
    for user in users:
        print(f"{user[0]:<5} {user[1]:<15} {user[2] or 'N/A':<20} {user[3]}")

def delete_user(username):
    """Menghapus user"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"User '{username}' berhasil dihapus!")
    else:
        print(f"User '{username}' tidak ditemukan!")
    
    conn.close()

def change_password(username, new_password):
    """Mengubah password user"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    hashed_password = hash_password(new_password)
    cursor.execute("UPDATE users SET password = ? WHERE username = ?", 
                  (hashed_password, username))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"Password user '{username}' berhasil diubah!")
    else:
        print(f"User '{username}' tidak ditemukan!")
    
    conn.close()

def main():
    if len(sys.argv) < 2:
        print("""
Penggunaan: python manage_db.py [command] [options]

Commands:
  init                    - Inisialisasi database
  add <username> <password> [email] - Tambah user baru
  list                    - Tampilkan semua user
  delete <username>       - Hapus user
  change-password <username> <new_password> - Ubah password user
  help                    - Tampilkan bantuan ini

Contoh:
  python manage_db.py init
  python manage_db.py add john password123 john@example.com
  python manage_db.py list
  python manage_db.py delete john
  python manage_db.py change-password john newpassword123
        """)
        return
    
    command = sys.argv[1].lower()
    
    if command == "init":
        init_db()
    
    elif command == "add":
        if len(sys.argv) < 4:
            print("Error: Username dan password diperlukan!")
            print("Contoh: python manage_db.py add username password [email]")
            return
        
        username = sys.argv[2]
        password = sys.argv[3]
        email = sys.argv[4] if len(sys.argv) > 4 else None
        
        add_user(username, password, email)
    
    elif command == "list":
        list_users()
    
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Username diperlukan!")
            print("Contoh: python manage_db.py delete username")
            return
        
        username = sys.argv[2]
        delete_user(username)
    
    elif command == "change-password":
        if len(sys.argv) < 4:
            print("Error: Username dan password baru diperlukan!")
            print("Contoh: python manage_db.py change-password username newpassword")
            return
        
        username = sys.argv[2]
        new_password = sys.argv[3]
        change_password(username, new_password)
    
    elif command == "help":
        main()
    
    else:
        print(f"Error: Command '{command}' tidak dikenal!")
        print("Gunakan 'python manage_db.py help' untuk bantuan.")

if __name__ == "__main__":
    main() 