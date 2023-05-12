<!DOCTYPE html>
<html>
<head>
    <title>Index</title>
</head>
<body>
    {% if session.logged_in %}
        <h1>{{ admin_home }}</h1>
        <p>Name: {{ data.name }}</p>
        <p>Age: {{ data.age }}</p>
        <p>Email: {{ data.email }}</p>
    {% else %}
        <p>You need to log in to access this page.</p>
    {% endif %}
</body>
</html>
