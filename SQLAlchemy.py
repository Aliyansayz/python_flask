
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)



This section of code imports and initializes Flask extensions for SQLAlchemy, Flask-Migrate, and Flask-Login.

# Flask-SQLAlchemy: 
This extension integrates SQLAlchemy with Flask, providing a simple and easy-to-use interface for database operations. 
It handles creating and managing database connections, sessions, and transactions.

# Flask-Migrate: 
This extension provides database migration support for Flask applications that use SQLAlchemy. 
It automates the process of generating and applying database schema changes across different environments, 
such as development, staging, and production.


Flask-Login: 
This extension provides user authentication and session management capabilities for Flask applications. 
It simplifies the process of adding user authentication to your application 
by providing login and logout views, user session management, and user roles and permissions.

The code initializes each of these extensions by passing in the Flask application instance, app, and 
any configuration settings required by the extension.


app.config['SQLALCHEMY_DATABASE_URI']: 
This sets the URI for the database that the application will use. In this example, it sets the URI to a local SQLite database named my_database.db.


db = SQLAlchemy(app): 
This creates a new SQLAlchemy object, db, and binds it to the Flask application instance, app.


migrate = Migrate(app, db): 
This creates a new Flask-Migrate object, migrate, and binds it to the Flask application instance and the SQLAlchemy object.


login_manager = LoginManager(app): 
This creates a new Flask-Login object, login_manager, and binds it to the Flask application instance.
