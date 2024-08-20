import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries
                 (id INTEGER PRIMARY KEY, 
                  name TEXT, 
                  value REAL, 
                  date TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
