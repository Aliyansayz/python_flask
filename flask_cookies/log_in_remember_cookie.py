Certainly! One of the most important use cases for cookies in Flask is storing login information when a user opts for the "Remember Me" option. 
Here's an example of how you can implement it:

1. Setting the "Remember Me" Cookie:
   ```python
   from flask import Flask, request, make_response

   app = Flask(__name__)

   @app.route('/login', methods=['POST'])
   def login():
       # Logic to validate username and password
       username = request.form.get('username')
       password = request.form.get('password')
       remember_me = request.form.get('remember_me')

       if remember_me:
           # Set a persistent cookie to store login information
           resp = make_response('Login Successful')
           resp.set_cookie('login_info', value=f'{username}:{password}', max_age=30 * 24 * 60 * 60)  # 30 days
           return resp
       else:
           # Handle login without "Remember Me" option
           return 'Login Successful'

   if __name__ == '__main__':
       app.run()
   ```

2. Retrieving the "Remember Me" Cookie:
   ```python
   @app.route('/dashboard')
   def dashboard():
       login_info = request.cookies.get('login_info')

       if login_info:
           username, password = login_info.split(':')
           # Verify the login credentials and proceed with authenticated access
           return f'Welcome, {username}!'
       else:
           # Handle unauthenticated access
           return 'Please log in'

   if __name__ == '__main__':
       app.run()
   ```

In this example, when the user logs in and selects the "Remember Me" option, a persistent cookie named 'login_info' is set with the username and password values. 
The cookie is set to expire after 30 days (`max_age` parameter). When the user visits the '/dashboard' route or any authenticated route later, 
the login information is retrieved from the cookie, allowing the user to remain logged in without explicitly logging in again.

Remember to handle cookie security carefully, use secure and HttpOnly flags where necessary, and implement appropriate measures to protect sensitive information stored in cookies.
