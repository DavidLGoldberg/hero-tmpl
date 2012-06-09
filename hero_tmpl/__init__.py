import os
from flask import Flask
from werkzeug import SharedDataMiddleware

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__,
        static_folder=os.path.join(PROJECT_ROOT, 'public'),
        static_url_path='/public')

    app.config.update(os.environ)

    app.config['SECRET_KEY'] = 'secret'
    app.config['MONGODB_DB'] = 'flask_security_test'
    app.config['MONGODB_HOST'] = 'localhost'
    app.config['MONGODB_PORT'] = 27017

    app.debug = app.config['X_HT_DEBUG'] == "True"

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, 
        {'/': os.path.join(os.path.dirname(__file__), 'public') })

    # import & register blueprints here:
    #===================================
    from hero_tmpl.views.security import security
    app.register_blueprint(security)

    from hero_tmpl.views.misc import misc
    app.register_blueprint(misc)

    return app
