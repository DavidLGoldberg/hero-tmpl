import os
from flask import Flask
from werkzeug import SharedDataMiddleware

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__,
        static_folder=os.path.join(PROJECT_ROOT, 'public'),
        static_url_path='/public')

    app.config.update(os.environ)
    app.debug = app.config['DEBUG']

    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, 
        {'/': os.path.join(os.path.dirname(__file__), 'public') })

    # import blueprints here
    # register blueprints here

    from hero_tmpl.views.bp_login import bp_login
    app.register_blueprint(bp_login)

    from hero_tmpl.views.frontend import frontend
    app.register_blueprint(frontend)

    return app
