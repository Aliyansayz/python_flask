Create a register route that stores user's email , username , name and password after hashing it 
then saving it in User table of sqlite if User table and super_admin table are empty then , 
store it in super_admin table but if super_admin table is not empty then simply into User table 
using Class Register and class method assigning JSON secret key or Session key to each registered user 
depending on developer strategy so later super_admin key can be used as jwt secret key when deploying and 
managing all powers of app.  , add this jwt secret key functionality in super_admin table with column secret_key 
, import secrets 
secret_key = secrets.token_urlsafe(16) , also set : 
app.config['JWT_SECRET_KEY'] = try: fetch secret key from super_admin column secret_key : except:  secrets.token_urlsafe(16)


Here's an implementation of the register route with the required functionalities:


import secrets
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import app, db
from models import User, SuperAdmin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)


# Set JWT_SECRET_KEY using secret_key from super_admin table or generate new one
try:
    super_admin = SuperAdmin.query.first()
    app.config['JWT_SECRET_KEY'] = super_admin.secret_key
except:
    app.config['JWT_SECRET_KEY'] = secrets.token_urlsafe(16)


class Register:
    @classmethod
    def add_user(cls, email, username, name, password):
        # Generate hashed password
        hashed_password = generate_password_hash(password, method='sha256')

        # Check if User and SuperAdmin tables are empty
        is_super_admin = False
        if not User.query.first() and not SuperAdmin.query.first():
            is_super_admin = True

        # Create new user
        user = User(email=email, username=username, name=name,
                    password=hashed_password, is_super_admin=is_super_admin)
        db.session.add(user)
        db.session.commit()

        # If user is super admin, create new super admin
        if is_super_admin:
            super_admin = SuperAdmin(secret_key=secrets.token_urlsafe(16))
            db.session.add(super_admin)
            db.session.commit()

        # Assign JSON secret key or Session key to user
        user.secret_key = secrets.token_urlsafe(16)
        db.session.commit()
        return user.secret_key


@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    username = request.json.get('username')
    name = request.json.get('name')
    password = request.json.get('password')

    if not email or not username or not name or not password:
        return jsonify({'message': 'All fields are required.'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists.'}), 400

    secret_key = Register.add_user(email, username, name, password)

    return jsonify({'secret_key': secret_key}), 201
  
    
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.find_by_username(username)
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200

Here's how this implementation works:

1. We import `secrets`, `request`, `jsonify`, `generate_password_hash`, `app`, `db`, `User`, and `SuperAdmin`.
2. We set the `JWT_SECRET_KEY` using the secret key from the `super_admin` table or 
generate a new one if the `super_admin` table is empty.
3. We create a `Register` class with a class method `add_user` that 
takes the required parameters and adds a new user to the `User` table. If the `User` and `SuperAdmin` tables are empty, 
we also create a new `SuperAdmin` with a new secret key.
4. We assign a new JSON secret key or Session key to the user and return it.
5. We create a `/register` route that takes a POST request with the required fields. 
We check if the email and username already exist, and if not, 
we add the user using the `Register` class method `add_user` and return the secret key.

Note that this implementation assumes that the `User` and `SuperAdmin` tables are already created and 
have the required fields. If not, you'll need to create the tables and fields first before running the code.
