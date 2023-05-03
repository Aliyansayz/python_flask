Sure, here is a cheat sheet for using cross-origin support in Flask with an example:

### Flask-CORS Setup

Install Flask-CORS:

```bash
pip install flask-cors
```

Import and initialize Flask-CORS in your Flask application:

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

### Configuring CORS

Configure CORS using the following options:

```python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

This allows all origins to access the "/api/*" routes.

```python
CORS(app, origins=['http://localhost:8080'])
```

This allows only "http://localhost:8080" to access the Flask application.

```python
CORS(app, methods=['GET', 'POST'], headers=['Content-Type'])
```

This allows only the specified HTTP methods and headers to access the Flask application.

### CORS in Routes

Enable CORS for a specific route using the `cross_origin()` decorator:

```python
from flask_cors import cross_origin

@app.route('/api')
@cross_origin()
def api():
    return 'Hello, World!'
```

This allows all origins to access the "/api" route.

### Example

Here is an example of using Flask-CORS to create a simple API that returns JSON data:

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = {
    'name': 'John',
    'age': 30,
    'email': 'john@example.com'
}

@app.route('/api')
def api():
    return jsonify(data)

if __name__ == '__main__':
    app.run()
```

This API returns the JSON data when accessed at "http://localhost:5000/api". By default, it allows all origins to access the "/api" route. You can modify the CORS options to restrict access to specific origins, methods, and headers as needed.

Remember to use CORS responsibly and securely by restricting access to trusted origins and configuring the appropriate options.
