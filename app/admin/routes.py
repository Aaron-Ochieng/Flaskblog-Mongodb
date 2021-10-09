from flask_admin import Admin,expose, AdminIndexView
from app.models import User,Role,Post
from flask_admin.contrib.mongoengine import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_security import current_user,auth_required
from flask import abort
from app.config import Config

class AuthModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('Administrator')

class AdminView(AdminIndexView):
    @expose('/')
    @auth_required()
    def index(self):
        if not current_user.has_role('Administrator'):
            return abort(403)
        return self.render('admin/index.html')


class FilesIndexView(FileAdmin):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('Administrator')

class UserModelView(AuthModel):
    pass

class RoleModelView(AuthModel):
    pass

class PostModelView(AuthModel):
    # column_filters  = ('title')
    # # column_select_related_list = ['author']
    pass

admin = Admin(name='Admin Panel',template_mode='bootstrap4',index_view=AdminView())
admin.add_view(UserModelView(User))
admin.add_view(RoleModelView(Role))
admin.add_view(PostModelView(Post))
admin.add_view(FilesIndexView(Config.STATIC_DIR, name='Static Files'))