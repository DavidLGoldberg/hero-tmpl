import os
from flask import Flask, render_template, current_app
from werkzeug import SharedDataMiddleware
from flask.ext.mail import Mail
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, UserMixin, RoleMixin
from flask.ext.security.datastore.mongoengine import MongoEngineUserDatastore

from hero_tmpl.security import populate_data

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__,
        static_folder=os.path.join(PROJECT_ROOT, 'public'),
        static_url_path='/public')

    app.config.update(os.environ)

    #TODO: read in right hand side from HT config vars
    app.config['SECRET_KEY'] = 'secret'
    app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
    app.config['MONGODB_DB'] = 'flask_security_test'
    app.config['MONGODB_HOST'] = 'localhost'
    app.config['MONGODB_PORT'] = 27017

    app.debug = app.config['X_HT_DEBUG'] == "True"

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, 
        {'/': os.path.join(os.path.dirname(__file__), 'public') })

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

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

    # import & register blueprints here:
    #===================================
    from hero_tmpl.views.security import security
    app.register_blueprint(security)

    from hero_tmpl.views.misc import misc
    app.register_blueprint(misc)

    return app
