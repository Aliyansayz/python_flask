Here's a cheat sheet for building a Flask REST API:

1. Install Flask and any necessary dependencies (`flask-restful`, `flask_sqlalchemy`, `flask_marshmallow`, etc.).

2. Create a Flask application instance:

   ```python
   from flask import Flask
   app = Flask(__name__)
   ```

3. Configure the Flask application:

   ```python
   app.config['DEBUG'] = True
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   # ...
   ```

4. Initialize any Flask extensions you will be using:

   ```python
   from flask_sqlalchemy import SQLAlchemy
   db = SQLAlchemy(app)
   # ...
   ```

5. Define your database models:

   ```python
   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(50), nullable=False)
       email = db.Column(db.String(120), nullable=False, unique=True)
       # ...
   ```

6. Define your Marshmallow schemas:

   ```python
   from marshmallow import Schema, fields
   class UserSchema(Schema):
       id = fields.Integer()
       name = fields.String(required=True)
       email = fields.Email(required=True)
       # ...
   ```

7. Define your REST API resources:

   ```python
   from flask_restful import Resource
   class UserResource(Resource):
       def get(self, user_id):
           user = User.query.get_or_404(user_id)
           return UserSchema().dump(user)
   
       def post(self):
           data = UserSchema().load(request.json)
           user = User(**data)
           db.session.add(user)
           db.session.commit()
           return UserSchema().dump(user)
   
       def put(self, user_id):
           user = User.query.get_or_404(user_id)
           data = UserSchema().load(request.json)
           for key, value in data.items():
               setattr(user, key, value)
           db.session.commit()
           return UserSchema().dump(user)
   
       def delete(self, user_id):
           user = User.query.get_or_404(user_id)
           db.session.delete(user)
           db.session.commit()
           return '', 204
   ```

8. Register your resources with the Flask application:

   ```python
   from flask_restful import Api
   api = Api(app)
   api.add_resource(UserResource, '/users', '/users/<int:user_id>')
   ```

9. Run the Flask application:

   ```python
   if __name__ == '__main__':
       app.run()
   ```

10. Test your API using a tool like `curl` or Postman.

Note that this is just a basic example and there are many additional features 
you may want to add, such as authentication, pagination, or filtering. 
You may also want to use blueprints to organize your code into modular components.
