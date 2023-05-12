Sure! Here's a Flask Blueprint cheat sheet:

### Creating a Blueprint
```python
from flask import Blueprint

bp_name = Blueprint('bp_name', __name__)
```

### Registering a Blueprint
```python
from flask import Flask

app = Flask(__name__)
app.register_blueprint(bp_name)
```

### Adding a Route
```python
@bp_name.route('/example')
def example():
    return 'This is an example route.'
```

### Adding a Route with Parameters
```python
@bp_name.route('/example/<string:param>')
def example(param):
    return f'This route received the parameter: {param}.'
```

### Adding a Route with Methods
```python
@bp_name.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return 'This is a GET request.'
    elif request.method == 'POST':
        return 'This is a POST request.'
```

### Adding a Route with a Template
```python
from flask import render_template

@bp_name.route('/example')
def example():
    return render_template('example.html')
```

### Adding a Static File
```python
bp_name = Blueprint('bp_name', __name__, static_folder='static')

# In HTML
<link rel="stylesheet" href="{{ url_for('bp_name.static', filename='style.css') }}">
```

I hope this helps! Let me know if you have any further questions.
