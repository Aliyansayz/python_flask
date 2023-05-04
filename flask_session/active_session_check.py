To count the current active sessions in real-time, you can store the session IDs in a Redis database (or any other in-memory database) and then retrieve them as needed. Here's some sample code that demonstrates how to do this using Redis and Flask-SocketIO:

```python
import json
import uuid
from flask import Flask, session, request
from flask_socketio import SocketIO
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.before_request
def assign_session_id():
    if 'session_id' not in session:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        redis_client.sadd('active_sessions', session_id)

@app.route('/')
def index():
    return 'Hello, world!'

@socketio.on('get_active_sessions')
def get_active_sessions():
    active_sessions = list(redis_client.smembers('active_sessions'))
    socketio.emit('active_sessions_count', len(active_sessions))

if __name__ == '__main__':
    socketio.run(app)
```

Here's how the code works:

- We import the necessary modules and set up a Flask-SocketIO app with a secret key.
- We create a Redis client object to connect to our Redis database.
- In the `assign_session_id()` function (which is run before each request), we generate a session ID and add it to the user's session. We also add the session ID to a Redis set called `active_sessions`.
- We define a route for the home page (`'/'`) that simply returns a string.
- We define a SocketIO event handler for the `'get_active_sessions'` event. When this event is received, we retrieve the list of active sessions from the `active_sessions` set in Redis and emit a `'active_sessions_count'` event with the count of active sessions.
- Finally, we run the SocketIO app using the `socketio.run()` method.

To display the count of active sessions in real-time on the client side, you can use a JavaScript SocketIO client that emits the `'get_active_sessions'` event and listens for the `'active_sessions_count'` event. Here's an example of how you might do this:
"""
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Active Sessions</title>
    <script src="//cdnjs.cloudflare.com/ajax/libs/socket.io/4.2.0/socket.io.min.js"></script>
    <script>
        var socket = io();
        socket.emit('get_active_sessions');
        socket.on('active_sessions_count', function(count) {
            document.getElementById('active-sessions-count').innerHTML = count;
        });
    </script>
</head>
<body>
    <p>Active sessions: <span id="active-sessions-count">0</span></p>
</body>
</html>
```
"""

This HTML file includes the SocketIO client library and sets up a connection to the server. 
When the page is loaded, it emits the `'get_active_sessions'` event to the server and listens for the `'active_sessions_count'` event. 
When the event is received, 
it updates the text of the `active-sessions-count` span element with the count of active sessions.
