from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    categories = conn.execute('SELECT category, COUNT(*) as count FROM products GROUP BY category').fetchall()
    products = conn.execute('SELECT * FROM products LIMIT 10').fetchall()
    conn.close()
    return render_template('homepage.html', categories=categories, products=products)

@app.route('/category/<category_name>')
def category(category_name):
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products WHERE category = ?', (category_name,)).fetchall()
    conn.close()
    return render_template('category.html', category=category_name, products=products)

@app.route('/search')

def search():
    query = request.args.get('q', '')
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM products WHERE title LIKE ? OR description LIKE ?', ('%'+query+'%', '%'+query+'%')).fetchall()
    conn.close()
    return render_template('search.html', products=products, query=query)

@app.route('/product/<int:ad_no>')
def product(ad_no):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE ad_no = ?', (ad_no,)).fetchone()
    conn.close()
    return render_template('detail.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
