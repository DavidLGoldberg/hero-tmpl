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
