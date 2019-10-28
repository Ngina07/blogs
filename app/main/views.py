from flask import render_template,redirect,url_for,request,abort
from flask_login import login_required,login_user,logout_user,current_user
from . import main
from app.models import User,Blog
# from .forms import PitchForm,CommentForm,UpdateProfile
from .. import db,photos

@main.route('/')
def index():
    title = 'Home'

    blogs = Blog.get_blogs()
    

    return render_template('index.html' ,title=title, blogs=blogs )