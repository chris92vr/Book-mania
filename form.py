from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, DateField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired('A username is required!'), Length(min=5, max=10, message='Must be between 5 and 10 characters.')])
    password = PasswordField('password', validators=[InputRequired('Password is required!'), Length(min=5, max=10, message='Must be between 5 and 10 characters.')])

class AddBookForm(FlaskForm):
    name = StringField('name', validators=[InputRequired('A book name is required!'), Length(min=3, max=25, message='Must be between 3 and 25 characters.')])
    author = StringField('author', validators=[InputRequired('A author is required!'), Length(min=3, max=25, message='Must be between 3 and 25 characters.')])
    publisher = StringField('publisher', validators=[InputRequired('A publisher is required!'), Length(min=4, max=20, message='Must be between 4 and 20 characters.')])
    npages = IntegerField('number pages',  validators=[InputRequired('Number of pages is required!'), NumberRange(min=1, max=20000, message='Must be between 1 and 20000.')])
    coverimageurl = StringField('cover image url', validators=[URL(message='Must be a valid URL.')])
    bookdescription = TextAreaField('book description', validators=[InputRequired('A coverimageurl is required!'), Length(min=3, max=1500, message='Must be between 3 and 1500 characters.')])
    bookreview = TextAreaField('book review', validators=[InputRequired('A bookreview is required!'), Length(min=3, max=1500, message='Must be between 3 and 1500 characters.')])