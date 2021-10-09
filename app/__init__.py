from flask import Flask, render_template
from .models import db, user_datastore
from .config import Config
from flask_security import Security
# from flask_debugtoolbar import DebugToolbarExtension
from app.admin.routes import admin

# toolbar = DebugToolbarExtension()
security = Security()


def create_app(konfig=Config()):
    app = Flask(__name__)
    app.config.from_object(konfig)

    db.init_app(app)
    security.init_app(app, user_datastore)
    admin.init_app(app)
    toolbar.init_app(app)

    from app.main.routes import main
    app.register_blueprint(main)

    from app.posts.routes import posts
    app.register_blueprint(posts)

    from app.users.routes import users
    app.register_blueprint(users)

    from app.errors.handlers import errors
    app.register_blueprint(errors)



    # @app.route('/')
    # def index(page=1):
    #     paginated_todos = Person.objects.paginate(page=page, per_page=10)
    #     return render_template('index.html',paginated_todos=paginated_todos)

    return app
