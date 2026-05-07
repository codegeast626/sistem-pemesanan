from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Fungsi koneksi database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # agar bisa akses pakai nama kolom
    return conn

# Route halaman utama (tampil data)
@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM pemesanan").fetchall()
    conn.close()
    return render_template('index.html', data=data)

# Route tambah data (form + proses)
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        pesanan = request.form['pesanan']

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO pemesanan (nama, pesanan) VALUES (?, ?)",
            (nama, pesanan)
        )
        conn.commit()
        conn.close()

        return redirect('/')
    
    return render_template('tambah.html')

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)