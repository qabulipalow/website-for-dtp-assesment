from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

#database connection helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # find columns by name
    return conn

#homepage route
@app.route('/')
def home():
    conn = get_db_connection()
    # Select the correct url column from the database
    designers = conn.execute('SELECT designer_id, name, designer_url FROM designer ORDER BY RANDOM() LIMIT 3').fetchall()
    brands = conn.execute('SELECT brand_id, name, brand_url FROM brand ORDER BY RANDOM() LIMIT 3').fetchall()
    items = conn.execute('SELECT item_id, name, price, item_url FROM item ORDER BY RANDOM() LIMIT 3').fetchall()
    
    conn.close()
    
    return render_template('home.html',
                         designers=designers,
                         brands=brands,
                         items=items)

# Designers route
@app.route('/designers')
def all_designer():
    conn = get_db_connection()
    designers = conn.execute('SELECT name, birth_year, country, bio, designer_url FROM designer ORDER BY name').fetchall()
    conn.close()
    return render_template('designers.html', designers=designers)

# Brands route
@app.route('/brands')
def all_brand():
    conn = get_db_connection()
    brands = conn.execute('SELECT name, year_founded, country, price_range, category, description, brand_url FROM brand ORDER BY name').fetchall()
    conn.close()
    return render_template('brands.html', brands=brands)

# Items route
@app.route('/items')
def all_items():
    conn = get_db_connection()
    items = conn.execute('SELECT name, price, category, description, item_url FROM item ORDER BY name').fetchall()
    conn.close()
    return render_template('items.html', items=items)

@app.route('/thehistory')
def thehistory():
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)