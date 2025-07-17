from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn

# Initialize database (run this once)
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS designers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image_url TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        logo_url TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clothing (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        image_url TEXT
    )''')
    
    conn.commit()
    conn.close()

# Homepage route - Enhanced version
@app.route('/')
def home():
    conn = get_db_connection()
    
    # Get 3 random featured items from each category
    designers = conn.execute(
        'SELECT id, name, image_url FROM designers ORDER BY RANDOM() LIMIT 3'
    ).fetchall()
    
    brands = conn.execute(
        'SELECT id, name, logo_url FROM brands ORDER BY RANDOM() LIMIT 3'
    ).fetchall()
    
    items = conn.execute(
        'SELECT id, name, image_url, price FROM clothing ORDER BY RANDOM() LIMIT 3'
    ).fetchall()
    
    conn.close()
    
    return render_template('home.html',
                         designers=designers,
                         brands=brands,
                         items=items)

if __name__ == '__main__':
    init_db()  # Initialize database tables (only needed once)
    app.run(debug=True)