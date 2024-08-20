from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM entries').fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = get_db_connection()
        conn.execute('INSERT INTO entries (name, value, date) VALUES (?, ?, ?)',
                     (name, value, date))
        conn.commit()
        conn.close()
        return redirect('/')

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
