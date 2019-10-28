from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Blog,Comment

class BlogForm(FlaskForm):

    name = StringField('Enter Blog Title ',validators=[Required()])
    description= TextAreaField('Enter Text ...')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Comment: ', validators=[Required()])
    submit = SubmitField('Submit')