from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    # Get all posts
    posts = Post.query.all()

    # Changed base.html to index.html for tailwind purposes
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/create-post")
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            # Added post & create to session
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('view.home'))


    return render_template('create_post.html', user=current_user)