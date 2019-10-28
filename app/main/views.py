from flask import render_template,redirect,url_for,request,abort
from flask_login import login_required,login_user,logout_user,current_user
from . import main
from app.models import User,Blog,Comment
from app.requests import get_quotes
from .forms import BlogForm,UpdateProfile,CommentForm
from .. import db,photos

@main.route('/')
def index():
    title = 'Home'

    quotes = get_quotes
    blogs = Blog.get_blogs()
    
    

    return render_template('index.html' ,title=title, blogs=blogs, quote = quotes)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    '''
    Method to update profile picture
    '''
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

# @main.route("/comment/<int:comment_id>", methods=['GET', 'POST'])
# def comment(comment_id):
#     '''
#     Method to add comment to blog post
#     '''
#     comment = Comment.query.get_or_404(comment_id)
    
#     return render_template('new_comment.html', title='Comment', comment=comment)

@main.route('/blog/<blog_id>/update',methods=['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(404)

    form = BlogForm()
    if form.validate_on_submit():
        blog.name= form.name.data
        blog.description = form.description.data
        db.session.commit()
        flash('You have updated your Blog')

        return redirect(url_for('main.index',id=blog_id))
    if request.method == 'GET':
        form.name.data = blog.name
        form.description.data = blog.description
    return render_template('blog.html',blog_form = form)

@main.route('/blog/<blog_id>/delete', methods=['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    db.session.delete(blog)
    db.session.commit()

    flash('You have deleted your Blog succesfully')
    return redirect(url_for('main.index'))
    