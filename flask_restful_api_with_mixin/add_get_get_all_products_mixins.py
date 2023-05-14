Sure, here's an example implementation of a Flask app that includes a class for a Product model, 
with methods for adding a new product and fetching products from the database:

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    @classmethod
    def create(cls, name, description, price, quantity):
        product = cls(name=name, description=description, price=price, quantity=quantity)
        db.session.add(product)
        db.session.commit()
        return product

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'price': self.price, 'quantity': self.quantity}


@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    result = {'products': [product.to_dict() for product in products]}
    return jsonify(result)


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'})
    return jsonify(product.to_dict())


@app.route('/products', methods=['POST'])
def add_product():
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    quantity = request.json.get('quantity')
    if not all([name, description, price, quantity]):
        return jsonify({'error': 'Missing required fields'})
    product = Product.create(name=name, description=description, price=price, quantity=quantity)
    return jsonify(product.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
```

In this example, we define a `Product` class that extends `db.Model` from SQLAlchemy. 
The class has attributes for `id`, `name`, `description`, `price`, and `quantity`. 
We define a class method `create` that creates a new product and adds it to the database, and 
an instance method `to_dict` that converts a `Product` instance to a dictionary.

We define three routes: 

- `/products` with a `GET` method to fetch all products from the database, a `POST` method to add a new product to the database. 
- `/products/<int:product_id>` with a `GET` method to fetch a specific product by ID.

In the `add_product` route, we use `request.json` to get the product information from the request body. 
We check that all required fields are present, and then create a new `Product` instance using the `create` class method. 
In the `get_products` and `get_product` routes, we fetch products 
from the database using `Product.query.all()` and `Product.query.get(product_id)`, respectively. 
We convert the results to dictionaries using the `to_dict` instance method and return them as JSON using `jsonify`.
