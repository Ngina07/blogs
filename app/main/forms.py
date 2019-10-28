from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,PasswordField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Blog

class BlogForm(FlaskForm):

    name = StringField('Enter Blog Title ',validators=[Required()])
    description= TextAreaField('Enter Text ...')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')