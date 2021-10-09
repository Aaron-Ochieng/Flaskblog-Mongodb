from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_security import current_user,login_required
from app.models import db,Post
from app.posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user).save()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',form=form, legend='New Post')


@posts.route("/post/<post_id>")
def post(post_id):
    post = Post.objects(id=str(post_id)).first_or_404()
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.objects(id=str(post_id)).get_or_404()
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.update(title=post.title,content=post.content)
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.objects(id=str(post_id)).get_or_404()
    if post.author != current_user:
        abort(403)
    post.delete()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))