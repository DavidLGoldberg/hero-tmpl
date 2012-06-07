from hero_tmpl import create_app

app = create_app()

from flask.ext.mail import Mail
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, UserMixin, RoleMixin
from flask.ext.security.datastore.mongoengine import MongoEngineUserDatastore

def create_roles():
    for role in ('admin', 'editor', 'author'):
        current_app.security.datastore.create_role(name=role)

def create_users():
    for u in  (('matt@lp.com', 'password', ['admin'], True),
               ('joe@lp.com', 'password', ['editor'], True),
               ('jill@lp.com', 'password', ['author'], True),
               ('tiya@lp.com', 'password', [], False)):
        current_app.security.datastore.create_user(
            email=u[0], password=u[1], roles=u[2], active=u[3])

def populate_data():
    create_roles()
    create_users()

db = MongoEngine()
try:
    db.init_app(app)

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

    Security(app, MongoEngineUserDatastore(db, User, Role))

    @security.before_first_request
    def before_first_request():
        User.drop_collection()
        Role.drop_collection()
        populate_data()
except:
    print 'cannot connect to mongo'

app.mail = Mail(app)
   

if __name__ == "__main__":
    print "Starting Server."

    import os
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

print "App Imported"
