To update and delete records from an SQLite database using Python Flask, you can follow these steps:

1. Import the required modules:
```python
from flask import Flask, render_template, request, redirect
import sqlite3
```

2. Create a Flask application:
```python
app = Flask(__name__)
```

3. Define a route to display the records and provide the option to update or delete:
```python
@app.route('/records')
def show_records():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tablename')
    records = cursor.fetchall()
    conn.close()
    return render_template('records.html', records=records)
```

4. Create a template (e.g., `records.html`) to display the records and provide update and delete options:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Records</title>
</head>
<body>
    <h1>Records</h1>
    <table>
        <tr>
            <th>Field 1</th>
            <th>Field 2</th>
            <th>Field 3</th>
            <th>Actions</th>
        </tr>
        {% for record in records %}
        <tr>
            <td>{{ record[0] }}</td>
            <td>{{ record[1] }}</td>
            <td>{{ record[2] }}</td>
            <td>
                <a href="/update/{{ record[0] }}">Edit</a>
                <a href="/delete/{{ record[0] }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```

5. Define routes for update and delete operations:
```python
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_record(id):
    if request.method == 'POST':
        # Get the updated values from the form
        field1 = request.form['field1']
        field2 = request.form['field2']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Update the record
        cursor.execute('UPDATE tablename SET field1=?, field2=? WHERE id=?', (field1, field2, id))
        conn.commit()
        conn.close()

        return redirect('/records')
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tablename WHERE id=?', (id,))
        record = cursor.fetchone()
        conn.close()

        return render_template('update.html', record=record)

@app.route('/delete/<int:id>')
def delete_record(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Delete the record
    cursor.execute('DELETE FROM tablename WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return redirect('/records')
```

6. Create a template (e.g., `update.html`) to display the update form:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Update Record</title>
</head>
<body>
    <h1>Update Record</h1>
    <form method="POST" action="/update/{{ record[0] }}">
        <label>Field 1</label>
        <input type="text" name="field1" value="{{ record[1] }}">
        <br>
        <label>Field 2</label>
        <input type="text" name="field2" value="{{ record[2] }}">
        <br>
        <input type="submit" value="Update">
    </form>
</body>
</html>
```

In this example, the `/records` route displays all the records from the "tablename
