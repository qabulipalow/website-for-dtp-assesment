from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Find columns by name
    return conn

# Designer image mapping
def get_designer_image_map():
    return {
        'Raf Simons': 'rafsimons.jpg',
        'Maison Martin Margiela': 'martin.jpg',
        'Yohji Yamamoto': 'yy.jpg',
        'Carol Christian Poell': 'carol.jpg',
        'Virgil Abloh': 'virgil.jpg',   
        'Cristóbal Balenciaga': 'cristobal.jpg',
        'James Jebbia': 'james.jpg',
        'Jerry Lorenzo': 'jerry.jpg',
        'Jun Takashi': 'juntakashi.jpg',
        'Louis Vuitton': 'louis.jpg',
        'Martine Rose': 'martine.jpg',
        'Maison Margiela': 'martin.jpg',
        'Nigo': 'nigo.jpg',
        'Richard Stark': 'richard.jpg',
        'Shayne Oliver': 'shayne.jpg'
    }

# Brand image mapping
def get_brand_image_map():
    return {
        'Balenciaga': 'balenciaga.png',
        'A Bathing Ape': 'bape.png',
        'Carol Christian Poell': 'ccp.jpg',
        'Chrome Hearts': 'chromehearts.png',
        'Fear Of God': 'fog.jpg',
        'Hood By Air': 'hoodbyair.png',
        'Le Grand Bleu': 'lgb.jpg',
        'Louis Vuitton': 'louisvuitton.png',
        'Maison Margiela': 'margiela.jpg',
        'Martine Rose': 'martinerose.jpg',
        'Off-White': 'offwhite.png',
        'Raf Simons': 'rafsimons.png',
        'Supreme': 'supreme.png',
        'Undercover': 'undercover.jpg',
        'Yohji Yamamoto': 'yohji.jpg'
    }

# Item image mapping
def get_item_image_map():
    return {
        'Supreme Box Logo "FW 23" cotton hoodie': 'boxlogo.jpg',
        'CCP Object Dyed Lined Rubber Drip Diagonal Zip Goodyear Boot': 'ccpboots.jpg',
        'Chrome Hearts Dagger Pendant Charm Sterling Silver 925': 'chdagger.jpg',
        'FEAR OF GOD ESSENTIALS logo pullover hoodie': 'essentialshoodie.jpg',
        'Hood By Air Black Box Logo S/S Double Zip T-Shirt': 'hbatee.jpeg',
        'L.G.B. Fur Hood Cotton Blend Zip Up Parka Jacket V2': 'lbgzip.jpg',
        'LV Trainer Sneaker': 'lvshoes.jpg',
        'Nike x Martine Rose Air Monarch 4 sneakers': 'martineshoes.jpg',
        'Off-White 2.0 Industrial Belt Yellow/Black': 'owbelt.jpg',
        'Raf Simons Archive "Riot Riot Riot" Bomber': 'riot.jpg',
        'Maison Margiela Tabi 30mm ankle boots': 'tabi.jpg',
        'Balenciaga Triple S sneakers': 'triples.png',
        'SUPREME X UNDERCOVER ANARCHY IS KEY T-SHIRT': 'undertee.jpg',
        'Y-3 Qasa High "Triple Black" sneakers': 'y3.jpg',
        'BAPE Shark Hoodie': 'bapezip.jpg'
    }

# Homepage route
@app.route('/')
def home():
    conn = get_db_connection()
    
    designers = conn.execute('SELECT designer_id, name FROM designer ORDER BY RANDOM() LIMIT 3').fetchall()
    brands = conn.execute('SELECT brand_id, name FROM brand ORDER BY RANDOM() LIMIT 3').fetchall()
    items = conn.execute('SELECT item_id, name, price FROM item ORDER BY RANDOM() LIMIT 3').fetchall()
    
    conn.close()
    
    # DEBUG: Print exact names from database
    print("DESIGNERS:", [designer['name'] for designer in designers])
    print("BRANDS:", [brand['name'] for brand in brands])
    print("ITEMS:", [item['name'] for item in items])
    
    return render_template('home.html',
                         designers=designers,
                         brands=brands,
                         items=items,
                         designer_image_map=get_designer_image_map(),
                         brand_image_map=get_brand_image_map(),
                         item_image_map=get_item_image_map())

@app.route('/designers')
def all_designer():
    conn = get_db_connection()
    # Select all the columns you want to display
    designers = conn.execute('SELECT name, birth_year, country, bio FROM designer ORDER BY name').fetchall()
    conn.close()
    return render_template('designers.html', 
                         designers=designers, 
                         designer_image_map=get_designer_image_map())

@app.route('/thehistory')
def thehistory():
    return render_template('history.html')

@app.route('/brands')
def all_brand():
    conn = get_db_connection()
    brands = conn.execute('SELECT * FROM brand ORDER BY name').fetchall()
    conn.close()
    return render_template('brands.html', 
                         brands=brands, 
                         brand_image_map=get_brand_image_map())

@app.route('/items')
def all_items():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM item ORDER BY name').fetchall()
    conn.close()
    return render_template('items.html', 
                         items=items, 
                         item_image_map=get_item_image_map())

if __name__ == '__main__':
    app.run(debug=True)