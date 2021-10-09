from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore,UserMixin,RoleMixin
from datetime import datetime

db = MongoEngine()


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    permissions = db.StringField(max_length=255)

    def __unicode__(self):
        return self.name


class User(db.Document, UserMixin):
    image_file = db.StringField()
    email = db.StringField(max_length=255, unique=True)
    username = db.StringField()
    password = db.StringField(max_length=255)
    last_login_at = db.DateTimeField()
    current_login_at =  db.DateTimeField()
    last_login_ip = db.StringField()
    current_login_ip = db.StringField()
    login_count = db.IntField()
    active = db.BooleanField(default=True)
    fs_uniquifier = db.StringField(max_length=64, unique=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __str__(self):
        return self.username


class Post(db.Document):
    title = db.StringField()
    date_posted = db.DateTimeField(nullable=False,default=datetime.utcnow)
    content = db.StringField()
    author = db.ReferenceField(User)

    def __str__(self):
        return self.title




user_datastore = MongoEngineUserDatastore(db, User, Role)