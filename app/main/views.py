from flask import render_template,redirect,url_for,request,abort
from flask_login import login_required,login_user,logout_user,current_user
from . import main
from app.models import User,Blog
from .forms import BlogForm
from .. import db,photos

@main.route('/')
def index():
    title = 'Home'

    blogs = Blog.get_blogs()
    

    return render_template('index.html' ,title=title, blogs=blogs )

@main.route('/blog/new',methods=['GET','POST'])
@login_required
def new_blog():
    '''
    Method to add new blog
    '''
    form= BlogForm()
    if form.validate_on_submit():
        name =form.name.data
        description=form.description.data
        like=0
        dislike=0
        new_blog=Blog(name = name ,description=description,like=like,dislike=dislike)
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title= 'Blogs'
    return render_template('blog.html',blog_form=form, title = title)