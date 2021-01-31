from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, NumberRange, URL


class LoginForm(FlaskForm):
    Username = StringField('username', validators=[InputRequired("""A username
                           is required!"""), Length(min=5, max=10,
                           message='Must be between 5 and 10 characters.')])
    Password = PasswordField('password', validators=[InputRequired("""Passwo
                             rd is required!"""), Length(min=5, max=10,
                             message="""Must be between 5 and 10 charac
                             ters.""")])


class AddBookForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("""A book name is req
                       uired!"""), Length(min=3, max=25, message="""Must be
                       between 3 and 25 characters.""")])
    author = StringField('Author', validators=[InputRequired("""A author is
                         required!"""), Length(min=3, max=25, message="""
                         Must be between 3 and 25 characters.""")])
    publisher = StringField('Publisher', validators=[InputRequired("""A
                            publisher is required!"""), Length(min=4, max=20,
                            message="Must be between 4 and 20 characters.")])
    npages = IntegerField('Number of Pages',  validators=[InputRequired("""
                          Number of pages is required!"""), NumberRange(min=1,
                          max=20000, message='Must be between 1 and 20000.')])
    coverimageurl = StringField('Cover Image Url', validators=[URL(message="""
                                Must be a valid URL.""")])
    bookdescription = TextAreaField('Book Description', validators=
                                   [InputRequired("""A coverimageurl is required
                                   !"""), Length(min=3,
                                    max=3500, message="""Must be between 3 and 3
                                    500 characters.""")])
    bookreview = TextAreaField('Book Review', validators=[InputRequired("""A
                               bookreview is required!"""), Length(min=3,
                               max=3500, message='Must be between 3 and 3500 characters.')])
