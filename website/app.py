from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Find columns by name
    return conn

# Homepage route
@app.route('/')
def home():
    conn = get_db_connection()
    
    # Get 3 random featured items from each category
    designers = conn.execute(
        'SELECT designer_id, name FROM designer ORDER BY RANDOM() LIMIT 3'  # Removed trailing comma
    ).fetchall()
    
    brands = conn.execute(
        'SELECT brand_id, name FROM brand ORDER BY RANDOM() LIMIT 3'  # Removed trailing comma
    ).fetchall()
    
    items = conn.execute(
        'SELECT item_id, name, price FROM item ORDER BY RANDOM() LIMIT 3'  # Removed trailing comma
    ).fetchall()
    
    conn.close()
    
    return render_template('home.html',
                         designers=designers,
                         brands=brands,
                         items=items)

@app.route('/designers')
def all_designer():
    conn = get_db_connection()
    designers = conn.execute('SELECT * FROM designer ORDER BY name').fetchall()
    conn.close()
    return render_template('designers.html', designers=designers)

@app.route('/thehistory')
def thehistory():
    return render_template('history.html')

@app.route('/brands')
def all_brand():
    conn = get_db_connection()
    brands = conn.execute('SELECT * FROM brand ORDER BY name').fetchall()
    conn.close()
    return render_template('brands.html', brands=brands)

@app.route('/items')
def all_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM item ORDER BY name').fetchall()
    conn.close()
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)