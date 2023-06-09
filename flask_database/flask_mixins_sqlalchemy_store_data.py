"""In Flask, a mixin is a class that provides functionality that can be easily added to other classes. 
Mixins are a way to reuse code and avoid duplication, as they allow you to define reusable behavior that can be shared 
across different classes. """
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Optional, Length
from flask_wtf import FlaskForm
from forms import MyForm
from flask.views import View


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'secret-key'
db = SQLAlchemy(app)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[Optional()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=255)])
    submit = SubmitField('Submit')

class User(db.Model):
    __tablename__ = 'users_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    password = db.Column(db.String(255))

class MyView:
    def __init__(self, form):
        self.form = form

    def save_user_data(self, form):
        user = User(name=form.name.data, email=form.email.data, phone=form.phone.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

    def get(self):
        if self.form.validate_on_submit():
            self.save_user_data(self.form)
            return redirect(url_for('success'))
        return render_template('form.html', form=self.form)
      
form = MyForm()

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    view = MyView(form)
    if request.method == 'POST':
        if view.form.validate_on_submit():
            view.save_user_data(view.form)
            flash('User data saved successfully!', 'success')
            return redirect(url_for('add_user'))
        else:
            flash('Form validation failed!', 'error')

"""
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}

<h1>My Form</h1>
<form method="POST">
    {{ form.csrf_token }}
    <div>
        {{ form.name.label }}
        {{ form.name() }}
    </div>
    <div>
        {{ form.email.label }}
        {{ form.email() }}
    </div>
    <div>
        {{ form.phone.label }}
        {{ form.phone() }}
    </div>
    <div>
        {{ form.password.label }}
        {{ form.password() }}
    </div>
    {{ form.submit() }}
</form>


"""
