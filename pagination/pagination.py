from flask import Flask, render_template, request
import sqlite3
import math

app = Flask(__name__)

# SQLite database configuration
DATABASE = 'your_database.db'

def get_products(page_num, items_per_page):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    offset = (page_num - 1) * items_per_page

    # Query the products table with LIMIT and OFFSET
    cursor.execute("SELECT * FROM products LIMIT ? OFFSET ?", (items_per_page, offset))
    products = cursor.fetchall()

    conn.close()

    return products

def max_pages(total_items, items_per_page):
    return math.ceil(total_items / items_per_page)

@app.route('/page')
def page():
    items_per_page = 20
    page = request.args.get('page', default=1, type=int)

    products = get_products(page, items_per_page)

    return render_template('index.html', products=products, page_num=page)

if __name__ == '__main__':
    app.run()

"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Product List</title>
</head>
<body>
    <h1>Product List</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            {% for product in products %}
            <tr>
                <td>{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>{{ product.price }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="pagination">
        {% if page_num > 1 %}
        <a href="/page/{{ page_num - 1 }}">Previous</a>
        {% endif %}

        {% for page in range(1, num_pages + 1) %}
        <a href="/page/{{ page }}" {% if page == page_num %}class="active"{% endif %}>{{ page }}</a>
        {% endfor %}

        {% if page_num < num_pages %}
        <a href="/page/{{ page_num + 1 }}">Next</a>
        {% endif %}
    </div>
</body>
</html>

"""
