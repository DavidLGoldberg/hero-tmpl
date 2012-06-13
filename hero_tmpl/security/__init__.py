from flask import current_app
from flask.ext.mail import Mail
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, UserMixin, RoleMixin
from flask.ext.security.datastore.mongoengine import MongoEngineUserDatastore

def create_roles():
    for role in ('admin', 'user'):
        current_app.user_datastore.create_role(name=role)

def create_users():
    #TODO: make configurable
    for u in  (('admin@testtttttt.com', 'password', ['admin'], True),
        ('user@testtttttt.com', 'password', ['user'], True)):
        current_app.user_datastore.create_user(
            username=u[0], email=u[0], password=u[1], roles=u[2], active=u[3])

def populate_data():
    create_roles()
    create_users()

class SecuritySetup:
    def __init__(self, app):
        
        app.mail = Mail(app)

        db = MongoEngine()

        #TODO: pull these files out
        class Role(db.Document, RoleMixin):
            name = db.StringField(required=True, unique=True, max_length=80)
            description = db.StringField(max_length=255)

        class User(db.Document, UserMixin):
            email = db.StringField(unique=True, max_length=255)
            password = db.StringField(required=True, max_length=120)
            active = db.BooleanField(default=True)
            confirmation_token = db.StringField(max_length=255)
            confirmation_sent_at = db.DateTimeField()
            confirmed_at = db.DateTimeField()
            reset_password_token = db.StringField(max_length=255)
            reset_password_sent_at = db.DateTimeField()
            roles = db.ListField(db.ReferenceField(Role), default=[])

        try:
            db.init_app(app)

            Security(app, MongoEngineUserDatastore(db))

            #TODO: make a fabric task?
            @app.before_first_request
            def before_first_request():
                User.drop_collection()
                Role.drop_collection()
                populate_data()

        except:
            print 'cannot connect to mongo'
