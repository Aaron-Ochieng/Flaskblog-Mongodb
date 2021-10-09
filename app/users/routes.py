from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_security import current_user,login_required
from app.models import User, Post,db
from app.users.forms import UpdateAccountForm
from app.users.utils import save_picture

users = Blueprint('users', __name__)





@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    user = User.objects(id=current_user.id).get_or_404()
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        # query = User(username=current_user.username,image_file=picture_file,email=current_user.email).save()
        user.update(username=current_user.username,image_file=picture_file,email=current_user.email)
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.objects.filter(username=username).first_or_404()
    # print(str(user.id))
    posts = Post.objects.filter(author = str(user.id) )\
        .order_by('-date_posted')\
        .paginate(page=page, per_page=5)
    
    return render_template('user_posts.html', posts=posts, user=user)



